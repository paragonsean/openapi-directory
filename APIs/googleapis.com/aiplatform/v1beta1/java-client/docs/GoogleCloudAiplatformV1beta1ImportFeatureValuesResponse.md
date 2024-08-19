

# GoogleCloudAiplatformV1beta1ImportFeatureValuesResponse

Response message for FeaturestoreService.ImportFeatureValues.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**importedEntityCount** | **String** | Number of entities that have been imported by the operation. |  [optional] |
|**importedFeatureValueCount** | **String** | Number of Feature values that have been imported by the operation. |  [optional] |
|**invalidRowCount** | **String** | The number of rows in input source that weren&#39;t imported due to either * Not having any featureValues. * Having a null entityId. * Having a null timestamp. * Not being parsable (applicable for CSV sources). |  [optional] |
|**timestampOutsideRetentionRowsCount** | **String** | The number rows that weren&#39;t ingested due to having feature timestamps outside the retention boundary. |  [optional] |



