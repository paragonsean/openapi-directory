

# IPAddress


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | IPv4 or IPv6 address (with mask) |  |
|**created** | **LocalDate** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**dnsName** | **String** | Hostname or FQDN (not case-sensitive) |  [optional] |
|**family** | [**Family**](Family.md) |  |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**_interface** | [**IPAddressInterface**](IPAddressInterface.md) |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**natInside** | [**NestedIPAddress**](NestedIPAddress.md) |  |  [optional] |
|**natOutside** | [**NestedIPAddress**](NestedIPAddress.md) |  |  [optional] |
|**role** | [**Role1**](Role1.md) |  |  [optional] |
|**status** | [**Status3**](Status3.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**tenant** | [**NestedTenant**](NestedTenant.md) |  |  [optional] |
|**vrf** | [**NestedVRF**](NestedVRF.md) |  |  [optional] |



