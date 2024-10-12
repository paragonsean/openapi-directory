# MicrosoftSupport.SupportTicketDetailsProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactDetails** | [**ContactProfile**](ContactProfile.md) |  | 
**createdDate** | **Date** | Time in UTC (ISO 8601 format) when support ticket was created. | [optional] [readonly] 
**description** | **String** | Detailed description of the question or issue. | 
**enrollmentId** | **String** | Enrollment ID associated with the support ticket. | [optional] [readonly] 
**modifiedDate** | **Date** | Time in UTC (ISO 8601 format) when support ticket was last modified. | [optional] [readonly] 
**problemClassificationDisplayName** | **String** | Localized name of problem classification. | [optional] [readonly] 
**problemClassificationId** | **String** | Each Azure service has its own set of issue category called problem classification that corresponds to the type of problem you&#39;re experiencing. This parameter is the resource id of ProblemClassification resource. | 
**problemStartTime** | **Date** | Time in UTC (ISO 8601 format) when the problem started. | [optional] 
**productionOutage** | **Boolean** | Indicates if this issue is a production outage. | [optional] [readonly] 
**quotaTicketDetails** | [**QuotaTicketDetails**](QuotaTicketDetails.md) |  | [optional] 
**require24X7Response** | **Boolean** | Indicates if this requires a 24x7 response from Azure. | [optional] 
**serviceDisplayName** | **String** | Localized name of Azure service. | [optional] [readonly] 
**serviceId** | **String** | This is the resource id of the Azure service resource associated with the support ticket. | 
**serviceLevelAgreement** | [**ServiceLevelAgreement**](ServiceLevelAgreement.md) |  | [optional] 
**severity** | **String** | A value that indicates the urgency of the case, which in turn determines the response time according to the service level agreement of the technical support plan you have with Azure. | 
**status** | **String** | Status of the support ticket. | [optional] [readonly] 
**supportEngineer** | [**SupportEngineer**](SupportEngineer.md) |  | [optional] 
**supportPlanType** | **String** | Support plan type associated with the support ticket. | [optional] [readonly] 
**supportTicketId** | **String** | System generated support ticket id that is unique. | [optional] 
**technicalTicketDetails** | [**TechnicalTicketDetails**](TechnicalTicketDetails.md) |  | [optional] 
**title** | **String** | Title of the support ticket. | 



## Enum: SeverityEnum


* `minimal` (value: `"minimal"`)

* `moderate` (value: `"moderate"`)

* `critical` (value: `"critical"`)




