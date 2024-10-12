

# GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequest

The request to export insights.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigQueryDestination** | [**GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequestBigQueryDestination**](GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequestBigQueryDestination.md) |  |  [optional] |
|**filter** | **String** | A filter to reduce results to a specific subset. Useful for exporting conversations with specific properties. |  [optional] |
|**kmsKey** | **String** | A fully qualified KMS key name for BigQuery tables protected by CMEK. Format: projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}/cryptoKeyVersions/{version} |  [optional] |
|**parent** | **String** | Required. The parent resource to export data from. |  [optional] |
|**writeDisposition** | [**WriteDispositionEnum**](#WriteDispositionEnum) | Options for what to do if the destination table already exists. |  [optional] |



## Enum: WriteDispositionEnum

| Name | Value |
|---- | -----|
| DISPOSITION_UNSPECIFIED | &quot;WRITE_DISPOSITION_UNSPECIFIED&quot; |
| TRUNCATE | &quot;WRITE_TRUNCATE&quot; |
| APPEND | &quot;WRITE_APPEND&quot; |



