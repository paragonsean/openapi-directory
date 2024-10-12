

# Note

A type of analysis that can be done for a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attestationAuthority** | [**Authority**](Authority.md) |  |  [optional] |
|**baseImage** | [**Basis**](Basis.md) |  |  [optional] |
|**build** | [**Build**](Build.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time this note was created. This field can be used as a filter in list requests. |  [optional] |
|**deployable** | [**Deployable**](Deployable.md) |  |  [optional] |
|**discovery** | [**Discovery**](Discovery.md) |  |  [optional] |
|**expirationTime** | **String** | Time of expiration for this note. Empty if note does not expire. |  [optional] |
|**intoto** | [**InToto**](InToto.md) |  |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Output only. The type of analysis. This field can be used as a filter in list requests. |  [optional] |
|**longDescription** | **String** | A detailed description of this note. |  [optional] |
|**name** | **String** | Output only. The name of the note in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. |  [optional] |
|**_package** | [**ModelPackage**](ModelPackage.md) |  |  [optional] |
|**relatedNoteNames** | **List&lt;String&gt;** | Other notes related to this note. |  [optional] |
|**relatedUrl** | [**List&lt;RelatedUrl&gt;**](RelatedUrl.md) | URLs associated with this note. |  [optional] |
|**sbom** | [**DocumentNote**](DocumentNote.md) |  |  [optional] |
|**sbomReference** | [**SBOMReferenceNote**](SBOMReferenceNote.md) |  |  [optional] |
|**shortDescription** | **String** | A one sentence description of this note. |  [optional] |
|**spdxFile** | [**FileNote**](FileNote.md) |  |  [optional] |
|**spdxPackage** | [**PackageInfoNote**](PackageInfoNote.md) |  |  [optional] |
|**spdxRelationship** | [**RelationshipNote**](RelationshipNote.md) |  |  [optional] |
|**updateTime** | **String** | Output only. The time this note was last updated. This field can be used as a filter in list requests. |  [optional] |
|**vulnerability** | [**Vulnerability**](Vulnerability.md) |  |  [optional] |
|**vulnerabilityAssessment** | [**VulnerabilityAssessmentNote**](VulnerabilityAssessmentNote.md) |  |  [optional] |



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



