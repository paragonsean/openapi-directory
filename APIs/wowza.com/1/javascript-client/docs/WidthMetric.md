# WowzaStreamingCloudRestApiReferenceDocumentation.WidthMetric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **String** | The status of the current key. Possible values are &lt;strong&gt;normal&lt;/strong&gt; (everything is fine), &lt;strong&gt;warning&lt;/strong&gt; (something may be misconfigured), and &lt;strong&gt;no_data&lt;/strong&gt; (no data was returned, perhaps because the instance isn&#39;t running). | [optional] 
**text** | **String** | A message related to the value and status of the current key. Usually blank unless there&#39;s a warning status. | [optional] 
**units** | **String** | The unit of the returned value, such as &lt;strong&gt;Kbps&lt;/strong&gt;, &lt;strong&gt;bps&lt;/strong&gt;, &lt;strong&gt;%&lt;/strong&gt;, &lt;strong&gt;FPS&lt;/strong&gt;, or &lt;strong&gt;GOP&lt;/strong&gt;. | [optional] 
**value** | **Number** | The value of the associated key. | [optional] 


