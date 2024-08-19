# AmazonElasticKubernetesService.RegisterClusterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Define a unique name for this cluster for your Region. | 
**connectorConfig** | [**RegisterClusterRequestConnectorConfig**](RegisterClusterRequestConnectorConfig.md) |  | 
**clientRequestToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. | [optional] 
**tags** | **{String: String}** | The metadata that you apply to the cluster to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Cluster tags do not propagate to any other resources associated with the cluster. | [optional] 


