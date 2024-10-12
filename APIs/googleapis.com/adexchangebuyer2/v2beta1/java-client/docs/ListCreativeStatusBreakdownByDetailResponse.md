

# ListCreativeStatusBreakdownByDetailResponse

Response message for listing all details associated with a given filtered bid reason.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detailType** | [**DetailTypeEnum**](#DetailTypeEnum) | The type of detail that the detail IDs represent. |  [optional] |
|**filteredBidDetailRows** | [**List&lt;FilteredBidDetailRow&gt;**](FilteredBidDetailRow.md) | List of rows, with counts of bids with a given creative status aggregated by detail. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the ListCreativeStatusBreakdownByDetailRequest.pageToken field in the subsequent call to the filteredBids.details.list method to retrieve the next page of results. |  [optional] |



## Enum: DetailTypeEnum

| Name | Value |
|---- | -----|
| DETAIL_TYPE_UNSPECIFIED | &quot;DETAIL_TYPE_UNSPECIFIED&quot; |
| CREATIVE_ATTRIBUTE | &quot;CREATIVE_ATTRIBUTE&quot; |
| VENDOR | &quot;VENDOR&quot; |
| SENSITIVE_CATEGORY | &quot;SENSITIVE_CATEGORY&quot; |
| PRODUCT_CATEGORY | &quot;PRODUCT_CATEGORY&quot; |
| DISAPPROVAL_REASON | &quot;DISAPPROVAL_REASON&quot; |
| POLICY_TOPIC | &quot;POLICY_TOPIC&quot; |
| ATP_VENDOR | &quot;ATP_VENDOR&quot; |
| VENDOR_DOMAIN | &quot;VENDOR_DOMAIN&quot; |
| GVL_ID | &quot;GVL_ID&quot; |



