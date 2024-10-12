# CloudRunAdminApi.DomainMappingStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**[GoogleCloudRunV1Condition]**](GoogleCloudRunV1Condition.md) | Array of observed DomainMappingConditions, indicating the current state of the DomainMapping. | [optional] 
**mappedRouteName** | **String** | The name of the route that the mapping currently points to. | [optional] 
**observedGeneration** | **Number** | ObservedGeneration is the &#39;Generation&#39; of the DomainMapping that was last processed by the controller. Clients polling for completed reconciliation should poll until observedGeneration &#x3D; metadata.generation and the Ready condition&#39;s status is True or False. | [optional] 
**resourceRecords** | [**[ResourceRecord]**](ResourceRecord.md) | The resource records required to configure this domain mapping. These records must be added to the domain&#39;s DNS configuration in order to serve the application via this domain mapping. | [optional] 
**url** | **String** | Optional. Not supported by Cloud Run. | [optional] 


