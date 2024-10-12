

# CreateManifestResponseBody

A create manifest response body

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**manifests** | [**List&lt;Manifest&gt;**](Manifest.md) | Resulting Manifests |  [optional] |
|**manifestRequests** | [**List&lt;ManifestRequest&gt;**](ManifestRequest.md) | Resulting manifest requests with statuses |  [optional] |
|**carrierId** | **String** | A string that uniquely identifies the carrier |  |
|**createdAt** | **OffsetDateTime** | The date-time that the manifest was created |  |
|**formId** | **String** | A string that uniquely identifies the form |  |
|**labelIds** | **List&lt;String&gt;** | An array of the label ids used in this manifest. |  [optional] [readonly] |
|**manifestDownload** | [**ManifestDownload**](ManifestDownload.md) |  |  |
|**manifestId** | **String** | A string that uniquely identifies the manifest |  |
|**shipDate** | **OffsetDateTime** | The date-time that the manifests shipments will be picked up |  |
|**shipments** | **Integer** | The number of shipments that are included in this manifest |  [readonly] |
|**submissionId** | **String** | A string that uniquely identifies the submission |  |
|**warehouseId** | **String** | A string that uniquely identifies the warehouse |  |
|**errors** | [**List&lt;Error&gt;**](Error.md) | The errors associated with the failed API call |  [readonly] |
|**requestId** | **UUID** | A UUID that uniquely identifies the request id. This can be given to the support team to help debug non-trivial issues that may occur  |  |



