# AnalyticsApi.RateLimit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiContext** | **String** | The context of the API for which rate-limit data is returned. For example &lt;code&gt;buy&lt;/code&gt;, &lt;code&gt;sell&lt;/code&gt;, &lt;code&gt;commerce&lt;/code&gt;, &lt;code&gt;developer&lt;/code&gt; or &lt;code&gt;tradingapi&lt;/code&gt;. | [optional] 
**apiName** | **String** | The name of the API for which rate-limit data is returned. For example &lt;code&gt;browse&lt;/code&gt; for the Buy API, &lt;code&gt;inventory&lt;/code&gt; for the Sell API, &lt;code&gt;taxonomy&lt;/code&gt; for the Commerce API, or &lt;code&gt;tradingapi&lt;/code&gt; for Trading API. | [optional] 
**apiVersion** | **String** | The version of the API for which rate-limit data is returned. For example &lt;code&gt;v1&lt;/code&gt; or &lt;code&gt;v2&lt;/code&gt;. | [optional] 
**resources** | [**[Resource]**](Resource.md) | A list of the methods for which rate-limit data is returned. For example &lt;code&gt;item&lt;/code&gt; for the Feed API, &lt;code&gt;getOrder&lt;/code&gt; for the Fulfillment API, &lt;code&gt;getProduct&lt;/code&gt; for the Catalog API, &lt;code&gt;AddItems&lt;/code&gt; for the Trading API. | [optional] 


