# ContainerAnalysisApi.VexAssessment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **String** | Holds the MITRE standard Common Vulnerabilities and Exposures (CVE) tracking number for the vulnerability. | [optional] 
**impacts** | **[String]** | Contains information about the impact of this vulnerability, this will change with time. | [optional] 
**justification** | [**Justification**](Justification.md) |  | [optional] 
**noteName** | **String** | The VulnerabilityAssessment note from which this VexAssessment was generated. This will be of the form: &#x60;projects/[PROJECT_ID]/notes/[NOTE_ID]&#x60;. | [optional] 
**relatedUris** | **[String]** | Holds a list of references associated with this vulnerability item and assessment. These uris have additional information about the vulnerability and the assessment itself. E.g. Link to a document which details how this assessment concluded the state of this vulnerability. | [optional] 
**remediations** | [**[Remediation]**](Remediation.md) | Specifies details on how to handle (and presumably, fix) a vulnerability. | [optional] 
**state** | **String** | Provides the state of this Vulnerability assessment. | [optional] 
**vulnerabilityId** | **String** | The vulnerability identifier for this Assessment. Will hold one of common identifiers e.g. CVE, GHSA etc. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `AFFECTED` (value: `"AFFECTED"`)

* `NOT_AFFECTED` (value: `"NOT_AFFECTED"`)

* `FIXED` (value: `"FIXED"`)

* `UNDER_INVESTIGATION` (value: `"UNDER_INVESTIGATION"`)




