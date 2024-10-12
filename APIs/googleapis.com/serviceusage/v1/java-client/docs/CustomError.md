

# CustomError

Customize service error responses. For example, list any service specific protobuf types that can appear in error detail lists of error responses. Example: custom_error: types: - google.foo.v1.CustomError - google.foo.v1.AnotherError

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**rules** | [**List&lt;CustomErrorRule&gt;**](CustomErrorRule.md) | The list of custom error rules that apply to individual API messages. **NOTE:** All service configuration rules follow \&quot;last one wins\&quot; order. |  [optional] |
|**types** | **List&lt;String&gt;** | The list of custom error detail types, e.g. &#39;google.foo.v1.CustomError&#39;. |  [optional] |



