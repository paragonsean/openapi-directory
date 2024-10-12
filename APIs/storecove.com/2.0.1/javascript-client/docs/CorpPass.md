# StorecoveApi.CorpPass

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientRedirectFailUrl** | **String** | The URL the CorpPass system will redirect to in case of a failure to perform identity verfication. | [optional] 
**clientRedirectSuccessUrl** | **String** | The URL the CorpPass system will redirect to in case of successful identity verfication. | [optional] 
**corppassUrl** | **String** | The CorpPass redirect URL. | [optional] 
**enabled** | **Boolean** | Whether or not the CorpPass flow is enabled. | [optional] [default to false]
**flowType** | **String** | The CorpPass flow type. | [optional] 
**signerEmail** | **String** | The email of the person who is going to perform the CorpPass process. | [optional] 
**signerName** | **String** | The name of the person who is going to perform the CorpPass process. | [optional] 
**simulateCorppass** | **Boolean** | Whether or not CorpPass is being simulated. | [optional] [default to false]
**status** | **String** | The status of the CorpPass process. | [optional] 



## Enum: FlowTypeEnum


* `redirect` (value: `"corppass_flow_redirect"`)

* `email` (value: `"corppass_flow_email"`)





## Enum: StatusEnum


* `no_status,` (value: `"corppass_no_status,"`)

* `initiated,` (value: `"corppass_initiated,"`)

* `cancelled,` (value: `"corppass_cancelled,"`)

* `failed,` (value: `"corppass_failed,"`)

* `succeeded` (value: `"corppass_succeeded"`)




