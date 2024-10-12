# CloudDnsApi.DnsKeySpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | String mnemonic specifying the DNSSEC algorithm of this key. | [optional] 
**keyLength** | **Number** | Length of the keys in bits. | [optional] 
**keyType** | **String** | Specifies whether this is a key signing key (KSK) or a zone signing key (ZSK). Key signing keys have the Secure Entry Point flag set and, when active, are only used to sign resource record sets of type DNSKEY. Zone signing keys do not have the Secure Entry Point flag set and are used to sign all other types of resource record sets. | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#dnsKeySpec&#39;]



## Enum: AlgorithmEnum


* `RSASHA1` (value: `"RSASHA1"`)

* `RSASHA256` (value: `"RSASHA256"`)

* `RSASHA512` (value: `"RSASHA512"`)

* `ECDSAP256SHA256` (value: `"ECDSAP256SHA256"`)

* `ECDSAP384SHA384` (value: `"ECDSAP384SHA384"`)





## Enum: KeyTypeEnum


* `KEY_SIGNING` (value: `"KEY_SIGNING"`)

* `ZONE_SIGNING` (value: `"ZONE_SIGNING"`)




