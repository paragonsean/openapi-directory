# VertexAiApi.GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigqueryReadInstances** | [**GoogleCloudAiplatformV1beta1BigQuerySource**](GoogleCloudAiplatformV1beta1BigQuerySource.md) |  | [optional] 
**csvReadInstances** | [**GoogleCloudAiplatformV1beta1CsvSource**](GoogleCloudAiplatformV1beta1CsvSource.md) |  | [optional] 
**destination** | [**GoogleCloudAiplatformV1beta1FeatureValueDestination**](GoogleCloudAiplatformV1beta1FeatureValueDestination.md) |  | [optional] 
**entityTypeSpecs** | [**[GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestEntityTypeSpec]**](GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestEntityTypeSpec.md) | Required. Specifies EntityType grouping Features to read values of and settings. | [optional] 
**passThroughFields** | [**[GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestPassThroughField]**](GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestPassThroughField.md) | When not empty, the specified fields in the *_read_instances source will be joined as-is in the output, in addition to those fields from the Featurestore Entity. For BigQuery source, the type of the pass-through values will be automatically inferred. For CSV source, the pass-through values will be passed as opaque bytes. | [optional] 
**startTime** | **String** | Optional. Excludes Feature values with feature generation timestamp before this timestamp. If not set, retrieve oldest values kept in Feature Store. Timestamp, if present, must not have higher than millisecond precision. | [optional] 


