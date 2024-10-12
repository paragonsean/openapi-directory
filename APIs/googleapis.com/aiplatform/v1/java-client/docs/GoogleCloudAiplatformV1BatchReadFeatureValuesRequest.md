

# GoogleCloudAiplatformV1BatchReadFeatureValuesRequest

Request message for FeaturestoreService.BatchReadFeatureValues.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigqueryReadInstances** | [**GoogleCloudAiplatformV1BigQuerySource**](GoogleCloudAiplatformV1BigQuerySource.md) |  |  [optional] |
|**csvReadInstances** | [**GoogleCloudAiplatformV1CsvSource**](GoogleCloudAiplatformV1CsvSource.md) |  |  [optional] |
|**destination** | [**GoogleCloudAiplatformV1FeatureValueDestination**](GoogleCloudAiplatformV1FeatureValueDestination.md) |  |  [optional] |
|**entityTypeSpecs** | [**List&lt;GoogleCloudAiplatformV1BatchReadFeatureValuesRequestEntityTypeSpec&gt;**](GoogleCloudAiplatformV1BatchReadFeatureValuesRequestEntityTypeSpec.md) | Required. Specifies EntityType grouping Features to read values of and settings. |  [optional] |
|**passThroughFields** | [**List&lt;GoogleCloudAiplatformV1BatchReadFeatureValuesRequestPassThroughField&gt;**](GoogleCloudAiplatformV1BatchReadFeatureValuesRequestPassThroughField.md) | When not empty, the specified fields in the *_read_instances source will be joined as-is in the output, in addition to those fields from the Featurestore Entity. For BigQuery source, the type of the pass-through values will be automatically inferred. For CSV source, the pass-through values will be passed as opaque bytes. |  [optional] |
|**startTime** | **String** | Optional. Excludes Feature values with feature generation timestamp before this timestamp. If not set, retrieve oldest values kept in Feature Store. Timestamp, if present, must not have higher than millisecond precision. |  [optional] |



