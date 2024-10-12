# Reverb.MyFollowsSearchPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptsGiftCards** | **Boolean** | If true, include only items that accept gift cards | [optional] 
**acceptsPaymentPlans** | **Boolean** | If true, only show items that can be purchased with a payment plan | [optional] 
**auctionPriceMax** | **Number** | Maximum current auction price | [optional] 
**category** | **String** | Category slug from /api/categories | [optional] 
**conditions** | **[String]** | Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint | [optional] 
**currency** | **String** | The currency to be used for the price filters | [optional] 
**decade** | **String** | Decade: e.g. 1970s, early 70s | [optional] 
**excludeAuctions** | **Boolean** | If true, exclude auctions | [optional] 
**finish** | **String** | Visual finish of the item, common for guitars | [optional] 
**handmade** | **Boolean** | Handmade items only | [optional] 
**itemCity** | **String** | City where item is located | [optional] 
**itemCountry** | **String** | DEPRECATED - Country code where item is located | [optional] 
**itemRegion** | **String** | Country code where item is located | [optional] 
**itemState** | **String** | State or region code where item is located | [optional] 
**listingType** | **String** | Type of listing: auctions,offers | [optional] 
**localPickup** | **Boolean** | Only items that offer local pickup | [optional] 
**make** | **[String]** | Make(s)/brand of item (e.g. Fender). Can take a single value or an array. | [optional] 
**model** | **String** | Model of item (e.g. Stratocaster) | [optional] 
**mustNot** | **String** | Search term negation. If you want to exclude a term, add it here | [optional] 
**notIds** | **[Number]** | Listing ID negation. If you want to exclude a listing, add it here. | [optional] 
**preferredSeller** | **Boolean** | If true, include only items by Reverb Preferred Sellers | [optional] 
**priceMax** | **Number** | Maximum price of search results (USD) | [optional] 
**priceMin** | **Number** | Minimum price of search results (USD) | [optional] 
**productType** | **String** | Product type slug from /api/categories | [optional] 
**query** | **String** | Search query. | [optional] 
**shipsTo** | **String** | Limit search to items that ship to this country code | [optional] 
**shop** | **String** | Slug of shop to search | [optional] 
**shopId** | **String** | ID of shop to search | [optional] 
**watchersCountMin** | **Number** | Minimum number of watchers (used to find popular items) | [optional] 
**yearMax** | **Number** | Maximum year of manufacture | [optional] 
**yearMin** | **Number** | Minumum year of manufacture | [optional] 



## Enum: ConditionsEnum






## Enum: CurrencyEnum


* `USD` (value: `"USD"`)

* `CAD` (value: `"CAD"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `AUD` (value: `"AUD"`)

* `JPY` (value: `"JPY"`)

* `NZD` (value: `"NZD"`)

* `MXN` (value: `"MXN"`)

* `DKK` (value: `"DKK"`)

* `SEK` (value: `"SEK"`)

* `CHF` (value: `"CHF"`)

* `ARS` (value: `"ARS"`)

* `BRL` (value: `"BRL"`)

* `HKD` (value: `"HKD"`)

* `NOK` (value: `"NOK"`)

* `PHP` (value: `"PHP"`)

* `PLN` (value: `"PLN"`)

* `RUB` (value: `"RUB"`)





## Enum: ListingTypeEnum


* `auctions` (value: `"auctions"`)

* `offers` (value: `"offers"`)




