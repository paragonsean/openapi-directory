# ContainerAnalysisApi.Note

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestationAuthority** | [**AttestationAuthority**](AttestationAuthority.md) |  | [optional] 
**baseImage** | [**Basis**](Basis.md) |  | [optional] 
**buildType** | [**BuildType**](BuildType.md) |  | [optional] 
**compliance** | [**ComplianceNote**](ComplianceNote.md) |  | [optional] 
**createTime** | **String** | Output only. The time this note was created. This field can be used as a filter in list requests. | [optional] 
**deployable** | [**Deployable**](Deployable.md) |  | [optional] 
**discovery** | [**Discovery**](Discovery.md) |  | [optional] 
**dsseAttestation** | [**DSSEAttestationNote**](DSSEAttestationNote.md) |  | [optional] 
**expirationTime** | **String** | Time of expiration for this note, null if note does not expire. | [optional] 
**kind** | **String** | Output only. This explicitly denotes which kind of note is specified. This field can be used as a filter in list requests. | [optional] 
**longDescription** | **String** | A detailed description of this &#x60;Note&#x60;. | [optional] 
**name** | **String** | The name of the note in the form \&quot;projects/{provider_project_id}/notes/{NOTE_ID}\&quot; | [optional] 
**_package** | [**Package**](Package.md) |  | [optional] 
**relatedUrl** | [**[RelatedUrl]**](RelatedUrl.md) | URLs associated with this note | [optional] 
**sbom** | [**DocumentNote**](DocumentNote.md) |  | [optional] 
**sbomReference** | [**SBOMReferenceNote**](SBOMReferenceNote.md) |  | [optional] 
**shortDescription** | **String** | A one sentence description of this &#x60;Note&#x60;. | [optional] 
**spdxFile** | [**FileNote**](FileNote.md) |  | [optional] 
**spdxPackage** | [**PackageInfoNote**](PackageInfoNote.md) |  | [optional] 
**spdxRelationship** | [**RelationshipNote**](RelationshipNote.md) |  | [optional] 
**updateTime** | **String** | Output only. The time this note was last updated. This field can be used as a filter in list requests. | [optional] 
**upgrade** | [**UpgradeNote**](UpgradeNote.md) |  | [optional] 
**vulnerabilityAssessment** | [**VulnerabilityAssessmentNote**](VulnerabilityAssessmentNote.md) |  | [optional] 
**vulnerabilityType** | [**VulnerabilityType**](VulnerabilityType.md) |  | [optional] 



## Enum: KindEnum


* `KIND_UNSPECIFIED` (value: `"KIND_UNSPECIFIED"`)

* `PACKAGE_VULNERABILITY` (value: `"PACKAGE_VULNERABILITY"`)

* `BUILD_DETAILS` (value: `"BUILD_DETAILS"`)

* `IMAGE_BASIS` (value: `"IMAGE_BASIS"`)

* `PACKAGE_MANAGER` (value: `"PACKAGE_MANAGER"`)

* `DEPLOYABLE` (value: `"DEPLOYABLE"`)

* `DISCOVERY` (value: `"DISCOVERY"`)

* `ATTESTATION_AUTHORITY` (value: `"ATTESTATION_AUTHORITY"`)

* `UPGRADE` (value: `"UPGRADE"`)

* `COMPLIANCE` (value: `"COMPLIANCE"`)

* `SBOM` (value: `"SBOM"`)

* `SPDX_PACKAGE` (value: `"SPDX_PACKAGE"`)

* `SPDX_FILE` (value: `"SPDX_FILE"`)

* `SPDX_RELATIONSHIP` (value: `"SPDX_RELATIONSHIP"`)

* `DSSE_ATTESTATION` (value: `"DSSE_ATTESTATION"`)

* `VULNERABILITY_ASSESSMENT` (value: `"VULNERABILITY_ASSESSMENT"`)

* `SBOM_REFERENCE` (value: `"SBOM_REFERENCE"`)




