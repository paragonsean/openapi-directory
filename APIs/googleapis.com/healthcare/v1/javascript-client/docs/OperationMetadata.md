# CloudHealthcareApi.OperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiMethodName** | **String** | The name of the API method that initiated the operation. | [optional] 
**cancelRequested** | **Boolean** | Specifies if cancellation was requested for the operation. | [optional] 
**counter** | [**ProgressCounter**](ProgressCounter.md) |  | [optional] 
**createTime** | **String** | The time at which the operation was created by the API. | [optional] 
**endTime** | **String** | The time at which execution was completed. | [optional] 
**logsUrl** | **String** | A link to audit and error logs in the log viewer. Error logs are generated only by some operations, listed at [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging). | [optional] 


