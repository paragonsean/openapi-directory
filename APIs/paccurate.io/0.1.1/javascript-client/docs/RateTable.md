# PaccurateIo.RateTable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basePrice** | **Number** | The basePrice can be found by estimating the lowest weight-based rate available for a given service, in the example above, solving for basePrice for a $10, 1lb package with the already-solved priceIncreaseRate yields &lt;pre&gt;$10 &#x3D; $5/lb * 1lb + basePrice&lt;br/&gt;$10 &#x3D; $5 + basePrice&lt;br/&gt;basePrice &#x3D; $5&lt;/pre&gt; | [optional] 
**carrier** | **String** | carrier name for rate table to use | [optional] 
**dimFactor** | **Number** | This is the Dimensional Weight divisor. It is given in units of volume per unit weight, e.g., the standard of \&quot;139\&quot; represents 139 cubic inches per pound, and is used to convert the total volume of a carton into a functional minimum weight to be used when rating the carton. E.g., a carton with dimensions 10\&quot; x 10\&quot; x 13.9\&quot; would yield a volume of 1390 cubic inches. This yields &lt;pre&gt;cartonEffectiveMinimumWeight &#x3D; 1390in&amp;sup3; / 139in&amp;sup3;/lb&lt;br/&gt;cartonEffectiveMinimumWeight &#x3D; 10lbs&lt;/pre&gt; | [optional] 
**priceIncreaseRate** | **Number** | Instead of providing the full rate table, you can list a carton \&quot;basePrice\&quot; and a carton \&quot;priceIncreaseRate\&quot;. These two values will be used in a simple linear model to guess carton price, i.e., &lt;pre&gt;cartonPrice &#x3D; priceIncreaseRate * cartonWeight + basePrice&lt;/pre&gt; Oftentimes, this will be enough to get accurate carton selections without needing to send complete customer-based rates. It&#39;s worth considering, as the prices are only estimates to be used in carton selection, with final rating of cartons happening outside of paccurate. This is the predicted rate of increase for a weight-based pricing model. The simplest way to find a servicable value is to take &lt;pre&gt;priceIncreaseRate &#x3D; (maximumPrice - minimumPrice)/(maximumWeight - minimumWeight)&lt;/pre&gt; In the example above, this would yield &lt;pre&gt;priceIncreaseRate &#x3D; ($20-$10)/(3lbs-1lb)&lt;br/&gt;priceIncreaseRate &#x3D; $10/2lbs&lt;br/&gt;priceIncreaseRate &#x3D; $5/lb&lt;/pre&gt; | [optional] 
**rates** | **[Number]** | list of prices to use for the weight that corresponds to its index, e.g., [10, 15, 20] would be $10 for 1lb, $15 for 2lbs, $20 for 3lbs. | [optional] 
**service** | **String** | service name for rate table to use | [optional] 
**weights** | **[Number]** | list of weights to use for the rate that corresponds to its index, e.g., [1, 2, 3] would mean 1lb for the minimum rate ($10), 2lbs for the second rate ($15), and 3lbs for the highest rate ($20). Note that if the highest value from this list is less than the weightMax of the carton, all carton weights exceeding the maximum from this list up to the carton weightMax will not pro-rate but will be estimated at the maximum value in the rate table. | [optional] 
**zone** | **String** | zone of rate table to use | [optional] 


