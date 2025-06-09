#!/bin/bash

# Read the input file
readarray -t f < chall.txt
n=${f[0]}
a=(${f[1]})
m=998244353

# Function to calculate factorial
factorial() {
    local num=$1
    local result=1
    for ((i=1; i<=num; i++)); do
        result=$(echo "$result * $i" | bc)
    done
    echo "$result"
}

# Function to calculate combinations (n choose r)
choose() {
    local n=$1
    local r=$2
    local numerator=$(factorial "$n")
    local denominator=$(echo "$(factorial "$r") * $(factorial $(($n - $r)))" | bc)
    echo "$(echo "$numerator / $denominator" | bc) % $m" | bc
}

# Calculate the answer
ans=1
for x in "${a[@]}"; do
    choice=$(choose "$n" "$x")
    ans=$(echo "$ans * $choice" | bc)
    ans=$(echo "$ans % $m" | bc)
done

# Print the result
echo "tjctf{$ans}"