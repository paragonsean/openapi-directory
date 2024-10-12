

# DomainProvisioning

The current certificate provisioning status information for a domain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certChallengeDiscoveredTxt** | **List&lt;String&gt;** | The TXT records (for the certificate challenge) that were found at the last DNS fetch. |  [optional] |
|**certChallengeDns** | [**CertDnsChallenge**](CertDnsChallenge.md) |  |  [optional] |
|**certChallengeHttp** | [**CertHttpChallenge**](CertHttpChallenge.md) |  |  [optional] |
|**certStatus** | [**CertStatusEnum**](#CertStatusEnum) | The certificate provisioning status; updated when Firebase Hosting provisions an SSL certificate for the domain. |  [optional] |
|**discoveredIps** | **List&lt;String&gt;** | The IPs found at the last DNS fetch. |  [optional] |
|**dnsFetchTime** | **String** | The time at which the last DNS fetch occurred. |  [optional] |
|**dnsStatus** | [**DnsStatusEnum**](#DnsStatusEnum) | The DNS record match status as of the last DNS fetch. |  [optional] |
|**expectedIps** | **List&lt;String&gt;** | The list of IPs to which the domain is expected to resolve. |  [optional] |



## Enum: CertStatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;CERT_STATUS_UNSPECIFIED&quot; |
| PENDING | &quot;CERT_PENDING&quot; |
| MISSING | &quot;CERT_MISSING&quot; |
| PROCESSING | &quot;CERT_PROCESSING&quot; |
| PROPAGATING | &quot;CERT_PROPAGATING&quot; |
| ACTIVE | &quot;CERT_ACTIVE&quot; |
| ERROR | &quot;CERT_ERROR&quot; |



## Enum: DnsStatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;DNS_STATUS_UNSPECIFIED&quot; |
| PENDING | &quot;DNS_PENDING&quot; |
| MISSING | &quot;DNS_MISSING&quot; |
| PARTIAL_MATCH | &quot;DNS_PARTIAL_MATCH&quot; |
| MATCH | &quot;DNS_MATCH&quot; |
| EXTRANEOUS_MATCH | &quot;DNS_EXTRANEOUS_MATCH&quot; |



