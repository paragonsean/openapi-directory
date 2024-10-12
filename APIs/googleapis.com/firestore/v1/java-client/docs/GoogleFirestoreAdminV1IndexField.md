

# GoogleFirestoreAdminV1IndexField

A field in an index. The field_path describes which field is indexed, the value_mode describes how the field value is indexed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arrayConfig** | [**ArrayConfigEnum**](#ArrayConfigEnum) | Indicates that this field supports operations on &#x60;array_value&#x60;s. |  [optional] |
|**fieldPath** | **String** | Can be __name__. For single field indexes, this must match the name of the field or may be omitted. |  [optional] |
|**order** | [**OrderEnum**](#OrderEnum) | Indicates that this field supports ordering by the specified order or comparing using &#x3D;, !&#x3D;, &lt;, &lt;&#x3D;, &gt;, &gt;&#x3D;. |  [optional] |
|**vectorConfig** | [**GoogleFirestoreAdminV1VectorConfig**](GoogleFirestoreAdminV1VectorConfig.md) |  |  [optional] |



## Enum: ArrayConfigEnum

| Name | Value |
|---- | -----|
| ARRAY_CONFIG_UNSPECIFIED | &quot;ARRAY_CONFIG_UNSPECIFIED&quot; |
| CONTAINS | &quot;CONTAINS&quot; |



## Enum: OrderEnum

| Name | Value |
|---- | -----|
| ORDER_UNSPECIFIED | &quot;ORDER_UNSPECIFIED&quot; |
| ASCENDING | &quot;ASCENDING&quot; |
| DESCENDING | &quot;DESCENDING&quot; |



