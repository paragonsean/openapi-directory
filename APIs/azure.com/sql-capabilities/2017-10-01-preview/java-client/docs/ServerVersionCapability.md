

# ServerVersionCapability

The server capability

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The server version name. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedEditions** | [**List&lt;EditionCapability&gt;**](EditionCapability.md) | The list of supported database editions. |  [optional] [readonly] |
|**supportedElasticPoolEditions** | [**List&lt;ElasticPoolEditionCapability&gt;**](ElasticPoolEditionCapability.md) | The list of supported elastic pool editions. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



