# GitHubV3RestApi.Hook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Determines whether the hook is actually triggered on pushes. | 
**config** | [**HookConfig**](HookConfig.md) |  | 
**createdAt** | **Date** |  | 
**deliveriesUrl** | **String** |  | [optional] 
**events** | **[String]** | Determines what events the hook is triggered for. Default: [&#39;push&#39;]. | 
**id** | **Number** | Unique identifier of the webhook. | 
**lastResponse** | [**HookResponse**](HookResponse.md) |  | 
**name** | **String** | The name of a valid service, use &#39;web&#39; for a webhook. | 
**pingUrl** | **String** |  | 
**testUrl** | **String** |  | 
**type** | **String** |  | 
**updatedAt** | **Date** |  | 
**url** | **String** |  | 


