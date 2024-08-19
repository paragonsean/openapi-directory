

# RateLimitedNetworkServiceConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | The capacity of the service in Mbps. If set to Null, the maximum capacity will be used, i.e. the virtual circuit is not rate-limited.  An exchange may choose to constrain the available capacity range of a &#x60;ProductOffering&#x60;.  That means, the service can consume up to the total bandwidth of the &#x60;Connection&#x60;.  Typically the service is charged based on the capacity. |  [optional] |



