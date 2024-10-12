

# GrpcRouteMethodMatch

Specifies a match against a method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caseSensitive** | **Boolean** | Optional. Specifies that matches are case sensitive. The default value is true. case_sensitive must not be used with a type of REGULAR_EXPRESSION. |  [optional] |
|**grpcMethod** | **String** | Required. Name of the method to match against. If unspecified, will match all methods. |  [optional] |
|**grpcService** | **String** | Required. Name of the service to match against. If unspecified, will match all services. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Optional. Specifies how to match against the name. If not specified, a default value of \&quot;EXACT\&quot; is used. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| EXACT | &quot;EXACT&quot; |
| REGULAR_EXPRESSION | &quot;REGULAR_EXPRESSION&quot; |



