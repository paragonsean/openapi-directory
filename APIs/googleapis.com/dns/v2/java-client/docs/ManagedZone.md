

# ManagedZone

A zone is a subtree of the DNS namespace under one administrative responsibility. A ManagedZone is a resource that represents a DNS zone hosted by the Cloud DNS service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudLoggingConfig** | [**ManagedZoneCloudLoggingConfig**](ManagedZoneCloudLoggingConfig.md) |  |  [optional] |
|**creationTime** | **String** | The time that this resource was created on the server. This is in RFC3339 text format. Output only. |  [optional] |
|**description** | **String** | A mutable string of at most 1024 characters associated with this resource for the user&#39;s convenience. Has no effect on the managed zone&#39;s function. |  [optional] |
|**dnsName** | **String** | The DNS name of this managed zone, for instance \&quot;example.com.\&quot;. |  [optional] |
|**dnssecConfig** | [**ManagedZoneDnsSecConfig**](ManagedZoneDnsSecConfig.md) |  |  [optional] |
|**forwardingConfig** | [**ManagedZoneForwardingConfig**](ManagedZoneForwardingConfig.md) |  |  [optional] |
|**id** | **String** | Unique identifier for the resource; defined by the server (output only) |  [optional] |
|**kind** | **String** |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | User labels. |  [optional] |
|**name** | **String** | User assigned name for this resource. Must be unique within the project. The name must be 1-63 characters long, must begin with a letter, end with a letter or digit, and only contain lowercase letters, digits or dashes. |  [optional] |
|**nameServerSet** | **String** | Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet is a set of DNS name servers that all host the same ManagedZones. Most users leave this field unset. If you need to use this field, contact your account team. |  [optional] |
|**nameServers** | **List&lt;String&gt;** | Delegate your managed_zone to these virtual name servers; defined by the server (output only) |  [optional] |
|**peeringConfig** | [**ManagedZonePeeringConfig**](ManagedZonePeeringConfig.md) |  |  [optional] |
|**privateVisibilityConfig** | [**ManagedZonePrivateVisibilityConfig**](ManagedZonePrivateVisibilityConfig.md) |  |  [optional] |
|**reverseLookupConfig** | [**ManagedZoneReverseLookupConfig**](ManagedZoneReverseLookupConfig.md) |  |  [optional] |
|**serviceDirectoryConfig** | [**ManagedZoneServiceDirectoryConfig**](ManagedZoneServiceDirectoryConfig.md) |  |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | The zone&#39;s visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources. |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;PUBLIC&quot; |
| PRIVATE | &quot;PRIVATE&quot; |



