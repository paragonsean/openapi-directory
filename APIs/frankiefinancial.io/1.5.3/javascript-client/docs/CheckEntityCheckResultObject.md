# FrankieFinancialApi.CheckEntityCheckResultObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blacklistCheckResults** | [**[ProcessResultObject]**](ProcessResultObject.md) | Collection of check results for the entity having been previously blacklisted.  An array of matched blacklisted entities sorted by match confidence level (highest first).  | [optional] 
**checkResultsListSummaries** | [**[ProcessResultObject]**](ProcessResultObject.md) | Contains a list of all checkSummary records (one for each check) | [optional] 
**checkRisk** | [**ProcessResultObject**](ProcessResultObject.md) |  | [optional] 
**checkSummary** | [**ProcessResultObject**](ProcessResultObject.md) |  | [optional] 
**deviceCheckResults** | [**[ProcessResultObject]**](ProcessResultObject.md) | We can perform a number of device checks on an entity, such as those from ThreatMetrix and/or BioCatch. If one of these checks was incorporated into the ID check, then these will appear here.  | [optional] 
**duplicateCheckResults** | [**[ProcessResultObject]**](ProcessResultObject.md) | Collection of check results for the entity having previously been checked.  An array of matched checked entities sorted by match confidence level (highest first).  | [optional] 
**entity** | [**EntityObject**](EntityObject.md) |  | [optional] 
**entityProfileResult** | [**EntityProfileResultObject**](EntityProfileResultObject.md) |  | [optional] 
**entityResult** | [**CheckEntityCheckResultObjectEntityResult**](CheckEntityCheckResultObjectEntityResult.md) |  | [optional] 
**fraudCheckResults** | [**FraudCheckResultObject**](FraudCheckResultObject.md) |  | [optional] 
**manualCheckResults** | [**[ProcessResultObject]**](ProcessResultObject.md) | Collection of check results for the manual KYC.  An array of one entry with the manual check result.  | [optional] 
**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  | [optional] 
**sharedBlocklistCheckResults** | [**[ProcessResultObject]**](ProcessResultObject.md) | Collection of check results for the entity having been previously blacklisted in shared blocklist.  An array of matched blacklisted entities sorted by match confidence level (highest first).  | [optional] 


