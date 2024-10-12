# FrankieFinancialApi.DocumentApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compareDocument**](DocumentApi.md#compareDocument) | **POST** /document/new/compare | Create Document and Compare to Original.
[**createDocument**](DocumentApi.md#createDocument) | **POST** /document | Create New Document.
[**createScanDocument**](DocumentApi.md#createScanDocument) | **POST** /document/new/scan | Create and OCR Scan Document.
[**deleteDocument**](DocumentApi.md#deleteDocument) | **DELETE** /document/{documentId} | Delete Document.
[**queryDocument**](DocumentApi.md#queryDocument) | **GET** /document/{documentId} | Retrieve Document Details
[**queryDocumentChecks**](DocumentApi.md#queryDocumentChecks) | **GET** /document/{documentId}/checks | Retrieve Document Verification Check Details. 
[**queryDocumentFull**](DocumentApi.md#queryDocumentFull) | **GET** /document/{documentId}/full | Retrieve Document and Scan Data
[**searchDocument**](DocumentApi.md#searchDocument) | **POST** /document/search | Search For a Document !! EXPERIMENTAL !!
[**updateCompareDocument**](DocumentApi.md#updateCompareDocument) | **POST** /document/{documentId}/compare | Update Document and Compare to Original.
[**updateDocument**](DocumentApi.md#updateDocument) | **POST** /document/{documentId} | Update Existing Document.
[**updateScanDocument**](DocumentApi.md#updateScanDocument) | **POST** /document/{documentId}/scan | Update and OCR Scan Document
[**updateVerifyDocument**](DocumentApi.md#updateVerifyDocument) | **POST** /document/{documentId}/verify | Update and Verify Document.
[**verifyDocument**](DocumentApi.md#verifyDocument) | **POST** /document/new/verify | Create and Verify Document.



## compareDocument

> DocumentCompareResultObject compareDocument(xFrankieCustomerID, comparisonSet, opts)

Create Document and Compare to Original.

Creates a new document from the \&quot;toDocument\&quot; parameter (usual rules apply in that it must be a valid document, with no existing documentId). The compareDocument can be an existing documentId, or it too can be new as well.   * If existing (i.e. a valid DocumentId is supplied), it will be updated with any new data supplied before being sent to the comparison process.   * If new, then a new document will be created too, and the ID returned in the result.    The document scans are then sent for processing and comparison, such as comparing a selfie-video against a drivers licence photo.  * NOTE: This is NOT the verification process (see /document/verify)  * NOTE: This is NOT the OCR data extraction process either (see /document/scan) 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let comparisonSet = new FrankieFinancialApi.ComparisonSet(); // ComparisonSet | Contains the document (compareDocument) we want to compare (toDocument) 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56 // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
};
apiInstance.compareDocument(xFrankieCustomerID, comparisonSet, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **comparisonSet** | [**ComparisonSet**](ComparisonSet.md)| Contains the document (compareDocument) we want to compare (toDocument)  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 

### Return type

[**DocumentCompareResultObject**](DocumentCompareResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDocument

> DocumentResultObject createDocument(xFrankieCustomerID, opts)

Create New Document.

Create a document object. A document object can be used to simply store data around a given identity or similar document. You can attach scans, PDFs, photos, videos, etc to the objectif you wish and these may be processed later (using the /scan function) to extract useful information. Or you can manually supply the extracted information if you choose. Document objects can be used to create an entity, based on extracted or supplied data; or it may be attached to an existing entity, either directly or through an ID check. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'document': new FrankieFinancialApi.IdentityDocumentObject() // IdentityDocumentObject | 
};
apiInstance.createDocument(xFrankieCustomerID, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)|  | [optional] 

### Return type

[**DocumentResultObject**](DocumentResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createScanDocument

> DocumentScanResultObject createScanDocument(xFrankieCustomerID, opts)

Create and OCR Scan Document.

Create a document object. This is then processed to extract useful information and create an entity; or it may be attached to an entity, either directly or through an ID check. The service will attempt to extract relevant data from any/all uploaded images/documents and will place those in the extraData KVP block. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56, // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
  'document': new FrankieFinancialApi.IdentityDocumentObject() // IdentityDocumentObject | 
};
apiInstance.createScanDocument(xFrankieCustomerID, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 
 **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)|  | [optional] 

### Return type

[**DocumentScanResultObject**](DocumentScanResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDocument

> BasicStatusResultObject deleteDocument(xFrankieCustomerID, documentId, opts)

Delete Document.

Mark this document as deleted. It will then become effectively invisible to all queries, but will be available in anonymised form for a past check. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let documentId = "documentId_example"; // String | The documentId returned previously from an earlier call to /check or /entity or /document
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56 // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
};
apiInstance.deleteDocument(xFrankieCustomerID, documentId, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **documentId** | **String**| The documentId returned previously from an earlier call to /check or /entity or /document | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 

### Return type

[**BasicStatusResultObject**](BasicStatusResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryDocument

> DocumentResultObject queryDocument(xFrankieCustomerID, documentId, opts)

Retrieve Document Details

Query the current status and details of a given documentId. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let documentId = "documentId_example"; // String | The documentId returned previously from an earlier call to /check or /entity or /document
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.queryDocument(xFrankieCustomerID, documentId, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **documentId** | **String**| The documentId returned previously from an earlier call to /check or /entity or /document | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**DocumentResultObject**](DocumentResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryDocumentChecks

> DocumentChecksResultObject queryDocumentChecks(xFrankieCustomerID, documentId, opts)

Retrieve Document Verification Check Details. 

Get the complete list of all checks that have been performed upon a given document, including the checks that have been performed by others (in those cases you just get the id, status and date run, none of the details). 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let documentId = "documentId_example"; // String | The documentId returned previously from an earlier call to /check or /entity or /document
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56 // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
};
apiInstance.queryDocumentChecks(xFrankieCustomerID, documentId, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **documentId** | **String**| The documentId returned previously from an earlier call to /check or /entity or /document | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 

### Return type

[**DocumentChecksResultObject**](DocumentChecksResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryDocumentFull

> DocumentResultObject queryDocumentFull(xFrankieCustomerID, documentId, opts)

Retrieve Document and Scan Data

Query the current status and details of a given documentId. Also returns all document file data, not just the metadata. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let documentId = "documentId_example"; // String | The documentId returned previously from an earlier call to /check or /entity or /document
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.queryDocumentFull(xFrankieCustomerID, documentId, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **documentId** | **String**| The documentId returned previously from an earlier call to /check or /entity or /document | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**DocumentResultObject**](DocumentResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchDocument

> DocumentSearchResultObject searchDocument(xFrankieCustomerID, searchDocument, opts)

Search For a Document !! EXPERIMENTAL !!

 Search for an existing document that matches the criteria supplied  There are of course limits to what can be searched upon. For a document search to work, you must supply at a minimum:    * idType   * country   * idNumber  The service will return a list of matching documents with confidence levels.  If you are the \&quot;owner\&quot; of the document - i.e. the same CustomerID and CustomerChildID (if relevant) - then the full details of the document will be returned, except for the contents of any attached scans. If you are not the owner of the document, then just the ID and confidence level is returned. You can still use this ID to retrieve any check results (see GET /document/{documentId}/checks)  Note: At this time, we cannot perform searches on document scans. But, you can supply extraData KVPs if they&#39;re known. These will help doublecheck search results with ambiguous results. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let searchDocument = new FrankieFinancialApi.IdentityDocumentObject(); // IdentityDocumentObject | A document object with the parameters you wish to search on. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example" // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
};
apiInstance.searchDocument(xFrankieCustomerID, searchDocument, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **searchDocument** | [**IdentityDocumentObject**](IdentityDocumentObject.md)| A document object with the parameters you wish to search on.  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 

### Return type

[**DocumentSearchResultObject**](DocumentSearchResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCompareDocument

> DocumentCompareResultObject updateCompareDocument(xFrankieCustomerID, documentId, comparisonSet, opts)

Update Document and Compare to Original.

Send the attached document scans to an external service for processing and comparison, such as comparing a selfie-video against a drivers licence photo.  * NOTE: This is NOT the verification process (see /document/verify)  * NOTE: This is NOT the OCR data extraction process either (see /document/scan) 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let documentId = "documentId_example"; // String | The documentId returned previously from an earlier call to /check or /entity or /document
let comparisonSet = new FrankieFinancialApi.ComparisonSet(); // ComparisonSet | Contains the document (compareDocument) we want to compare (toDocument).  In this case, the toDocument should be left blank, and is assumed to be \"this\" document 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56 // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
};
apiInstance.updateCompareDocument(xFrankieCustomerID, documentId, comparisonSet, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **documentId** | **String**| The documentId returned previously from an earlier call to /check or /entity or /document | 
 **comparisonSet** | [**ComparisonSet**](ComparisonSet.md)| Contains the document (compareDocument) we want to compare (toDocument).  In this case, the toDocument should be left blank, and is assumed to be \&quot;this\&quot; document  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 

### Return type

[**DocumentCompareResultObject**](DocumentCompareResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDocument

> DocumentResultObject updateDocument(xFrankieCustomerID, documentId, document, opts)

Update Existing Document.

Using a previously uploaded but incomplete document, you can optionally supply updated details (such as corrections on a previous scan), along with one or more additional ID scans (e.g. additional pages). 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let documentId = "documentId_example"; // String | The documentId returned previously from an earlier call to /check or /entity or /document
let document = new FrankieFinancialApi.IdentityDocumentObject(); // IdentityDocumentObject | The document to be updated
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56, // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
  'noInvalidate': true // Boolean | Disable check result invalidation for this update request. 
};
apiInstance.updateDocument(xFrankieCustomerID, documentId, document, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **documentId** | **String**| The documentId returned previously from an earlier call to /check or /entity or /document | 
 **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)| The document to be updated | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 
 **noInvalidate** | **Boolean**| Disable check result invalidation for this update request.  | [optional] 

### Return type

[**DocumentResultObject**](DocumentResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateScanDocument

> DocumentScanResultObject updateScanDocument(xFrankieCustomerID, documentId, document, opts)

Update and OCR Scan Document

Using a previously uploaded but potentially incomplete document, you can optionally supply updated details (such as corrections on a previous scan), along with one or more additional ID scans (e.g. additional pages). Includes a follow-on action as well initiating OCR processing proceedures immediately. The service will attempt to extract relevant data from any/all uploaded images/documents and will place those in the extraData KVP block. 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let documentId = "documentId_example"; // String | The documentId returned previously from an earlier call to /check or /entity or /document
let document = new FrankieFinancialApi.IdentityDocumentObject(); // IdentityDocumentObject | The entity to be optionally updated, then processed. If updating a document, you only need to populate the fields you're actually adding/updating. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56 // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
};
apiInstance.updateScanDocument(xFrankieCustomerID, documentId, document, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **documentId** | **String**| The documentId returned previously from an earlier call to /check or /entity or /document | 
 **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)| The entity to be optionally updated, then processed. If updating a document, you only need to populate the fields you&#39;re actually adding/updating.  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 

### Return type

[**DocumentScanResultObject**](DocumentScanResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVerifyDocument

> DocumentVerifyResultObject updateVerifyDocument(xFrankieCustomerID, documentId, processDocument, opts)

Update and Verify Document.

Using a previously uploaded but potentially incomplete document, you can optionally supply updated details (such as corrections on a previous scan), along with one or more additional ID scans (e.g. additional pages). Includes a follow-on action as well initiating verification proceedures immediately.  Sends the updated document to an external service to have the detailed verified.  For example, we could send through the details of a drivers licence to be checked against a national database.  * NOTE: This is NOT the OCR data extraction process (see /document/scan) * NOTE: This is NOT the comparison process (see /document/compare) 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let documentId = "documentId_example"; // String | The documentId returned previously from an earlier call to /check or /entity or /document
let processDocument = new FrankieFinancialApi.DocumentVerify(); // DocumentVerify | The document and (possibly) its associated scans to be verified.  There is also an optional entity object (normally stripped back to it's bare minimum) that can be used to provide supporting data, such as name, address, etc. The entity object may be empty, and is not processed or stored in any way. 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56 // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
};
apiInstance.updateVerifyDocument(xFrankieCustomerID, documentId, processDocument, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **documentId** | **String**| The documentId returned previously from an earlier call to /check or /entity or /document | 
 **processDocument** | [**DocumentVerify**](DocumentVerify.md)| The document and (possibly) its associated scans to be verified.  There is also an optional entity object (normally stripped back to it&#39;s bare minimum) that can be used to provide supporting data, such as name, address, etc. The entity object may be empty, and is not processed or stored in any way.  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 

### Return type

[**DocumentVerifyResultObject**](DocumentVerifyResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## verifyDocument

> DocumentVerifyResultObject verifyDocument(xFrankieCustomerID, processDocument, opts)

Create and Verify Document.

Send the document to an external service to have the detailed verified.  For example, we could send through the details of a drivers licence to be checked against a national database.  * NOTE: This is NOT the OCR data extraction process (see /document/scan) * NOTE: This is NOT the comparison process (see /document/compare) 

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';
let defaultClient = FrankieFinancialApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new FrankieFinancialApi.DocumentApi();
let xFrankieCustomerID = "xFrankieCustomerID_example"; // String | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
let processDocument = new FrankieFinancialApi.DocumentVerify(); // DocumentVerify | The document and (possibly) its associated scans to be verified.  There is also an entity object (normally stripped back to it's bare minimum) that can be used to provide supporting data, such as name, address, etc. The entity object may be empty/ 
let opts = {
  'xFrankieCustomerChildID': "xFrankieCustomerChildID_example", // String | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
  'xFrankieBackground': 56 // Number | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
};
apiInstance.verifyDocument(xFrankieCustomerID, processDocument, opts, (error, data, response) => {
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
 **xFrankieCustomerID** | **String**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | 
 **processDocument** | [**DocumentVerify**](DocumentVerify.md)| The document and (possibly) its associated scans to be verified.  There is also an entity object (normally stripped back to it&#39;s bare minimum) that can be used to provide supporting data, such as name, address, etc. The entity object may be empty/  | 
 **xFrankieCustomerChildID** | **String**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] 
 **xFrankieBackground** | **Number**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] 

### Return type

[**DocumentVerifyResultObject**](DocumentVerifyResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

