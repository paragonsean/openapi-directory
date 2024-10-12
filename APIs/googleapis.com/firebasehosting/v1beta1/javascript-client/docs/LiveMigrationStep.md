# FirebaseHostingApi.LiveMigrationStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certVerification** | [**CertVerification**](CertVerification.md) |  | [optional] 
**dnsUpdates** | [**DnsUpdates**](DnsUpdates.md) |  | [optional] 
**issues** | [**[Status]**](Status.md) | Output only. Issues that prevent the current step from completing. | [optional] [readonly] 
**state** | **String** | Output only. The state of the live migration step, indicates whether you should work to complete the step now, in the future, or have already completed it. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `PREPARING` (value: `"PREPARING"`)

* `PENDING` (value: `"PENDING"`)

* `INCOMPLETE` (value: `"INCOMPLETE"`)

* `PROCESSING` (value: `"PROCESSING"`)

* `COMPLETE` (value: `"COMPLETE"`)




