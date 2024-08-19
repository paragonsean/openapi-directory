

# Manifest

Used for combining packages into one scannable form that a carrier can use when picking up a large  number of shipments 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carrierId** | **String** | A string that uniquely identifies the carrier |  [optional] [readonly] |
|**createdAt** | **OffsetDateTime** | The date-time that the manifest was created |  [optional] [readonly] |
|**formId** | **String** | A string that uniquely identifies the form |  [optional] [readonly] |
|**labelIds** | **List&lt;String&gt;** | An array of the label ids used in this manifest. |  [optional] [readonly] |
|**manifestDownload** | [**ManifestDownload**](ManifestDownload.md) |  |  [optional] [readonly] |
|**manifestId** | **String** | A string that uniquely identifies the manifest |  [optional] [readonly] |
|**shipDate** | **OffsetDateTime** | The date-time that the manifests shipments will be picked up |  [optional] [readonly] |
|**shipments** | **Integer** | The number of shipments that are included in this manifest |  [optional] [readonly] |
|**submissionId** | **String** | A string that uniquely identifies the submission |  [optional] [readonly] |
|**warehouseId** | **String** | A string that uniquely identifies the warehouse |  [optional] [readonly] |



