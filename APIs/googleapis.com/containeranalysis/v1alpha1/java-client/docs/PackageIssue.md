

# PackageIssue

This message wraps a location affected by a vulnerability and its associated fix (if one is available).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**affectedLocation** | [**VulnerabilityLocation**](VulnerabilityLocation.md) |  |  [optional] |
|**effectiveSeverity** | [**EffectiveSeverityEnum**](#EffectiveSeverityEnum) | Output only. The distro or language system assigned severity for this vulnerability when that is available and note provider assigned severity when distro or language system has not yet assigned a severity for this vulnerability. |  [optional] [readonly] |
|**fixedLocation** | [**VulnerabilityLocation**](VulnerabilityLocation.md) |  |  [optional] |
|**packageType** | **String** | The type of package (e.g. OS, MAVEN, GO). |  [optional] |
|**severityName** | **String** |  |  [optional] |



## Enum: EffectiveSeverityEnum

| Name | Value |
|---- | -----|
| SEVERITY_UNSPECIFIED | &quot;SEVERITY_UNSPECIFIED&quot; |
| MINIMAL | &quot;MINIMAL&quot; |
| LOW | &quot;LOW&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| HIGH | &quot;HIGH&quot; |
| CRITICAL | &quot;CRITICAL&quot; |



