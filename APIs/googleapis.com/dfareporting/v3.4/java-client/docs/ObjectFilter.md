

# ObjectFilter

Object Filter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#objectFilter\&quot;. |  [optional] |
|**objectIds** | **List&lt;String&gt;** | Applicable when status is ASSIGNED. The user has access to objects with these object IDs. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the filter. NONE means the user has access to none of the objects. ALL means the user has access to all objects. ASSIGNED means the user has access to the objects with IDs in the objectIds list. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| ASSIGNED | &quot;ASSIGNED&quot; |
| ALL | &quot;ALL&quot; |



