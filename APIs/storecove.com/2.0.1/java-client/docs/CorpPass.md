

# CorpPass


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRedirectFailUrl** | **String** | The URL the CorpPass system will redirect to in case of a failure to perform identity verfication. |  [optional] |
|**clientRedirectSuccessUrl** | **String** | The URL the CorpPass system will redirect to in case of successful identity verfication. |  [optional] |
|**corppassUrl** | **String** | The CorpPass redirect URL. |  [optional] |
|**enabled** | **Boolean** | Whether or not the CorpPass flow is enabled. |  [optional] |
|**flowType** | [**FlowTypeEnum**](#FlowTypeEnum) | The CorpPass flow type. |  [optional] |
|**signerEmail** | **String** | The email of the person who is going to perform the CorpPass process. |  [optional] |
|**signerName** | **String** | The name of the person who is going to perform the CorpPass process. |  [optional] |
|**simulateCorppass** | **Boolean** | Whether or not CorpPass is being simulated. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the CorpPass process. |  [optional] |



## Enum: FlowTypeEnum

| Name | Value |
|---- | -----|
| REDIRECT | &quot;corppass_flow_redirect&quot; |
| EMAIL | &quot;corppass_flow_email&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NO_STATUS_ | &quot;corppass_no_status,&quot; |
| INITIATED_ | &quot;corppass_initiated,&quot; |
| CANCELLED_ | &quot;corppass_cancelled,&quot; |
| FAILED_ | &quot;corppass_failed,&quot; |
| SUCCEEDED | &quot;corppass_succeeded&quot; |



