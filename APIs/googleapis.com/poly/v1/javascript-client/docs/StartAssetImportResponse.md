# PolyApi.StartAssetImportResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetId** | **String** | The id of newly created asset. If this is empty when the operation is complete it means the import failed. Please refer to the assetImportMessages field to understand what went wrong. | [optional] 
**assetImportId** | **String** | The id of the asset import. | [optional] 
**assetImportMessages** | [**[AssetImportMessage]**](AssetImportMessage.md) | The message from the asset import. This will contain any warnings (or - in the case of failure - errors) that occurred during import. | [optional] 
**publishUrl** | **String** | The publish URL for the asset. | [optional] 


