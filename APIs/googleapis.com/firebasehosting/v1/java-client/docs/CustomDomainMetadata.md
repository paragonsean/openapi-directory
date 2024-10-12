

# CustomDomainMetadata

Metadata associated with a`CustomDomain` operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certState** | [**CertStateEnum**](#CertStateEnum) | The &#x60;CertState&#x60; of the domain name&#39;s SSL certificate. |  [optional] |
|**hostState** | [**HostStateEnum**](#HostStateEnum) | The &#x60;HostState&#x60; of the domain name this &#x60;CustomDomain&#x60; refers to. |  [optional] |
|**issues** | [**List&lt;Status&gt;**](Status.md) | A list of issues that are currently preventing Hosting from completing the operation. These are generally DNS-related issues that Hosting encounters when querying a domain name&#39;s records or attempting to mint an SSL certificate. |  [optional] |
|**liveMigrationSteps** | [**List&lt;LiveMigrationStep&gt;**](LiveMigrationStep.md) | A set of DNS record updates and ACME challenges that allow you to transition domain names to Firebase Hosting with zero downtime. These updates allow Hosting to create an SSL certificate and establish ownership for your custom domain before Hosting begins serving traffic on it. If your domain name is already in active use with another provider, add one of the challenges and make the recommended DNS updates. After adding challenges and adjusting DNS records as necessary, wait for the &#x60;ownershipState&#x60; to be &#x60;OWNERSHIP_ACTIVE&#x60; and the &#x60;certState&#x60; to be &#x60;CERT_ACTIVE&#x60; before sending traffic to Hosting. |  [optional] |
|**ownershipState** | [**OwnershipStateEnum**](#OwnershipStateEnum) | The &#x60;OwnershipState&#x60; of the domain name this &#x60;CustomDomain&#x60; refers to. |  [optional] |
|**quickSetupUpdates** | [**DnsUpdates**](DnsUpdates.md) |  |  [optional] |



## Enum: CertStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;CERT_STATE_UNSPECIFIED&quot; |
| PREPARING | &quot;CERT_PREPARING&quot; |
| VALIDATING | &quot;CERT_VALIDATING&quot; |
| PROPAGATING | &quot;CERT_PROPAGATING&quot; |
| ACTIVE | &quot;CERT_ACTIVE&quot; |
| EXPIRING_SOON | &quot;CERT_EXPIRING_SOON&quot; |
| EXPIRED | &quot;CERT_EXPIRED&quot; |



## Enum: HostStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;HOST_STATE_UNSPECIFIED&quot; |
| UNHOSTED | &quot;HOST_UNHOSTED&quot; |
| UNREACHABLE | &quot;HOST_UNREACHABLE&quot; |
| MISMATCH | &quot;HOST_MISMATCH&quot; |
| CONFLICT | &quot;HOST_CONFLICT&quot; |
| ACTIVE | &quot;HOST_ACTIVE&quot; |



## Enum: OwnershipStateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;OWNERSHIP_STATE_UNSPECIFIED&quot; |
| MISSING | &quot;OWNERSHIP_MISSING&quot; |
| UNREACHABLE | &quot;OWNERSHIP_UNREACHABLE&quot; |
| MISMATCH | &quot;OWNERSHIP_MISMATCH&quot; |
| CONFLICT | &quot;OWNERSHIP_CONFLICT&quot; |
| PENDING | &quot;OWNERSHIP_PENDING&quot; |
| ACTIVE | &quot;OWNERSHIP_ACTIVE&quot; |



