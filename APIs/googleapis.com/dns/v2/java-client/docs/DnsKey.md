

# DnsKey

A DNSSEC key pair.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | String mnemonic specifying the DNSSEC algorithm of this key. Immutable after creation time. |  [optional] |
|**creationTime** | **String** | The time that this resource was created in the control plane. This is in RFC3339 text format. Output only. |  [optional] |
|**description** | **String** | A mutable string of at most 1024 characters associated with this resource for the user&#39;s convenience. Has no effect on the resource&#39;s function. |  [optional] |
|**digests** | [**List&lt;DnsKeyDigest&gt;**](DnsKeyDigest.md) | Cryptographic hashes of the DNSKEY resource record associated with this DnsKey. These digests are needed to construct a DS record that points at this DNS key. Output only. |  [optional] |
|**id** | **String** | Unique identifier for the resource; defined by the server (output only). |  [optional] |
|**isActive** | **Boolean** | Active keys are used to sign subsequent changes to the ManagedZone. Inactive keys are still present as DNSKEY Resource Records for the use of resolvers validating existing signatures. |  [optional] |
|**keyLength** | **Integer** | Length of the key in bits. Specified at creation time, and then immutable. |  [optional] |
|**keyTag** | **Integer** | The key tag is a non-cryptographic hash of the a DNSKEY resource record associated with this DnsKey. The key tag can be used to identify a DNSKEY more quickly (but it is not a unique identifier). In particular, the key tag is used in a parent zone&#39;s DS record to point at the DNSKEY in this child ManagedZone. The key tag is a number in the range [0, 65535] and the algorithm to calculate it is specified in RFC4034 Appendix B. Output only. |  [optional] |
|**kind** | **String** |  |  [optional] |
|**publicKey** | **String** | Base64 encoded public half of this key. Output only. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | One of \&quot;KEY_SIGNING\&quot; or \&quot;ZONE_SIGNING\&quot;. Keys of type KEY_SIGNING have the Secure Entry Point flag set and, when active, are used to sign only resource record sets of type DNSKEY. Otherwise, the Secure Entry Point flag is cleared, and this key is used to sign only resource record sets of other types. Immutable after creation time. |  [optional] |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| RSASHA1 | &quot;RSASHA1&quot; |
| RSASHA256 | &quot;RSASHA256&quot; |
| RSASHA512 | &quot;RSASHA512&quot; |
| ECDSAP256_SHA256 | &quot;ECDSAP256SHA256&quot; |
| ECDSAP384_SHA384 | &quot;ECDSAP384SHA384&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| KEY_SIGNING | &quot;KEY_SIGNING&quot; |
| ZONE_SIGNING | &quot;ZONE_SIGNING&quot; |



