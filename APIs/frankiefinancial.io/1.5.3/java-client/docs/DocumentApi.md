# DocumentApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**compareDocument**](DocumentApi.md#compareDocument) | **POST** /document/new/compare | Create Document and Compare to Original. |
| [**createDocument**](DocumentApi.md#createDocument) | **POST** /document | Create New Document. |
| [**createScanDocument**](DocumentApi.md#createScanDocument) | **POST** /document/new/scan | Create and OCR Scan Document. |
| [**deleteDocument**](DocumentApi.md#deleteDocument) | **DELETE** /document/{documentId} | Delete Document. |
| [**queryDocument**](DocumentApi.md#queryDocument) | **GET** /document/{documentId} | Retrieve Document Details |
| [**queryDocumentChecks**](DocumentApi.md#queryDocumentChecks) | **GET** /document/{documentId}/checks | Retrieve Document Verification Check Details.  |
| [**queryDocumentFull**](DocumentApi.md#queryDocumentFull) | **GET** /document/{documentId}/full | Retrieve Document and Scan Data |
| [**searchDocument**](DocumentApi.md#searchDocument) | **POST** /document/search | Search For a Document !! EXPERIMENTAL !! |
| [**updateCompareDocument**](DocumentApi.md#updateCompareDocument) | **POST** /document/{documentId}/compare | Update Document and Compare to Original. |
| [**updateDocument**](DocumentApi.md#updateDocument) | **POST** /document/{documentId} | Update Existing Document. |
| [**updateScanDocument**](DocumentApi.md#updateScanDocument) | **POST** /document/{documentId}/scan | Update and OCR Scan Document |
| [**updateVerifyDocument**](DocumentApi.md#updateVerifyDocument) | **POST** /document/{documentId}/verify | Update and Verify Document. |
| [**verifyDocument**](DocumentApi.md#verifyDocument) | **POST** /document/new/verify | Create and Verify Document. |


<a id="compareDocument"></a>
# **compareDocument**
> DocumentCompareResultObject compareDocument(xFrankieCustomerID, comparisonSet, xFrankieCustomerChildID, xFrankieBackground)

Create Document and Compare to Original.

Creates a new document from the \&quot;toDocument\&quot; parameter (usual rules apply in that it must be a valid document, with no existing documentId). The compareDocument can be an existing documentId, or it too can be new as well.   * If existing (i.e. a valid DocumentId is supplied), it will be updated with any new data supplied before being sent to the comparison process.   * If new, then a new document will be created too, and the ID returned in the result.    The document scans are then sent for processing and comparison, such as comparing a selfie-video against a drivers licence photo.  * NOTE: This is NOT the verification process (see /document/verify)  * NOTE: This is NOT the OCR data extraction process either (see /document/scan) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    ComparisonSet comparisonSet = new ComparisonSet(); // ComparisonSet | Contains the document (compareDocument) we want to compare (toDocument) 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    try {
      DocumentCompareResultObject result = apiInstance.compareDocument(xFrankieCustomerID, comparisonSet, xFrankieCustomerChildID, xFrankieBackground);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#compareDocument");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **comparisonSet** | [**ComparisonSet**](ComparisonSet.md)| Contains the document (compareDocument) we want to compare (toDocument)  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |

### Return type

[**DocumentCompareResultObject**](DocumentCompareResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the results of the document comparison process.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

<a id="createDocument"></a>
# **createDocument**
> DocumentResultObject createDocument(xFrankieCustomerID, xFrankieCustomerChildID, document)

Create New Document.

Create a document object. A document object can be used to simply store data around a given identity or similar document. You can attach scans, PDFs, photos, videos, etc to the objectif you wish and these may be processed later (using the /scan function) to extract useful information. Or you can manually supply the extracted information if you choose. Document objects can be used to create an entity, based on extracted or supplied data; or it may be attached to an existing entity, either directly or through an ID check. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    IdentityDocumentObject document = new IdentityDocumentObject(); // IdentityDocumentObject | 
    try {
      DocumentResultObject result = apiInstance.createDocument(xFrankieCustomerID, xFrankieCustomerChildID, document);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#createDocument");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)|  | [optional] |

### Return type

[**DocumentResultObject**](DocumentResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the document object as it stands now. No docScan file data will be returned unless the /full variant is requested. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="createScanDocument"></a>
# **createScanDocument**
> DocumentScanResultObject createScanDocument(xFrankieCustomerID, xFrankieCustomerChildID, xFrankieBackground, document)

Create and OCR Scan Document.

Create a document object. This is then processed to extract useful information and create an entity; or it may be attached to an entity, either directly or through an ID check. The service will attempt to extract relevant data from any/all uploaded images/documents and will place those in the extraData KVP block. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    IdentityDocumentObject document = new IdentityDocumentObject(); // IdentityDocumentObject | 
    try {
      DocumentScanResultObject result = apiInstance.createScanDocument(xFrankieCustomerID, xFrankieCustomerChildID, xFrankieBackground, document);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#createScanDocument");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |
| **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)|  | [optional] |

### Return type

[**DocumentScanResultObject**](DocumentScanResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the results of the document scanning process.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="deleteDocument"></a>
# **deleteDocument**
> BasicStatusResultObject deleteDocument(xFrankieCustomerID, documentId, xFrankieCustomerChildID, xFrankieBackground)

Delete Document.

Mark this document as deleted. It will then become effectively invisible to all queries, but will be available in anonymised form for a past check. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID documentId = UUID.randomUUID(); // UUID | The documentId returned previously from an earlier call to /check or /entity or /document
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    try {
      BasicStatusResultObject result = apiInstance.deleteDocument(xFrankieCustomerID, documentId, xFrankieCustomerChildID, xFrankieBackground);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#deleteDocument");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **documentId** | **UUID**| The documentId returned previously from an earlier call to /check or /entity or /document | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |

### Return type

[**BasicStatusResultObject**](BasicStatusResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Returns a simple status to indicate that the deletion has taken place.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="queryDocument"></a>
# **queryDocument**
> DocumentResultObject queryDocument(xFrankieCustomerID, documentId, xFrankieCustomerChildID)

Retrieve Document Details

Query the current status and details of a given documentId. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID documentId = UUID.randomUUID(); // UUID | The documentId returned previously from an earlier call to /check or /entity or /document
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    try {
      DocumentResultObject result = apiInstance.queryDocument(xFrankieCustomerID, documentId, xFrankieCustomerChildID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#queryDocument");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **documentId** | **UUID**| The documentId returned previously from an earlier call to /check or /entity or /document | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |

### Return type

[**DocumentResultObject**](DocumentResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the document object as it stands now. No docScan file data will be returned unless the /full variant is requested. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="queryDocumentChecks"></a>
# **queryDocumentChecks**
> DocumentChecksResultObject queryDocumentChecks(xFrankieCustomerID, documentId, xFrankieCustomerChildID, xFrankieBackground)

Retrieve Document Verification Check Details. 

Get the complete list of all checks that have been performed upon a given document, including the checks that have been performed by others (in those cases you just get the id, status and date run, none of the details). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID documentId = UUID.randomUUID(); // UUID | The documentId returned previously from an earlier call to /check or /entity or /document
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    try {
      DocumentChecksResultObject result = apiInstance.queryDocumentChecks(xFrankieCustomerID, documentId, xFrankieCustomerChildID, xFrankieBackground);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#queryDocumentChecks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **documentId** | **UUID**| The documentId returned previously from an earlier call to /check or /entity or /document | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |

### Return type

[**DocumentChecksResultObject**](DocumentChecksResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the results of all checks carried out upon this document.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="queryDocumentFull"></a>
# **queryDocumentFull**
> DocumentResultObject queryDocumentFull(xFrankieCustomerID, documentId, xFrankieCustomerChildID)

Retrieve Document and Scan Data

Query the current status and details of a given documentId. Also returns all document file data, not just the metadata. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID documentId = UUID.randomUUID(); // UUID | The documentId returned previously from an earlier call to /check or /entity or /document
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    try {
      DocumentResultObject result = apiInstance.queryDocumentFull(xFrankieCustomerID, documentId, xFrankieCustomerChildID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#queryDocumentFull");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **documentId** | **UUID**| The documentId returned previously from an earlier call to /check or /entity or /document | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |

### Return type

[**DocumentResultObject**](DocumentResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the document object as it stands now. No docScan file data will be returned unless the /full variant is requested. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |

<a id="searchDocument"></a>
# **searchDocument**
> DocumentSearchResultObject searchDocument(xFrankieCustomerID, searchDocument, xFrankieCustomerChildID)

Search For a Document !! EXPERIMENTAL !!

 Search for an existing document that matches the criteria supplied  There are of course limits to what can be searched upon. For a document search to work, you must supply at a minimum:    * idType   * country   * idNumber  The service will return a list of matching documents with confidence levels.  If you are the \&quot;owner\&quot; of the document - i.e. the same CustomerID and CustomerChildID (if relevant) - then the full details of the document will be returned, except for the contents of any attached scans. If you are not the owner of the document, then just the ID and confidence level is returned. You can still use this ID to retrieve any check results (see GET /document/{documentId}/checks)  Note: At this time, we cannot perform searches on document scans. But, you can supply extraData KVPs if they&#39;re known. These will help doublecheck search results with ambiguous results. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    IdentityDocumentObject searchDocument = new IdentityDocumentObject(); // IdentityDocumentObject | A document object with the parameters you wish to search on. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    try {
      DocumentSearchResultObject result = apiInstance.searchDocument(xFrankieCustomerID, searchDocument, xFrankieCustomerChildID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#searchDocument");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **searchDocument** | [**IdentityDocumentObject**](IdentityDocumentObject.md)| A document object with the parameters you wish to search on.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |

### Return type

[**DocumentSearchResultObject**](DocumentSearchResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Returns a list of potentially matching documents or document references, along with a confidence level in the match.  |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

<a id="updateCompareDocument"></a>
# **updateCompareDocument**
> DocumentCompareResultObject updateCompareDocument(xFrankieCustomerID, documentId, comparisonSet, xFrankieCustomerChildID, xFrankieBackground)

Update Document and Compare to Original.

Send the attached document scans to an external service for processing and comparison, such as comparing a selfie-video against a drivers licence photo.  * NOTE: This is NOT the verification process (see /document/verify)  * NOTE: This is NOT the OCR data extraction process either (see /document/scan) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID documentId = UUID.randomUUID(); // UUID | The documentId returned previously from an earlier call to /check or /entity or /document
    ComparisonSet comparisonSet = new ComparisonSet(); // ComparisonSet | Contains the document (compareDocument) we want to compare (toDocument).  In this case, the toDocument should be left blank, and is assumed to be \"this\" document 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    try {
      DocumentCompareResultObject result = apiInstance.updateCompareDocument(xFrankieCustomerID, documentId, comparisonSet, xFrankieCustomerChildID, xFrankieBackground);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#updateCompareDocument");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **documentId** | **UUID**| The documentId returned previously from an earlier call to /check or /entity or /document | |
| **comparisonSet** | [**ComparisonSet**](ComparisonSet.md)| Contains the document (compareDocument) we want to compare (toDocument).  In this case, the toDocument should be left blank, and is assumed to be \&quot;this\&quot; document  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |

### Return type

[**DocumentCompareResultObject**](DocumentCompareResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the results of the document comparison process.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

<a id="updateDocument"></a>
# **updateDocument**
> DocumentResultObject updateDocument(xFrankieCustomerID, documentId, document, xFrankieCustomerChildID, xFrankieBackground, noInvalidate)

Update Existing Document.

Using a previously uploaded but incomplete document, you can optionally supply updated details (such as corrections on a previous scan), along with one or more additional ID scans (e.g. additional pages). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID documentId = UUID.randomUUID(); // UUID | The documentId returned previously from an earlier call to /check or /entity or /document
    IdentityDocumentObject document = new IdentityDocumentObject(); // IdentityDocumentObject | The document to be updated
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    Boolean noInvalidate = true; // Boolean | Disable check result invalidation for this update request. 
    try {
      DocumentResultObject result = apiInstance.updateDocument(xFrankieCustomerID, documentId, document, xFrankieCustomerChildID, xFrankieBackground, noInvalidate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#updateDocument");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **documentId** | **UUID**| The documentId returned previously from an earlier call to /check or /entity or /document | |
| **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)| The document to be updated | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |
| **noInvalidate** | **Boolean**| Disable check result invalidation for this update request.  | [optional] |

### Return type

[**DocumentResultObject**](DocumentResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the document object as it stands now. No docScan file data will be returned unless the /full variant is requested. |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

<a id="updateScanDocument"></a>
# **updateScanDocument**
> DocumentScanResultObject updateScanDocument(xFrankieCustomerID, documentId, document, xFrankieCustomerChildID, xFrankieBackground)

Update and OCR Scan Document

Using a previously uploaded but potentially incomplete document, you can optionally supply updated details (such as corrections on a previous scan), along with one or more additional ID scans (e.g. additional pages). Includes a follow-on action as well initiating OCR processing proceedures immediately. The service will attempt to extract relevant data from any/all uploaded images/documents and will place those in the extraData KVP block. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID documentId = UUID.randomUUID(); // UUID | The documentId returned previously from an earlier call to /check or /entity or /document
    IdentityDocumentObject document = new IdentityDocumentObject(); // IdentityDocumentObject | The entity to be optionally updated, then processed. If updating a document, you only need to populate the fields you're actually adding/updating. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    try {
      DocumentScanResultObject result = apiInstance.updateScanDocument(xFrankieCustomerID, documentId, document, xFrankieCustomerChildID, xFrankieBackground);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#updateScanDocument");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **documentId** | **UUID**| The documentId returned previously from an earlier call to /check or /entity or /document | |
| **document** | [**IdentityDocumentObject**](IdentityDocumentObject.md)| The entity to be optionally updated, then processed. If updating a document, you only need to populate the fields you&#39;re actually adding/updating.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |

### Return type

[**DocumentScanResultObject**](DocumentScanResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the results of the document scanning process.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

<a id="updateVerifyDocument"></a>
# **updateVerifyDocument**
> DocumentVerifyResultObject updateVerifyDocument(xFrankieCustomerID, documentId, processDocument, xFrankieCustomerChildID, xFrankieBackground)

Update and Verify Document.

Using a previously uploaded but potentially incomplete document, you can optionally supply updated details (such as corrections on a previous scan), along with one or more additional ID scans (e.g. additional pages). Includes a follow-on action as well initiating verification proceedures immediately.  Sends the updated document to an external service to have the detailed verified.  For example, we could send through the details of a drivers licence to be checked against a national database.  * NOTE: This is NOT the OCR data extraction process (see /document/scan) * NOTE: This is NOT the comparison process (see /document/compare) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    UUID documentId = UUID.randomUUID(); // UUID | The documentId returned previously from an earlier call to /check or /entity or /document
    DocumentVerify processDocument = new DocumentVerify(); // DocumentVerify | The document and (possibly) its associated scans to be verified.  There is also an optional entity object (normally stripped back to it's bare minimum) that can be used to provide supporting data, such as name, address, etc. The entity object may be empty, and is not processed or stored in any way. 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    try {
      DocumentVerifyResultObject result = apiInstance.updateVerifyDocument(xFrankieCustomerID, documentId, processDocument, xFrankieCustomerChildID, xFrankieBackground);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#updateVerifyDocument");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **documentId** | **UUID**| The documentId returned previously from an earlier call to /check or /entity or /document | |
| **processDocument** | [**DocumentVerify**](DocumentVerify.md)| The document and (possibly) its associated scans to be verified.  There is also an optional entity object (normally stripped back to it&#39;s bare minimum) that can be used to provide supporting data, such as name, address, etc. The entity object may be empty, and is not processed or stored in any way.  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |

### Return type

[**DocumentVerifyResultObject**](DocumentVerifyResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the results of the document verification process.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

<a id="verifyDocument"></a>
# **verifyDocument**
> DocumentVerifyResultObject verifyDocument(xFrankieCustomerID, processDocument, xFrankieCustomerChildID, xFrankieBackground)

Create and Verify Document.

Send the document to an external service to have the detailed verified.  For example, we could send through the details of a drivers licence to be checked against a national database.  * NOTE: This is NOT the OCR data extraction process (see /document/scan) * NOTE: This is NOT the comparison process (see /document/compare) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DocumentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.demo.frankiefinancial.io/compliance/v1.2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DocumentApi apiInstance = new DocumentApi(defaultClient);
    UUID xFrankieCustomerID = UUID.randomUUID(); // UUID | Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time. 
    DocumentVerify processDocument = new DocumentVerify(); // DocumentVerify | The document and (possibly) its associated scans to be verified.  There is also an entity object (normally stripped back to it's bare minimum) that can be used to provide supporting data, such as name, address, etc. The entity object may be empty/ 
    UUID xFrankieCustomerChildID = UUID.randomUUID(); // UUID | If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer's Children will not be able to see each other's data.  A Customer can see the documents/entities and checks of all their Children. 
    Integer xFrankieBackground = 56; // Integer | If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes 
    try {
      DocumentVerifyResultObject result = apiInstance.verifyDocument(xFrankieCustomerID, processDocument, xFrankieCustomerChildID, xFrankieBackground);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DocumentApi#verifyDocument");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xFrankieCustomerID** | **UUID**| Customer ID issued by Frankie Financial. This will never change. Your API key, which is mapped to this identity, will change over time.  | |
| **processDocument** | [**DocumentVerify**](DocumentVerify.md)| The document and (possibly) its associated scans to be verified.  There is also an entity object (normally stripped back to it&#39;s bare minimum) that can be used to provide supporting data, such as name, address, etc. The entity object may be empty/  | |
| **xFrankieCustomerChildID** | **UUID**| If, as a Frankie Customer, you are acting on behalf of your own customers, then you can populate this field with a Frankie-assigned ID.  Note: If using a CustomerChildID, you will also need a separate api_key for each child.  Any documents, checks, entities that are created when this field has been populated will now be tied to this CustomerID + CustomerChildID combination. Just as Customers cannot see data created by other Customers, so too a Customer&#39;s Children will not be able to see each other&#39;s data.  A Customer can see the documents/entities and checks of all their Children.  | [optional] |
| **xFrankieBackground** | **Integer**| If this header parameter is supplied and set to 1, then the request will not wait for the process to finish, and will return a 202 if there are no obvious errors in the input. The request will then run in the background and send a notification back to the customer. See out callback API for details on this.  See more details here:   https://apidocs.frankiefinancial.com/docs/asynchronous-calls-backgrounding-processes  | [optional] |

### Return type

[**DocumentVerifyResultObject**](DocumentVerifyResultObject.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was valid and able to be processed in some fashion. Results may or may not be successful, but it was completed as far as practical with no actual errors. Returns the results of the document verification process.  |  -  |
| **202** | The request was valid and can potentially be fulfilled. The Frankie service has now accepted responsibility for processing and we will either push the results to you, or send you a notification, depending on the request and your configuration. |  -  |
| **400** | Bad request. One or more request fields is either missing or incorrect. Details are in the error response. |  -  |
| **401** | The request has failed an authorisation check. This can happen for a variety of reasons, such as an invalid or expired API key, or invalid Customer/CustomerChildIDs.  * NOTE: This does not include attempts to read/write data you don&#39;t have access to - that&#39;s a 404 error (as we don&#39;t want to leak information through guessing)  |  -  |
| **404** | Cannot return response. In the case of a query, or reference to a specific entity/check/etc, it means that the requested item was not found, or you don&#39;t have access to it. Please check your query before trying again. |  -  |
| **405** | A request to POST an update to an object was not allowed due to it&#39;s state. This may indicate an already completed check, or a document that has been processed. You need to create a new document/check if you wish to update the object in question. |  -  |
| **415** | For requests with payloads, an unsupported Content-Type was specified. The Frankie Financial API only supports a content type of application/json. |  -  |
| **422** | Unprocessable request. This can be triggered in a number of ways. * An attempt to force a check or scan to run, but there is insufficient data to be able to do so. * An attempt to run a utility comparison, or similar industry/document/entity specific scan or process on an unsupported document type (e.g. electricity comparison on a passport) Details of what is required will be in the issues list of the error response.  |  -  |
| **429** | The API client is making too many concurrent requests, and some are being throttled. Throttled requests can be retried after a short delay. |  -  |
| **500** | Unexpected error. Something went wrong during the checking process. |  -  |
| **503** | All of the ID sources configured by the customer are unavailable, or there is no available document processor. |  -  |

