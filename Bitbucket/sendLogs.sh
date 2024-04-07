search_dir=/root/Bitbucket/logs/
for entry in "$search_dir"*
do
  echo "$entry";
  /opt/qradar/bin/logrun.pl -u 10.10.10.12 -f $entry  10; rm -rf $entry
done
~

