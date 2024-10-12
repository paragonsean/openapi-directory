

# ListReviewsResponse

Response message for Reviews.ListReviews.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**averageRating** | **Double** | The average star rating of all reviews for this location on a scale of 1 to 5, where 5 is the highest rating. |  [optional] |
|**nextPageToken** | **String** | If the number of reviews exceeded the requested page size, this field is populated with a token to fetch the next page of reviews on a subsequent call to ListReviews. If there are no more reviews, this field is not present in the response. |  [optional] |
|**reviews** | [**List&lt;Review&gt;**](Review.md) | The reviews. |  [optional] |
|**totalReviewCount** | **Integer** | The total number of reviews for this location. |  [optional] |



