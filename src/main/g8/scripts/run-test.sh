#!/bin/sh

cd \$(dirname "\$0")/..

coverage run --source=apps manage.py test
RET=\$?

coverage html
coverage report

exit \$RET
