

# RetryPolicy

Number of times to retry a request and how long to wait before timing out.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numRetries** | **Long** | Number of times to retry an upstream request. Note that the initial connection attempt is not included in this number, hence 0 means initial attempt and no retries, and 1 means initial attempt plus one retry.  |  [optional] |
|**perTryTimeoutMsec** | **Long** | Time limit in milliseconds for a single attempt. |  [optional] |
|**timeoutMsec** | **Long** | Total time limit in milliseconds for all attempts (including the initial attempt)  |  [optional] |



