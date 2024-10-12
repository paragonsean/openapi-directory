

# CheckEntityCheckResultObject

Describes all of the checks that were carried out against an entity as part of our cascading check process. Because there are a number of steps involved in checking an entity, (including the use of past checks done by you or others), there is an overall summary check result that will tell you the final disposition of the the check you requested.  So if you requested a 2+2+governmentID+pep/sanctions/etc (i.e. everything) then there would have been several checks done in order to meet this requirement. Some may have even failed, but eventually we got there. The summary gives the final assessment, based on all available data.  Detailed writeups on how this all works can be found here:   https://apidocs.frankiefinancial.com/docs/understanding-checksummary-results 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blacklistCheckResults** | [**List&lt;ProcessResultObject&gt;**](ProcessResultObject.md) | Collection of check results for the entity having been previously blacklisted.  An array of matched blacklisted entities sorted by match confidence level (highest first).  |  [optional] |
|**checkResultsListSummaries** | [**List&lt;ProcessResultObject&gt;**](ProcessResultObject.md) | Contains a list of all checkSummary records (one for each check) |  [optional] |
|**checkRisk** | [**ProcessResultObject**](ProcessResultObject.md) |  |  [optional] |
|**checkSummary** | [**ProcessResultObject**](ProcessResultObject.md) |  |  [optional] |
|**deviceCheckResults** | [**List&lt;ProcessResultObject&gt;**](ProcessResultObject.md) | We can perform a number of device checks on an entity, such as those from ThreatMetrix and/or BioCatch. If one of these checks was incorporated into the ID check, then these will appear here.  |  [optional] |
|**duplicateCheckResults** | [**List&lt;ProcessResultObject&gt;**](ProcessResultObject.md) | Collection of check results for the entity having previously been checked.  An array of matched checked entities sorted by match confidence level (highest first).  |  [optional] |
|**entity** | [**EntityObject**](EntityObject.md) |  |  [optional] |
|**entityProfileResult** | [**EntityProfileResultObject**](EntityProfileResultObject.md) |  |  [optional] |
|**entityResult** | [**CheckEntityCheckResultObjectEntityResult**](CheckEntityCheckResultObjectEntityResult.md) |  |  [optional] |
|**fraudCheckResults** | [**FraudCheckResultObject**](FraudCheckResultObject.md) |  |  [optional] |
|**manualCheckResults** | [**List&lt;ProcessResultObject&gt;**](ProcessResultObject.md) | Collection of check results for the manual KYC.  An array of one entry with the manual check result.  |  [optional] |
|**requestId** | **String** | Unique identifier for every request. Can be used for tracking down answers with technical support.   Uses the ULID format (a time-based, sortable UUID)  Note: this will be different for every request.  |  [optional] |
|**sharedBlocklistCheckResults** | [**List&lt;ProcessResultObject&gt;**](ProcessResultObject.md) | Collection of check results for the entity having been previously blacklisted in shared blocklist.  An array of matched blacklisted entities sorted by match confidence level (highest first).  |  [optional] |



