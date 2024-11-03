#!/bin/bash

script_dir="$(dirname "$0")"
icons_dir="${script_dir}/front/icons"

if [[ ! -d ${icons_dir} ]]; then
  mkdir "${icons_dir}"
fi


data="${script_dir}/icons.txt"

while read -r line; do
  echo -e "$line\n"
  mv "$line" "${icons_dir}/"
done < "$data"
