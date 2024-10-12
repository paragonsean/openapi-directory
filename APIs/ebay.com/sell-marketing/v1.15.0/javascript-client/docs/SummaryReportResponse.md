# MarketingApi.SummaryReportResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseSale** | [**Amount**](Amount.md) |  | [optional] 
**lastUpdated** | **String** | The date the report was generated. | [optional] 
**percentageSalesLift** | **String** | The percentage of the total dollar amount gained due to promotions. This value is calculated as follows:  &lt;br&gt;&lt;br&gt;&lt;b&gt;precentageSalesLift&lt;/b&gt; &#x3D; &lt;b&gt;promotionSale&lt;/b&gt; / (&lt;b&gt;baseSale&lt;/b&gt; + &lt;b&gt;promotionSale&lt;/b&gt;) | [optional] 
**promotionSale** | [**Amount**](Amount.md) |  | [optional] 
**totalSale** | [**Amount**](Amount.md) |  | [optional] 


