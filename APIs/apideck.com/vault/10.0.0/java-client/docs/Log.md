

# Log


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiStyle** | **String** | Indicates if the request was made via REST or Graphql endpoint. |  |
|**baseUrl** | **String** | The Apideck base URL the request was made to. |  |
|**childRequest** | **Boolean** | Indicates whether or not this is a child or parent request. |  |
|**consumerId** | **String** | The consumer Id associated with the request. |  |
|**duration** | **BigDecimal** | The entire execution time in milliseconds it took to call the Apideck service provider. |  |
|**errorMessage** | **String** | If error occurred, this is brief explanation |  [optional] |
|**execution** | **Integer** | The entire execution time in milliseconds it took to make the request. |  |
|**hasChildren** | **Boolean** | When request is a parent request, this indicates if there are child requests associated. |  |
|**httpMethod** | **String** | HTTP Method of request. |  |
|**id** | **String** | UUID acting as Request Identifier. |  |
|**latency** | **BigDecimal** | Latency added by making this request via Unified Api. |  |
|**operation** | [**LogOperation**](LogOperation.md) |  |  |
|**parentId** | **String** | When request is a child request, this UUID indicates it&#39;s parent request. |  |
|**path** | **String** | The path component of the URI the request was made to. |  |
|**sandbox** | **Boolean** | Indicates whether the request was made using Apidecks sandbox credentials or not. |  |
|**service** | [**LogService**](LogService.md) |  |  |
|**sourceIp** | **String** | The IP address of the source of the request. |  [optional] |
|**statusCode** | **Integer** | HTTP Status code that was returned. |  |
|**success** | **Boolean** | Whether or not the request was successful. |  |
|**timestamp** | **String** | ISO Date and time when the request was made. |  |
|**unifiedApi** | [**UnifiedApiEnum**](#UnifiedApiEnum) | Which Unified Api request was made to. |  |



## Enum: UnifiedApiEnum

| Name | Value |
|---- | -----|
| CRM | &quot;crm&quot; |
| LEAD | &quot;lead&quot; |
| PROXY | &quot;proxy&quot; |
| VAULT | &quot;vault&quot; |
| ACCOUNTING | &quot;accounting&quot; |
| HRIS | &quot;hris&quot; |
| ATS | &quot;ats&quot; |
| ECOMMERCE | &quot;ecommerce&quot; |
| ISSUE_TRACKING | &quot;issue-tracking&quot; |
| POS | &quot;pos&quot; |
| FILE_STORAGE | &quot;file-storage&quot; |
| SMS | &quot;sms&quot; |



