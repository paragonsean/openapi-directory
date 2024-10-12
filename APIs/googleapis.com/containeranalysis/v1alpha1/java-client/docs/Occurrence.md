

# Occurrence

`Occurrence` includes information about analysis occurrences for an image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attestation** | [**Attestation**](Attestation.md) |  |  [optional] |
|**buildDetails** | [**BuildDetails**](BuildDetails.md) |  |  [optional] |
|**compliance** | [**ComplianceOccurrence**](ComplianceOccurrence.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time this &#x60;Occurrence&#x60; was created. |  [optional] |
|**deployment** | [**Deployment**](Deployment.md) |  |  [optional] |
|**derivedImage** | [**Derived**](Derived.md) |  |  [optional] |
|**discovered** | [**Discovered**](Discovered.md) |  |  [optional] |
|**dsseAttestation** | [**DSSEAttestationOccurrence**](DSSEAttestationOccurrence.md) |  |  [optional] |
|**envelope** | [**Envelope**](Envelope.md) |  |  [optional] |
|**installation** | [**Installation**](Installation.md) |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Output only. This explicitly denotes which of the &#x60;Occurrence&#x60; details are specified. This field can be used as a filter in list requests. |  [optional] |
|**name** | **String** | Output only. The name of the &#x60;Occurrence&#x60; in the form \&quot;projects/{project_id}/occurrences/{OCCURRENCE_ID}\&quot; |  [optional] |
|**noteName** | **String** | An analysis note associated with this image, in the form \&quot;providers/{provider_id}/notes/{NOTE_ID}\&quot; This field can be used as a filter in list requests. |  [optional] |
|**remediation** | **String** | A description of actions that can be taken to remedy the &#x60;Note&#x60; |  [optional] |
|**resource** | [**Resource**](Resource.md) |  |  [optional] |
|**resourceUrl** | **String** | The unique URL of the image or the container for which the &#x60;Occurrence&#x60; applies. For example, https://gcr.io/project/image@sha256:foo This field can be used as a filter in list requests. |  [optional] |
|**sbom** | [**DocumentOccurrence**](DocumentOccurrence.md) |  |  [optional] |
|**sbomReference** | [**SBOMReferenceOccurrence**](SBOMReferenceOccurrence.md) |  |  [optional] |
|**spdxFile** | [**FileOccurrence**](FileOccurrence.md) |  |  [optional] |
|**spdxPackage** | [**PackageInfoOccurrence**](PackageInfoOccurrence.md) |  |  [optional] |
|**spdxRelationship** | [**RelationshipOccurrence**](RelationshipOccurrence.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The time this &#x60;Occurrence&#x60; was last updated. |  [optional] |
|**upgrade** | [**UpgradeOccurrence**](UpgradeOccurrence.md) |  |  [optional] |
|**vulnerabilityDetails** | [**VulnerabilityDetails**](VulnerabilityDetails.md) |  |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| KIND_UNSPECIFIED | &quot;KIND_UNSPECIFIED&quot; |
| PACKAGE_VULNERABILITY | &quot;PACKAGE_VULNERABILITY&quot; |
| BUILD_DETAILS | &quot;BUILD_DETAILS&quot; |
| IMAGE_BASIS | &quot;IMAGE_BASIS&quot; |
| PACKAGE_MANAGER | &quot;PACKAGE_MANAGER&quot; |
| DEPLOYABLE | &quot;DEPLOYABLE&quot; |
| DISCOVERY | &quot;DISCOVERY&quot; |
| ATTESTATION_AUTHORITY | &quot;ATTESTATION_AUTHORITY&quot; |
| UPGRADE | &quot;UPGRADE&quot; |
| COMPLIANCE | &quot;COMPLIANCE&quot; |
| SBOM | &quot;SBOM&quot; |
| SPDX_PACKAGE | &quot;SPDX_PACKAGE&quot; |
| SPDX_FILE | &quot;SPDX_FILE&quot; |
| SPDX_RELATIONSHIP | &quot;SPDX_RELATIONSHIP&quot; |
| DSSE_ATTESTATION | &quot;DSSE_ATTESTATION&quot; |
| VULNERABILITY_ASSESSMENT | &quot;VULNERABILITY_ASSESSMENT&quot; |
| SBOM_REFERENCE | &quot;SBOM_REFERENCE&quot; |



