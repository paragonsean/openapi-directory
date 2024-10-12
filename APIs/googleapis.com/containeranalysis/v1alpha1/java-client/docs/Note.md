

# Note

Provides a detailed description of a `Note`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attestationAuthority** | [**AttestationAuthority**](AttestationAuthority.md) |  |  [optional] |
|**baseImage** | [**Basis**](Basis.md) |  |  [optional] |
|**buildType** | [**BuildType**](BuildType.md) |  |  [optional] |
|**compliance** | [**ComplianceNote**](ComplianceNote.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time this note was created. This field can be used as a filter in list requests. |  [optional] |
|**deployable** | [**Deployable**](Deployable.md) |  |  [optional] |
|**discovery** | [**Discovery**](Discovery.md) |  |  [optional] |
|**dsseAttestation** | [**DSSEAttestationNote**](DSSEAttestationNote.md) |  |  [optional] |
|**expirationTime** | **String** | Time of expiration for this note, null if note does not expire. |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Output only. This explicitly denotes which kind of note is specified. This field can be used as a filter in list requests. |  [optional] |
|**longDescription** | **String** | A detailed description of this &#x60;Note&#x60;. |  [optional] |
|**name** | **String** | The name of the note in the form \&quot;projects/{provider_project_id}/notes/{NOTE_ID}\&quot; |  [optional] |
|**_package** | [**ModelPackage**](ModelPackage.md) |  |  [optional] |
|**relatedUrl** | [**List&lt;RelatedUrl&gt;**](RelatedUrl.md) | URLs associated with this note |  [optional] |
|**sbom** | [**DocumentNote**](DocumentNote.md) |  |  [optional] |
|**sbomReference** | [**SBOMReferenceNote**](SBOMReferenceNote.md) |  |  [optional] |
|**shortDescription** | **String** | A one sentence description of this &#x60;Note&#x60;. |  [optional] |
|**spdxFile** | [**FileNote**](FileNote.md) |  |  [optional] |
|**spdxPackage** | [**PackageInfoNote**](PackageInfoNote.md) |  |  [optional] |
|**spdxRelationship** | [**RelationshipNote**](RelationshipNote.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The time this note was last updated. This field can be used as a filter in list requests. |  [optional] |
|**upgrade** | [**UpgradeNote**](UpgradeNote.md) |  |  [optional] |
|**vulnerabilityAssessment** | [**VulnerabilityAssessmentNote**](VulnerabilityAssessmentNote.md) |  |  [optional] |
|**vulnerabilityType** | [**VulnerabilityType**](VulnerabilityType.md) |  |  [optional] |



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



