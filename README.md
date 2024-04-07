Connecting Bitbucket Workspace to Atlassian Admin

To connect your Bitbucket Workspace to Atlassian Admin, follow these steps:

1. [Read about Bitbucket Audit Logs in Atlassian Access](https://bitbucket.org/blog/bitbucket-audit-logs-are-now-available-in-atlassian-access)

2. [Create an API Key](https://support.atlassian.com/organization-administration/docs/manage-an-organization-with-the-admin-apis)
Once you complete the process, you will receive the logs. Here is a link to the logs you will receive at the end of the process:
[Bitbucket Cloud Audit Log Events](https://confluence.atlassian.com/bbkb/bitbucket-cloud-audit-log-events-1178872155.html)

Connecting Bitbucket API Logs to syslog

Add the following command to the crontab on the QRadar console/collector:
Make sure you will use the same path

```bash
# Bitbucket Logs
*/4 * * * * python3 /root/Bitbucket/bitbucket.py;bash /root/Bitbucket/sendLogs.sh
```

Create a Log source with the following identifier: 10.10.10.12. 
You can change it, but you will need to update it in the sendLogs.sh script as well.
Note: This integration was developed and tested in my lab and is not supported by IBM DSM guide. 
Use it at your own risk.




