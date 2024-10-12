

# LinuxHostingDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actualSize** | **Integer** | Used webspace size in MB |  [optional] |
|**domainName** | **String** | Domain name for the Linux hosting account. |  [optional] |
|**ftpEnabled** | **Boolean** | Indicates whether ftp is enabled for the hosting account. |  [optional] |
|**ftpUsername** | **String** | Ftp username |  [optional] |
|**ip** | **String** | Linux hosting IP address |  [optional] |
|**ipType** | **LinuxIpType** |  |  [optional] |
|**maxSize** | **Integer** | Maximum webspace size in MB |  [optional] |
|**maxWebspaceSize** | **Integer** | Maximum webspace size in MB&lt;br /&gt;  Use max_size instead. |  [optional] |
|**mysqlDatabaseNames** | **List&lt;String&gt;** | A list of mysql databases linked to the hosting account.&lt;br /&gt;  Details of the database can be read using the mysql database detail. |  [optional] |
|**phpVersion** | **String** | The active php version for the hosting account. |  [optional] |
|**servicepackId** | **Integer** | Id of Linux hosting service package. |  [optional] |
|**sites** | [**List&lt;LinuxSite&gt;**](LinuxSite.md) | A list of websites on the hosting account. |  [optional] |
|**sshHost** | **String** | Ssh host of the linux hosting account |  [optional] |
|**sshUsername** | **String** | Ssh username |  [optional] |
|**webspaceUsage** | **Integer** | Used webspace size in MB&lt;br /&gt;  Use actual_size instead. |  [optional] |



