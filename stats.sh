#!/usr/bin/env bash
declare -a all_ips

function extract_ips () {
  ip_found=false
  for word in $1; do
     if [[ $word =~ [[0-9.]{7,}] ]]; then
      IFS=',' read -ra IPS <<< "${word:1:-1}"
      for ip in "${IPS[@]}"; do
        if [[ ! " ${all_ips[@]} " =~ " ${ip} " ]]; then
           ip_found=true
           all_ips+=("$ip")
           printf "\n>> `ip_in_range.py $ip` << "
        fi
      done
    fi
  done
  if $ip_found; then
    printf "\n"
  fi
}

while [[ 1 ]]; do
  m_lines=`grep "\"GET /\"" minisite.log`

  extract_ips "$m_lines"
  printf "$(date '+%H:%M')."
  sleep 30
done

