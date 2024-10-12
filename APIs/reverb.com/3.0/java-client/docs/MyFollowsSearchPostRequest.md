

# MyFollowsSearchPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptsGiftCards** | **Boolean** | If true, include only items that accept gift cards |  [optional] |
|**acceptsPaymentPlans** | **Boolean** | If true, only show items that can be purchased with a payment plan |  [optional] |
|**auctionPriceMax** | **Float** | Maximum current auction price |  [optional] |
|**category** | **String** | Category slug from /api/categories |  [optional] |
|**conditions** | [**ConditionsEnum**](#ConditionsEnum) | Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint |  [optional] |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The currency to be used for the price filters |  [optional] |
|**decade** | **String** | Decade: e.g. 1970s, early 70s |  [optional] |
|**excludeAuctions** | **Boolean** | If true, exclude auctions |  [optional] |
|**finish** | **String** | Visual finish of the item, common for guitars |  [optional] |
|**handmade** | **Boolean** | Handmade items only |  [optional] |
|**itemCity** | **String** | City where item is located |  [optional] |
|**itemCountry** | **String** | DEPRECATED - Country code where item is located |  [optional] |
|**itemRegion** | **String** | Country code where item is located |  [optional] |
|**itemState** | **String** | State or region code where item is located |  [optional] |
|**listingType** | [**ListingTypeEnum**](#ListingTypeEnum) | Type of listing: auctions,offers |  [optional] |
|**localPickup** | **Boolean** | Only items that offer local pickup |  [optional] |
|**make** | **List&lt;String&gt;** | Make(s)/brand of item (e.g. Fender). Can take a single value or an array. |  [optional] |
|**model** | **String** | Model of item (e.g. Stratocaster) |  [optional] |
|**mustNot** | **String** | Search term negation. If you want to exclude a term, add it here |  [optional] |
|**notIds** | **List&lt;Integer&gt;** | Listing ID negation. If you want to exclude a listing, add it here. |  [optional] |
|**preferredSeller** | **Boolean** | If true, include only items by Reverb Preferred Sellers |  [optional] |
|**priceMax** | **Float** | Maximum price of search results (USD) |  [optional] |
|**priceMin** | **Float** | Minimum price of search results (USD) |  [optional] |
|**productType** | **String** | Product type slug from /api/categories |  [optional] |
|**query** | **String** | Search query. |  [optional] |
|**shipsTo** | **String** | Limit search to items that ship to this country code |  [optional] |
|**shop** | **String** | Slug of shop to search |  [optional] |
|**shopId** | **String** | ID of shop to search |  [optional] |
|**watchersCountMin** | **Integer** | Minimum number of watchers (used to find popular items) |  [optional] |
|**yearMax** | **Integer** | Maximum year of manufacture |  [optional] |
|**yearMin** | **Integer** | Minumum year of manufacture |  [optional] |



## Enum: ConditionsEnum

| Name | Value |
|---- | -----|



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| USD | &quot;USD&quot; |
| CAD | &quot;CAD&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| AUD | &quot;AUD&quot; |
| JPY | &quot;JPY&quot; |
| NZD | &quot;NZD&quot; |
| MXN | &quot;MXN&quot; |
| DKK | &quot;DKK&quot; |
| SEK | &quot;SEK&quot; |
| CHF | &quot;CHF&quot; |
| ARS | &quot;ARS&quot; |
| BRL | &quot;BRL&quot; |
| HKD | &quot;HKD&quot; |
| NOK | &quot;NOK&quot; |
| PHP | &quot;PHP&quot; |
| PLN | &quot;PLN&quot; |
| RUB | &quot;RUB&quot; |



## Enum: ListingTypeEnum

| Name | Value |
|---- | -----|
| AUCTIONS | &quot;auctions&quot; |
| OFFERS | &quot;offers&quot; |



