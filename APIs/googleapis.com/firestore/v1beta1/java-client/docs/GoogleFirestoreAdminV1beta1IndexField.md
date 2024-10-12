

# GoogleFirestoreAdminV1beta1IndexField

A field of an index.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldPath** | **String** | The path of the field. Must match the field path specification described by google.firestore.v1beta1.Document.fields. Special field path &#x60;__name__&#x60; may be used by itself or at the end of a path. &#x60;__type__&#x60; may be used only at the end of path. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | The field&#39;s mode. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;MODE_UNSPECIFIED&quot; |
| ASCENDING | &quot;ASCENDING&quot; |
| DESCENDING | &quot;DESCENDING&quot; |
| ARRAY_CONTAINS | &quot;ARRAY_CONTAINS&quot; |



