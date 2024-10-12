

# ClientConfig

The configuration of the circuit breaker for a service descriptor

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backoffFactor** | **Integer** | Specify the factor to multiply the delay for each retry |  |
|**callTimeout** | **Integer** | Specify how long each call should last at most in milliseconds |  |
|**globalTimeout** | **Integer** | Specify how long the global call (with retries) should last at most in milliseconds |  |
|**maxErrors** | **Integer** | Specify how many errors can pass before opening the circuit breaker |  |
|**retries** | **Integer** | Specify how many times the client will try to fetch the result of the request after an error before giving up. |  |
|**retryInitialDelay** | **Integer** | Specify the delay between two retries. Each retry, the delay is multiplied by the backoff factor |  |
|**sampleInterval** | **Integer** | Specify the sliding window time for the circuit breaker in milliseconds, after this time, error count will be reseted |  |
|**useCircuitBreaker** | **Boolean** | Use a circuit breaker to avoid cascading failure when calling chains of services. Highly recommended ! |  |



