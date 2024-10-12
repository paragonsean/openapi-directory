# Vimeo.CreateVodAlt1Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceptedCurrencies** | **String** | An array of accepted currencies.  Option descriptions:  * &#x60;AUD&#x60; - Australian Dollar  * &#x60;CAD&#x60; - Canadian Dollar  * &#x60;CHF&#x60; - Swiss Franc  * &#x60;DKK&#x60; - Danish Krone  * &#x60;EUR&#x60; - Euro  * &#x60;GBP&#x60; - British Pound  * &#x60;JPY&#x60; - Japanese Yen  * &#x60;KRW&#x60; - South Korean Won  * &#x60;NOK&#x60; - Norwegian Krone  * &#x60;PLN&#x60; - Polish Zloty  * &#x60;SEK&#x60; - Swedish Krona  * &#x60;USD&#x60; - US Dollar  | [optional] 
**buy** | [**CreateVodAlt1RequestBuy**](CreateVodAlt1RequestBuy.md) |  | [optional] 
**contentRating** | **String** | One or more ratings, either as a comma-separated list or as a JSON array depending on the request format. | 
**description** | **String** | The description of the On Demand page. | 
**domainLink** | **String** | The custom domain of the On Demand page. | [optional] 
**episodes** | [**CreateVodAlt1RequestEpisodes**](CreateVodAlt1RequestEpisodes.md) |  | [optional] 
**link** | **String** | The custom string to use in this On Demand page&#39;s Vimeo URL. | [optional] 
**name** | **String** | The name of the On Demand page. | 
**rent** | [**CreateVodAlt1RequestRent**](CreateVodAlt1RequestRent.md) |  | [optional] 
**subscription** | [**CreateVodAlt1RequestSubscription**](CreateVodAlt1RequestSubscription.md) |  | [optional] 
**type** | **String** | The type of On Demand page. | 



## Enum: AcceptedCurrenciesEnum


* `AUD` (value: `"AUD"`)

* `CAD` (value: `"CAD"`)

* `CHF` (value: `"CHF"`)

* `DKK` (value: `"DKK"`)

* `EUR` (value: `"EUR"`)

* `GBP` (value: `"GBP"`)

* `JPY` (value: `"JPY"`)

* `KRW` (value: `"KRW"`)

* `NOK` (value: `"NOK"`)

* `PLN` (value: `"PLN"`)

* `SEK` (value: `"SEK"`)

* `USD` (value: `"USD"`)





## Enum: ContentRatingEnum


* `drugs` (value: `"drugs"`)

* `language` (value: `"language"`)

* `nudity` (value: `"nudity"`)

* `safe` (value: `"safe"`)

* `unrated` (value: `"unrated"`)

* `violence` (value: `"violence"`)





## Enum: TypeEnum


* `film` (value: `"film"`)

* `series` (value: `"series"`)




