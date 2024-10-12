

# EventSecondaryEntity

Detailed information about the Event's secondary entity, which provides additional information for events such as, but not limited to, `linode_boot`, `linode_reboot`, `linode_create`, and `linode_clone` Event actions. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The ID of the object that is the secondary entity.  |  [optional] |
|**label** | **String** | The label of this object.  |  [optional] |
|**type** | **String** | The type of entity that is being referenced by the Event.  |  [optional] [readonly] |
|**url** | **String** | The URL where you can access the object this Event is for. If a relative URL, it is relative to the domain you retrieved the Event from.  |  [optional] |



