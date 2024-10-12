

# TagConsentSetting


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consentStatus** | [**ConsentStatusEnum**](#ConsentStatusEnum) | The tag&#39;s consent status. If set to NEEDED, the runtime will check that the consent types specified by the consent_type field have been granted. |  [optional] |
|**consentType** | [**Parameter**](Parameter.md) |  |  [optional] |



## Enum: ConsentStatusEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;notSet&quot; |
| NOT_NEEDED | &quot;notNeeded&quot; |
| NEEDED | &quot;needed&quot; |



