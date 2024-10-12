

# Status


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiVersion** | **String** | Represents current version of the exposed API |  |
|**serviceStatus** | [**ServiceStatusEnum**](#ServiceStatusEnum) | Represents the availability of the service |  |
|**serviceVersion** | **String** | Represents current version of the Semantria service |  |
|**supportedCompression** | **String** | Exposes supported compression algorithms. Currently only gzip and deflate are supported |  |
|**supportedEncoding** | **String** | Exposes supported content encoding. Currently only UTF-8 is supported |  |
|**supportedLanguages** | **List&lt;String&gt;** | Exposes list of supported languages |  |



## Enum: ServiceStatusEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| PENDING | &quot;pending&quot; |
| SOLD | &quot;sold&quot; |



