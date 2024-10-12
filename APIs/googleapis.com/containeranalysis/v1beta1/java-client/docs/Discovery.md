

# Discovery

A note that indicates a type of analysis a provider would perform. This note exists in a provider's project. A `Discovery` occurrence is created in a consumer's project at the start of analysis.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysisKind** | [**AnalysisKindEnum**](#AnalysisKindEnum) | Required. Immutable. The kind of analysis that is handled by this discovery. |  [optional] |



## Enum: AnalysisKindEnum

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



