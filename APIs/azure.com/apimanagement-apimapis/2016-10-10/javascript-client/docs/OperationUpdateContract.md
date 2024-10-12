# ApiManagementClient.OperationUpdateContract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Uniquely identifies the operation within the current API Management service instance. The value is a valid relative URL in the format of /apis/{aid}/operations/{id} where {aid} is an API identifier and {id} is an operation identifier. | [optional] [readonly] 
**method** | **String** | A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them. | [optional] 
**name** | **String** | Operation Name. | [optional] 
**urlTemplate** | **String** | Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date&#x3D;{date} | [optional] 
**description** | **String** | Description of the operation. May include HTML formatting tags. | [optional] 
**request** | [**RequestContract**](RequestContract.md) |  | [optional] 
**responses** | [**[ResultContract]**](ResultContract.md) | Array of Operation responses. | [optional] 
**templateParameters** | [**[ParameterContract]**](ParameterContract.md) | Collection of URL template parameters. | [optional] 


