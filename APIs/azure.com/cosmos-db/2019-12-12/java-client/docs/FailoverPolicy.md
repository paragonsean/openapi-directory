

# FailoverPolicy

The failover policy for a given region of a database account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failoverPriority** | **Integer** | The failover priority of the region. A failover priority of 0 indicates a write region. The maximum value for a failover priority &#x3D; (total number of regions - 1). Failover priority values must be unique for each of the regions in which the database account exists. |  [optional] |
|**id** | **String** | The unique identifier of the region in which the database account replicates to. Example: &amp;lt;accountName&amp;gt;-&amp;lt;locationName&amp;gt;. |  [optional] [readonly] |
|**locationName** | **String** | The name of the region in which the database account exists. |  [optional] |



