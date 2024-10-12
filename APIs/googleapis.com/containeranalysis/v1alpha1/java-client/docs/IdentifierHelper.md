

# IdentifierHelper

Helps in identifying the underlying product. This should be treated like a one-of field. Only one field should be set in this proto. This is a workaround because spanner indexes on one-of fields restrict addition and deletion of fields.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**field** | [**FieldEnum**](#FieldEnum) | The field that is set in the API proto. |  [optional] |
|**genericUri** | **String** | Contains a URI which is vendor-specific. Example: The artifact repository URL of an image. |  [optional] |



## Enum: FieldEnum

| Name | Value |
|---- | -----|
| IDENTIFIER_HELPER_FIELD_UNSPECIFIED | &quot;IDENTIFIER_HELPER_FIELD_UNSPECIFIED&quot; |
| GENERIC_URI | &quot;GENERIC_URI&quot; |



