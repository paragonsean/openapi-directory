

# ApiHealth

API Healt response object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectors** | [**List&lt;ApiHealthConnectors&gt;**](ApiHealthConnectors.md) | Connector availability |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Overall connect platform availability status |  |
|**statusMessage** | **String** | Additional informational message |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UP | &quot;UP&quot; |
| DOWN | &quot;DOWN&quot; |
| DEGRADED | &quot;DEGRADED&quot; |



