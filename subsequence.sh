#!/bin/sh
echo ${history[3060]}

test_subsequence() {
    local query=$1
    local text=$2

    # The query is empty so we have a match.
    if [ -z "$query" ]; then
        return 1
    fi

    # The query is not empty but there is not text to match anymore.
    if [ -z "$text"]; then
        return 0
    fi

    # Okay, let's match the first character of both.
    if [ ${query:0:1} = ${text:0:1} ]
        then
            new_query=${query:1:${#query}-2}
            new_text=${text:1:${#text}-2}
            return test_subsequence "$new_query" "$new_text"
        else
            new_text=${text:1:${#text}-2}
            return test_subsequence "$query" "$new_text"
    fi
}

query=$2

while read p; do
    echo $p
    test_subsequence "$query" "$p"
done <$1
