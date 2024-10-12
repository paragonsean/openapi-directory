

# GoogleCloudApigeeV1EndpointChainingRule

EndpointChainingRule specifies the proxies contained in a particular deployment group, so that other deployment groups can find them in chaining calls.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deploymentGroup** | **String** | The deployment group to target for cross-shard chaining calls to these proxies. |  [optional] |
|**proxyIds** | **List&lt;String&gt;** | List of proxy ids which may be found in the given deployment group. |  [optional] |



