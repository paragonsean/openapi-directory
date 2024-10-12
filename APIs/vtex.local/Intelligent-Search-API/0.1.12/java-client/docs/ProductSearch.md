

# ProductSearch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**correction** | [**ProductSearchCorrection**](ProductSearchCorrection.md) |  |  [optional] |
|**fuzzy** | **String** | Indicates how the search engine corrected the misspelled word by using fuzzy logic. It can be a number representing the max number of misspelled letters, or the string &#x60;auto&#x60; suggesting that the search-engine should set this value by itself. |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Indicates how the search-engine dealt with the fullText when there is more than one word.  * &#x60;and&#x60; - It means that the products contains all the words in the query.  * &#x60;or&#x60; - It means that the results will contain at least one word from the original search query. If &#x60;and&#x60; was not possible, &#x60;or&#x60; will be the fallback. |  [optional] |
|**products** | **List&lt;Object&gt;** | List of products |  [optional] |
|**recordsFiltered** | **BigDecimal** | Total number of products. |  [optional] |
|**translated** | **Boolean** | Whether the list of products was translated by the IS (&#x60;true&#x60;) or not (&#x60;false&#x60;). |  [optional] |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| AND | &quot;and&quot; |
| OR | &quot;or&quot; |



