# ContainerAnalysisApi.Occurrence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestation** | [**AttestationOccurrence**](AttestationOccurrence.md) |  | [optional] 
**build** | [**BuildOccurrence**](BuildOccurrence.md) |  | [optional] 
**compliance** | [**ComplianceOccurrence**](ComplianceOccurrence.md) |  | [optional] 
**createTime** | **String** | Output only. The time this occurrence was created. | [optional] 
**deployment** | [**DeploymentOccurrence**](DeploymentOccurrence.md) |  | [optional] 
**discovery** | [**DiscoveryOccurrence**](DiscoveryOccurrence.md) |  | [optional] 
**dsseAttestation** | [**DSSEAttestationOccurrence**](DSSEAttestationOccurrence.md) |  | [optional] 
**envelope** | [**Envelope**](Envelope.md) |  | [optional] 
**image** | [**ImageOccurrence**](ImageOccurrence.md) |  | [optional] 
**kind** | **String** | Output only. This explicitly denotes which of the occurrence details are specified. This field can be used as a filter in list requests. | [optional] 
**name** | **String** | Output only. The name of the occurrence in the form of &#x60;projects/[PROJECT_ID]/occurrences/[OCCURRENCE_ID]&#x60;. | [optional] 
**noteName** | **String** | Required. Immutable. The analysis note associated with this occurrence, in the form of &#x60;projects/[PROVIDER_ID]/notes/[NOTE_ID]&#x60;. This field can be used as a filter in list requests. | [optional] 
**_package** | [**PackageOccurrence**](PackageOccurrence.md) |  | [optional] 
**remediation** | **String** | A description of actions that can be taken to remedy the note. | [optional] 
**resourceUri** | **String** | Required. Immutable. A URI that represents the resource for which the occurrence applies. For example, &#x60;https://gcr.io/project/image@sha256:123abc&#x60; for a Docker image. | [optional] 
**sbomReference** | [**SBOMReferenceOccurrence**](SBOMReferenceOccurrence.md) |  | [optional] 
**updateTime** | **String** | Output only. The time this occurrence was last updated. | [optional] 
**upgrade** | [**UpgradeOccurrence**](UpgradeOccurrence.md) |  | [optional] 
**vulnerability** | [**VulnerabilityOccurrence**](VulnerabilityOccurrence.md) |  | [optional] 



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




