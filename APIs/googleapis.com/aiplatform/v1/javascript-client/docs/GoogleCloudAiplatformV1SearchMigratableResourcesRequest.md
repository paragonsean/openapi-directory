# VertexAiApi.GoogleCloudAiplatformV1SearchMigratableResourcesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **String** | A filter for your search. You can use the following types of filters: * Resource type filters. The following strings filter for a specific type of MigratableResource: * &#x60;ml_engine_model_version:*&#x60; * &#x60;automl_model:*&#x60; * &#x60;automl_dataset:*&#x60; * &#x60;data_labeling_dataset:*&#x60; * \&quot;Migrated or not\&quot; filters. The following strings filter for resources that either have or have not already been migrated: * &#x60;last_migrate_time:*&#x60; filters for migrated resources. * &#x60;NOT last_migrate_time:*&#x60; filters for not yet migrated resources. | [optional] 
**pageSize** | **Number** | The standard page size. The default and maximum value is 100. | [optional] 
**pageToken** | **String** | The standard page token. | [optional] 


