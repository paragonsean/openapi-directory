# HealthRepositoryProviderSpecificationsForHiu.PatientAuthNotificationAuth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | access token for initialization of subsequent action. | [optional] 
**patient** | [**PatientDemographicResponse**](PatientDemographicResponse.md) |  | [optional] 
**status** | **String** |  | 
**transactionId** | **String** | transaction id for auth session | 
**validity** | [**AccessTokenValidity**](AccessTokenValidity.md) |  | [optional] 



## Enum: StatusEnum


* `GRANTED` (value: `"GRANTED"`)

* `DENIED` (value: `"DENIED"`)




