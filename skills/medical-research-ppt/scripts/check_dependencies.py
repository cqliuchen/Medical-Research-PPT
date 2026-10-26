"""Inspect installed skill files. Does not authenticate or call remote services."""

import argparse
import json
import os
import re
from pathlib import Path


MODES = {
    'plan': [],
    'research': ['academic-search', 'pdf'],
    'web': ['agent-reach'],
    'build': ['presentations'],
    'image': ['codex-ppt', 'imagegen'],
    'editable': ['image-to-editable-ppt', 'presentations'],
    'word': ['documents'],
    'notes': ['presentations'],
}


def scan(roots):
    found = {}
    for root in roots:
        if not root.is_dir():
            continue
        for path in root.rglob('SKILL.md'):
            try:
                text = path.read_text(encoding='utf-8-sig')
            except (OSError, UnicodeError):
                continue
            front = re.match(r'^---\s*\n(.*?)\n---', text, re.S)
            if not front:
                continue
            match = re.search(r'^name:\s*[\"\']?([^\n\"\']+)', front.group(1), re.M)
            if match:
                name = match.group(1).strip().lower().split(':')[-1]
                found.setdefault(name, str(path))
            found.setdefault(path.parent.name.lower(), str(path))
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=MODES, default='build')
    parser.add_argument('--skills-root', action='append', default=[])
    parser.add_argument('--no-defaults', action='store_true')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--strict', action='store_true')
    args = parser.parse_args()
    home = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex')))
    roots = [Path(p).expanduser() for p in args.skills_root]
    if not args.no_defaults:
        roots.extend([home / 'skills', home / 'plugins' / 'cache', Path.home() / '.agents' / 'skills'])
    installed = scan(roots)
    required = MODES[args.mode]
    missing = [name for name in required if name not in installed]
    report = {
        'mode': args.mode,
        'file_check_only': True,
        'skills': {name: installed.get(name) for name in required},
        'missing': missing,
        'service_status': 'not_checked',
    }
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print('Mode:', args.mode)
        for name in required:
            print(('FOUND ' if name in installed else 'MISSING ') + name)
        if not required:
            print('Planning and page-review instructions are included in this skill.')
        print('File presence only; OCR, accounts, image backend and Office are not verified.')
    return 1 if args.strict and missing else 0


if __name__ == '__main__':
    raise SystemExit(main())
