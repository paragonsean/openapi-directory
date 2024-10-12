

# DatafeedStatusError

An error occurring in the feed, like \"invalid price\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **String** | The code of the error, e.g., \&quot;validation/invalid_value\&quot;. |  [optional] |
|**count** | **String** | The number of occurrences of the error in the feed. |  [optional] |
|**examples** | [**List&lt;DatafeedStatusExample&gt;**](DatafeedStatusExample.md) | A list of example occurrences of the error, grouped by product. |  [optional] |
|**message** | **String** | The error message, e.g., \&quot;Invalid price\&quot;. |  [optional] |



