

# CreateApiCacheRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ttl** | **Integer** | &lt;p&gt;TTL in seconds for cache entries.&lt;/p&gt; &lt;p&gt;Valid values are 1–3,600 seconds.&lt;/p&gt; |  |
|**transitEncryptionEnabled** | **Boolean** | Transit encryption flag when connecting to cache. You cannot update this setting after creation. |  [optional] |
|**atRestEncryptionEnabled** | **Boolean** | At-rest encryption flag for cache. You cannot update this setting after creation. |  [optional] |
|**apiCachingBehavior** | [**ApiCachingBehaviorEnum**](#ApiCachingBehaviorEnum) | &lt;p&gt;Caching behavior.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;FULL_REQUEST_CACHING&lt;/b&gt;: All requests are fully cached.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;PER_RESOLVER_CACHING&lt;/b&gt;: Individual resolvers that you specify are cached.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |
|**type** | [**TypeEnum**](#TypeEnum) | &lt;p&gt;The cache instance type. Valid values are &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SMALL&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MEDIUM&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LARGE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;XLARGE&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LARGE_2X&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LARGE_4X&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LARGE_8X&lt;/code&gt; (not available in all regions)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LARGE_12X&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.&lt;/p&gt; &lt;p&gt;The following legacy instance types are available, but their use is discouraged:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;T2_SMALL&lt;/b&gt;: A t2.small instance type.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;T2_MEDIUM&lt;/b&gt;: A t2.medium instance type.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;R4_LARGE&lt;/b&gt;: A r4.large instance type.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;R4_XLARGE&lt;/b&gt;: A r4.xlarge instance type.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;R4_2XLARGE&lt;/b&gt;: A r4.2xlarge instance type.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;R4_4XLARGE&lt;/b&gt;: A r4.4xlarge instance type.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;R4_8XLARGE&lt;/b&gt;: A r4.8xlarge instance type.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |



## Enum: ApiCachingBehaviorEnum

| Name | Value |
|---- | -----|
| FULL_REQUEST_CACHING | &quot;FULL_REQUEST_CACHING&quot; |
| PER_RESOLVER_CACHING | &quot;PER_RESOLVER_CACHING&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| T2_SMALL | &quot;T2_SMALL&quot; |
| T2_MEDIUM | &quot;T2_MEDIUM&quot; |
| R4_LARGE | &quot;R4_LARGE&quot; |
| R4_XLARGE | &quot;R4_XLARGE&quot; |
| R4_2_XLARGE | &quot;R4_2XLARGE&quot; |
| R4_4_XLARGE | &quot;R4_4XLARGE&quot; |
| R4_8_XLARGE | &quot;R4_8XLARGE&quot; |
| SMALL | &quot;SMALL&quot; |
| MEDIUM | &quot;MEDIUM&quot; |
| LARGE | &quot;LARGE&quot; |
| XLARGE | &quot;XLARGE&quot; |
| LARGE_2_X | &quot;LARGE_2X&quot; |
| LARGE_4_X | &quot;LARGE_4X&quot; |
| LARGE_8_X | &quot;LARGE_8X&quot; |
| LARGE_12_X | &quot;LARGE_12X&quot; |



