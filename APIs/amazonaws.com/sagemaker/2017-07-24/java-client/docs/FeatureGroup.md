

# FeatureGroup

Amazon SageMaker Feature Store stores features in a collection called Feature Group. A Feature Group can be visualized as a table which has rows, with a unique identifier for each row where each column in the table is a feature. In principle, a Feature Group is composed of features and values per features.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**featureGroupArn** | [**String**](String.md) |  |  [optional] |
|**featureGroupName** | [**String**](String.md) |  |  [optional] |
|**recordIdentifierFeatureName** | [**String**](String.md) |  |  [optional] |
|**eventTimeFeatureName** | [**String**](String.md) |  |  [optional] |
|**featureDefinitions** | [**List**](List.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**onlineStoreConfig** | [**OnlineStoreConfig**](OnlineStoreConfig.md) |  |  [optional] |
|**offlineStoreConfig** | [**OfflineStoreConfig**](OfflineStoreConfig.md) |  |  [optional] |
|**roleArn** | [**String**](String.md) |  |  [optional] |
|**featureGroupStatus** | [**FeatureGroupStatus**](FeatureGroupStatus.md) |  |  [optional] |
|**offlineStoreStatus** | [**OfflineStoreStatus**](OfflineStoreStatus.md) |  |  [optional] |
|**lastUpdateStatus** | [**FeatureGroupLastUpdateStatus**](FeatureGroupLastUpdateStatus.md) |  |  [optional] |
|**failureReason** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |



