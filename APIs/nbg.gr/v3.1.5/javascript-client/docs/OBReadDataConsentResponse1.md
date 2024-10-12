# AccountAndTransactionApiSpecificationUk.OBReadDataConsentResponse1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consentId** | **String** | Unique identification as assigned to identify the account access consent resource. | 
**creationDateTime** | **Date** | Date and time at which the resource was created. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00 | 
**expirationDateTime** | **Date** | Specified date and time the permissions will expire. If this is not populated, the permissions will be open ended. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00 | [optional] 
**permissions** | [**[OBExternalPermissions1Code]**](OBExternalPermissions1Code.md) | Specifies the Open Banking account access data types. This is a list of the data clusters being consented by the PSU, and requested for authorisation with the ASPSP. | 
**status** | [**OBExternalRequestStatus1Code**](OBExternalRequestStatus1Code.md) |  | 
**statusUpdateDateTime** | **Date** | Date and time at which the resource status was updated. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00 | 
**transactionFromDateTime** | **Date** | Specified start date and time for the transaction query period. If this is not populated, the start date will be open ended, and data will be returned from the earliest available transaction. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00 | [optional] 
**transactionToDateTime** | **Date** | Specified end date and time for the transaction query period. If this is not populated, the end date will be open ended, and data will be returned to the latest available transaction. All dates in the JSON payloads are represented in ISO 8601 date-time format.  All date-time fields in responses must include the timezone. An example is below: 2017-04-05T10:43:07+00:00 | [optional] 


