#!/bin/bash
git add .
echo "enter the message for commit:"
read message
echo "$message"
git commit -m "$message"
git push