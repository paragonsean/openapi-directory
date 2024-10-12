

# CorpPassCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientRedirectFailUrl** | **String** | The URL the CorpPass system will redirect to in case of a failure to perform identity verfication. Mandatory for flow_type&#x3D;\&quot;corppass_flow_redirect\&quot; |  [optional] |
|**clientRedirectSuccessUrl** | **String** | The URL the CorpPass system will redirect to in case of successful identity verfication. Mandatory for flow_type&#x3D;\&quot;corppass_flow_redirect\&quot; |  [optional] |
|**enabled** | **Boolean** | DEPRECATED. Whether or not to enable the CorpPass flow. Must be true if provided. |  [optional] |
|**flowType** | [**FlowTypeEnum**](#FlowTypeEnum) | The CorpPass flow type. |  |
|**signerEmail** | **String** | The email of the person who is going to perform the CorpPass process. Mandatory for flow_type&#x3D;\&quot;corppass_flow_email\&quot; |  [optional] |
|**signerName** | **String** | The name of the person who is going to perform the CorpPass process. Mandatory for flow_type&#x3D;\&quot;corppass_flow_email\&quot; |  [optional] |
|**simulateCorppass** | **Boolean** | Whether or not to simulate CorpPass. Instead of redirecting to a CorpPass URL, you will receive a redirect to a Storecove URL which will show a page with two buttons: success and fail. This makes development without having test CorpPass credentials possible. Note this only works in sandbox, not in the production environment. |  [optional] |



## Enum: FlowTypeEnum

| Name | Value |
|---- | -----|
| REDIRECT | &quot;corppass_flow_redirect&quot; |
| EMAIL | &quot;corppass_flow_email&quot; |



