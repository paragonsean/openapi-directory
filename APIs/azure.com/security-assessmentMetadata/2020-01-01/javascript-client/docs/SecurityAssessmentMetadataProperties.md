# SecurityCenter.SecurityAssessmentMetadataProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessmentType** | **String** | BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment based on custom Azure Policy definition | 
**category** | **[String]** |  | [optional] 
**description** | **String** | Human readable description of the assessment | [optional] 
**displayName** | **String** | User friendly display name of the assessment | 
**implementationEffort** | **String** | The implementation effort required to remediate this assessment | [optional] 
**partnerData** | [**SecurityAssessmentMetadataPartnerData**](SecurityAssessmentMetadataPartnerData.md) |  | [optional] 
**policyDefinitionId** | **String** | Azure resource ID of the policy definition that turns this assessment calculation on | [optional] [readonly] 
**preview** | **Boolean** | True if this assessment is in preview release status | [optional] 
**remediationDescription** | **String** | Human readable description of what you should do to mitigate this security issue | [optional] 
**severity** | **String** | The severity level of the assessment | 
**threats** | **[String]** |  | [optional] 
**userImpact** | **String** | The user impact of the assessment | [optional] 



## Enum: AssessmentTypeEnum


* `BuiltIn` (value: `"BuiltIn"`)

* `CustomPolicy` (value: `"CustomPolicy"`)

* `CustomerManaged` (value: `"CustomerManaged"`)

* `VerifiedPartner` (value: `"VerifiedPartner"`)





## Enum: [CategoryEnum]


* `Compute` (value: `"Compute"`)

* `Networking` (value: `"Networking"`)

* `Data` (value: `"Data"`)

* `IdentityAndAccess` (value: `"IdentityAndAccess"`)

* `IoT` (value: `"IoT"`)





## Enum: ImplementationEffortEnum


* `Low` (value: `"Low"`)

* `Moderate` (value: `"Moderate"`)

* `High` (value: `"High"`)





## Enum: SeverityEnum


* `Low` (value: `"Low"`)

* `Medium` (value: `"Medium"`)

* `High` (value: `"High"`)





## Enum: [ThreatsEnum]


* `accountBreach` (value: `"accountBreach"`)

* `dataExfiltration` (value: `"dataExfiltration"`)

* `dataSpillage` (value: `"dataSpillage"`)

* `maliciousInsider` (value: `"maliciousInsider"`)

* `elevationOfPrivilege` (value: `"elevationOfPrivilege"`)

* `threatResistance` (value: `"threatResistance"`)

* `missingCoverage` (value: `"missingCoverage"`)

* `denialOfService` (value: `"denialOfService"`)





## Enum: UserImpactEnum


* `Low` (value: `"Low"`)

* `Moderate` (value: `"Moderate"`)

* `High` (value: `"High"`)




