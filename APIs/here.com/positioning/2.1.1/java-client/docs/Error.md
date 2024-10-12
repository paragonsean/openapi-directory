

# Error

Object wrapper for the error response to a request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | Actionable instructions for the user |  |
|**cause** | **String** | Reason for the error |  |
|**code** | **String** | Error code |  |
|**correlationId** | **UUID** | Copy from X-Correlation-ID header for logging |  |
|**details** | [**List&lt;ErrorDetail&gt;**](ErrorDetail.md) |  |  [optional] |
|**status** | **BigDecimal** | Equals HTTP status code |  |
|**title** | **String** | Localized error string |  |



