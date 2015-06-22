#!/usr/bin/env python
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import flags

f = flags.Flags(help_start='Some tool that searches for stuff',
                help_end='This is licensed under the ASDRQ239.1 Public License F')
f.add('E', help='Use extended regular expressions')
f.add('F', help='Match using fixed strings')
f.add('c', help='Write only a the number of matched lines to standard output')
f.add('e', help='Specify patterns to be used during the input search', coll=True,
      value='pattern')
f.add('f', help='Read patterns from the given file')
f.add('i', help='Ignore case')
f.add('l', help='Write only the file names to standard output')
f.add('n', help='Add line numbers to each printed matching line')
f.add('q', help="Don't print anything")
f.add('s', help='Suppress errors for nonexistent or unreadable files')
f.add('v', help='Print lines that do not match the given patterns')
f.add('x', help='Match the entire line')
f.add_positional('pattern', help='The pattern to match')
f.add_positional('file', help='The file to search', opt=True, coll=True)
print(f.parse_dict())
