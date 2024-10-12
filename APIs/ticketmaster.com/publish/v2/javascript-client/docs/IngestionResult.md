# TicketmasterPublishApi.IngestionResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Id of the entity ingested in the discovery api | [optional] 
**ignoredProperties** | **{String: Object}** | List properties that are ignored in the validation | [optional] 
**invalidProperties** | **{String: Object}** | List of invalid properties | [optional] 
**invalidValues** | **{String: Object}** | List of invalid values | [optional] 
**missingProperties** | **{String: Object}** | List of properties that should be present in your entity to ease its dicovery | [optional] 
**status** | **String** | Status of the result | 
**unknownProperties** | **{String: Object}** | List of unknown properties that will be dropped | [optional] 



## Enum: StatusEnum


* `Error` (value: `"Error"`)

* `SuccessWarning` (value: `"SuccessWarning"`)

* `Success` (value: `"Success"`)




