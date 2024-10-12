# VerificationApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Account/v6*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postCheckAccountHolder**](VerificationApi.md#postCheckAccountHolder) | **POST** /checkAccountHolder | Trigger verification |
| [**postDeleteBankAccounts**](VerificationApi.md#postDeleteBankAccounts) | **POST** /deleteBankAccounts | Delete bank accounts |
| [**postDeleteLegalArrangements**](VerificationApi.md#postDeleteLegalArrangements) | **POST** /deleteLegalArrangements | Delete legal arrangements |
| [**postDeletePayoutMethods**](VerificationApi.md#postDeletePayoutMethods) | **POST** /deletePayoutMethods | Delete payout methods |
| [**postDeleteShareholders**](VerificationApi.md#postDeleteShareholders) | **POST** /deleteShareholders | Delete shareholders |
| [**postDeleteSignatories**](VerificationApi.md#postDeleteSignatories) | **POST** /deleteSignatories | Delete signatories |
| [**postGetUploadedDocuments**](VerificationApi.md#postGetUploadedDocuments) | **POST** /getUploadedDocuments | Get documents |
| [**postUploadDocument**](VerificationApi.md#postUploadDocument) | **POST** /uploadDocument | Upload a document |


<a id="postCheckAccountHolder"></a>
# **postCheckAccountHolder**
> GenericResponse postCheckAccountHolder(performVerificationRequest)

Trigger verification

Triggers the verification of an account holder even if the checks are not yet required for the volume that they are currently processing.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    PerformVerificationRequest performVerificationRequest = new PerformVerificationRequest(); // PerformVerificationRequest | 
    try {
      GenericResponse result = apiInstance.postCheckAccountHolder(performVerificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#postCheckAccountHolder");
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
| **performVerificationRequest** | [**PerformVerificationRequest**](PerformVerificationRequest.md)|  | [optional] |

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postDeleteBankAccounts"></a>
# **postDeleteBankAccounts**
> GenericResponse postDeleteBankAccounts(deleteBankAccountRequest)

Delete bank accounts

Deletes bank accounts associated with an account holder. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    DeleteBankAccountRequest deleteBankAccountRequest = new DeleteBankAccountRequest(); // DeleteBankAccountRequest | 
    try {
      GenericResponse result = apiInstance.postDeleteBankAccounts(deleteBankAccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#postDeleteBankAccounts");
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
| **deleteBankAccountRequest** | [**DeleteBankAccountRequest**](DeleteBankAccountRequest.md)|  | [optional] |

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postDeleteLegalArrangements"></a>
# **postDeleteLegalArrangements**
> GenericResponse postDeleteLegalArrangements(deleteLegalArrangementRequest)

Delete legal arrangements

Deletes legal arrangements and/or legal arrangement entities associated with an account holder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    DeleteLegalArrangementRequest deleteLegalArrangementRequest = new DeleteLegalArrangementRequest(); // DeleteLegalArrangementRequest | 
    try {
      GenericResponse result = apiInstance.postDeleteLegalArrangements(deleteLegalArrangementRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#postDeleteLegalArrangements");
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
| **deleteLegalArrangementRequest** | [**DeleteLegalArrangementRequest**](DeleteLegalArrangementRequest.md)|  | [optional] |

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postDeletePayoutMethods"></a>
# **postDeletePayoutMethods**
> GenericResponse postDeletePayoutMethods(deletePayoutMethodRequest)

Delete payout methods

Deletes payout methods associated with an account holder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    DeletePayoutMethodRequest deletePayoutMethodRequest = new DeletePayoutMethodRequest(); // DeletePayoutMethodRequest | 
    try {
      GenericResponse result = apiInstance.postDeletePayoutMethods(deletePayoutMethodRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#postDeletePayoutMethods");
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
| **deletePayoutMethodRequest** | [**DeletePayoutMethodRequest**](DeletePayoutMethodRequest.md)|  | [optional] |

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postDeleteShareholders"></a>
# **postDeleteShareholders**
> GenericResponse postDeleteShareholders(deleteShareholderRequest)

Delete shareholders

Deletes shareholders associated with an account holder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    DeleteShareholderRequest deleteShareholderRequest = new DeleteShareholderRequest(); // DeleteShareholderRequest | 
    try {
      GenericResponse result = apiInstance.postDeleteShareholders(deleteShareholderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#postDeleteShareholders");
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
| **deleteShareholderRequest** | [**DeleteShareholderRequest**](DeleteShareholderRequest.md)|  | [optional] |

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postDeleteSignatories"></a>
# **postDeleteSignatories**
> GenericResponse postDeleteSignatories(deleteSignatoriesRequest)

Delete signatories

Deletes signatories associated with an account holder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    DeleteSignatoriesRequest deleteSignatoriesRequest = new DeleteSignatoriesRequest(); // DeleteSignatoriesRequest | 
    try {
      GenericResponse result = apiInstance.postDeleteSignatories(deleteSignatoriesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#postDeleteSignatories");
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
| **deleteSignatoriesRequest** | [**DeleteSignatoriesRequest**](DeleteSignatoriesRequest.md)|  | [optional] |

### Return type

[**GenericResponse**](GenericResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postGetUploadedDocuments"></a>
# **postGetUploadedDocuments**
> GetUploadedDocumentsResponse postGetUploadedDocuments(getUploadedDocumentsRequest)

Get documents

Returns documents that were previously uploaded for an account holder. Adyen uses the documents during the [verification process](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    GetUploadedDocumentsRequest getUploadedDocumentsRequest = new GetUploadedDocumentsRequest(); // GetUploadedDocumentsRequest | 
    try {
      GetUploadedDocumentsResponse result = apiInstance.postGetUploadedDocuments(getUploadedDocumentsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#postGetUploadedDocuments");
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
| **getUploadedDocumentsRequest** | [**GetUploadedDocumentsRequest**](GetUploadedDocumentsRequest.md)|  | [optional] |

### Return type

[**GetUploadedDocumentsResponse**](GetUploadedDocumentsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postUploadDocument"></a>
# **postUploadDocument**
> UpdateAccountHolderResponse postUploadDocument(uploadDocumentRequest)

Upload a document

Uploads a document for an account holder. Adyen uses the documents during the [verification process](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Account/v6");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    UploadDocumentRequest uploadDocumentRequest = new UploadDocumentRequest(); // UploadDocumentRequest | 
    try {
      UpdateAccountHolderResponse result = apiInstance.postUploadDocument(uploadDocumentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#postUploadDocument");
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
| **uploadDocumentRequest** | [**UploadDocumentRequest**](UploadDocumentRequest.md)|  | [optional] |

### Return type

[**UpdateAccountHolderResponse**](UpdateAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

