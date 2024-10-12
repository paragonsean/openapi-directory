# BcLaws.DocumentApi

All URIs are relative to *http://www.bclaws.ca/civix*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documentIdAspectIdCivixIndexIdCivixDocumentIdGet**](DocumentApi.md#documentIdAspectIdCivixIndexIdCivixDocumentIdGet) | **GET** /document/id/{aspectId}/{civixIndexId}/{civixDocumentId} | Retrieves a specific document from the BCLaws legislative repository (HTML format)
[**documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet**](DocumentApi.md#documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet) | **GET** /document/id/{aspectId}/{civixIndexId}/{civixDocumentId}/search/{searchString} | Retrieves a specific document from the BCLaws legislative repository with search text highlighted (HTML format)
[**documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet**](DocumentApi.md#documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet) | **GET** /document/id/{aspectId}/{civixIndexId}/{civixDocumentId}/xml | Retrieves a specific document from the BCLaws legislative repository (XML format)
[**documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet**](DocumentApi.md#documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet) | **GET** /document/id/{aspectId}/{civixIndexId}/{civixDocumentId}/xml/search/{searchString} | Retrieves a specific document from the BCLaws legislative repository with search text highlighted (XML format)



## documentIdAspectIdCivixIndexIdCivixDocumentIdGet

> documentIdAspectIdCivixIndexIdCivixDocumentIdGet(aspectId, civixIndexId, civixDocumentId)

Retrieves a specific document from the BCLaws legislative repository (HTML format)

The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

### Example

```javascript
import BcLaws from 'bc_laws';

let apiInstance = new BcLaws.DocumentApi();
let aspectId = "'complete'"; // String | The identifier of the 'aspect' (content group) to search
let civixIndexId = "'statreg'"; // String | Index identification code
let civixDocumentId = "'01009_01'"; // String | The document identification code for an index or directory
apiInstance.documentIdAspectIdCivixIndexIdCivixDocumentIdGet(aspectId, civixIndexId, civixDocumentId, (error, data, response) => {
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
 **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to &#39;complete&#39;]
 **civixIndexId** | **String**| Index identification code | [default to &#39;statreg&#39;]
 **civixDocumentId** | **String**| The document identification code for an index or directory | [default to &#39;01009_01&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet

> documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet(aspectId, civixIndexId, civixDocumentId, searchString)

Retrieves a specific document from the BCLaws legislative repository with search text highlighted (HTML format)

The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

### Example

```javascript
import BcLaws from 'bc_laws';

let apiInstance = new BcLaws.DocumentApi();
let aspectId = "'complete'"; // String | The identifier of the 'aspect' (content group) to search
let civixIndexId = "'statreg'"; // String | Index identification code
let civixDocumentId = "'01009_01'"; // String | The document identification code for an index or directory
let searchString = "'water'"; // String | The text to search for within the document
apiInstance.documentIdAspectIdCivixIndexIdCivixDocumentIdSearchSearchStringGet(aspectId, civixIndexId, civixDocumentId, searchString, (error, data, response) => {
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
 **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to &#39;complete&#39;]
 **civixIndexId** | **String**| Index identification code | [default to &#39;statreg&#39;]
 **civixDocumentId** | **String**| The document identification code for an index or directory | [default to &#39;01009_01&#39;]
 **searchString** | **String**| The text to search for within the document | [default to &#39;water&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet

> documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet(aspectId, civixIndexId, civixDocumentId)

Retrieves a specific document from the BCLaws legislative repository (XML format)

The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

### Example

```javascript
import BcLaws from 'bc_laws';

let apiInstance = new BcLaws.DocumentApi();
let aspectId = "'complete'"; // String | The identifier of the 'aspect' (content group) to search
let civixIndexId = "'statreg'"; // String | Index identification code
let civixDocumentId = "'01009_01'"; // String | The document identification code for an index or directory
apiInstance.documentIdAspectIdCivixIndexIdCivixDocumentIdXmlGet(aspectId, civixIndexId, civixDocumentId, (error, data, response) => {
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
 **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to &#39;complete&#39;]
 **civixIndexId** | **String**| Index identification code | [default to &#39;statreg&#39;]
 **civixDocumentId** | **String**| The document identification code for an index or directory | [default to &#39;01009_01&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet

> documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet(aspectId, civixIndexId, civixDocumentId, searchString)

Retrieves a specific document from the BCLaws legislative repository with search text highlighted (XML format)

The /document API allows you to retrieve actual documents from the BCLaws legislative repository. To retrieve a document from the repository you need the aspect identifier and two other specific pieces of information about the document: the index identifier and the document identifier. These unique identifiers can be retrieved from the /content API.

### Example

```javascript
import BcLaws from 'bc_laws';

let apiInstance = new BcLaws.DocumentApi();
let aspectId = "'complete'"; // String | The identifier of the 'aspect' (content group) to search
let civixIndexId = "'statreg'"; // String | Index identification code
let civixDocumentId = "'01009_01'"; // String | The document identification code for an index or directory
let searchString = "'water'"; // String | The text to search for within the document
apiInstance.documentIdAspectIdCivixIndexIdCivixDocumentIdXmlSearchSearchStringGet(aspectId, civixIndexId, civixDocumentId, searchString, (error, data, response) => {
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
 **aspectId** | **String**| The identifier of the &#39;aspect&#39; (content group) to search | [default to &#39;complete&#39;]
 **civixIndexId** | **String**| Index identification code | [default to &#39;statreg&#39;]
 **civixDocumentId** | **String**| The document identification code for an index or directory | [default to &#39;01009_01&#39;]
 **searchString** | **String**| The text to search for within the document | [default to &#39;water&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

