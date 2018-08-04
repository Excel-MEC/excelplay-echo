#!/bin/bash


# CURDIR=$( cd $(dirname $0) ; pwd )
# echo $CURDIR
# HOMEROOT=/home
# RSHELL=/bin/rbash
# CHOWN=root:root

unset COMMANDS
unset USERGROUP
unset HOMEDIR
unset PASSWD
unset OPT_RSHELL
unset OPT_CHATTR
unset test
unset verbose
unset initialize
unset force

bash() {
    echo "Do nothing";
}
export -f bash

 rbash

