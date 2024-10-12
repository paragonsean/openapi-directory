# AdyenTestCardsApi.TestCardRangeCreationResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cardNumberRangeEnd** | **String** | The last test card number in the generated test card range.  Example: 5432 1234 1234 4321 | 
**cardNumberRangeStart** | **String** | The first test card number in the generated test card range.  Example: 5432 1234 1234 1234 | 
**creationResultCode** | **String** | Notification message. It informs about the outcome of the operation. Possible values: * CREATED * ALREADY_EXISTS * ERROR | 
**message** | **String** | An optional information message about the result. | [optional] 



## Enum: CreationResultCodeEnum


* `ALREADY_EXISTS` (value: `"ALREADY_EXISTS"`)

* `CREATED` (value: `"CREATED"`)

* `ERROR` (value: `"ERROR"`)




