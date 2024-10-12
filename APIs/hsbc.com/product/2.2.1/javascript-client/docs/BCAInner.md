# ProductFinderApi.BCAInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bCAMarketingState** | [**[BCAMarketingStateInner]**](BCAMarketingStateInner.md) | The marketing state (promotional or regular) of the BCA Product. | 
**feeFreeLength** | **Number** | The length/duration of the fee free period | [optional] 
**feeFreeLengthPeriod** | **String** | The unit of period (days, weeks, months etc.) of the promotional length | [optional] 
**identification** | **String** | The unique ID that has been internally assigned by the financial institution to each of the current account banking products they market to their retail and/or small to medium enterprise (SME) customers. | 
**name** | **String** | The name of the BCA product used for marketing purposes from a customer perspective. I.e. what the customer would recognise. | 
**notes** | **[String]** | Optional additional notes to supplement the product details | [optional] 
**onSaleIndicator** | **Boolean** | Indicates that the published product is OnSale(value 1) or Back Book (value 0)  | [optional] 
**segment** | **[String]** | Market segmentation is a marketing term referring to the aggregating of prospective buyers into groups, or segments, that have common needs and respond similarly to a marketing action. Market segmentation enables companies to target different categories of consumers who perceive the full value of certain products and services differently from one another.  Read more: Market Segmentation http://www.investopedia.com/terms/m/marketsegmentation.asp#ixzz4gfEEalTd  Follow us: Investopedia on Facebook  With respect to BCA products, they are segmented in relation to different markets that they wish to focus on. | [optional] 



## Enum: FeeFreeLengthPeriodEnum


* `Day` (value: `"Day"`)

* `Half Year` (value: `"Half Year"`)

* `Month` (value: `"Month"`)

* `Quarter` (value: `"Quarter"`)

* `Week` (value: `"Week"`)

* `AcademicTerm` (value: `"AcademicTerm"`)

* `Year` (value: `"Year"`)





## Enum: [SegmentEnum]


* `ClientAccount` (value: `"ClientAccount"`)

* `Standard` (value: `"Standard"`)

* `NonCommercialChaitiesClbSoc` (value: `"NonCommercialChaitiesClbSoc"`)

* `NonCommercialPublicAuthGovt` (value: `"NonCommercialPublicAuthGovt"`)

* `Religious` (value: `"Religious"`)

* `SectorSpecific` (value: `"SectorSpecific"`)

* `Startup` (value: `"Startup"`)

* `Switcher` (value: `"Switcher"`)

* `NonCommercial` (value: `"NonCommercial"`)




