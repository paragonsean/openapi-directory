# CertificateManagerApi.AuthorizationAttemptInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **String** | Output only. Human readable explanation for reaching the state. Provided to help address the configuration issues. Not guaranteed to be stable. For programmatic access use FailureReason enum. | [optional] [readonly] 
**domain** | **String** | Domain name of the authorization attempt. | [optional] 
**failureReason** | **String** | Output only. Reason for failure of the authorization attempt for the domain. | [optional] [readonly] 
**state** | **String** | Output only. State of the domain for managed certificate issuance. | [optional] [readonly] 



## Enum: FailureReasonEnum


* `FAILURE_REASON_UNSPECIFIED` (value: `"FAILURE_REASON_UNSPECIFIED"`)

* `CONFIG` (value: `"CONFIG"`)

* `CAA` (value: `"CAA"`)

* `RATE_LIMITED` (value: `"RATE_LIMITED"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `AUTHORIZING` (value: `"AUTHORIZING"`)

* `AUTHORIZED` (value: `"AUTHORIZED"`)

* `FAILED` (value: `"FAILED"`)




