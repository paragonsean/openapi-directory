

# Gzip

Configuration for gzip of service responses

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blackList** | **List&lt;String&gt;** | Blacklisted mime types. Wildcard supported |  |
|**bufferSize** | **Long** | Size of the GZip buffer |  |
|**chunkedThreshold** | **Long** | Threshold for chunking data |  |
|**compressionLevel** | **Integer** | Compression level. From 0 to 9 |  |
|**enabled** | **Boolean** | Whether gzip compression is enabled or not |  |
|**excludedPatterns** | **List&lt;String&gt;** | Patterns that are excluded from gzipping |  |
|**whiteList** | **List&lt;String&gt;** | Whitelisted mime types. Wildcard supported |  |



