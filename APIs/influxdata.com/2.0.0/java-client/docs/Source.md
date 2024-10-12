

# Source


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_default** | **Boolean** |  |  [optional] |
|**defaultRP** | **String** |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**insecureSkipVerify** | **Boolean** |  |  [optional] |
|**languages** | [**List&lt;LanguagesEnum&gt;**](#List&lt;LanguagesEnum&gt;) |  |  [optional] [readonly] |
|**links** | [**SourceLinks**](SourceLinks.md) |  |  [optional] |
|**metaUrl** | **URI** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**orgID** | **String** |  |  [optional] |
|**password** | **String** |  |  [optional] |
|**sharedSecret** | **String** |  |  [optional] |
|**telegraf** | **String** |  |  [optional] |
|**token** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**url** | **URI** |  |  [optional] |
|**username** | **String** |  |  [optional] |



## Enum: List&lt;LanguagesEnum&gt;

| Name | Value |
|---- | -----|
| FLUX | &quot;flux&quot; |
| INFLUXQL | &quot;influxql&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| V1 | &quot;v1&quot; |
| V2 | &quot;v2&quot; |
| SELF | &quot;self&quot; |



