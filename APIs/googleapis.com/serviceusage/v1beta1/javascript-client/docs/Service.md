# ServiceUsageApi.Service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**ServiceConfig**](ServiceConfig.md) |  | [optional] 
**name** | **String** | The resource name of the consumer and service. A valid name would be: - &#x60;projects/123/services/serviceusage.googleapis.com&#x60; | [optional] 
**parent** | **String** | The resource name of the consumer. A valid name would be: - &#x60;projects/123&#x60; | [optional] 
**state** | **String** | Whether or not the service has been enabled for use by the consumer. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `DISABLED` (value: `"DISABLED"`)

* `ENABLED` (value: `"ENABLED"`)




