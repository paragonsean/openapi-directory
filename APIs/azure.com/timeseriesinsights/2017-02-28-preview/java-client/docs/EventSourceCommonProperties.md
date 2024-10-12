

# EventSourceCommonProperties

Properties of the event source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**timestampPropertyName** | **String** | The event property that will be used as the event source&#39;s timestamp. If a value isn&#39;t specified for timestampPropertyName, or if null or empty-string is specified, the event creation time will be used. |  [optional] |
|**creationTime** | **OffsetDateTime** | The time the resource was created. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the resource. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;Accepted&quot; |
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| DELETING | &quot;Deleting&quot; |



