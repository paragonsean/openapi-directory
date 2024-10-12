# FirebaseHostingApi.Certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The certificate&#39;s creation time. For &#x60;TEMPORARY&#x60; certs this is the time Hosting first generated challenges for your domain name. For all other cert types, it&#39;s the time the actual cert was created. | [optional] [readonly] 
**expireTime** | **String** | Output only. The certificate&#39;s expiration time. After this time, the cert can no longer be used to provide secure communication between Hosting and your site&#39;s visitors. | [optional] [readonly] 
**issues** | [**[Status]**](Status.md) | Output only. A set of errors Hosting encountered when attempting to create a cert for your domain name. Resolve these issues to ensure Hosting is able to provide secure communication with your site&#39;s visitors. | [optional] [readonly] 
**state** | **String** | Output only. The state of the certificate. Only the &#x60;CERT_ACTIVE&#x60; and &#x60;CERT_EXPIRING_SOON&#x60; states provide SSL coverage for a domain name. If the state is &#x60;PROPAGATING&#x60; and Hosting had an active cert for the domain name before, that formerly-active cert provides SSL coverage for the domain name until the current cert propagates. | [optional] [readonly] 
**type** | **String** | Output only. The certificate&#39;s type. | [optional] [readonly] 
**verification** | [**CertVerification**](CertVerification.md) |  | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"CERT_STATE_UNSPECIFIED"`)

* `PREPARING` (value: `"CERT_PREPARING"`)

* `VALIDATING` (value: `"CERT_VALIDATING"`)

* `PROPAGATING` (value: `"CERT_PROPAGATING"`)

* `ACTIVE` (value: `"CERT_ACTIVE"`)

* `EXPIRING_SOON` (value: `"CERT_EXPIRING_SOON"`)

* `EXPIRED` (value: `"CERT_EXPIRED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `TEMPORARY` (value: `"TEMPORARY"`)

* `GROUPED` (value: `"GROUPED"`)

* `PROJECT_GROUPED` (value: `"PROJECT_GROUPED"`)

* `DEDICATED` (value: `"DEDICATED"`)




