

# Attributes

A set of attributes as key-value pairs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeMap** | [**Map&lt;String, AttributeValue&gt;**](AttributeValue.md) | A set of attributes. Each attribute&#39;s key can be up to 128 bytes long. The value can be a string up to 256 bytes, a signed 64-bit integer, or the boolean values &#x60;true&#x60; or &#x60;false&#x60;. For example: \&quot;/instance_id\&quot;: { \&quot;string_value\&quot;: { \&quot;value\&quot;: \&quot;my-instance\&quot; } } \&quot;/http/request_bytes\&quot;: { \&quot;int_value\&quot;: 300 } \&quot;example.com/myattribute\&quot;: { \&quot;bool_value\&quot;: false } |  [optional] |
|**droppedAttributesCount** | **Integer** | The number of attributes that were discarded. Attributes can be discarded because their keys are too long or because there are too many attributes. If this value is 0 then all attributes are valid. |  [optional] |



