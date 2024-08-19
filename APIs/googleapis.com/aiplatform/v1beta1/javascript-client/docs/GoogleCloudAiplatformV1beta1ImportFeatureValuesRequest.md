# VertexAiApi.GoogleCloudAiplatformV1beta1ImportFeatureValuesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avroSource** | [**GoogleCloudAiplatformV1beta1AvroSource**](GoogleCloudAiplatformV1beta1AvroSource.md) |  | [optional] 
**bigquerySource** | [**GoogleCloudAiplatformV1beta1BigQuerySource**](GoogleCloudAiplatformV1beta1BigQuerySource.md) |  | [optional] 
**csvSource** | [**GoogleCloudAiplatformV1beta1CsvSource**](GoogleCloudAiplatformV1beta1CsvSource.md) |  | [optional] 
**disableIngestionAnalysis** | **Boolean** | If true, API doesn&#39;t start ingestion analysis pipeline. | [optional] 
**disableOnlineServing** | **Boolean** | If set, data will not be imported for online serving. This is typically used for backfilling, where Feature generation timestamps are not in the timestamp range needed for online serving. | [optional] 
**entityIdField** | **String** | Source column that holds entity IDs. If not provided, entity IDs are extracted from the column named entity_id. | [optional] 
**featureSpecs** | [**[GoogleCloudAiplatformV1beta1ImportFeatureValuesRequestFeatureSpec]**](GoogleCloudAiplatformV1beta1ImportFeatureValuesRequestFeatureSpec.md) | Required. Specifications defining which Feature values to import from the entity. The request fails if no feature_specs are provided, and having multiple feature_specs for one Feature is not allowed. | [optional] 
**featureTime** | **String** | Single Feature timestamp for all entities being imported. The timestamp must not have higher than millisecond precision. | [optional] 
**featureTimeField** | **String** | Source column that holds the Feature timestamp for all Feature values in each entity. | [optional] 
**workerCount** | **Number** | Specifies the number of workers that are used to write data to the Featurestore. Consider the online serving capacity that you require to achieve the desired import throughput without interfering with online serving. The value must be positive, and less than or equal to 100. If not set, defaults to using 1 worker. The low count ensures minimal impact on online serving performance. | [optional] 


