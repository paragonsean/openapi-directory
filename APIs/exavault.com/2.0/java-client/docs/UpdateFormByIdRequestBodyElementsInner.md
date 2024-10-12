

# UpdateFormByIdRequestBodyElementsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** | ID of the form element. If you&#39;re adding a new element to the form, do not include this field. |  [optional] |
|**name** | **String** | Name of the form element. |  [optional] |
|**order** | **Integer** | The order the fields will be displayed to the recipient. Starts at 0.  |  [optional] |
|**settings** | [**UpdateFormByIdRequestBodyElementsInnerSettings**](UpdateFormByIdRequestBodyElementsInnerSettings.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of form field to use. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NAME | &quot;name&quot; |
| EMAIL | &quot;email&quot; |
| TEXT | &quot;text&quot; |
| TEXTAREA | &quot;textarea&quot; |
| UPLOAD_AREA | &quot;upload_area&quot; |



