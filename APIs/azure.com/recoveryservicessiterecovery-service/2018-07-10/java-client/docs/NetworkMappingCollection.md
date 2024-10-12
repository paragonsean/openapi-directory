

# NetworkMappingCollection

List of network mappings. As with NetworkMapping, it should be possible to reuse a prev version of this class. It doesn't seem likely this class could be anything more than a slightly bespoke collection of NetworkMapping. Hence it makes sense to override Load with Base.NetworkMapping instead of existing CurrentVersion.NetworkMapping.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextLink** | **String** | The value of next link. |  [optional] |
|**value** | [**List&lt;NetworkMapping&gt;**](NetworkMapping.md) | The Network Mappings list. |  [optional] |



