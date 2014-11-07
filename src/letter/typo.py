#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Pandoc filter to convert all regular text to uppercase.
Code, link URLs, etc. are not affected.
"""
from pandocfilters import *

# Pandoc block and inline element documentation:
# https://hackage.haskell.org/package/pandoc-types-1.12.3.3/docs/Text-Pandoc-Definition.html

# Str String                 Text (string)
# Emph [Inline]              Emphasized text (list of inlines)
# Strong [Inline]            Strongly emphasized text (list of inlines)
# Strikeout [Inline]         Strikeout text (list of inlines)
# Superscript [Inline]       Superscripted text (list of inlines)
# Subscript [Inline]         Subscripted text (list of inlines)
# SmallCaps [Inline]         Small caps text (list of inlines)
# Quoted QuoteType [Inline]  Quoted text (list of inlines)
# Cite [Citation] [Inline]   Citation (list of inlines)
# Code Attr String           Inline code (literal)
# Space                      Inter-word space
# LineBreak                  Hard line break
# Math MathType String       TeX math (literal)
# RawInline Format String    Raw inline
# Link [Inline] Target       Hyperlink: text (list of inlines), target
# Image [Inline] Target      Image: alt text (list of inlines), target
# Note [Block]               Footnote or endnote
# Span Attr [Inline]         Generic inline container with attributes

# We need a marker element because otherwise we cause endless
# recursion.
#
# Without StrMarker: Str("BLAH") -> SmallCaps[Str("BLAH")] and now we
# move to reprocess Str("Blah") creating endless recursion
StrMarker = elt('StrMarker', 1)

def small_caps(key, value, format, meta):
    min_length = 4
    if key != 'Str' or len(value) <= min_length:
        return None

    if value[:min_length].isupper():
        # So we have 's or ’s (fancy apostrophe)
        if value[-2:] in [u"'s", u"’s"]:
            return [SmallCaps([StrMarker(value[:-2])]),
                    StrMarker(value[-2:])]
        # A pluralized acronym
        elif value[-1] == 's':
            return [SmallCaps([StrMarker(value[:-1])]),
                    StrMarker(value[-1])]
        else:
            return SmallCaps([StrMarker(value)])


def add_ordinal_superscript(key, value, format, meta):
    # need to have at least 3 characters
    min_length = 3

    if key != 'Str' or len(value) <= min_length:
        return None

    ordinal_indicators = ["1st", "2nd", "3rd", "4th", "5th", "6th",
                          "7th", "8th", "9th"]

    if value[-min_length:] in ordinal_indicators:
        # because st, nd, rd, and th are all 2 letters long
        ordinal_length = 2
        return [StrMarker(value[:-ordinal_length]),
                Superscript([StrMarker(value[-ordinal_length:])])]

def replace_str_marker(key, value, format, meta):
    if key == 'StrMarker':
        return Str(value)

def toJSONFilter_pure(doc, actions, format):
    altered = doc
    for action in actions:
        altered = walk(altered, action, format, doc[0]['unMeta'])
    return altered

if __name__ == "__main__":
    doc = json.loads(sys.stdin.read())
    if len(sys.argv) > 1:
        format = sys.argv[1]
    else:
        format = ""
    altered = toJSONFilter_pure(doc, [small_caps, replace_str_marker], format)
    altered = toJSONFilter_pure(altered, [add_ordinal_superscript,
                                          replace_str_marker],
                                format)
    json.dump(altered, sys.stdout)
