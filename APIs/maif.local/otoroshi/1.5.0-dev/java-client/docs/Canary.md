

# Canary

The configuration of the canary mode for a service descriptor

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Use canary mode for this service |  |
|**root** | **String** | Otoroshi will append this root to any target choosen. If the specified root is &#39;/api/foo&#39;, then a request to https://yyyyyyy/bar will actually hit https://xxxxxxxxx/api/foo/bar |  |
|**targets** | [**List&lt;Target&gt;**](Target.md) | The list of target that Otoroshi will proxy and expose through the subdomain defined before. Otoroshi will do round-robin load balancing between all those targets with circuit breaker mecanism to avoid cascading failures |  |
|**traffic** | **Integer** | Ratio of traffic that will be sent to canary targets. |  |



