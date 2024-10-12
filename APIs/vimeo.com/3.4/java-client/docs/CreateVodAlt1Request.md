

# CreateVodAlt1Request


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptedCurrencies** | [**AcceptedCurrenciesEnum**](#AcceptedCurrenciesEnum) | An array of accepted currencies.  Option descriptions:  * &#x60;AUD&#x60; - Australian Dollar  * &#x60;CAD&#x60; - Canadian Dollar  * &#x60;CHF&#x60; - Swiss Franc  * &#x60;DKK&#x60; - Danish Krone  * &#x60;EUR&#x60; - Euro  * &#x60;GBP&#x60; - British Pound  * &#x60;JPY&#x60; - Japanese Yen  * &#x60;KRW&#x60; - South Korean Won  * &#x60;NOK&#x60; - Norwegian Krone  * &#x60;PLN&#x60; - Polish Zloty  * &#x60;SEK&#x60; - Swedish Krona  * &#x60;USD&#x60; - US Dollar  |  [optional] |
|**buy** | [**CreateVodAlt1RequestBuy**](CreateVodAlt1RequestBuy.md) |  |  [optional] |
|**contentRating** | [**ContentRatingEnum**](#ContentRatingEnum) | One or more ratings, either as a comma-separated list or as a JSON array depending on the request format. |  |
|**description** | **String** | The description of the On Demand page. |  |
|**domainLink** | **String** | The custom domain of the On Demand page. |  [optional] |
|**episodes** | [**CreateVodAlt1RequestEpisodes**](CreateVodAlt1RequestEpisodes.md) |  |  [optional] |
|**link** | **String** | The custom string to use in this On Demand page&#39;s Vimeo URL. |  [optional] |
|**name** | **String** | The name of the On Demand page. |  |
|**rent** | [**CreateVodAlt1RequestRent**](CreateVodAlt1RequestRent.md) |  |  [optional] |
|**subscription** | [**CreateVodAlt1RequestSubscription**](CreateVodAlt1RequestSubscription.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of On Demand page. |  |



## Enum: AcceptedCurrenciesEnum

| Name | Value |
|---- | -----|
| AUD | &quot;AUD&quot; |
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| DKK | &quot;DKK&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| KRW | &quot;KRW&quot; |
| NOK | &quot;NOK&quot; |
| PLN | &quot;PLN&quot; |
| SEK | &quot;SEK&quot; |
| USD | &quot;USD&quot; |



## Enum: ContentRatingEnum

| Name | Value |
|---- | -----|
| DRUGS | &quot;drugs&quot; |
| LANGUAGE | &quot;language&quot; |
| NUDITY | &quot;nudity&quot; |
| SAFE | &quot;safe&quot; |
| UNRATED | &quot;unrated&quot; |
| VIOLENCE | &quot;violence&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FILM | &quot;film&quot; |
| SERIES | &quot;series&quot; |



