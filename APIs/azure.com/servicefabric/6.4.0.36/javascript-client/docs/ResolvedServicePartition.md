# ServiceFabricClientApis.ResolvedServicePartition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**[ResolvedServiceEndpoint]**](ResolvedServiceEndpoint.md) | List of resolved service endpoints of a service partition. | 
**name** | **String** | The full name of the service with &#39;fabric:&#39; URI scheme. | 
**partitionInformation** | [**PartitionInformation**](PartitionInformation.md) |  | 
**version** | **String** | The version of this resolved service partition result. This version should be passed in the next time the ResolveService call is made via the PreviousRspVersion query parameter. | 


