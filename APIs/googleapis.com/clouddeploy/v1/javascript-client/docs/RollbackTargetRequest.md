# CloudDeployApi.RollbackTargetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**releaseId** | **String** | Optional. ID of the &#x60;Release&#x60; to roll back to. If this isn&#39;t specified, the previous successful &#x60;Rollout&#x60; to the specified target will be used to determine the &#x60;Release&#x60;. | [optional] 
**rollbackConfig** | [**RollbackTargetConfig**](RollbackTargetConfig.md) |  | [optional] 
**rolloutId** | **String** | Required. ID of the rollback &#x60;Rollout&#x60; to create. | [optional] 
**rolloutToRollBack** | **String** | Optional. If provided, this must be the latest &#x60;Rollout&#x60; that is on the &#x60;Target&#x60;. | [optional] 
**targetId** | **String** | Required. ID of the &#x60;Target&#x60; that is being rolled back. | [optional] 
**validateOnly** | **Boolean** | Optional. If set to true, the request is validated and the user is provided with a &#x60;RollbackTargetResponse&#x60;. | [optional] 


