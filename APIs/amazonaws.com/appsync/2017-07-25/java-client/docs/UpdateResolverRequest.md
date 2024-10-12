

# UpdateResolverRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceName** | **String** | The new data source name. |  [optional] |
|**requestMappingTemplate** | **String** | &lt;p&gt;The new request mapping template.&lt;/p&gt; &lt;p&gt;A resolver uses a request mapping template to convert a GraphQL expression into a format that a data source can understand. Mapping templates are written in Apache Velocity Template Language (VTL).&lt;/p&gt; &lt;p&gt;VTL request mapping templates are optional when using an Lambda data source. For all other data sources, VTL request and response mapping templates are required.&lt;/p&gt; |  [optional] |
|**responseMappingTemplate** | **String** | The new response mapping template. |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | &lt;p&gt;The resolver type.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;UNIT&lt;/b&gt;: A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;PIPELINE&lt;/b&gt;: A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of &lt;code&gt;Function&lt;/code&gt; objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  [optional] |
|**pipelineConfig** | [**CreateResolverRequestPipelineConfig**](CreateResolverRequestPipelineConfig.md) |  |  [optional] |
|**syncConfig** | [**CreateFunctionRequestSyncConfig**](CreateFunctionRequestSyncConfig.md) |  |  [optional] |
|**cachingConfig** | [**CreateResolverRequestCachingConfig**](CreateResolverRequestCachingConfig.md) |  |  [optional] |
|**maxBatchSize** | **Integer** | The maximum batching size for a resolver. |  [optional] |
|**runtime** | [**CreateFunctionRequestRuntime**](CreateFunctionRequestRuntime.md) |  |  [optional] |
|**code** | **String** | The &lt;code&gt;resolver&lt;/code&gt; code that contains the request and response functions. When code is used, the &lt;code&gt;runtime&lt;/code&gt; is required. The &lt;code&gt;runtime&lt;/code&gt; value must be &lt;code&gt;APPSYNC_JS&lt;/code&gt;. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| UNIT | &quot;UNIT&quot; |
| PIPELINE | &quot;PIPELINE&quot; |



