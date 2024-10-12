# CertificateManagerApi.DnsAuthorization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The creation timestamp of a DnsAuthorization. | [optional] [readonly] 
**description** | **String** | One or more paragraphs of text description of a DnsAuthorization. | [optional] 
**dnsResourceRecord** | [**DnsResourceRecord**](DnsResourceRecord.md) |  | [optional] 
**domain** | **String** | Required. Immutable. A domain that is being authorized. A DnsAuthorization resource covers a single domain and its wildcard, e.g. authorization for &#x60;example.com&#x60; can be used to issue certificates for &#x60;example.com&#x60; and &#x60;*.example.com&#x60;. | [optional] 
**labels** | **{String: String}** | Set of labels associated with a DnsAuthorization. | [optional] 
**name** | **String** | A user-defined name of the dns authorization. DnsAuthorization names must be unique globally and match pattern &#x60;projects/_*_/locations/_*_/dnsAuthorizations/_*&#x60;. | [optional] 
**type** | **String** | Immutable. Type of DnsAuthorization. If unset during resource creation the following default will be used: - in location global: FIXED_RECORD. | [optional] 
**updateTime** | **String** | Output only. The last update timestamp of a DnsAuthorization. | [optional] [readonly] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `FIXED_RECORD` (value: `"FIXED_RECORD"`)

* `PER_PROJECT_RECORD` (value: `"PER_PROJECT_RECORD"`)




