# ENanoMapperDatabase.SearchApi

All URIs are relative to *https://api.ideaconsult.net/nanoreg1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**solrqueryGet**](SearchApi.md#solrqueryGet) | **GET** /select | Apache Solr powered search
[**solrqueryPost**](SearchApi.md#solrqueryPost) | **POST** /select | Apache Solr powered search



## solrqueryGet

> SolrResponse solrqueryGet(opts)

Apache Solr powered search

GET is simpler to use, but imposes restrictions on the complexity and the lenght of the parameters.

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.SearchApi();
let opts = {
  'q': "*:*", // String | The query
  'start': 0, // Number | Starting page
  'rows': 10, // Number | Page size
  'wt': "json" // String | Response format
};
apiInstance.solrqueryGet(opts, (error, data, response) => {
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
 **q** | **String**| The query | [optional] 
 **start** | **Number**| Starting page | [optional] 
 **rows** | **Number**| Page size | [optional] 
 **wt** | **String**| Response format | [optional] [default to &#39;xml&#39;]

### Return type

[**SolrResponse**](SolrResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## solrqueryPost

> SolrResponse solrqueryPost(opts)

Apache Solr powered search

POST is more complex to use, but also allows for much for complex and lengthy queries.

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.SearchApi();
let opts = {
  'wt': "json", // String | Response format
  'solrqueryPostRequest': new ENanoMapperDatabase.SolrqueryPostRequest() // SolrqueryPostRequest | a JSON object with Solr query parameters
};
apiInstance.solrqueryPost(opts, (error, data, response) => {
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
 **wt** | **String**| Response format | [optional] [default to &#39;xml&#39;]
 **solrqueryPostRequest** | [**SolrqueryPostRequest**](SolrqueryPostRequest.md)| a JSON object with Solr query parameters | [optional] 

### Return type

[**SolrResponse**](SolrResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml

