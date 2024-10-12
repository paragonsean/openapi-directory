

# SecurityAssessmentMetadataProperties

Describes properties of an assessment metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assessmentType** | [**AssessmentTypeEnum**](#AssessmentTypeEnum) | BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment based on custom Azure Policy definition |  |
|**category** | [**List&lt;CategoryEnum&gt;**](#List&lt;CategoryEnum&gt;) |  |  [optional] |
|**description** | **String** | Human readable description of the assessment |  [optional] |
|**displayName** | **String** | User friendly display name of the assessment |  |
|**implementationEffort** | [**ImplementationEffortEnum**](#ImplementationEffortEnum) | The implementation effort required to remediate this assessment |  [optional] |
|**policyDefinitionId** | **String** | Azure resource ID of the policy definition that turns this assessment calculation on |  [optional] [readonly] |
|**preview** | **Boolean** | True if this assessment is in preview release status |  [optional] |
|**remediationDescription** | **String** | Human readable description of what you should do to mitigate this security issue |  [optional] |
|**severity** | [**SeverityEnum**](#SeverityEnum) | The severity level of the assessment |  |
|**threats** | [**List&lt;ThreatsEnum&gt;**](#List&lt;ThreatsEnum&gt;) |  |  [optional] |
|**userImpact** | [**UserImpactEnum**](#UserImpactEnum) | The user impact of the assessment |  [optional] |



## Enum: AssessmentTypeEnum

| Name | Value |
|---- | -----|
| BUILT_IN | &quot;BuiltIn&quot; |
| CUSTOM_POLICY | &quot;CustomPolicy&quot; |
| CUSTOMER_MANAGED | &quot;CustomerManaged&quot; |



## Enum: List&lt;CategoryEnum&gt;

| Name | Value |
|---- | -----|
| COMPUTE | &quot;Compute&quot; |
| NETWORKING | &quot;Networking&quot; |
| DATA | &quot;Data&quot; |
| IDENTITY_AND_ACCESS | &quot;IdentityAndAccess&quot; |
| IO_T | &quot;IoT&quot; |



## Enum: ImplementationEffortEnum

| Name | Value |
|---- | -----|
| LOW | &quot;Low&quot; |
| MODERATE | &quot;Moderate&quot; |
| HIGH | &quot;High&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| LOW | &quot;Low&quot; |
| MEDIUM | &quot;Medium&quot; |
| HIGH | &quot;High&quot; |



## Enum: List&lt;ThreatsEnum&gt;

| Name | Value |
|---- | -----|
| ACCOUNT_BREACH | &quot;accountBreach&quot; |
| DATA_EXFILTRATION | &quot;dataExfiltration&quot; |
| DATA_SPILLAGE | &quot;dataSpillage&quot; |
| MALICIOUS_INSIDER | &quot;maliciousInsider&quot; |
| ELEVATION_OF_PRIVILEGE | &quot;elevationOfPrivilege&quot; |
| THREAT_RESISTANCE | &quot;threatResistance&quot; |
| MISSING_COVERAGE | &quot;missingCoverage&quot; |
| DENIAL_OF_SERVICE | &quot;denialOfService&quot; |



## Enum: UserImpactEnum

| Name | Value |
|---- | -----|
| LOW | &quot;Low&quot; |
| MODERATE | &quot;Moderate&quot; |
| HIGH | &quot;High&quot; |



