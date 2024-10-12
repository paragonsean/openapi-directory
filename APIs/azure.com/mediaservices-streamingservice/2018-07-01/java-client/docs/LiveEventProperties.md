

# LiveEventProperties

The Live Event properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | The exact time the Live Event was created. |  [optional] [readonly] |
|**crossSiteAccessPolicies** | [**CrossSiteAccessPolicies**](CrossSiteAccessPolicies.md) |  |  [optional] |
|**description** | **String** | The Live Event description. |  [optional] |
|**encoding** | [**LiveEventEncoding**](LiveEventEncoding.md) |  |  [optional] |
|**input** | [**LiveEventInput**](LiveEventInput.md) |  |  |
|**lastModified** | **OffsetDateTime** | The exact time the Live Event was last modified. |  [optional] [readonly] |
|**preview** | [**LiveEventPreview**](LiveEventPreview.md) |  |  [optional] |
|**provisioningState** | **String** | The provisioning state of the Live Event. |  [optional] [readonly] |
|**resourceState** | [**ResourceStateEnum**](#ResourceStateEnum) | The resource state of the Live Event. |  [optional] [readonly] |
|**streamOptions** | [**List&lt;StreamOptionsEnum&gt;**](#List&lt;StreamOptionsEnum&gt;) | The options to use for the LiveEvent.  This value is specified at creation time and cannot be updated. |  [optional] |
|**vanityUrl** | **Boolean** | Specifies whether to use a vanity url with the Live Event.  This value is specified at creation time and cannot be updated. |  [optional] |



## Enum: ResourceStateEnum

| Name | Value |
|---- | -----|
| STOPPED | &quot;Stopped&quot; |
| STARTING | &quot;Starting&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPING | &quot;Stopping&quot; |
| DELETING | &quot;Deleting&quot; |



## Enum: List&lt;StreamOptionsEnum&gt;

| Name | Value |
|---- | -----|
| DEFAULT | &quot;Default&quot; |
| LOW_LATENCY | &quot;LowLatency&quot; |



