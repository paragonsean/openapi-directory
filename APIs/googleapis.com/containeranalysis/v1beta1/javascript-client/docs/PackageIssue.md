# ContainerAnalysisApi.PackageIssue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affectedLocation** | [**VulnerabilityLocation**](VulnerabilityLocation.md) |  | [optional] 
**effectiveSeverity** | **String** | Output only. The distro or language system assigned severity for this vulnerability when that is available and note provider assigned severity when it is not available. | [optional] [readonly] 
**fixedLocation** | [**VulnerabilityLocation**](VulnerabilityLocation.md) |  | [optional] 
**packageType** | **String** | The type of package (e.g. OS, MAVEN, GO). | [optional] 
**severityName** | **String** | Deprecated, use Details.effective_severity instead The severity (e.g., distro assigned severity) for this vulnerability. | [optional] 



## Enum: EffectiveSeverityEnum


* `SEVERITY_UNSPECIFIED` (value: `"SEVERITY_UNSPECIFIED"`)

* `MINIMAL` (value: `"MINIMAL"`)

* `LOW` (value: `"LOW"`)

* `MEDIUM` (value: `"MEDIUM"`)

* `HIGH` (value: `"HIGH"`)

* `CRITICAL` (value: `"CRITICAL"`)




