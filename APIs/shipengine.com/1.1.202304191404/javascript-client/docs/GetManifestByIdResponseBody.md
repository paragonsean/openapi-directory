# ShipEngineApi.GetManifestByIdResponseBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrierId** | **String** | A string that uniquely identifies the carrier | [readonly] 
**createdAt** | **Date** | The date-time that the manifest was created | [readonly] 
**formId** | **String** | A string that uniquely identifies the form | [readonly] 
**labelIds** | **[String]** | An array of the label ids used in this manifest. | [readonly] 
**manifestDownload** | [**ManifestDownload**](ManifestDownload.md) |  | [readonly] 
**manifestId** | **String** | A string that uniquely identifies the manifest | [readonly] 
**shipDate** | **Date** | The date-time that the manifests shipments will be picked up | [readonly] 
**shipments** | **Number** | The number of shipments that are included in this manifest | [readonly] 
**submissionId** | **String** | A string that uniquely identifies the submission | [readonly] 
**warehouseId** | **String** | A string that uniquely identifies the warehouse | [readonly] 


