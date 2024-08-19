

# GetManifestByIdResponseBody

A get manifest by id response body

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrierId** | **String** | A string that uniquely identifies the carrier |  [readonly] |
|**createdAt** | **OffsetDateTime** | The date-time that the manifest was created |  [readonly] |
|**formId** | **String** | A string that uniquely identifies the form |  [readonly] |
|**labelIds** | **List&lt;String&gt;** | An array of the label ids used in this manifest. |  [readonly] |
|**manifestDownload** | [**ManifestDownload**](ManifestDownload.md) |  |  [readonly] |
|**manifestId** | **String** | A string that uniquely identifies the manifest |  [readonly] |
|**shipDate** | **OffsetDateTime** | The date-time that the manifests shipments will be picked up |  [readonly] |
|**shipments** | **Integer** | The number of shipments that are included in this manifest |  [readonly] |
|**submissionId** | **String** | A string that uniquely identifies the submission |  [readonly] |
|**warehouseId** | **String** | A string that uniquely identifies the warehouse |  [readonly] |



