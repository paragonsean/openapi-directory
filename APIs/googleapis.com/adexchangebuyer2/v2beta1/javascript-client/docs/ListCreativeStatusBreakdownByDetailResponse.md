# AdExchangeBuyerApiIi.ListCreativeStatusBreakdownByDetailResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detailType** | **String** | The type of detail that the detail IDs represent. | [optional] 
**filteredBidDetailRows** | [**[FilteredBidDetailRow]**](FilteredBidDetailRow.md) | List of rows, with counts of bids with a given creative status aggregated by detail. | [optional] 
**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the ListCreativeStatusBreakdownByDetailRequest.pageToken field in the subsequent call to the filteredBids.details.list method to retrieve the next page of results. | [optional] 



## Enum: DetailTypeEnum


* `DETAIL_TYPE_UNSPECIFIED` (value: `"DETAIL_TYPE_UNSPECIFIED"`)

* `CREATIVE_ATTRIBUTE` (value: `"CREATIVE_ATTRIBUTE"`)

* `VENDOR` (value: `"VENDOR"`)

* `SENSITIVE_CATEGORY` (value: `"SENSITIVE_CATEGORY"`)

* `PRODUCT_CATEGORY` (value: `"PRODUCT_CATEGORY"`)

* `DISAPPROVAL_REASON` (value: `"DISAPPROVAL_REASON"`)

* `POLICY_TOPIC` (value: `"POLICY_TOPIC"`)

* `ATP_VENDOR` (value: `"ATP_VENDOR"`)

* `VENDOR_DOMAIN` (value: `"VENDOR_DOMAIN"`)

* `GVL_ID` (value: `"GVL_ID"`)




