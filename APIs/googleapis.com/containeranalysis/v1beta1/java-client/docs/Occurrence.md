

# Occurrence

An instance of an analysis type that has been found on a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attestation** | [**Details**](Details.md) |  |  [optional] |
|**build** | [**GrafeasV1beta1BuildDetails**](GrafeasV1beta1BuildDetails.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time this occurrence was created. |  [optional] |
|**deployment** | [**GrafeasV1beta1DeploymentDetails**](GrafeasV1beta1DeploymentDetails.md) |  |  [optional] |
|**derivedImage** | [**GrafeasV1beta1ImageDetails**](GrafeasV1beta1ImageDetails.md) |  |  [optional] |
|**discovered** | [**GrafeasV1beta1DiscoveryDetails**](GrafeasV1beta1DiscoveryDetails.md) |  |  [optional] |
|**envelope** | [**Envelope**](Envelope.md) |  |  [optional] |
|**installation** | [**GrafeasV1beta1PackageDetails**](GrafeasV1beta1PackageDetails.md) |  |  [optional] |
|**intoto** | [**GrafeasV1beta1IntotoDetails**](GrafeasV1beta1IntotoDetails.md) |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Output only. This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests. |  [optional] |
|**name** | **String** | Output only. The name of the occurrence in the form of &#x60;projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]&#x60;. |  [optional] |
|**noteName** | **String** | Required. Immutable. The analysis note associated with this occurrence, in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. This field can be used as a filter in list requests. |  [optional] |
|**remediation** | **String** | A description of actions that can be taken to remedy the note. |  [optional] |
|**resource** | [**Resource**](Resource.md) |  |  [optional] |
|**sbom** | [**DocumentOccurrence**](DocumentOccurrence.md) |  |  [optional] |
|**sbomReference** | [**SBOMReferenceOccurrence**](SBOMReferenceOccurrence.md) |  |  [optional] |
|**spdxFile** | [**FileOccurrence**](FileOccurrence.md) |  |  [optional] |
|**spdxPackage** | [**PackageInfoOccurrence**](PackageInfoOccurrence.md) |  |  [optional] |
|**spdxRelationship** | [**RelationshipOccurrence**](RelationshipOccurrence.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The time this occurrence was last updated. |  [optional] |
|**vulnerability** | [**GrafeasV1beta1VulnerabilityDetails**](GrafeasV1beta1VulnerabilityDetails.md) |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| NOTE_KIND_UNSPECIFIED | &quot;NOTE_KIND_UNSPECIFIED&quot; |
| VULNERABILITY | &quot;VULNERABILITY&quot; |
| BUILD | &quot;BUILD&quot; |
| IMAGE | &quot;IMAGE&quot; |
| PACKAGE | &quot;PACKAGE&quot; |
| DEPLOYMENT | &quot;DEPLOYMENT&quot; |
| DISCOVERY | &quot;DISCOVERY&quot; |
| ATTESTATION | &quot;ATTESTATION&quot; |
| INTOTO | &quot;INTOTO&quot; |
| SBOM | &quot;SBOM&quot; |
| SPDX_PACKAGE | &quot;SPDX_PACKAGE&quot; |
| SPDX_FILE | &quot;SPDX_FILE&quot; |
| SPDX_RELATIONSHIP | &quot;SPDX_RELATIONSHIP&quot; |
| VULNERABILITY_ASSESSMENT | &quot;VULNERABILITY_ASSESSMENT&quot; |
| SBOM_REFERENCE | &quot;SBOM_REFERENCE&quot; |



