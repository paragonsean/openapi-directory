# CallFireApiDocumentation.ContactList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Number** | A time when a given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 
**id** | **Number** | An Id of a contact list | [optional] 
**name** | **String** | A name of a contact list | [optional] 
**size** | **Number** | A number of contacts in a contact list | [optional] 
**status** | **String** | A current status of a contact list, available values: ACTIVE - contact list is ready, VALIDATING - contact list validation is in progress, IMPORTING - importing is in progress, IMPORT_FAILED - in case of errors occurred during the importing, ERRORS - contact list has validation errors, DELETED - contact list was deleted, PARSE_FAILED - contacts cannot be parsed, COLUMN_TOO_LARGE - if size of phone number or any other column exceeds 255 characters | [optional] 



## Enum: StatusEnum


* `ACTIVE` (value: `"ACTIVE"`)

* `VALIDATING` (value: `"VALIDATING"`)

* `IMPORTING` (value: `"IMPORTING"`)

* `IMPORT_FAILED` (value: `"IMPORT_FAILED"`)

* `ERRORS` (value: `"ERRORS"`)

* `DELETED` (value: `"DELETED"`)

* `PARSE_FAILED` (value: `"PARSE_FAILED"`)

* `COLUMN_TOO_LARGE` (value: `"COLUMN_TOO_LARGE"`)




