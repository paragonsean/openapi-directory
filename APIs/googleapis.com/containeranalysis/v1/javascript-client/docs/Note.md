# ContainerAnalysisApi.Note

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestation** | [**AttestationNote**](AttestationNote.md) |  | [optional] 
**build** | [**BuildNote**](BuildNote.md) |  | [optional] 
**compliance** | [**ComplianceNote**](ComplianceNote.md) |  | [optional] 
**createTime** | **String** | Output only. The time this note was created. This field can be used as a filter in list requests. | [optional] 
**deployment** | [**DeploymentNote**](DeploymentNote.md) |  | [optional] 
**discovery** | [**DiscoveryNote**](DiscoveryNote.md) |  | [optional] 
**dsseAttestation** | [**DSSEAttestationNote**](DSSEAttestationNote.md) |  | [optional] 
**expirationTime** | **String** | Time of expiration for this note. Empty if note does not expire. | [optional] 
**image** | [**ImageNote**](ImageNote.md) |  | [optional] 
**kind** | **String** | Output only. The type of analysis. This field can be used as a filter in list requests. | [optional] 
**longDescription** | **String** | A detailed description of this note. | [optional] 
**name** | **String** | Output only. The name of the note in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. | [optional] 
**_package** | [**PackageNote**](PackageNote.md) |  | [optional] 
**relatedNoteNames** | **[String]** | Other notes related to this note. | [optional] 
**relatedUrl** | [**[RelatedUrl]**](RelatedUrl.md) | URLs associated with this note. | [optional] 
**sbomReference** | [**SBOMReferenceNote**](SBOMReferenceNote.md) |  | [optional] 
**shortDescription** | **String** | A one sentence description of this note. | [optional] 
**updateTime** | **String** | Output only. The time this note was last updated. This field can be used as a filter in list requests. | [optional] 
**upgrade** | [**UpgradeNote**](UpgradeNote.md) |  | [optional] 
**vulnerability** | [**VulnerabilityNote**](VulnerabilityNote.md) |  | [optional] 
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

* `UPGRADE` (value: `"UPGRADE"`)

* `COMPLIANCE` (value: `"COMPLIANCE"`)

* `DSSE_ATTESTATION` (value: `"DSSE_ATTESTATION"`)

* `VULNERABILITY_ASSESSMENT` (value: `"VULNERABILITY_ASSESSMENT"`)

* `SBOM_REFERENCE` (value: `"SBOM_REFERENCE"`)




