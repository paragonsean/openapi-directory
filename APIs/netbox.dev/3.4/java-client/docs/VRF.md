

# VRF


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**enforceUnique** | **Boolean** | Prevent duplicate prefixes/IP addresses within this VRF |  [optional] |
|**exportTargets** | [**Set&lt;NestedRouteTarget&gt;**](NestedRouteTarget.md) |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**importTargets** | [**Set&lt;NestedRouteTarget&gt;**](NestedRouteTarget.md) |  |  [optional] |
|**ipaddressCount** | **Integer** |  |  [optional] [readonly] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**prefixCount** | **Integer** |  |  [optional] [readonly] |
|**rd** | **String** | Unique route distinguisher (as defined in RFC 4364) |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | [**NestedTenant**](NestedTenant.md) |  |  [optional] |
|**url** | **URI** |  |  [optional] [readonly] |



