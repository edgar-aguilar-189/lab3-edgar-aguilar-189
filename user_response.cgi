#!/bin/bash

USERNAME=${QUERY_STRING#*username=}
USERNAME=${USERNAME%%&*}
USERNAME=${USERNAME//+/ }

echo "Content-Type:text/html"
echo ""

cat << EOF
<!--Start of the Body -->
<html>
  <head>
    <title>Answer</title>
  </head>
  <body>
  Here is what you entered.
 <br>Username: $USERNAME
  </body>
</html>
EOF
