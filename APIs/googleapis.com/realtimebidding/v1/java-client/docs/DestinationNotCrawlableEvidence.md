

# DestinationNotCrawlableEvidence

Evidence that the creative's destination URL was not crawlable by Google.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**crawlTime** | **String** | Approximate time of the crawl. |  [optional] |
|**crawledUrl** | **String** | Destination URL that was attempted to be crawled. |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | Reason of destination not crawlable. |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| REASON_UNSPECIFIED | &quot;REASON_UNSPECIFIED&quot; |
| UNREACHABLE_ROBOTS | &quot;UNREACHABLE_ROBOTS&quot; |
| TIMEOUT_ROBOTS | &quot;TIMEOUT_ROBOTS&quot; |
| ROBOTED_DENIED | &quot;ROBOTED_DENIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |



