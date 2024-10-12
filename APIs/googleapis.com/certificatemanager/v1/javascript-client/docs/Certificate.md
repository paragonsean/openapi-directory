# CertificateManagerApi.Certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The creation timestamp of a Certificate. | [optional] [readonly] 
**description** | **String** | One or more paragraphs of text description of a certificate. | [optional] 
**expireTime** | **String** | Output only. The expiry timestamp of a Certificate. | [optional] [readonly] 
**labels** | **{String: String}** | Set of labels associated with a Certificate. | [optional] 
**managed** | [**ManagedCertificate**](ManagedCertificate.md) |  | [optional] 
**name** | **String** | A user-defined name of the certificate. Certificate names must be unique globally and match pattern &#x60;projects/_*_/locations/_*_/certificates/_*&#x60;. | [optional] 
**pemCertificate** | **String** | Output only. The PEM-encoded certificate chain. | [optional] [readonly] 
**sanDnsnames** | **[String]** | Output only. The list of Subject Alternative Names of dnsName type defined in the certificate (see RFC 5280 4.2.1.6). Managed certificates that haven&#39;t been provisioned yet have this field populated with a value of the managed.domains field. | [optional] [readonly] 
**scope** | **String** | Immutable. The scope of the certificate. | [optional] 
**selfManaged** | [**SelfManagedCertificate**](SelfManagedCertificate.md) |  | [optional] 
**updateTime** | **String** | Output only. The last update timestamp of a Certificate. | [optional] [readonly] 



## Enum: ScopeEnum


* `DEFAULT` (value: `"DEFAULT"`)

* `EDGE_CACHE` (value: `"EDGE_CACHE"`)

* `ALL_REGIONS` (value: `"ALL_REGIONS"`)




