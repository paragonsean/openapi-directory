

# FirewallEndpoint

Message describing Endpoint object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associatedNetworks** | **List&lt;String&gt;** | Output only. List of networks that are associated with this endpoint in the local zone. This is a projection of the FirewallEndpointAssociations pointing at this endpoint. A network will only appear in this list after traffic routing is fully configured. Format: projects/{project}/global/networks/{name}. |  [optional] [readonly] |
|**associations** | [**List&lt;FirewallEndpointAssociationReference&gt;**](FirewallEndpointAssociationReference.md) | Output only. List of FirewallEndpointAssociations that are associated to this endpoint. An association will only appear in this list after traffic routing is fully configured. |  [optional] [readonly] |
|**billingProjectId** | **String** | Required. Project to bill on endpoint uptime usage. |  [optional] |
|**createTime** | **String** | Output only. Create time stamp |  [optional] [readonly] |
|**description** | **String** | Optional. Description of the firewall endpoint. Max length 2048 characters. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Labels as key value pairs |  [optional] |
|**name** | **String** | Immutable. Identifier. name of resource |  [optional] |
|**reconciling** | **Boolean** | Output only. Whether reconciling is in progress, recommended per https://google.aip.dev/128. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the endpoint. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Update time stamp |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| INACTIVE | &quot;INACTIVE&quot; |



