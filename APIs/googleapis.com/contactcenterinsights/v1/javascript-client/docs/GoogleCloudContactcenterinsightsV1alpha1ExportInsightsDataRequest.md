# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigQueryDestination** | [**GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequestBigQueryDestination**](GoogleCloudContactcenterinsightsV1alpha1ExportInsightsDataRequestBigQueryDestination.md) |  | [optional] 
**filter** | **String** | A filter to reduce results to a specific subset. Useful for exporting conversations with specific properties. | [optional] 
**kmsKey** | **String** | A fully qualified KMS key name for BigQuery tables protected by CMEK. Format: projects/{project}/locations/{location}/keyRings/{keyring}/cryptoKeys/{key}/cryptoKeyVersions/{version} | [optional] 
**parent** | **String** | Required. The parent resource to export data from. | [optional] 
**writeDisposition** | **String** | Options for what to do if the destination table already exists. | [optional] 



## Enum: WriteDispositionEnum


* `DISPOSITION_UNSPECIFIED` (value: `"WRITE_DISPOSITION_UNSPECIFIED"`)

* `TRUNCATE` (value: `"WRITE_TRUNCATE"`)

* `APPEND` (value: `"WRITE_APPEND"`)




