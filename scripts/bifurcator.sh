#!/bin/bash

set -e

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <can-log-file>"
    exit 1
fi

INPUT_FILE="$1"
WORKING_FILE="bifurcate_current.log"

cp "$INPUT_FILE" "$WORKING_FILE"

while true; do
    LINES=$(wc -l < "$WORKING_FILE")
    echo "Current segment: $WORKING_FILE ($LINES lines)"

    if [[ "$LINES" -le 1 ]]; then
        echo "Behavior isolated to:"
        cat "$WORKING_FILE"
        exit 0
    fi

    MID=$((LINES / 2))
    PART_A="bifurcate_A.log"
    PART_B="bifurcate_B.log"

    head -n "$MID" "$WORKING_FILE" > "$PART_A"
    tail -n "$((LINES - MID))" "$WORKING_FILE" > "$PART_B"

    echo "Replaying first half (A)..."
    canplayer -I "$PART_A" 

    echo -n "Did the behavior occur in A? (y/n): "
    read -r response

    if [[ "$response" == "y" ]]; then
        cp "$PART_A" "$WORKING_FILE"
    else
        echo "Replaying second half (B)..."
        canplayer -I "$PART_B" 
        echo -n "Did the behavior occur in B? (y/n): "
        read -r response_b
        if [[ "$response_b" == "y" ]]; then
            cp "$PART_B" "$WORKING_FILE"
        else
            echo "Behavior not found in either half. Exiting."
            exit 1
        fi
    fi
done

