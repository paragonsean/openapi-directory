

# BatchGetReviewsRequest

Request message for Reviews.BatchGetReviews.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ignoreRatingOnlyReviews** | **Boolean** | Whether to ignore rating-only reviews. |  [optional] |
|**locationNames** | **List&lt;String&gt;** | A collection of locations to fetch reviews for, specified by their names. |  [optional] |
|**orderBy** | **String** | Optional. Specifies the field to sort reviews by. If unspecified, the order of reviews returned will default to &#x60;update_time desc&#x60;. Valid orders to sort by are &#x60;rating&#x60;, &#x60;rating desc&#x60; and &#x60;update_time desc&#x60;. &#x60;rating&#x60; will return reviews in ascending order. &#x60;update_time&#x60;(i.e. ascending order) is not supported. |  [optional] |
|**pageSize** | **Integer** | How many reviews to fetch per page. The default value is 200. |  [optional] |
|**pageToken** | **String** | If specified, it fetches the next page of reviews. |  [optional] |



