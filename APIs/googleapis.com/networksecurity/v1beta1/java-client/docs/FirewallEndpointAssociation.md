

# FirewallEndpointAssociation

Message describing Association object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Create time stamp |  [optional] [readonly] |
|**firewallEndpoint** | **String** | Required. The URL of the FirewallEndpoint that is being associated. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Labels as key value pairs |  [optional] |
|**name** | **String** | Immutable. Identifier. name of resource |  [optional] |
|**network** | **String** | Required. The URL of the network that is being associated. |  [optional] |
|**reconciling** | **Boolean** | Output only. Whether reconciling is in progress, recommended per https://google.aip.dev/128. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the association. |  [optional] [readonly] |
|**tlsInspectionPolicy** | **String** | Optional. The URL of the TlsInspectionPolicy that is being associated. |  [optional] |
|**updateTime** | **String** | Output only. Update time stamp |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| INACTIVE | &quot;INACTIVE&quot; |



