

# MerchandisedProduct

The type that defines the fields for product information, including price, condition, ratings, etc.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**averageRating** | **String** | The average rating for the product based on eBay user ratings. |  [optional] |
|**epid** | **String** | The eBay product identifier of a product from the eBay product catalog. You can use this value in the Browse API &lt;b&gt;search&lt;/b&gt; method to retrieve items for this product. |  [optional] |
|**image** | [**Image**](Image.md) |  |  [optional] |
|**marketPriceDetails** | [**List&lt;MarketPriceDetail&gt;**](MarketPriceDetail.md) | An array of containers for the product market price details, such as condition and market price. |  [optional] |
|**ratingAspects** | [**List&lt;RatingAspect&gt;**](RatingAspect.md) | An array of containers for ratings of the product aspects, such as \&quot;Is it a good value\&quot;. |  [optional] |
|**ratingCount** | **Integer** | The total number of eBay users that rated the product. |  [optional] |
|**reviewCount** | **Integer** | The total number of eBay users that wrote a review for the product.  |  [optional] |
|**title** | **String** | The title of the product. |  [optional] |



