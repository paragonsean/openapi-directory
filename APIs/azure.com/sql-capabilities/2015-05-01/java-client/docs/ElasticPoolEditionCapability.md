

# ElasticPoolEditionCapability

The elastic pool edition capability.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The elastic pool edition name. |  [optional] [readonly] |
|**reason** | **String** | The reason for the capability not being available. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the capability. |  [optional] [readonly] |
|**supportedElasticPoolDtus** | [**List&lt;ElasticPoolDtuCapability&gt;**](ElasticPoolDtuCapability.md) | The list of supported elastic pool DTU levels for the edition. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| VISIBLE | &quot;Visible&quot; |
| AVAILABLE | &quot;Available&quot; |
| DEFAULT | &quot;Default&quot; |
| DISABLED | &quot;Disabled&quot; |



