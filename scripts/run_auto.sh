#!/usr/bin/expect

set timeout -1

spawn python3 scripts/main.py

expect "Continue (y/n):"
send "y\r"

expect "Input:"
send "y -12\r"

expect eof
