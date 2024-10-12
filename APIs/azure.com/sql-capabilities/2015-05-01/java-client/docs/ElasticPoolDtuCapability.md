

# ElasticPoolDtuCapability

The Elastic Pool DTU capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**includedMaxSize** | [**MaxSizeCapability**](MaxSizeCapability.md) |  |  [optional] |
|**limit** | **Integer** | The DTU limit for the pool. |  [optional] [readonly] |
|**maxDatabaseCount** | **Integer** | The maximum number of databases supported. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedMaxSizes** | [**List&lt;MaxSizeCapability&gt;**](MaxSizeCapability.md) | The list of supported max sizes. |  [optional] [readonly] |
|**supportedPerDatabaseMaxDtus** | [**List&lt;ElasticPoolPerDatabaseMaxDtuCapability&gt;**](ElasticPoolPerDatabaseMaxDtuCapability.md) | The list of supported per database max DTUs. |  [optional] [readonly] |
|**supportedPerDatabaseMaxSizes** | [**List&lt;MaxSizeCapability&gt;**](MaxSizeCapability.md) | The list of supported per database max sizes. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



