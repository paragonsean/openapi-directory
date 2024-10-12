# ApigeeApi.GoogleCloudApigeeV1EndpointAttachment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionState** | **String** | Output only. State of the endpoint attachment connection to the service attachment. | [optional] [readonly] 
**host** | **String** | Output only. Host that can be used in either the HTTP target endpoint directly or as the host in target server. | [optional] [readonly] 
**location** | **String** | Required. Location of the endpoint attachment. | [optional] 
**name** | **String** | Name of the endpoint attachment. Use the following structure in your request: &#x60;organizations/{org}/endpointAttachments/{endpoint_attachment}&#x60; | [optional] 
**serviceAttachment** | **String** | Format: projects/_*_/regions/_*_/serviceAttachments/_* | [optional] 
**state** | **String** | Output only. State of the endpoint attachment. Values other than &#x60;ACTIVE&#x60; mean the resource is not ready to use. | [optional] [readonly] 



## Enum: ConnectionStateEnum


* `CONNECTION_STATE_UNSPECIFIED` (value: `"CONNECTION_STATE_UNSPECIFIED"`)

* `UNAVAILABLE` (value: `"UNAVAILABLE"`)

* `PENDING` (value: `"PENDING"`)

* `ACCEPTED` (value: `"ACCEPTED"`)

* `REJECTED` (value: `"REJECTED"`)

* `CLOSED` (value: `"CLOSED"`)

* `FROZEN` (value: `"FROZEN"`)

* `NEEDS_ATTENTION` (value: `"NEEDS_ATTENTION"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)




