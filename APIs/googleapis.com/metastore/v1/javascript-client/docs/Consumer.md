# DataprocMetastoreApi.Consumer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpointLocation** | **String** | Output only. The location of the endpoint URI. Format: projects/{project}/locations/{location}. | [optional] [readonly] 
**endpointUri** | **String** | Output only. The URI of the endpoint used to access the metastore service. | [optional] [readonly] 
**subnetwork** | **String** | Immutable. The subnetwork of the customer project from which an IP address is reserved and used as the Dataproc Metastore service&#39;s endpoint. It is accessible to hosts in the subnet and to all hosts in a subnet in the same region and same network. There must be at least one IP address available in the subnet&#39;s primary range. The subnet is specified in the following form:projects/{project_number}/regions/{region_id}/subnetworks/{subnetwork_id} | [optional] 


