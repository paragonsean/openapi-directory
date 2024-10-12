

# WatchlistScreeningIndividualProgramGetResponse

A program that configures the active lists, search parameters, and other behavior for initial and ongoing screening of individuals.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auditTrail** | **WatchlistScreeningAuditTrail** |  |  |
|**createdAt** | **OffsetDateTime** | An ISO8601 formatted timestamp. |  |
|**id** | **String** | ID of the associated program. |  |
|**isArchived** | **Boolean** | Archived programs are read-only and cannot screen new customers nor participate in ongoing monitoring. |  |
|**isRescanningEnabled** | **Boolean** | Indicator specifying whether the program is enabled and will perform daily rescans. |  |
|**listsEnabled** | **Set&lt;IndividualWatchlistCode&gt;** | Watchlists enabled for the associated program |  |
|**name** | **String** | A name for the program to define its purpose. For example, \&quot;High Risk Individuals\&quot;, \&quot;US Cardholders\&quot;, or \&quot;Applicants\&quot;. |  |
|**nameSensitivity** | **ProgramNameSensitivity** |  |  |
|**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |  |



