

# ErrorResponse

Error response returned by all error conditions in Velo Services

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**correlationId** | **UUID** | a unique identifier to track a request or related sequence of requests |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | one or more errors |  [optional] |
|**httpStatusCode** | **Integer** | this will mirror the Status-Code part of the Status-Line http response header and is included for extra clarity |  [optional] |



