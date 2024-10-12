

# DnsRecord

DNS records are resource records that define how systems and services should behave when handling requests for a domain name. For example, when you add `A` records to your domain name's DNS records, you're informing other systems (such as your users' web browsers) to contact those IPv4 addresses to retrieve resources relevant to your domain name (such as your Hosting site files).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainName** | **String** | Output only. The domain name the record pertains to, e.g. &#x60;foo.bar.com.&#x60;. |  [optional] [readonly] |
|**rdata** | **String** | Output only. The data of the record. The meaning of the value depends on record type: - A and AAAA: IP addresses for the domain name. - CNAME: Another domain to check for records. - TXT: Arbitrary text strings associated with the domain name. Hosting uses TXT records to determine which Firebase projects have permission to act on the domain name&#39;s behalf. - CAA: The record&#39;s flags, tag, and value, e.g. &#x60;0 issue \&quot;pki.goog\&quot;&#x60;. |  [optional] [readonly] |
|**requiredAction** | [**RequiredActionEnum**](#RequiredActionEnum) | Output only. An enum that indicates the a required action for this record. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The record&#39;s type, which determines what data the record contains. |  [optional] [readonly] |



## Enum: RequiredActionEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| ADD | &quot;ADD&quot; |
| REMOVE | &quot;REMOVE&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| A | &quot;A&quot; |
| CNAME | &quot;CNAME&quot; |
| TXT | &quot;TXT&quot; |
| AAAA | &quot;AAAA&quot; |
| CAA | &quot;CAA&quot; |



