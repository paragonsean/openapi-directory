

# Discovery

A note that indicates a type of analysis a provider would perform. This note exists in a provider's project. A `Discovery` occurrence is created in a consumer's project at the start of analysis. The occurrence's operation will indicate the status of the analysis. Absence of an occurrence linked to this note for a resource indicates that analysis hasn't started.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysisKind** | [**AnalysisKindEnum**](#AnalysisKindEnum) | The kind of analysis that is handled by this discovery. |  [optional] |



## Enum: AnalysisKindEnum

| Name | Value |
|---- | -----|
| KIND_UNSPECIFIED | &quot;KIND_UNSPECIFIED&quot; |
| PACKAGE_VULNERABILITY | &quot;PACKAGE_VULNERABILITY&quot; |
| BUILD_DETAILS | &quot;BUILD_DETAILS&quot; |
| IMAGE_BASIS | &quot;IMAGE_BASIS&quot; |
| PACKAGE_MANAGER | &quot;PACKAGE_MANAGER&quot; |
| DEPLOYABLE | &quot;DEPLOYABLE&quot; |
| DISCOVERY | &quot;DISCOVERY&quot; |
| ATTESTATION_AUTHORITY | &quot;ATTESTATION_AUTHORITY&quot; |
| UPGRADE | &quot;UPGRADE&quot; |
| COMPLIANCE | &quot;COMPLIANCE&quot; |
| SBOM | &quot;SBOM&quot; |
| SPDX_PACKAGE | &quot;SPDX_PACKAGE&quot; |
| SPDX_FILE | &quot;SPDX_FILE&quot; |
| SPDX_RELATIONSHIP | &quot;SPDX_RELATIONSHIP&quot; |
| DSSE_ATTESTATION | &quot;DSSE_ATTESTATION&quot; |
| VULNERABILITY_ASSESSMENT | &quot;VULNERABILITY_ASSESSMENT&quot; |
| SBOM_REFERENCE | &quot;SBOM_REFERENCE&quot; |



