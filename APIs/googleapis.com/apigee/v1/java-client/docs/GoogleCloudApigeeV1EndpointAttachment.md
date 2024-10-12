

# GoogleCloudApigeeV1EndpointAttachment

Apigee endpoint attachment. For more information, see [Southbound networking patterns] (https://cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionState** | [**ConnectionStateEnum**](#ConnectionStateEnum) | Output only. State of the endpoint attachment connection to the service attachment. |  [optional] [readonly] |
|**host** | **String** | Output only. Host that can be used in either the HTTP target endpoint directly or as the host in target server. |  [optional] [readonly] |
|**location** | **String** | Required. Location of the endpoint attachment. |  [optional] |
|**name** | **String** | Name of the endpoint attachment. Use the following structure in your request: &#x60;organizations/{org}/endpointAttachments/{endpoint_attachment}&#x60; |  [optional] |
|**serviceAttachment** | **String** | Format: projects/_*_/regions/_*_/serviceAttachments/_* |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the endpoint attachment. Values other than &#x60;ACTIVE&#x60; mean the resource is not ready to use. |  [optional] [readonly] |



## Enum: ConnectionStateEnum

| Name | Value |
|---- | -----|
| CONNECTION_STATE_UNSPECIFIED | &quot;CONNECTION_STATE_UNSPECIFIED&quot; |
| UNAVAILABLE | &quot;UNAVAILABLE&quot; |
| PENDING | &quot;PENDING&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |
| REJECTED | &quot;REJECTED&quot; |
| CLOSED | &quot;CLOSED&quot; |
| FROZEN | &quot;FROZEN&quot; |
| NEEDS_ATTENTION | &quot;NEEDS_ATTENTION&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| UPDATING | &quot;UPDATING&quot; |



