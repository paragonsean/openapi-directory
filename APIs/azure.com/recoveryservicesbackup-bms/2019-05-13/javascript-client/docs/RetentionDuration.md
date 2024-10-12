# RecoveryServicesBackupClient.RetentionDuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **Number** | Count of duration types. Retention duration is obtained by the counting the duration type Count times.  For example, when Count &#x3D; 3 and DurationType &#x3D; Weeks, retention duration will be three weeks. | [optional] 
**durationType** | **String** | Retention duration type of retention policy. | [optional] 



## Enum: DurationTypeEnum


* `Invalid` (value: `"Invalid"`)

* `Days` (value: `"Days"`)

* `Weeks` (value: `"Weeks"`)

* `Months` (value: `"Months"`)

* `Years` (value: `"Years"`)




