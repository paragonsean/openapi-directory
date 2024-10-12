# ContainerAnalysisApi.Occurrence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestation** | [**Attestation**](Attestation.md) |  | [optional] 
**buildDetails** | [**BuildDetails**](BuildDetails.md) |  | [optional] 
**compliance** | [**ComplianceOccurrence**](ComplianceOccurrence.md) |  | [optional] 
**createTime** | **String** | Output only. The time this &#x60;Occurrence&#x60; was created. | [optional] 
**deployment** | [**Deployment**](Deployment.md) |  | [optional] 
**derivedImage** | [**Derived**](Derived.md) |  | [optional] 
**discovered** | [**Discovered**](Discovered.md) |  | [optional] 
**dsseAttestation** | [**DSSEAttestationOccurrence**](DSSEAttestationOccurrence.md) |  | [optional] 
**envelope** | [**Envelope**](Envelope.md) |  | [optional] 
**installation** | [**Installation**](Installation.md) |  | [optional] 
**kind** | **String** | Output only. This explicitly denotes which of the &#x60;Occurrence&#x60; details are specified. This field can be used as a filter in list requests. | [optional] 
**name** | **String** | Output only. The name of the &#x60;Occurrence&#x60; in the form \&quot;projects/{project_id}/occurrences/{OCCURRENCE_ID}\&quot; | [optional] 
**noteName** | **String** | An analysis note associated with this image, in the form \&quot;providers/{provider_id}/notes/{NOTE_ID}\&quot; This field can be used as a filter in list requests. | [optional] 
**remediation** | **String** | A description of actions that can be taken to remedy the &#x60;Note&#x60; | [optional] 
**resource** | [**Resource**](Resource.md) |  | [optional] 
**resourceUrl** | **String** | The unique URL of the image or the container for which the &#x60;Occurrence&#x60; applies. For example, https://gcr.io/project/image@sha256:foo This field can be used as a filter in list requests. | [optional] 
**sbom** | [**DocumentOccurrence**](DocumentOccurrence.md) |  | [optional] 
**sbomReference** | [**SBOMReferenceOccurrence**](SBOMReferenceOccurrence.md) |  | [optional] 
**spdxFile** | [**FileOccurrence**](FileOccurrence.md) |  | [optional] 
**spdxPackage** | [**PackageInfoOccurrence**](PackageInfoOccurrence.md) |  | [optional] 
**spdxRelationship** | [**RelationshipOccurrence**](RelationshipOccurrence.md) |  | [optional] 
**updateTime** | **String** | Output only. The time this &#x60;Occurrence&#x60; was last updated. | [optional] 
**upgrade** | [**UpgradeOccurrence**](UpgradeOccurrence.md) |  | [optional] 
**vulnerabilityDetails** | [**VulnerabilityDetails**](VulnerabilityDetails.md) |  | [optional] 



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




