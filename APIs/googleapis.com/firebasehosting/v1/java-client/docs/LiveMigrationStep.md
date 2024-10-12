

# LiveMigrationStep

A set of updates including ACME challenges and DNS records that allow Hosting to create an SSL certificate and establish project ownership for your domain name before you direct traffic to Hosting servers. Use these updates to facilitate zero downtime migrations to Hosting from other services. After you've made the recommended updates, check your custom domain's `ownershipState` and `certState`. To avoid downtime, they should be `OWNERSHIP_ACTIVE` and `CERT_ACTIVE`, respectively, before you update your `A` and `AAAA` records.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certVerification** | [**CertVerification**](CertVerification.md) |  |  [optional] |
|**dnsUpdates** | [**DnsUpdates**](DnsUpdates.md) |  |  [optional] |
|**issues** | [**List&lt;Status&gt;**](Status.md) | Output only. Issues that prevent the current step from completing. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the live migration step, indicates whether you should work to complete the step now, in the future, or have already completed it. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| PREPARING | &quot;PREPARING&quot; |
| PENDING | &quot;PENDING&quot; |
| INCOMPLETE | &quot;INCOMPLETE&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



