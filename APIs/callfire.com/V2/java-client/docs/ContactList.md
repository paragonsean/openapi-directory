

# ContactList

Represents a contact list in CallFire system

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **Long** | A time when a given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT |  [optional] |
|**id** | **Long** | An Id of a contact list |  [optional] |
|**name** | **String** | A name of a contact list |  [optional] |
|**size** | **Integer** | A number of contacts in a contact list |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | A current status of a contact list, available values: ACTIVE - contact list is ready, VALIDATING - contact list validation is in progress, IMPORTING - importing is in progress, IMPORT_FAILED - in case of errors occurred during the importing, ERRORS - contact list has validation errors, DELETED - contact list was deleted, PARSE_FAILED - contacts cannot be parsed, COLUMN_TOO_LARGE - if size of phone number or any other column exceeds 255 characters |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| VALIDATING | &quot;VALIDATING&quot; |
| IMPORTING | &quot;IMPORTING&quot; |
| IMPORT_FAILED | &quot;IMPORT_FAILED&quot; |
| ERRORS | &quot;ERRORS&quot; |
| DELETED | &quot;DELETED&quot; |
| PARSE_FAILED | &quot;PARSE_FAILED&quot; |
| COLUMN_TOO_LARGE | &quot;COLUMN_TOO_LARGE&quot; |



