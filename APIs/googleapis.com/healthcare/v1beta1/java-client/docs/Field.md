

# Field

A (sub) field of a type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxOccurs** | **Integer** | The maximum number of times this field can be repeated. 0 or -1 means unbounded. |  [optional] |
|**minOccurs** | **Integer** | The minimum number of times this field must be present/repeated. |  [optional] |
|**name** | **String** | The name of the field. For example, \&quot;PID-1\&quot; or just \&quot;1\&quot;. |  [optional] |
|**table** | **String** | The HL7v2 table this field refers to. For example, PID-15 (Patient&#39;s Primary Language) usually refers to table \&quot;0296\&quot;. |  [optional] |
|**type** | **String** | The type of this field. A Type with this name must be defined in an Hl7TypesConfig. |  [optional] |



