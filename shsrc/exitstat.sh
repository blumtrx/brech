#!/bin/bash
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit
fi

tools=(
  "curl"
  "httpx-toolkit"
  "whatweb"
  "wafw00f"
)
#
for tool in "${tools[@]}"; do
  if ! command -v "$tool" &> /dev/null; then
    echo "$tool is not installed. installing $tool."
    apt-get install -y "$tool" > /dev/null 2>&1
    if [ $? -ne 0 ]; then
      echo "Failed to install $tool. Please check your internet connection or package manager."
      exit 1
    fi
  else
    echo "$tool is installed."
  fi
done

exit 0;
