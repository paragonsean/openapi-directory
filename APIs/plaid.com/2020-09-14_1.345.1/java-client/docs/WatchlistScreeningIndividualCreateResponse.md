

# WatchlistScreeningIndividualCreateResponse

The screening object allows you to represent a customer in your system, update their profile, and search for them on various watchlists. Note: Rejected customers will not receive new hits, regardless of program configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**assignee** | **String** | ID of the associated user. |  |
|**auditTrail** | **WatchlistScreeningAuditTrail** |  |  |
|**clientUserId** | **String** | An identifier to help you connect this object to your internal systems. For example, your database ID corresponding to this object. |  |
|**id** | **String** | ID of the associated screening. |  |
|**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. |  |
|**searchTerms** | **WatchlistScreeningSearchTerms** |  |  |
|**status** | **WatchlistScreeningStatus** |  |  |



