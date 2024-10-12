

# Attributes

A set of attributes, each in the format `[KEY]:[VALUE]`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeMap** | [**Map&lt;String, AttributeValue&gt;**](AttributeValue.md) | The set of attributes. Each attribute&#39;s key can be up to 128 bytes long. The value can be a string up to 256 bytes, a signed 64-bit integer, or the Boolean values &#x60;true&#x60; and &#x60;false&#x60;. For example: \&quot;/instance_id\&quot;: \&quot;my-instance\&quot; \&quot;/http/user_agent\&quot;: \&quot;\&quot; \&quot;/http/request_bytes\&quot;: 300 \&quot;abc.com/myattribute\&quot;: true |  [optional] |
|**droppedAttributesCount** | **Integer** | The number of attributes that were discarded. Attributes can be discarded because their keys are too long or because there are too many attributes. If this value is 0 then all attributes are valid. |  [optional] |



