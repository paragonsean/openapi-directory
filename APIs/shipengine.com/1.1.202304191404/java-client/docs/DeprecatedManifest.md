

# DeprecatedManifest

Deprecated manifest resource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrierId** | **String** | A string that uniquely identifies the carrier |  [optional] |
|**createdAt** | **OffsetDateTime** | The date-time that the manifest was created |  [optional] |
|**formId** | **String** | A string that uniquely identifies the form |  [optional] |
|**labelIds** | **List&lt;String&gt;** | An array of the label ids used in this manifest. |  [optional] [readonly] |
|**manifestDownload** | [**ManifestDownload**](ManifestDownload.md) |  |  [optional] |
|**manifestId** | **String** | A string that uniquely identifies the manifest |  [optional] |
|**shipDate** | **OffsetDateTime** | The date-time that the manifests shipments will be picked up |  [optional] |
|**shipments** | **Integer** | The number of shipments that are included in this manifest |  [optional] [readonly] |
|**submissionId** | **String** | A string that uniquely identifies the submission |  [optional] |
|**warehouseId** | **String** | A string that uniquely identifies the warehouse |  [optional] |



