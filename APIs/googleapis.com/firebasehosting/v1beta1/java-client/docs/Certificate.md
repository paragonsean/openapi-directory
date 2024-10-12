

# Certificate

An SSL certificate used to provide end-to-end encryption for requests against your domain name. A `Certificate` can be an actual SSL certificate or, for newly-created custom domains, Hosting's intent to create one.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The certificate&#39;s creation time. For &#x60;TEMPORARY&#x60; certs this is the time Hosting first generated challenges for your domain name. For all other cert types, it&#39;s the time the actual cert was created. |  [optional] [readonly] |
|**expireTime** | **String** | Output only. The certificate&#39;s expiration time. After this time, the cert can no longer be used to provide secure communication between Hosting and your site&#39;s visitors. |  [optional] [readonly] |
|**issues** | [**List&lt;Status&gt;**](Status.md) | Output only. A set of errors Hosting encountered when attempting to create a cert for your domain name. Resolve these issues to ensure Hosting is able to provide secure communication with your site&#39;s visitors. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the certificate. Only the &#x60;CERT_ACTIVE&#x60; and &#x60;CERT_EXPIRING_SOON&#x60; states provide SSL coverage for a domain name. If the state is &#x60;PROPAGATING&#x60; and Hosting had an active cert for the domain name before, that formerly-active cert provides SSL coverage for the domain name until the current cert propagates. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The certificate&#39;s type. |  [optional] [readonly] |
|**verification** | [**CertVerification**](CertVerification.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;CERT_STATE_UNSPECIFIED&quot; |
| PREPARING | &quot;CERT_PREPARING&quot; |
| VALIDATING | &quot;CERT_VALIDATING&quot; |
| PROPAGATING | &quot;CERT_PROPAGATING&quot; |
| ACTIVE | &quot;CERT_ACTIVE&quot; |
| EXPIRING_SOON | &quot;CERT_EXPIRING_SOON&quot; |
| EXPIRED | &quot;CERT_EXPIRED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| TEMPORARY | &quot;TEMPORARY&quot; |
| GROUPED | &quot;GROUPED&quot; |
| PROJECT_GROUPED | &quot;PROJECT_GROUPED&quot; |
| DEDICATED | &quot;DEDICATED&quot; |



