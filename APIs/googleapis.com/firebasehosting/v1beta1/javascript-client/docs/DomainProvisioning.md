# FirebaseHostingApi.DomainProvisioning

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certChallengeDiscoveredTxt** | **[String]** | The TXT records (for the certificate challenge) that were found at the last DNS fetch. | [optional] 
**certChallengeDns** | [**CertDnsChallenge**](CertDnsChallenge.md) |  | [optional] 
**certChallengeHttp** | [**CertHttpChallenge**](CertHttpChallenge.md) |  | [optional] 
**certStatus** | **String** | The certificate provisioning status; updated when Firebase Hosting provisions an SSL certificate for the domain. | [optional] 
**discoveredIps** | **[String]** | The IPs found at the last DNS fetch. | [optional] 
**dnsFetchTime** | **String** | The time at which the last DNS fetch occurred. | [optional] 
**dnsStatus** | **String** | The DNS record match status as of the last DNS fetch. | [optional] 
**expectedIps** | **[String]** | The list of IPs to which the domain is expected to resolve. | [optional] 



## Enum: CertStatusEnum


* `STATUS_UNSPECIFIED` (value: `"CERT_STATUS_UNSPECIFIED"`)

* `PENDING` (value: `"CERT_PENDING"`)

* `MISSING` (value: `"CERT_MISSING"`)

* `PROCESSING` (value: `"CERT_PROCESSING"`)

* `PROPAGATING` (value: `"CERT_PROPAGATING"`)

* `ACTIVE` (value: `"CERT_ACTIVE"`)

* `ERROR` (value: `"CERT_ERROR"`)





## Enum: DnsStatusEnum


* `STATUS_UNSPECIFIED` (value: `"DNS_STATUS_UNSPECIFIED"`)

* `PENDING` (value: `"DNS_PENDING"`)

* `MISSING` (value: `"DNS_MISSING"`)

* `PARTIAL_MATCH` (value: `"DNS_PARTIAL_MATCH"`)

* `MATCH` (value: `"DNS_MATCH"`)

* `EXTRANEOUS_MATCH` (value: `"DNS_EXTRANEOUS_MATCH"`)




