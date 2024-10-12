

# Assessment

Assessment provides all information that is related to a single vulnerability for this product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cve** | **String** | Holds the MITRE standard Common Vulnerabilities and Exposures (CVE) tracking number for the vulnerability. Deprecated: Use vulnerability_id instead to denote CVEs. |  [optional] |
|**impacts** | **List&lt;String&gt;** | Contains information about the impact of this vulnerability, this will change with time. |  [optional] |
|**justification** | [**Justification**](Justification.md) |  |  [optional] |
|**longDescription** | **String** | A detailed description of this Vex. |  [optional] |
|**relatedUris** | [**List&lt;RelatedUrl&gt;**](RelatedUrl.md) | Holds a list of references associated with this vulnerability item and assessment. These uris have additional information about the vulnerability and the assessment itself. E.g. Link to a document which details how this assessment concluded the state of this vulnerability. |  [optional] |
|**remediations** | [**List&lt;Remediation&gt;**](Remediation.md) | Specifies details on how to handle (and presumably, fix) a vulnerability. |  [optional] |
|**shortDescription** | **String** | A one sentence description of this Vex. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Provides the state of this Vulnerability assessment. |  [optional] |
|**vulnerabilityId** | **String** | The vulnerability identifier for this Assessment. Will hold one of common identifiers e.g. CVE, GHSA etc. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| AFFECTED | &quot;AFFECTED&quot; |
| NOT_AFFECTED | &quot;NOT_AFFECTED&quot; |
| FIXED | &quot;FIXED&quot; |
| UNDER_INVESTIGATION | &quot;UNDER_INVESTIGATION&quot; |



