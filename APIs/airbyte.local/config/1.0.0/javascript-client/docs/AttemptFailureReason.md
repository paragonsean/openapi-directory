# AirbyteConfigurationApi.AttemptFailureReason

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**externalMessage** | **String** |  | [optional] 
**failureOrigin** | [**AttemptFailureOrigin**](AttemptFailureOrigin.md) |  | [optional] 
**failureType** | [**AttemptFailureType**](AttemptFailureType.md) |  | [optional] 
**internalMessage** | **String** |  | [optional] 
**retryable** | **Boolean** | True if it is known that retrying may succeed, e.g. for a transient failure. False if it is known that a retry will not succeed, e.g. for a configuration issue. If not set, retryable status is not well known. | [optional] 
**stacktrace** | **String** |  | [optional] 
**timestamp** | **Number** |  | 


