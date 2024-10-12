

# Spoke

A Spoke is an abstraction of a network attachment being attached to a Hub. A Spoke can be underlying a VPN tunnel, a VLAN (interconnect) attachment, a Router appliance, etc.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | The time when the Spoke was created. |  [optional] |
|**description** | **String** | Short description of the spoke resource |  [optional] |
|**hub** | **String** | The resource URL of the hub resource that the spoke is attached to |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels. |  [optional] |
|**linkedInterconnectAttachments** | **List&lt;String&gt;** | The URIs of linked interconnect attachment resources |  [optional] |
|**linkedRouterApplianceInstances** | [**List&lt;RouterApplianceInstance&gt;**](RouterApplianceInstance.md) | The URIs of linked Router appliance resources |  [optional] |
|**linkedVpnTunnels** | **List&lt;String&gt;** | The URIs of linked VPN tunnel resources |  [optional] |
|**name** | **String** | Immutable. The name of a Spoke resource. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current lifecycle state of this Hub. |  [optional] [readonly] |
|**uniqueId** | **String** | Output only. Google-generated UUID for this resource. This is unique across all Spoke resources. If a Spoke resource is deleted and another with the same name is created, it gets a different unique_id. |  [optional] [readonly] |
|**updateTime** | **String** | The time when the Spoke was updated. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DELETING | &quot;DELETING&quot; |
| UPDATING | &quot;UPDATING&quot; |



