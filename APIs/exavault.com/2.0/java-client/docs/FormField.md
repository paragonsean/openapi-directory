

# FormField


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** | ID of the form field.  |  [optional] |
|**name** | **String** | Label of the field. |  [optional] |
|**order** | **Integer** | Order that field appears on the form, starting from 0 |  [optional] |
|**settings** | [**FormFieldSettings**](FormFieldSettings.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Field type |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EMAIL | &quot;email&quot; |
| TEXTAREA | &quot;textarea&quot; |
| NAME | &quot;name&quot; |
| TEXT | &quot;text&quot; |



