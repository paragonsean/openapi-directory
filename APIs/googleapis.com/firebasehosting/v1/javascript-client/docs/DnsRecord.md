# FirebaseHostingApi.DnsRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainName** | **String** | Output only. The domain name the record pertains to, e.g. &#x60;foo.bar.com.&#x60;. | [optional] [readonly] 
**rdata** | **String** | Output only. The data of the record. The meaning of the value depends on record type: - A and AAAA: IP addresses for the domain name. - CNAME: Another domain to check for records. - TXT: Arbitrary text strings associated with the domain name. Hosting uses TXT records to determine which Firebase projects have permission to act on the domain name&#39;s behalf. - CAA: The record&#39;s flags, tag, and value, e.g. &#x60;0 issue \&quot;pki.goog\&quot;&#x60;. | [optional] [readonly] 
**requiredAction** | **String** | Output only. An enum that indicates the a required action for this record. | [optional] [readonly] 
**type** | **String** | Output only. The record&#39;s type, which determines what data the record contains. | [optional] [readonly] 



## Enum: RequiredActionEnum


* `NONE` (value: `"NONE"`)

* `ADD` (value: `"ADD"`)

* `REMOVE` (value: `"REMOVE"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `A` (value: `"A"`)

* `CNAME` (value: `"CNAME"`)

* `TXT` (value: `"TXT"`)

* `AAAA` (value: `"AAAA"`)

* `CAA` (value: `"CAA"`)




