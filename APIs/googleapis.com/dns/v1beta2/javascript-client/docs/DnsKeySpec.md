# CloudDnsApi.DnsKeySpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | String mnemonic specifying the DNSSEC algorithm of this key. | [optional] 
**keyLength** | **Number** | Length of the keys in bits. | [optional] 
**keyType** | **String** | Specifies whether this is a key signing key (KSK) or a zone signing key (ZSK). Key signing keys have the Secure Entry Point flag set and, when active, are only used to sign resource record sets of type DNSKEY. Zone signing keys do not have the Secure Entry Point flag set and are used to sign all other types of resource record sets. | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#dnsKeySpec&#39;]



## Enum: AlgorithmEnum


* `rsasha1` (value: `"rsasha1"`)

* `rsasha256` (value: `"rsasha256"`)

* `rsasha512` (value: `"rsasha512"`)

* `ecdsap256sha256` (value: `"ecdsap256sha256"`)

* `ecdsap384sha384` (value: `"ecdsap384sha384"`)





## Enum: KeyTypeEnum


* `keySigning` (value: `"keySigning"`)

* `zoneSigning` (value: `"zoneSigning"`)




