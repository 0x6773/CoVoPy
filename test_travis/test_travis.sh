#! /bin/zsh

set -x
set -e

SRC="$(pwd)/src"

check()
{
  file=$1
  op=$2
  NSPACE="[^ ]"
  SPACE="[ ]"
  reg="$NSPACE${op}$NSPACE"
  if ! test -z "$(cat $file|grep -e $reg)"; then
    echo "$file contains $(cat $file|grep -e $reg) <==> Operator : $op"
    exit 1
  fi
}

for file in $(ls -R $SRC | awk '/:$/&&f{s=$0;f=0}/:$/&&!f{sub(/:$/,"");s=$0;f=1;next}NF&&f{ print s"/"$0 }');
do
  if test -f $file; then
    for op in '+' '=';
    do
      check $file $op
    done
    echo "$file Passed"
  fi
done
