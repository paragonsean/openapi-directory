# AnthosOnPremApi.ListVmwareClustersResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | A token identifying a page of results the server should return. If the token is not empty this means that more results are available and should be retrieved by repeating the request with the provided page token. | [optional] 
**unreachable** | **[String]** | Locations that could not be reached. | [optional] 
**vmwareClusters** | [**[VmwareCluster]**](VmwareCluster.md) | The list of VMware Cluster. | [optional] 


