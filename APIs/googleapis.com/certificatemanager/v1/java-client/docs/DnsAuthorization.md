

# DnsAuthorization

A DnsAuthorization resource describes a way to perform domain authorization for certificate issuance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The creation timestamp of a DnsAuthorization. |  [optional] [readonly] |
|**description** | **String** | One or more paragraphs of text description of a DnsAuthorization. |  [optional] |
|**dnsResourceRecord** | [**DnsResourceRecord**](DnsResourceRecord.md) |  |  [optional] |
|**domain** | **String** | Required. Immutable. A domain that is being authorized. A DnsAuthorization resource covers a single domain and its wildcard, e.g. authorization for &#x60;example.com&#x60; can be used to issue certificates for &#x60;example.com&#x60; and &#x60;*.example.com&#x60;. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Set of labels associated with a DnsAuthorization. |  [optional] |
|**name** | **String** | A user-defined name of the dns authorization. DnsAuthorization names must be unique globally and match pattern &#x60;projects/_*_/locations/_*_/dnsAuthorizations/_*&#x60;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Immutable. Type of DnsAuthorization. If unset during resource creation the following default will be used: - in location global: FIXED_RECORD. |  [optional] |
|**updateTime** | **String** | Output only. The last update timestamp of a DnsAuthorization. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| FIXED_RECORD | &quot;FIXED_RECORD&quot; |
| PER_PROJECT_RECORD | &quot;PER_PROJECT_RECORD&quot; |



