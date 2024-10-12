# AmazonFsx.OntapFileSystemConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automaticBackupRetentionDays** | **Number** | The number of days to retain automatic backups. Setting this property to &lt;code&gt;0&lt;/code&gt; disables automatic backups. You can retain automatic backups for a maximum of 90 days. The default is &lt;code&gt;30&lt;/code&gt;. | [optional] 
**dailyAutomaticBackupStartTime** | **String** | A recurring daily time, in the format &lt;code&gt;HH:MM&lt;/code&gt;. &lt;code&gt;HH&lt;/code&gt; is the zero-padded hour of the day (0-23), and &lt;code&gt;MM&lt;/code&gt; is the zero-padded minute of the hour. For example, &lt;code&gt;05:00&lt;/code&gt; specifies 5 AM daily.  | [optional] 
**deploymentType** | [**OntapDeploymentType**](OntapDeploymentType.md) |  | [optional] 
**endpointIpAddressRange** | **String** |  | [optional] 
**endpoints** | [**OntapFileSystemConfigurationEndpoints**](OntapFileSystemConfigurationEndpoints.md) |  | [optional] 
**diskIopsConfiguration** | [**OntapFileSystemConfigurationDiskIopsConfiguration**](OntapFileSystemConfigurationDiskIopsConfiguration.md) |  | [optional] 
**preferredSubnetId** | **String** | The ID for a subnet. A &lt;i&gt;subnet&lt;/i&gt; is a range of IP addresses in your virtual private cloud (VPC). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html\&quot;&gt;VPC and subnets&lt;/a&gt; in the &lt;i&gt;Amazon VPC User Guide.&lt;/i&gt;  | [optional] 
**routeTableIds** | **Array** |  | [optional] 
**throughputCapacity** | **Number** | The sustained throughput of an Amazon FSx file system in Megabytes per second (MBps). | [optional] 
**weeklyMaintenanceStartTime** | **String** | &lt;p&gt;A recurring weekly time, in the format &lt;code&gt;D:HH:MM&lt;/code&gt;. &lt;/p&gt; &lt;p&gt; &lt;code&gt;D&lt;/code&gt; is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_week_date\&quot;&gt;the ISO-8601 spec as described on Wikipedia&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;HH&lt;/code&gt; is the zero-padded hour of the day (0-23), and &lt;code&gt;MM&lt;/code&gt; is the zero-padded minute of the hour. &lt;/p&gt; &lt;p&gt;For example, &lt;code&gt;1:05:00&lt;/code&gt; specifies maintenance at 5 AM Monday.&lt;/p&gt; | [optional] 
**fsxAdminPassword** | **String** |  | [optional] 


