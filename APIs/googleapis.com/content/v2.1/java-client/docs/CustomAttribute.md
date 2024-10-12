

# CustomAttribute

A message that represents custom attributes. Exactly one of `value` or `groupValues` must be provided. Maximum allowed number of characters for each custom attribute is 10240 (represents sum of characters for name and value). Maximum 2500 custom attributes can be set per merchant, with total size of 102.4kB.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupValues** | [**List&lt;CustomAttribute&gt;**](CustomAttribute.md) | Subattributes within this attribute group. Exactly one of value or groupValues must be provided. |  [optional] |
|**name** | **String** | The name of the attribute. Underscores will be replaced by spaces upon insertion. |  [optional] |
|**value** | **String** | The value of the attribute. |  [optional] |



