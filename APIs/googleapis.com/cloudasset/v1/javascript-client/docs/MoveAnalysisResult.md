# CloudAssetApi.MoveAnalysisResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockers** | [**[MoveImpact]**](MoveImpact.md) | Blocking information that would prevent the target resource from moving to the specified destination at runtime. | [optional] 
**warnings** | [**[MoveImpact]**](MoveImpact.md) | Warning information indicating that moving the target resource to the specified destination might be unsafe. This can include important policy information and configuration changes, but will not block moves at runtime. | [optional] 


