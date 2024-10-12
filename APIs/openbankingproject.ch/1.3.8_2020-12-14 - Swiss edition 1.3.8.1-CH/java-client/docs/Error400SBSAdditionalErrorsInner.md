

# Error400SBSAdditionalErrorsInner

This is a data element to support the declaration of additional errors in the context of [RFC7807].

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **MessageCode400SBS** |  |  |
|**detail** | **String** | Detailed human readable text specific to this instance of the error. XPath might be used to point to the issue generating the error in addition. Remark for Future: In future, a dedicated field might be introduced for the XPath.  |  [optional] |
|**title** | **String** | Short human readable description of error type. Could be in local language. To be provided by ASPSPs.  |  [optional] |



