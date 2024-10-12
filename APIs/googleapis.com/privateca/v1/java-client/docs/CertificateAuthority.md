

# CertificateAuthority

A CertificateAuthority represents an individual Certificate Authority. A CertificateAuthority can be used to create Certificates.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessUrls** | [**AccessUrls**](AccessUrls.md) |  |  [optional] |
|**caCertificateDescriptions** | [**List&lt;CertificateDescription&gt;**](CertificateDescription.md) | Output only. A structured description of this CertificateAuthority&#39;s CA certificate and its issuers. Ordered as self-to-root. |  [optional] [readonly] |
|**config** | [**CertificateConfig**](CertificateConfig.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time at which this CertificateAuthority was created. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. The time at which this CertificateAuthority was soft deleted, if it is in the DELETED state. |  [optional] [readonly] |
|**expireTime** | **String** | Output only. The time at which this CertificateAuthority will be permanently purged, if it is in the DELETED state. |  [optional] [readonly] |
|**gcsBucket** | **String** | Immutable. The name of a Cloud Storage bucket where this CertificateAuthority will publish content, such as the CA certificate and CRLs. This must be a bucket name, without any prefixes (such as &#x60;gs://&#x60;) or suffixes (such as &#x60;.googleapis.com&#x60;). For example, to use a bucket named &#x60;my-bucket&#x60;, you would simply specify &#x60;my-bucket&#x60;. If not specified, a managed bucket will be created. |  [optional] |
|**keySpec** | [**KeyVersionSpec**](KeyVersionSpec.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Labels with user-defined metadata. |  [optional] |
|**lifetime** | **String** | Required. Immutable. The desired lifetime of the CA certificate. Used to create the \&quot;not_before_time\&quot; and \&quot;not_after_time\&quot; fields inside an X.509 certificate. |  [optional] |
|**name** | **String** | Output only. The resource name for this CertificateAuthority in the format &#x60;projects/_*_/locations/_*_/caPools/_*_/certificateAuthorities/_*&#x60;. |  [optional] [readonly] |
|**pemCaCertificates** | **List&lt;String&gt;** | Output only. This CertificateAuthority&#39;s certificate chain, including the current CertificateAuthority&#39;s certificate. Ordered such that the root issuer is the final element (consistent with RFC 5246). For a self-signed CA, this will only list the current CertificateAuthority&#39;s certificate. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The State for this CertificateAuthority. |  [optional] [readonly] |
|**subordinateConfig** | [**SubordinateConfig**](SubordinateConfig.md) |  |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | Output only. The CaPool.Tier of the CaPool that includes this CertificateAuthority. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Immutable. The Type of this CertificateAuthority. |  [optional] |
|**updateTime** | **String** | Output only. The time at which this CertificateAuthority was last updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ENABLED | &quot;ENABLED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| STAGED | &quot;STAGED&quot; |
| AWAITING_USER_ACTIVATION | &quot;AWAITING_USER_ACTIVATION&quot; |
| DELETED | &quot;DELETED&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| TIER_UNSPECIFIED | &quot;TIER_UNSPECIFIED&quot; |
| ENTERPRISE | &quot;ENTERPRISE&quot; |
| DEVOPS | &quot;DEVOPS&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| SELF_SIGNED | &quot;SELF_SIGNED&quot; |
| SUBORDINATE | &quot;SUBORDINATE&quot; |



