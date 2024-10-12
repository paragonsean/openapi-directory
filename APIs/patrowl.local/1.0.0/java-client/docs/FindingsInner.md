

# FindingsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidence** | **String** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**issueId** | **Integer** |  |  [optional] |
|**metaLinks** | **List&lt;String&gt;** |  |  [optional] |
|**metaRisk** | [**FindingsInnerMetaRisk**](FindingsInnerMetaRisk.md) |  |  [optional] |
|**metaTags** | **List&lt;String&gt;** |  |  [optional] |
|**metaVulnRefs** | [**FindingsInnerMetaVulnRefs**](FindingsInnerMetaVulnRefs.md) |  |  [optional] |
|**raw** | **String** |  |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) |  |  [optional] |
|**solution** | **String** |  |  [optional] |
|**targetAddrs** | **List&lt;String&gt;** |  |  [optional] |
|**targetProto** | **List&lt;String&gt;** |  |  [optional] |
|**timestamp** | **OffsetDateTime** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**type** | **String** |  |  [optional] |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| INFO | &quot;info&quot; |
| LOW | &quot;low&quot; |
| MEDIUM | &quot;medium&quot; |
| HIGH | &quot;high&quot; |



