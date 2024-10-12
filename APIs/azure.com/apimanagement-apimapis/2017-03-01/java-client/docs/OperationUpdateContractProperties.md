

# OperationUpdateContractProperties

Operation Update Contract Properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Operation Name. |  [optional] |
|**method** | **String** | A Valid HTTP Operation Method. Typical Http Methods like GET, PUT, POST but not limited by only them. |  [optional] |
|**urlTemplate** | **String** | Relative URL template identifying the target resource for this operation. May include parameters. Example: /customers/{cid}/orders/{oid}/?date&#x3D;{date} |  [optional] |
|**description** | **String** | Description of the operation. May include HTML formatting tags. |  [optional] |
|**policies** | **String** | Operation Policies |  [optional] |
|**request** | [**RequestContract**](RequestContract.md) |  |  [optional] |
|**responses** | [**List&lt;ResponseContract&gt;**](ResponseContract.md) | Array of Operation responses. |  [optional] |
|**templateParameters** | [**List&lt;ParameterContract&gt;**](ParameterContract.md) | Collection of URL template parameters. |  [optional] |



