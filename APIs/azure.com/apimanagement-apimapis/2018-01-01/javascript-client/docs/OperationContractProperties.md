# ApiManagementClient.OperationContractProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Operation Name. | 
**method** | **String** | A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them. | 
**urlTemplate** | **String** | Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date&#x3D;{date} | 
**description** | **String** | Description of the operation. May include HTML formatting tags. | [optional] 
**policies** | **String** | Operation Policies | [optional] 
**request** | [**RequestContract**](RequestContract.md) |  | [optional] 
**responses** | [**[ResponseContract]**](ResponseContract.md) | Array of Operation responses. | [optional] 
**templateParameters** | [**[ParameterContract]**](ParameterContract.md) | Collection of URL template parameters. | [optional] 


