

# DedicatedHostGroupUpdate

Specifies information about the dedicated host group that the dedicated host should be assigned to. Only tags may be updated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**DedicatedHostGroupProperties**](DedicatedHostGroupProperties.md) |  |  [optional] |
|**zones** | **List&lt;String&gt;** | Availability Zone to use for this host group. Only single zone is supported. The zone can be assigned only during creation. If not provided, the group supports all zones in the region. If provided, enforces each host in the group to be in the same zone. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Resource tags |  [optional] |



