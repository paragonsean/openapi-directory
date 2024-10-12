# Semantria.ProcessingCollectionsApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelCollection**](ProcessingCollectionsApi.md#cancelCollection) | **DELETE** /collection/{collection_id}.{content_type} | Cancel collection analysis
[**queueCollection**](ProcessingCollectionsApi.md#queueCollection) | **POST** /collection.{content_type} | Queue collection for analysis
[**receiveCollectionAnalyticData**](ProcessingCollectionsApi.md#receiveCollectionAnalyticData) | **GET** /collection/{collection_id}.{content_type} | Retrieve collection analysis or its status in queue
[**retrieveProcessedCollections**](ProcessingCollectionsApi.md#retrieveProcessedCollections) | **GET** /collection/processed.{content_type} | Retrieve collections analysis



## cancelCollection

> cancelCollection(collectionId, contentType, opts)

Cancel collection analysis

This method cancels collection analysis by unique ID on Semantria side if it is waiting for analysis in queue.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ProcessingCollectionsApi();
let collectionId = "collectionId_example"; // String | Collection ID
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration used for analysis.
};
apiInstance.cancelCollection(collectionId, contentType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collectionId** | **String**| Collection ID | 
 **contentType** | **String**|  | 
 **configId** | **String**| Identifier of configuration used for analysis. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## queueCollection

> Collection queueCollection(contentType, collection, opts)

Queue collection for analysis

This method queues collection of documents onto the server for analysis. Queued collection of documents analyzes in common context as entire thing. If unique configuration ID provided, Semantria uses settings of that configuration during analysis, in opposite the primary configuration uses. Collection IDs are unique in scope of configuration. If the same ID appears twice, Semantria overrides existing collection with the new Data

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ProcessingCollectionsApi();
let contentType = "contentType_example"; // String | 
let collection = {key: null}; // Object | Parametrized JSON or XML object.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration used for analysis.
};
apiInstance.queueCollection(contentType, collection, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **collection** | **Object**| Parametrized JSON or XML object. | 
 **configId** | **String**| Identifier of configuration used for analysis. | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## receiveCollectionAnalyticData

> CollectionAnalyticData receiveCollectionAnalyticData(collectionId, contentType, opts)

Retrieve collection analysis or its status in queue

This method retrieves analysis results for documents collection by its unique ID or the collection’s status in queue if it did not analyzed yet. Semantria guarantees delivering of all collections back to the client even if they FAILED on Semantria side due to some reason.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ProcessingCollectionsApi();
let collectionId = "collectionId_example"; // String | Collection ID
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration used for analysis.
};
apiInstance.receiveCollectionAnalyticData(collectionId, contentType, opts, (error, data, response) => {
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
 **collectionId** | **String**| Collection ID | 
 **contentType** | **String**|  | 
 **configId** | **String**| Identifier of configuration used for analysis. | [optional] 

### Return type

[**CollectionAnalyticData**](CollectionAnalyticData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## retrieveProcessedCollections

> CollectionAnalyticData retrieveProcessedCollections(contentType, opts)

Retrieve collections analysis

This method retrieves analysis results for processed collections from Semantria. FAILED collections will have FAILED status in response. Semantria responds with limited amount of results per API call. If configuration ID provided, Semantria responds with the collections, which were queued using the same configuration ID, in opposite Primary configuration uses.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ProcessingCollectionsApi();
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration used for analysis.
};
apiInstance.retrieveProcessedCollections(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **configId** | **String**| Identifier of configuration used for analysis. | [optional] 

### Return type

[**CollectionAnalyticData**](CollectionAnalyticData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

