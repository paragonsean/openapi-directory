# OpenTrialsApi.TrialsApi

All URIs are relative to *http://opentrials.local/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRecord**](TrialsApi.md#getRecord) | **GET** /trials/{trialId}/records/{id} | 
[**getRecords**](TrialsApi.md#getRecords) | **GET** /trials/{id}/records | 
[**getTrial**](TrialsApi.md#getTrial) | **GET** /trials/{id} | 
[**searchTrials**](TrialsApi.md#searchTrials) | **GET** /search | 



## getRecord

> Record getRecord(trialId, id)



Returns a trial&#39;s raw record from its sources

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.TrialsApi();
let trialId = "trialId_example"; // String | ID of the trial
let id = "id_example"; // String | ID of the trial's record
apiInstance.getRecord(trialId, id, (error, data, response) => {
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
 **trialId** | **String**| ID of the trial | 
 **id** | **String**| ID of the trial&#39;s record | 

### Return type

[**Record**](Record.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecords

> [Record] getRecords(id)



Returns a trial&#39;s raw records from its sources

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.TrialsApi();
let id = "id_example"; // String | ID of the trial
apiInstance.getRecords(id, (error, data, response) => {
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
 **id** | **String**| ID of the trial | 

### Return type

[**[Record]**](Record.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrial

> Trial getTrial(id)



Returns a trial&#39;s details and related entities (e.g. &#x60;conditions&#x60;).

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.TrialsApi();
let id = "id_example"; // String | ID of the trial
apiInstance.getTrial(id, (error, data, response) => {
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
 **id** | **String**| ID of the trial | 

### Return type

[**Trial**](Trial.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchTrials

> TrialSearchResults searchTrials(opts)



Returns trials based on a search query. By default, it&#39;ll search in all of a trial&#39;s attributes. - &#x60;q&#x60; is a [ElasticSearch query string](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) (e.g. &#x60;public_title:(depressive OR depression)&#x60;) - &#x60;page&#x60; can take a value between &#x60;1&#x60; and &#x60;100&#x60; - &#x60;per_page&#x60; can take a value between &#x60;10&#x60; and &#x60;100&#x60;

### Example

```javascript
import OpenTrialsApi from 'open_trials_api';

let apiInstance = new OpenTrialsApi.TrialsApi();
let opts = {
  'q': "q_example", // String | The search query (follows the [ElasticSearch Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) syntax)
  'page': 1, // Number | The page number
  'perPage': 20 // Number | Number of items per page
};
apiInstance.searchTrials(opts, (error, data, response) => {
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
 **q** | **String**| The search query (follows the [ElasticSearch Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) syntax) | [optional] 
 **page** | **Number**| The page number | [optional] [default to 1]
 **perPage** | **Number**| Number of items per page | [optional] [default to 20]

### Return type

[**TrialSearchResults**](TrialSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

