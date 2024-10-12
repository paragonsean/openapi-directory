# SwissNextGenBankingApiFramework.Error401PIS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**LinksAll**](LinksAll.md) |  | [optional] 
**additionalErrors** | [**[Error401PISAdditionalErrorsInner]**](Error401PISAdditionalErrorsInner.md) | Array of Error Information Blocks.  Might be used if more than one error is to be communicated  | [optional] 
**code** | [**MessageCode401PIS**](MessageCode401PIS.md) |  | 
**detail** | **String** | Detailed human readable text specific to this instance of the error. XPath might be used to point to the issue generating the error in addition. Remark for Future: In future, a dedicated field might be introduced for the XPath.  | [optional] 
**title** | **String** | Short human readable description of error type. Could be in local language. To be provided by ASPSPs.  | [optional] 
**type** | **String** | A URI reference [RFC3986] that identifies the problem type. Remark For Future: These URI will be provided by NextGen in future.  | 


