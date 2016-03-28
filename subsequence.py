#!/usr/bin/env python
import argparse
import sys

def test_subsequence(query, text):
    '''Returns True if query is a subsequence of text.'''
    if not query:
        return True
    elif not text and query:
        return False
    else:
        # Compare heads
        if query[0] == text[0]:
            return test_subsequence(query[1:], text[1:])
        else:
            return test_subsequence(query, text[1:])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fuzzy subsequence search')
    parser.add_argument('--file', type=argparse.FileType('r'), required=True,
                        help='file to search')
    parser.add_argument('query', metavar='Q', help='query')

    args = parser.parse_args()

    for line in args.file.readlines():
        text = line.strip()
        if test_subsequence(args.query, text):
            query_rest = args.query
            for c in text:
                if query_rest and c == query_rest[0]:
                    sys.stdout.write("\033[31m")
                    sys.stdout.write(c)
                    sys.stdout.write("\033[0m")
                    query_rest = query_rest[1:]
                else:
                    sys.stdout.write(c)
            sys.stdout.write('\n')
            sys.stdout.flush()


    args.file.close()
