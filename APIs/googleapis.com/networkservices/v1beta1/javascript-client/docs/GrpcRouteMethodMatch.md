# NetworkServicesApi.GrpcRouteMethodMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caseSensitive** | **Boolean** | Optional. Specifies that matches are case sensitive. The default value is true. case_sensitive must not be used with a type of REGULAR_EXPRESSION. | [optional] 
**grpcMethod** | **String** | Required. Name of the method to match against. If unspecified, will match all methods. | [optional] 
**grpcService** | **String** | Required. Name of the service to match against. If unspecified, will match all services. | [optional] 
**type** | **String** | Optional. Specifies how to match against the name. If not specified, a default value of \&quot;EXACT\&quot; is used. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `EXACT` (value: `"EXACT"`)

* `REGULAR_EXPRESSION` (value: `"REGULAR_EXPRESSION"`)




