# NetworkServicesApi.GrpcRouteHeaderMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **String** | Required. The key of the header. | [optional] 
**type** | **String** | Optional. Specifies how to match against the value of the header. If not specified, a default value of EXACT is used. | [optional] 
**value** | **String** | Required. The value of the header. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `EXACT` (value: `"EXACT"`)

* `REGULAR_EXPRESSION` (value: `"REGULAR_EXPRESSION"`)




