

# BCAInner

BCA means a Business Current Account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bcAMarketingState** | [**List&lt;BCAMarketingStateInner&gt;**](BCAMarketingStateInner.md) | The marketing state (promotional or regular) of the BCA Product. |  |
|**feeFreeLength** | **Float** | The length/duration of the fee free period |  [optional] |
|**feeFreeLengthPeriod** | [**FeeFreeLengthPeriodEnum**](#FeeFreeLengthPeriodEnum) | The unit of period (days, weeks, months etc.) of the promotional length |  [optional] |
|**identification** | **String** | The unique ID that has been internally assigned by the financial institution to each of the current account banking products they market to their retail and/or small to medium enterprise (SME) customers. |  |
|**name** | **String** | The name of the BCA product used for marketing purposes from a customer perspective. I.e. what the customer would recognise. |  |
|**notes** | **List&lt;String&gt;** | Optional additional notes to supplement the product details |  [optional] |
|**onSaleIndicator** | **Boolean** | Indicates that the published product is OnSale(value 1) or Back Book (value 0)  |  [optional] |
|**segment** | [**List&lt;SegmentEnum&gt;**](#List&lt;SegmentEnum&gt;) | Market segmentation is a marketing term referring to the aggregating of prospective buyers into groups, or segments, that have common needs and respond similarly to a marketing action. Market segmentation enables companies to target different categories of consumers who perceive the full value of certain products and services differently from one another.  Read more: Market Segmentation http://www.investopedia.com/terms/m/marketsegmentation.asp#ixzz4gfEEalTd  Follow us: Investopedia on Facebook  With respect to BCA products, they are segmented in relation to different markets that they wish to focus on. |  [optional] |



## Enum: FeeFreeLengthPeriodEnum

| Name | Value |
|---- | -----|
| DAY | &quot;Day&quot; |
| HALF_YEAR | &quot;Half Year&quot; |
| MONTH | &quot;Month&quot; |
| QUARTER | &quot;Quarter&quot; |
| WEEK | &quot;Week&quot; |
| ACADEMIC_TERM | &quot;AcademicTerm&quot; |
| YEAR | &quot;Year&quot; |



## Enum: List&lt;SegmentEnum&gt;

| Name | Value |
|---- | -----|
| CLIENT_ACCOUNT | &quot;ClientAccount&quot; |
| STANDARD | &quot;Standard&quot; |
| NON_COMMERCIAL_CHAITIES_CLB_SOC | &quot;NonCommercialChaitiesClbSoc&quot; |
| NON_COMMERCIAL_PUBLIC_AUTH_GOVT | &quot;NonCommercialPublicAuthGovt&quot; |
| RELIGIOUS | &quot;Religious&quot; |
| SECTOR_SPECIFIC | &quot;SectorSpecific&quot; |
| STARTUP | &quot;Startup&quot; |
| SWITCHER | &quot;Switcher&quot; |
| NON_COMMERCIAL | &quot;NonCommercial&quot; |



