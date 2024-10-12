# OtoroshiAdminApi.ClientConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backoffFactor** | **Number** | Specify the factor to multiply the delay for each retry | 
**callTimeout** | **Number** | Specify how long each call should last at most in milliseconds | 
**globalTimeout** | **Number** | Specify how long the global call (with retries) should last at most in milliseconds | 
**maxErrors** | **Number** | Specify how many errors can pass before opening the circuit breaker | 
**retries** | **Number** | Specify how many times the client will try to fetch the result of the request after an error before giving up. | 
**retryInitialDelay** | **Number** | Specify the delay between two retries. Each retry, the delay is multiplied by the backoff factor | 
**sampleInterval** | **Number** | Specify the sliding window time for the circuit breaker in milliseconds, after this time, error count will be reseted | 
**useCircuitBreaker** | **Boolean** | Use a circuit breaker to avoid cascading failure when calling chains of services. Highly recommended ! | 


