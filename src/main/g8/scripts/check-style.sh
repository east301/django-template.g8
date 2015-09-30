#!/bin/sh

cd $(dirname $0)/..

flake8 --exclude vendor --max-line-length 100 --max-complexity 10 .
exit $?
