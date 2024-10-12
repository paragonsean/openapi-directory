

# GoogleCloudRetailV2alphaRating

The rating of a Product.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**averageRating** | **Float** | The average rating of the Product. The rating is scaled at 1-5. Otherwise, an INVALID_ARGUMENT error is returned. |  [optional] |
|**ratingCount** | **Integer** | The total number of ratings. This value is independent of the value of rating_histogram. This value must be nonnegative. Otherwise, an INVALID_ARGUMENT error is returned. |  [optional] |
|**ratingHistogram** | **List&lt;Integer&gt;** | List of rating counts per rating value (index &#x3D; rating - 1). The list is empty if there is no rating. If the list is non-empty, its size is always 5. Otherwise, an INVALID_ARGUMENT error is returned. For example, [41, 14, 13, 47, 303]. It means that the Product got 41 ratings with 1 star, 14 ratings with 2 star, and so on. |  [optional] |



