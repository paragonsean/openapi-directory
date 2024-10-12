

# CacheConfiguration

Caching settings for a caching-type route. To disable caching, do not provide a cacheConfiguration object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dynamicCompression** | [**DynamicCompressionEnum**](#DynamicCompressionEnum) | Whether to use dynamic compression for cached content |  [optional] |
|**queryParameterStripDirective** | [**QueryParameterStripDirectiveEnum**](#QueryParameterStripDirectiveEnum) | Treatment of URL query terms when forming the cache key. |  [optional] |



## Enum: DynamicCompressionEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: QueryParameterStripDirectiveEnum

| Name | Value |
|---- | -----|
| STRIP_NONE | &quot;StripNone&quot; |
| STRIP_ALL | &quot;StripAll&quot; |



