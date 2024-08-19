# IxApi.NetworkServiceConfigsDestroy400Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **String** | A human-readable explanation specific to this occurrence of the problem. | [optional] 
**instance** | **String** | A URI reference that identifies the specific occurrence of the problem.  It may or may not yield further information if dereferenced. | [optional] 
**status** | **Object** |  | [optional] 
**title** | **Object** |  | [optional] 
**type** | **String** |  | 
**chargedUntil** | **Date** | The date until the service is payed for. Typically &#x60;≥ decommission_at&#x60;. | [optional] 
**decommissionAt** | **Date** | This field denotes the first possible cancellation date of the service.  See the service &#x60;cancellation-policy&#x60; for details. | [optional] 



## Enum: TypeEnum


* `cancellation-policy-error.html` (value: `"https://errors.ix-api.net/v2/cancellation-policy-error.html"`)

* `unable-to-fulfill.html` (value: `"https://errors.ix-api.net/v2/unable-to-fulfill.html"`)




