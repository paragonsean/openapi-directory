

# DnsKeySpec

Parameters for DnsKey key generation. Used for generating initial keys for a new ManagedZone and as default when adding a new DnsKey.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | String mnemonic specifying the DNSSEC algorithm of this key. |  [optional] |
|**keyLength** | **Integer** | Length of the keys in bits. |  [optional] |
|**keyType** | [**KeyTypeEnum**](#KeyTypeEnum) | Specifies whether this is a key signing key (KSK) or a zone signing key (ZSK). Key signing keys have the Secure Entry Point flag set and, when active, are only used to sign resource record sets of type DNSKEY. Zone signing keys do not have the Secure Entry Point flag set and are used to sign all other types of resource record sets. |  [optional] |
|**kind** | **String** |  |  [optional] |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| RSASHA1 | &quot;RSASHA1&quot; |
| RSASHA256 | &quot;RSASHA256&quot; |
| RSASHA512 | &quot;RSASHA512&quot; |
| ECDSAP256_SHA256 | &quot;ECDSAP256SHA256&quot; |
| ECDSAP384_SHA384 | &quot;ECDSAP384SHA384&quot; |



## Enum: KeyTypeEnum

| Name | Value |
|---- | -----|
| KEY_SIGNING | &quot;KEY_SIGNING&quot; |
| ZONE_SIGNING | &quot;ZONE_SIGNING&quot; |



