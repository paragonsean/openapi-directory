# ThePlaidApi.EntityWatchlistScreeningReview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auditTrail** | [**WatchlistScreeningAuditTrail**](WatchlistScreeningAuditTrail.md) |  | 
**comment** | **String** | A comment submitted by a team member as part of reviewing a watchlist screening. | 
**confirmedHits** | **[String]** | Hits marked as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected. | 
**dismissedHits** | **[String]** | Hits marked as a false positive after thorough manual review. These hits will never recur or be updated once dismissed. | 
**id** | **String** | ID of the associated entity review. | 


