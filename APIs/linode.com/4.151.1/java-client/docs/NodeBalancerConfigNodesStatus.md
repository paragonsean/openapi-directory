

# NodeBalancerConfigNodesStatus

A structure containing information about the health of the backends for this port.  This information is updated periodically as checks are performed against backends. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**down** | **Integer** | The number of backends considered to be \&quot;DOWN\&quot; and unhealthy.  These are not in rotation, and not serving requests.  |  [optional] [readonly] |
|**up** | **Integer** | The number of backends considered to be \&quot;UP\&quot; and healthy, and that are serving requests.  |  [optional] [readonly] |



