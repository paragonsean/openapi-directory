# SecurityCenter.TopologySingleResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**[TopologySingleResourceChild]**](TopologySingleResourceChild.md) | Azure resources connected to this resource which are in lower level in the topology view | [optional] [readonly] 
**location** | **String** | The location of this resource | [optional] [readonly] 
**networkZones** | **String** | Indicates the resource connectivity level to the Internet (InternetFacing, Internal ,etc.) | [optional] [readonly] 
**parents** | [**[TopologySingleResourceParent]**](TopologySingleResourceParent.md) | Azure resources connected to this resource which are in higher level in the topology view | [optional] [readonly] 
**recommendationsExist** | **Boolean** | Indicates if the resource has security recommendations | [optional] [readonly] 
**resourceId** | **String** | Azure resource id | [optional] [readonly] 
**severity** | **String** | The security severity of the resource | [optional] [readonly] 
**topologyScore** | **Number** | Score of the resource based on its security severity | [optional] [readonly] 


