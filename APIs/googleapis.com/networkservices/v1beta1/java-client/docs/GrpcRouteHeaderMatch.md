

# GrpcRouteHeaderMatch

A match against a collection of headers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | Required. The key of the header. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Optional. Specifies how to match against the value of the header. If not specified, a default value of EXACT is used. |  [optional] |
|**value** | **String** | Required. The value of the header. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| EXACT | &quot;EXACT&quot; |
| REGULAR_EXPRESSION | &quot;REGULAR_EXPRESSION&quot; |



