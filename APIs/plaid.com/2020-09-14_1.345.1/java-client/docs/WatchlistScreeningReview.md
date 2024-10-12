

# WatchlistScreeningReview

A review submitted by a team member for an individual watchlist screening. A review can be either a comment on the current screening state, actions taken against hits attached to the watchlist screening, or both.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auditTrail** | **WatchlistScreeningAuditTrail** |  |  |
|**comment** | **String** | A comment submitted by a team member as part of reviewing a watchlist screening. |  |
|**confirmedHits** | **List&lt;String&gt;** | Hits marked as a true positive after thorough manual review. These hits will never recur or be updated once dismissed. In most cases, confirmed hits indicate that the customer should be rejected. |  |
|**dismissedHits** | **List&lt;String&gt;** | Hits marked as a false positive after thorough manual review. These hits will never recur or be updated once dismissed. |  |
|**id** | **String** | ID of the associated review. |  |



