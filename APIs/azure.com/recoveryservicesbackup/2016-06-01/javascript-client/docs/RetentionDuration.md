# RecoveryServicesBackupClient.RetentionDuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **Number** | Count of the duration types. Retention duration is determined by the combining the Count times and durationType.      For example, if Count &#x3D; 3 and durationType &#x3D; Weeks, then the retention duration is three weeks. | [optional] 
**durationType** | **String** | The retention duration type of the retention policy. | [optional] 



## Enum: DurationTypeEnum


* `Invalid` (value: `"Invalid"`)

* `Days` (value: `"Days"`)

* `Weeks` (value: `"Weeks"`)

* `Months` (value: `"Months"`)

* `Years` (value: `"Years"`)




