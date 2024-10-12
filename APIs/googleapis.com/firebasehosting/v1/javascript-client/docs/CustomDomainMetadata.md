# FirebaseHostingApi.CustomDomainMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certState** | **String** | The &#x60;CertState&#x60; of the domain name&#39;s SSL certificate. | [optional] 
**hostState** | **String** | The &#x60;HostState&#x60; of the domain name this &#x60;CustomDomain&#x60; refers to. | [optional] 
**issues** | [**[Status]**](Status.md) | A list of issues that are currently preventing Hosting from completing the operation. These are generally DNS-related issues that Hosting encounters when querying a domain name&#39;s records or attempting to mint an SSL certificate. | [optional] 
**liveMigrationSteps** | [**[LiveMigrationStep]**](LiveMigrationStep.md) | A set of DNS record updates and ACME challenges that allow you to transition domain names to Firebase Hosting with zero downtime. These updates allow Hosting to create an SSL certificate and establish ownership for your custom domain before Hosting begins serving traffic on it. If your domain name is already in active use with another provider, add one of the challenges and make the recommended DNS updates. After adding challenges and adjusting DNS records as necessary, wait for the &#x60;ownershipState&#x60; to be &#x60;OWNERSHIP_ACTIVE&#x60; and the &#x60;certState&#x60; to be &#x60;CERT_ACTIVE&#x60; before sending traffic to Hosting. | [optional] 
**ownershipState** | **String** | The &#x60;OwnershipState&#x60; of the domain name this &#x60;CustomDomain&#x60; refers to. | [optional] 
**quickSetupUpdates** | [**DnsUpdates**](DnsUpdates.md) |  | [optional] 



## Enum: CertStateEnum


* `STATE_UNSPECIFIED` (value: `"CERT_STATE_UNSPECIFIED"`)

* `PREPARING` (value: `"CERT_PREPARING"`)

* `VALIDATING` (value: `"CERT_VALIDATING"`)

* `PROPAGATING` (value: `"CERT_PROPAGATING"`)

* `ACTIVE` (value: `"CERT_ACTIVE"`)

* `EXPIRING_SOON` (value: `"CERT_EXPIRING_SOON"`)

* `EXPIRED` (value: `"CERT_EXPIRED"`)





## Enum: HostStateEnum


* `STATE_UNSPECIFIED` (value: `"HOST_STATE_UNSPECIFIED"`)

* `UNHOSTED` (value: `"HOST_UNHOSTED"`)

* `UNREACHABLE` (value: `"HOST_UNREACHABLE"`)

* `MISMATCH` (value: `"HOST_MISMATCH"`)

* `CONFLICT` (value: `"HOST_CONFLICT"`)

* `ACTIVE` (value: `"HOST_ACTIVE"`)





## Enum: OwnershipStateEnum


* `STATE_UNSPECIFIED` (value: `"OWNERSHIP_STATE_UNSPECIFIED"`)

* `MISSING` (value: `"OWNERSHIP_MISSING"`)

* `UNREACHABLE` (value: `"OWNERSHIP_UNREACHABLE"`)

* `MISMATCH` (value: `"OWNERSHIP_MISMATCH"`)

* `CONFLICT` (value: `"OWNERSHIP_CONFLICT"`)

* `PENDING` (value: `"OWNERSHIP_PENDING"`)

* `ACTIVE` (value: `"OWNERSHIP_ACTIVE"`)




