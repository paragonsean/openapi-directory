# CloudDnsApi.ManagedZoneDnsSecConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultKeySpecs** | [**[DnsKeySpec]**](DnsKeySpec.md) | Specifies parameters for generating initial DnsKeys for this ManagedZone. Can only be changed while the state is OFF. | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#managedZoneDnsSecConfig&#39;]
**nonExistence** | **String** | Specifies the mechanism for authenticated denial-of-existence responses. Can only be changed while the state is OFF. | [optional] 
**state** | **String** | Specifies whether DNSSEC is enabled, and what mode it is in. | [optional] 



## Enum: NonExistenceEnum


* `NSEC` (value: `"NSEC"`)

* `NSEC3` (value: `"NSEC3"`)





## Enum: StateEnum


* `false` (value: `"false"`)

* `true` (value: `"true"`)

* `TRANSFER` (value: `"TRANSFER"`)




