

# CreateNodeBalancerRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientConnThrottle** | **Integer** | Throttle connections per second.  Set to 0 (zero) to disable throttling.  |  [optional] |
|**configs** | [**List&lt;CreateNodeBalancerRequestConfigsInner&gt;**](CreateNodeBalancerRequestConfigsInner.md) | The port Config(s) to create for this NodeBalancer.  Each Config must have a unique port and at least one Node.  |  [optional] |
|**label** | **String** | This NodeBalancer&#39;s label. These must be unique on your Account.  |  [optional] |
|**region** | **String** | The ID of the Region to create this NodeBalancer in.  |  |



