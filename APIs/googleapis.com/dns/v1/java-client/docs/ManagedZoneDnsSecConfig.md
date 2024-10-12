

# ManagedZoneDnsSecConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultKeySpecs** | [**List&lt;DnsKeySpec&gt;**](DnsKeySpec.md) | Specifies parameters for generating initial DnsKeys for this ManagedZone. Can only be changed while the state is OFF. |  [optional] |
|**kind** | **String** |  |  [optional] |
|**nonExistence** | [**NonExistenceEnum**](#NonExistenceEnum) | Specifies the mechanism for authenticated denial-of-existence responses. Can only be changed while the state is OFF. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Specifies whether DNSSEC is enabled, and what mode it is in. |  [optional] |



## Enum: NonExistenceEnum

| Name | Value |
|---- | -----|
| NSEC | &quot;nsec&quot; |
| NSEC3 | &quot;nsec3&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| FALSE | &quot;false&quot; |
| TRUE | &quot;true&quot; |
| TRANSFER | &quot;transfer&quot; |



