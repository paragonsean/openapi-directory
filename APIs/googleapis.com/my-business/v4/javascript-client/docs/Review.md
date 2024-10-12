# GoogleMyBusinessApi.Review

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **String** | The body of the review as plain text with markups. | [optional] 
**createTime** | **String** | The timestamp for when the review was written. | [optional] 
**name** | **String** | The resource name. For Review it is of the form &#x60;accounts/{account_id}/locations/{location_id}/reviews/{review_id}&#x60; | [optional] 
**reviewId** | **String** | The encrypted unique identifier. | [optional] 
**reviewReply** | [**ReviewReply**](ReviewReply.md) |  | [optional] 
**reviewer** | [**Reviewer**](Reviewer.md) |  | [optional] 
**starRating** | **String** | The star rating of the review. | [optional] 
**updateTime** | **String** | The timestamp for when the review was last modified. | [optional] 



## Enum: StarRatingEnum


* `STAR_RATING_UNSPECIFIED` (value: `"STAR_RATING_UNSPECIFIED"`)

* `ONE` (value: `"ONE"`)

* `TWO` (value: `"TWO"`)

* `THREE` (value: `"THREE"`)

* `FOUR` (value: `"FOUR"`)

* `FIVE` (value: `"FIVE"`)




