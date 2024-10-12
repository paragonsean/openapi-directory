

# UpdateFunctionRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The &lt;code&gt;Function&lt;/code&gt; name. |  |
|**description** | **String** | The &lt;code&gt;Function&lt;/code&gt; description. |  [optional] |
|**dataSourceName** | **String** | The &lt;code&gt;Function&lt;/code&gt; &lt;code&gt;DataSource&lt;/code&gt; name. |  |
|**requestMappingTemplate** | **String** | The &lt;code&gt;Function&lt;/code&gt; request mapping template. Functions support only the 2018-05-29 version of the request mapping template. |  [optional] |
|**responseMappingTemplate** | **String** | The &lt;code&gt;Function&lt;/code&gt; request mapping template. |  [optional] |
|**functionVersion** | **String** | The &lt;code&gt;version&lt;/code&gt; of the request mapping template. Currently, the supported value is 2018-05-29. Note that when using VTL and mapping templates, the &lt;code&gt;functionVersion&lt;/code&gt; is required. |  [optional] |
|**syncConfig** | [**CreateFunctionRequestSyncConfig**](CreateFunctionRequestSyncConfig.md) |  |  [optional] |
|**maxBatchSize** | **Integer** | The maximum batching size for a resolver. |  [optional] |
|**runtime** | [**CreateFunctionRequestRuntime**](CreateFunctionRequestRuntime.md) |  |  [optional] |
|**code** | **String** | The &lt;code&gt;function&lt;/code&gt; code that contains the request and response functions. When code is used, the &lt;code&gt;runtime&lt;/code&gt; is required. The &lt;code&gt;runtime&lt;/code&gt; value must be &lt;code&gt;APPSYNC_JS&lt;/code&gt;. |  [optional] |



