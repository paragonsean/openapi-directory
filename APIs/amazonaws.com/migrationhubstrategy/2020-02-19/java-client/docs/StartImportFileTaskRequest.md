

# StartImportFileTaskRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**s3Bucket** | **String** |  The S3 bucket where the import file is located. The bucket name is required to begin with &lt;code&gt;migrationhub-strategy-&lt;/code&gt;. |  |
|**dataSourceType** | [**DataSourceTypeEnum**](#DataSourceTypeEnum) | Specifies the source that the servers are coming from. By default, Strategy Recommendations assumes that the servers specified in the import file are available in AWS Application Discovery Service.  |  [optional] |
|**groupId** | [**List&lt;Group&gt;**](Group.md) | Groups the resources in the import file together with a unique name. This ID can be as filter in &lt;code&gt;ListApplicationComponents&lt;/code&gt; and &lt;code&gt;ListServers&lt;/code&gt;.  |  [optional] |
|**name** | **String** |  A descriptive name for the request.  |  |
|**s3bucketForReportData** | **String** |  The S3 bucket where Strategy Recommendations uploads import results. The bucket name is required to begin with migrationhub-strategy-.  |  [optional] |
|**s3key** | **String** |  The Amazon S3 key name of the import file.  |  |



## Enum: DataSourceTypeEnum

| Name | Value |
|---- | -----|
| APPLICATION_DISCOVERY_SERVICE | &quot;ApplicationDiscoveryService&quot; |
| MPA | &quot;MPA&quot; |
| IMPORT | &quot;Import&quot; |



