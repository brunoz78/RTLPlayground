"""List the translation keys of LANG.en that are missing in one language.

Usage: check_i18n.py <app.js> <lang>
Prints one missing key per line; exit code 0 in any case.
"""
import re
import sys


def blocks(path):
    src = open(path, encoding="utf-8").read().replace("\r\n", "\n").split("var rtlLang")[0]
    return dict(re.findall(r"\n(\w\w):\{\n(.*?)\n\}", src, re.S))


def keys(block):
    return re.findall(r'(\w+):"(?:[^"\\]|\\.)*"', block)


def main():
    path, lang = sys.argv[1], sys.argv[2]
    langs = blocks(path)
    if lang not in langs:
        print(f"(Sprache {lang} fehlt ganz)")
        return
    have = set(keys(langs[lang]))
    for k in keys(langs["en"]):
        if k not in have:
            print(k)


if __name__ == "__main__":
    main()
