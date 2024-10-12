

# WritableL2VPN


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comments** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**display** | **String** |  |  [optional] [readonly] |
|**exportTargets** | **Set&lt;Integer&gt;** |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**identifier** | **Integer** |  |  [optional] |
|**importTargets** | **Set&lt;Integer&gt;** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**slug** | **String** |  |  |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**tenant** | **Integer** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**url** | **URI** |  |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| VPWS | &quot;vpws&quot; |
| VPLS | &quot;vpls&quot; |
| VXLAN | &quot;vxlan&quot; |
| VXLAN_EVPN | &quot;vxlan-evpn&quot; |
| MPLS_EVPN | &quot;mpls-evpn&quot; |
| PBB_EVPN | &quot;pbb-evpn&quot; |
| EPL | &quot;epl&quot; |
| EVPL | &quot;evpl&quot; |
| EP_LAN | &quot;ep-lan&quot; |
| EVP_LAN | &quot;evp-lan&quot; |
| EP_TREE | &quot;ep-tree&quot; |
| EVP_TREE | &quot;evp-tree&quot; |



