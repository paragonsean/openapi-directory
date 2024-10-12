# TagManagerApi.TagConsentSetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consentStatus** | **String** | The tag&#39;s consent status. If set to NEEDED, the runtime will check that the consent types specified by the consent_type field have been granted. | [optional] 
**consentType** | [**Parameter**](Parameter.md) |  | [optional] 



## Enum: ConsentStatusEnum


* `notSet` (value: `"notSet"`)

* `notNeeded` (value: `"notNeeded"`)

* `needed` (value: `"needed"`)




