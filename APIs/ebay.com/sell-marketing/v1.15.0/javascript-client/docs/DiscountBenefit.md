# MarketingApi.DiscountBenefit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountOffItem** | [**Amount**](Amount.md) |  | [optional] 
**amountOffOrder** | [**Amount**](Amount.md) |  | [optional] 
**percentageOffItem** | **String** | The percentage applied to the sales price that is discounted off the promoted item (or items) when the promotion criteria is met.  &lt;br&gt;&lt;br&gt;Valid integer values for percentage off: &amp;nbsp;&amp;nbsp;&lt;b&gt;Min:&lt;/b&gt; &lt;code&gt;5&lt;/code&gt; &amp;nbsp;&amp;nbsp;&lt;b&gt;Max:&lt;/b&gt; &lt;code&gt;80&lt;/code&gt; | [optional] 
**percentageOffOrder** | **String** | Used for threshold promotions, this is the percentage of the order price that is discounted off the order when the promotion criteria is met. This field is not value for markdown promotions.  &lt;br&gt;&lt;br&gt;Valid integer values for ORDER_DISCOUNT promotions: &amp;nbsp;&amp;nbsp;&lt;b&gt;Min:&lt;/b&gt; &lt;code&gt;5&lt;/code&gt; &amp;nbsp;&amp;nbsp;&lt;b&gt;Max:&lt;/b&gt; &lt;code&gt;80&lt;/code&gt;  &lt;br&gt;&lt;br&gt;For VOLUME_DISCOUNT promotions: Must be set to &lt;code&gt;0&lt;/code&gt; for the first discount rule. | [optional] 


