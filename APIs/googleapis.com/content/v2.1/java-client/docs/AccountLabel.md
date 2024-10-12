

# AccountLabel

Label assigned by CSS domain or CSS group to one of its sub-accounts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Immutable. The ID of account this label belongs to. |  [optional] |
|**description** | **String** | The description of this label. |  [optional] |
|**labelId** | **String** | Output only. The ID of the label. |  [optional] [readonly] |
|**labelType** | [**LabelTypeEnum**](#LabelTypeEnum) | Output only. The type of this label. |  [optional] [readonly] |
|**name** | **String** | The display name of this label. |  [optional] |



## Enum: LabelTypeEnum

| Name | Value |
|---- | -----|
| LABEL_TYPE_UNSPECIFIED | &quot;LABEL_TYPE_UNSPECIFIED&quot; |
| MANUAL | &quot;MANUAL&quot; |
| AUTOMATIC | &quot;AUTOMATIC&quot; |



