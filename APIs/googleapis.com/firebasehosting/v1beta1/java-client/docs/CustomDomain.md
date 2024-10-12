

# CustomDomain

A `CustomDomain` is an entity that links a domain name to a Firebase Hosting site. Add a `CustomDomain` to your site to allow Hosting to serve the site's content in response to requests against your domain name.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Annotations you can add to leave both human- and machine-readable metadata about your &#x60;CustomDomain&#x60;. |  [optional] |
|**cert** | [**Certificate**](Certificate.md) |  |  [optional] |
|**certPreference** | [**CertPreferenceEnum**](#CertPreferenceEnum) | A field that lets you specify which SSL certificate type Hosting creates for your domain name. Spark plan custom domains only have access to the &#x60;GROUPED&#x60; cert type, while Blaze plan domains can select any option. |  [optional] |
|**createTime** | **String** | Output only. The custom domain&#39;s create time. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. The time the &#x60;CustomDomain&#x60; was deleted; null for custom domains that haven&#39;t been deleted. Deleted custom domains persist for approximately 30 days, after which time Hosting removes them completely. To restore a deleted custom domain, make an &#x60;UndeleteCustomDomain&#x60; request. |  [optional] [readonly] |
|**etag** | **String** | Output only. A string that represents the current state of the &#x60;CustomDomain&#x60; and allows you to confirm its initial state in requests that would modify it. Use the tag to ensure consistency when making &#x60;UpdateCustomDomain&#x60;, &#x60;DeleteCustomDomain&#x60;, and &#x60;UndeleteCustomDomain&#x60; requests. |  [optional] [readonly] |
|**expireTime** | **String** | Output only. The minimum time before a soft-deleted &#x60;CustomDomain&#x60; is completely removed from Hosting; null for custom domains that haven&#39;t been deleted. |  [optional] [readonly] |
|**hostState** | [**HostStateEnum**](#HostStateEnum) | Output only. The &#x60;HostState&#x60; of the domain name this &#x60;CustomDomain&#x60; refers to. |  [optional] [readonly] |
|**issues** | [**List&lt;Status&gt;**](Status.md) | Output only. A set of errors Hosting systems encountered when trying to establish Hosting&#39;s ability to serve secure content for your domain name. Resolve these issues to ensure your &#x60;CustomDomain&#x60; behaves properly. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Labels used for extra metadata and/or filtering. |  [optional] |
|**name** | **String** | Output only. The fully-qualified name of the &#x60;CustomDomain&#x60;. |  [optional] [readonly] |
|**ownershipState** | [**OwnershipStateEnum**](#OwnershipStateEnum) | Output only. The &#x60;OwnershipState&#x60; of the domain name this &#x60;CustomDomain&#x60; refers to. |  [optional] [readonly] |
|**reconciling** | **Boolean** | Output only. A field that, if true, indicates that Hosting&#39;s systems are attmepting to make the custom domain&#39;s state match your preferred state. This is most frequently &#x60;true&#x60; when initially provisioning a &#x60;CustomDomain&#x60; after a &#x60;CreateCustomDomain&#x60; request or when creating a new SSL certificate to match an updated &#x60;cert_preference&#x60; after an &#x60;UpdateCustomDomain&#x60; request. |  [optional] [readonly] |
|**redirectTarget** | **String** | A domain name that this &#x60;CustomDomain&#x60; should direct traffic towards. If specified, Hosting will respond to requests against this custom domain with an HTTP 301 code, and route traffic to the specified &#x60;redirect_target&#x60; instead. |  [optional] |
|**requiredDnsUpdates** | [**DnsUpdates**](DnsUpdates.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The last time the &#x60;CustomDomain&#x60; was updated. |  [optional] [readonly] |



## Enum: CertPreferenceEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| TEMPORARY | &quot;TEMPORARY&quot; |
| GROUPED | &quot;GROUPED&quot; |
| PROJECT_GROUPED | &quot;PROJECT_GROUPED&quot; |
| DEDICATED | &quot;DEDICATED&quot; |



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



