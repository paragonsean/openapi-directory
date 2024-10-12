

# Error


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** | The error category |  |
|**context** | **Map&lt;String, List&lt;String&gt;&gt;** | Context about the error condition |  [optional] |
|**correlationId** | **UUID** | A unique identifier for the request. Include this value with any error reports or support tickets |  |
|**errors** | [**List&lt;ErrorDetail&gt;**](ErrorDetail.md) | further information about the error |  [optional] |
|**links** | **Map&lt;String, String&gt;** | A map of link names to associated URIs containing documentation about the error or recommended remediation steps |  [optional] |
|**message** | **String** | A human readable message describing the error along with remediation steps where appropriate |  |
|**subCategory** | **String** | A specific category that contains more specific detail about the error |  [optional] |



