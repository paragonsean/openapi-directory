# PublicApi.LinuxHostingDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actualSize** | **Number** | Used webspace size in MB | [optional] 
**domainName** | **String** | Domain name for the Linux hosting account. | [optional] 
**ftpEnabled** | **Boolean** | Indicates whether ftp is enabled for the hosting account. | [optional] 
**ftpUsername** | **String** | Ftp username | [optional] 
**ip** | **String** | Linux hosting IP address | [optional] 
**ipType** | [**LinuxIpType**](LinuxIpType.md) |  | [optional] 
**maxSize** | **Number** | Maximum webspace size in MB | [optional] 
**maxWebspaceSize** | **Number** | Maximum webspace size in MB&lt;br /&gt;  Use max_size instead. | [optional] 
**mysqlDatabaseNames** | **[String]** | A list of mysql databases linked to the hosting account.&lt;br /&gt;  Details of the database can be read using the mysql database detail. | [optional] 
**phpVersion** | **String** | The active php version for the hosting account. | [optional] 
**servicepackId** | **Number** | Id of Linux hosting service package. | [optional] 
**sites** | [**[LinuxSite]**](LinuxSite.md) | A list of websites on the hosting account. | [optional] 
**sshHost** | **String** | Ssh host of the linux hosting account | [optional] 
**sshUsername** | **String** | Ssh username | [optional] 
**webspaceUsage** | **Number** | Used webspace size in MB&lt;br /&gt;  Use actual_size instead. | [optional] 


