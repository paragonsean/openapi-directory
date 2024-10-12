# InfluxOssApiService.QueryApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getQuerySuggestions**](QueryApi.md#getQuerySuggestions) | **GET** /query/suggestions | Retrieve query suggestions
[**getQuerySuggestionsName**](QueryApi.md#getQuerySuggestionsName) | **GET** /query/suggestions/{name} | Retrieve query suggestions for a branching suggestion
[**postQuery**](QueryApi.md#postQuery) | **POST** /query | Query InfluxDB
[**postQueryAnalyze**](QueryApi.md#postQueryAnalyze) | **POST** /query/analyze | Analyze an InfluxQL or Flux query
[**postQueryAst**](QueryApi.md#postQueryAst) | **POST** /query/ast | Generate an Abstract Syntax Tree (AST) from a query



## getQuerySuggestions

> FluxSuggestions getQuerySuggestions(opts)

Retrieve query suggestions

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.QueryApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getQuerySuggestions(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**FluxSuggestions**](FluxSuggestions.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQuerySuggestionsName

> FluxSuggestion getQuerySuggestionsName(name, opts)

Retrieve query suggestions for a branching suggestion

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.QueryApi();
let name = "name_example"; // String | The name of the branching suggestion.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getQuerySuggestionsName(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The name of the branching suggestion. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**FluxSuggestion**](FluxSuggestion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postQuery

> File postQuery(opts)

Query InfluxDB

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.QueryApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'acceptEncoding': "'identity'", // String | The Accept-Encoding request HTTP header advertises which content encoding, usually a compression algorithm, the client is able to understand.
  'contentType': "contentType_example", // String | 
  'org': "org_example", // String | Specifies the name of the organization executing the query. Takes either the ID or Name interchangeably. If both `orgID` and `org` are specified, `org` takes precedence.
  'orgID': "orgID_example", // String | Specifies the ID of the organization executing the query. If both `orgID` and `org` are specified, `org` takes precedence.
  'postQueryRequest': new InfluxOssApiService.PostQueryRequest() // PostQueryRequest | Flux query or specification to execute
};
apiInstance.postQuery(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **acceptEncoding** | **String**| The Accept-Encoding request HTTP header advertises which content encoding, usually a compression algorithm, the client is able to understand. | [optional] [default to &#39;identity&#39;]
 **contentType** | **String**|  | [optional] 
 **org** | **String**| Specifies the name of the organization executing the query. Takes either the ID or Name interchangeably. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence. | [optional] 
 **orgID** | **String**| Specifies the ID of the organization executing the query. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence. | [optional] 
 **postQueryRequest** | [**PostQueryRequest**](PostQueryRequest.md)| Flux query or specification to execute | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/vnd.flux
- **Accept**: application/vnd.influx.arrow, text/csv, application/json


## postQueryAnalyze

> AnalyzeQueryResponse postQueryAnalyze(opts)

Analyze an InfluxQL or Flux query

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.QueryApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'contentType': "contentType_example", // String | 
  'query': new InfluxOssApiService.Query() // Query | Flux or InfluxQL query to analyze
};
apiInstance.postQueryAnalyze(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **contentType** | **String**|  | [optional] 
 **query** | [**Query**](Query.md)| Flux or InfluxQL query to analyze | [optional] 

### Return type

[**AnalyzeQueryResponse**](AnalyzeQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postQueryAst

> ASTResponse postQueryAst(opts)

Generate an Abstract Syntax Tree (AST) from a query

Analyzes flux query and generates a query specification.

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.QueryApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'contentType': "contentType_example", // String | 
  'languageRequest': new InfluxOssApiService.LanguageRequest() // LanguageRequest | Analyzed Flux query to generate abstract syntax tree.
};
apiInstance.postQueryAst(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **contentType** | **String**|  | [optional] 
 **languageRequest** | [**LanguageRequest**](LanguageRequest.md)| Analyzed Flux query to generate abstract syntax tree. | [optional] 

### Return type

[**ASTResponse**](ASTResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

