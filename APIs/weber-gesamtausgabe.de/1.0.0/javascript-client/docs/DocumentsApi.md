# WeGaApi.DocumentsApi

All URIs are relative to *http://localhost:8080/exist/apps/WeGA-WebApp/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documentsDocIDGet**](DocumentsApi.md#documentsDocIDGet) | **GET** /documents/{docID} | Returns documents by ID
[**documentsFindByAuthorAuthorIDGet**](DocumentsApi.md#documentsFindByAuthorAuthorIDGet) | **GET** /documents/findByAuthor/{authorID} | Finds documents by author
[**documentsFindByDateGet**](DocumentsApi.md#documentsFindByDateGet) | **GET** /documents/findByDate | Finds documents by date
[**documentsFindByMentionDocIDGet**](DocumentsApi.md#documentsFindByMentionDocIDGet) | **GET** /documents/findByMention/{docID} | Finds documents by reference
[**documentsGet**](DocumentsApi.md#documentsGet) | **GET** /documents | Lists all documents



## documentsDocIDGet

> [Document] documentsDocIDGet(docID)

Returns documents by ID

This endpoint returns documents, indicated by an ID.  Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662 

### Example

```javascript
import WeGaApi from 'we_ga_api';

let apiInstance = new WeGaApi.DocumentsApi();
let docID = "'A002068'"; // String | The document identifier to search for
apiInstance.documentsDocIDGet(docID, (error, data, response) => {
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
 **docID** | **String**| The document identifier to search for | [default to &#39;A002068&#39;]

### Return type

[**[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## documentsFindByAuthorAuthorIDGet

> [Document] documentsFindByAuthorAuthorIDGet(authorID, opts)

Finds documents by author

This endpoint returns a list of documents by a given author – optionally filtered by document type  

### Example

```javascript
import WeGaApi from 'we_ga_api';

let apiInstance = new WeGaApi.DocumentsApi();
let authorID = "'A002068'"; // String | The author ID to search for. Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662 
let opts = {
  'docType': ["null"], // [String] | The WeGA document type
  'offset': 1, // Number | Position of first item to retrieve (starting from 1)
  'limit': 10 // Number | Number of items to retrieve (200 max)
};
apiInstance.documentsFindByAuthorAuthorIDGet(authorID, opts, (error, data, response) => {
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
 **authorID** | **String**| The author ID to search for. Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662  | [default to &#39;A002068&#39;]
 **docType** | [**[String]**](String.md)| The WeGA document type | [optional] 
 **offset** | **Number**| Position of first item to retrieve (starting from 1) | [optional] [default to 1]
 **limit** | **Number**| Number of items to retrieve (200 max) | [optional] [default to 10]

### Return type

[**[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## documentsFindByDateGet

> [Document] documentsFindByDateGet(fromDate, opts)

Finds documents by date

This endpoint returns a list of documents related to the given date – optionally filtered by document type.  

### Example

```javascript
import WeGaApi from 'we_ga_api';

let apiInstance = new WeGaApi.DocumentsApi();
let fromDate = new Date("2013-10-20"); // Date | The min date to search for
let opts = {
  'toDate': new Date("2013-10-20"), // Date | The max date to search for
  'docType': ["null"], // [String] | The WeGA document type
  'offset': 1, // Number | Position of first item to retrieve (starting from 1)
  'limit': 10 // Number | Number of items to retrieve (200 max)
};
apiInstance.documentsFindByDateGet(fromDate, opts, (error, data, response) => {
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
 **fromDate** | **Date**| The min date to search for | 
 **toDate** | **Date**| The max date to search for | [optional] 
 **docType** | [**[String]**](String.md)| The WeGA document type | [optional] 
 **offset** | **Number**| Position of first item to retrieve (starting from 1) | [optional] [default to 1]
 **limit** | **Number**| Number of items to retrieve (200 max) | [optional] [default to 10]

### Return type

[**[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## documentsFindByMentionDocIDGet

> [Document] documentsFindByMentionDocIDGet(docID, opts)

Finds documents by reference

This endpoint returns a list of documents that reference a particular docID – optionally filtered by document type.  

### Example

```javascript
import WeGaApi from 'we_ga_api';

let apiInstance = new WeGaApi.DocumentsApi();
let docID = "'A002068'"; // String | The document ID that is to be mentioned. Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662 
let opts = {
  'docType': ["null"], // [String] | The WeGA document type
  'offset': 1, // Number | Position of first item to retrieve (starting from 1)
  'limit': 10 // Number | Number of items to retrieve (200 max)
};
apiInstance.documentsFindByMentionDocIDGet(docID, opts, (error, data, response) => {
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
 **docID** | **String**| The document ID that is to be mentioned. Accepted ID formats are WeGA, e.g. A002068 or http://weber-gesamtausgabe.de/A002068, VIAF, e.g. http://viaf.org/viaf/14959938, or  GND, e.g. http://d-nb.info/gnd/118629662  | [default to &#39;A002068&#39;]
 **docType** | [**[String]**](String.md)| The WeGA document type | [optional] 
 **offset** | **Number**| Position of first item to retrieve (starting from 1) | [optional] [default to 1]
 **limit** | **Number**| Number of items to retrieve (200 max) | [optional] [default to 10]

### Return type

[**[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## documentsGet

> [Document] documentsGet(opts)

Lists all documents

The Documents endpoint returns a list of all documents from the WeGA digital edition. 

### Example

```javascript
import WeGaApi from 'we_ga_api';

let apiInstance = new WeGaApi.DocumentsApi();
let opts = {
  'docType': ["null"], // [String] | The WeGA document type
  'offset': 1, // Number | Position of first item to retrieve (starting from 1)
  'limit': 10 // Number | Number of items to retrieve (200 max)
};
apiInstance.documentsGet(opts, (error, data, response) => {
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
 **docType** | [**[String]**](String.md)| The WeGA document type | [optional] 
 **offset** | **Number**| Position of first item to retrieve (starting from 1) | [optional] [default to 1]
 **limit** | **Number**| Number of items to retrieve (200 max) | [optional] [default to 10]

### Return type

[**[Document]**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

