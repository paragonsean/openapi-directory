# CertificateAuthorityApi.CertificateRevocationList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessUrl** | **String** | Output only. The location where &#39;pem_crl&#39; can be accessed. | [optional] [readonly] 
**createTime** | **String** | Output only. The time at which this CertificateRevocationList was created. | [optional] [readonly] 
**labels** | **{String: String}** | Optional. Labels with user-defined metadata. | [optional] 
**name** | **String** | Output only. The resource name for this CertificateRevocationList in the format &#x60;projects/_*_/locations/_*_/caPools/_*certificateAuthorities/_*_/ certificateRevocationLists/_*&#x60;. | [optional] [readonly] 
**pemCrl** | **String** | Output only. The PEM-encoded X.509 CRL. | [optional] [readonly] 
**revisionId** | **String** | Output only. The revision ID of this CertificateRevocationList. A new revision is committed whenever a new CRL is published. The format is an 8-character hexadecimal string. | [optional] [readonly] 
**revokedCertificates** | [**[RevokedCertificate]**](RevokedCertificate.md) | Output only. The revoked serial numbers that appear in pem_crl. | [optional] [readonly] 
**sequenceNumber** | **String** | Output only. The CRL sequence number that appears in pem_crl. | [optional] [readonly] 
**state** | **String** | Output only. The State for this CertificateRevocationList. | [optional] [readonly] 
**updateTime** | **String** | Output only. The time at which this CertificateRevocationList was updated. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `SUPERSEDED` (value: `"SUPERSEDED"`)




