# VertexAiApi.GoogleCloudAiplatformV1beta1DeleteFeatureValuesResponseSelectTimeRangeAndFeature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**impactedFeatureCount** | **String** | The count of the features or columns impacted. This is the same as the feature count in the request. | [optional] 
**offlineStorageModifiedEntityRowCount** | **String** | The count of modified entity rows in the offline storage. Each row corresponds to the combination of an entity ID and a timestamp. One entity ID can have multiple rows in the offline storage. Within each row, only the features specified in the request are deleted. | [optional] 
**onlineStorageModifiedEntityCount** | **String** | The count of modified entities in the online storage. Each entity ID corresponds to one entity. Within each entity, only the features specified in the request are deleted. | [optional] 


