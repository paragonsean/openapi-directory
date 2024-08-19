# ThePlaidApi.WatchlistScreeningIndividualProgramGetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auditTrail** | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) |  | 
**createdAt** | **Date** | An ISO8601 formatted timestamp. | 
**id** | **String** | ID of the associated program. | 
**isArchived** | **Boolean** | Archived programs are read-only and cannot screen new customers nor participate in ongoing monitoring. | 
**isRescanningEnabled** | **Boolean** | Indicator specifying whether the program is enabled and will perform daily rescans. | 
**listsEnabled** | [**[IndividualWatchlistCode]**](IndividualWatchlistCode.md) | Watchlists enabled for the associated program | 
**name** | **String** | A name for the program to define its purpose. For example, \&quot;High Risk Individuals\&quot;, \&quot;US Cardholders\&quot;, or \&quot;Applicants\&quot;. | 
**nameSensitivity** | [**ProgramNameSensitivity**](ProgramNameSensitivity.md) |  | 
**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 


