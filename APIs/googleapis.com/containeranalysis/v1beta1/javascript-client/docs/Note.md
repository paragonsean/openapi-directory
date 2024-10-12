# ContainerAnalysisApi.Note

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestationAuthority** | [**Authority**](Authority.md) |  | [optional] 
**baseImage** | [**Basis**](Basis.md) |  | [optional] 
**build** | [**Build**](Build.md) |  | [optional] 
**createTime** | **String** | Output only. The time this note was created. This field can be used as a filter in list requests. | [optional] 
**deployable** | [**Deployable**](Deployable.md) |  | [optional] 
**discovery** | [**Discovery**](Discovery.md) |  | [optional] 
**expirationTime** | **String** | Time of expiration for this note. Empty if note does not expire. | [optional] 
**intoto** | [**InToto**](InToto.md) |  | [optional] 
**kind** | **String** | Output only. The type of analysis. This field can be used as a filter in list requests. | [optional] 
**longDescription** | **String** | A detailed description of this note. | [optional] 
**name** | **String** | Output only. The name of the note in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | [optional] 
**_package** | [**Package**](Package.md) |  | [optional] 
**relatedNoteNames** | **[String]** | Other notes related to this note. | [optional] 
**relatedUrl** | [**[RelatedUrl]**](RelatedUrl.md) | URLs associated with this note. | [optional] 
**sbom** | [**DocumentNote**](DocumentNote.md) |  | [optional] 
**sbomReference** | [**SBOMReferenceNote**](SBOMReferenceNote.md) |  | [optional] 
**shortDescription** | **String** | A one sentence description of this note. | [optional] 
**spdxFile** | [**FileNote**](FileNote.md) |  | [optional] 
**spdxPackage** | [**PackageInfoNote**](PackageInfoNote.md) |  | [optional] 
**spdxRelationship** | [**RelationshipNote**](RelationshipNote.md) |  | [optional] 
**updateTime** | **String** | Output only. The time this note was last updated. This field can be used as a filter in list requests. | [optional] 
**vulnerability** | [**Vulnerability**](Vulnerability.md) |  | [optional] 
**vulnerabilityAssessment** | [**VulnerabilityAssessmentNote**](VulnerabilityAssessmentNote.md) |  | [optional] 



## Enum: KindEnum


* `NOTE_KIND_UNSPECIFIED` (value: `"NOTE_KIND_UNSPECIFIED"`)

* `VULNERABILITY` (value: `"VULNERABILITY"`)

* `BUILD` (value: `"BUILD"`)

* `IMAGE` (value: `"IMAGE"`)

* `PACKAGE` (value: `"PACKAGE"`)

* `DEPLOYMENT` (value: `"DEPLOYMENT"`)

* `DISCOVERY` (value: `"DISCOVERY"`)

* `ATTESTATION` (value: `"ATTESTATION"`)

* `INTOTO` (value: `"INTOTO"`)

* `SBOM` (value: `"SBOM"`)

* `SPDX_PACKAGE` (value: `"SPDX_PACKAGE"`)

* `SPDX_FILE` (value: `"SPDX_FILE"`)

* `SPDX_RELATIONSHIP` (value: `"SPDX_RELATIONSHIP"`)

* `VULNERABILITY_ASSESSMENT` (value: `"VULNERABILITY_ASSESSMENT"`)

* `SBOM_REFERENCE` (value: `"SBOM_REFERENCE"`)




