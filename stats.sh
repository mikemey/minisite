declare -a all_ips

function extract_ips () {
  for word in $1; do
     if [[ $word =~ [[0-9.]{7,}] ]]; then
      ip=${word:1:-1}
      if [[ ! " ${all_ips[@]} " =~ " ${ip} " ]]; then
         all_ips+=("$ip")
         printf "\n>> `ip_in_range.py $ip` << "
      fi
    fi
  done
}

while [[ 1 ]]; do
  m_lines=`grep "\"GET /\"" minisite.log`

  extract_ips "$m_lines"
  printf "$(date '+%H:%M')."
  sleep 30
done

