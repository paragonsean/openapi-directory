# DefaultApi

All URIs are relative to *https://westcentralus.api.cognitive.microsoft.com/vision/v2.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**batchReadFile**](DefaultApi.md#batchReadFile) | **POST** /read/core/asyncBatchAnalyze |  |
| [**getReadOperationResult**](DefaultApi.md#getReadOperationResult) | **GET** /read/operations/{operationId} |  |
| [**getTextOperationResult**](DefaultApi.md#getTextOperationResult) | **GET** /textOperations/{operationId} |  |
| [**recognizeText**](DefaultApi.md#recognizeText) | **POST** /recognizeText |  |


<a id="batchReadFile"></a>
# **batchReadFile**
> batchReadFile(imageUrl)



Use this interface to get the result of a Read operation, employing the state-of-the-art Optical Character Recognition (OCR) algorithms optimized for text-heavy documents. When you use the Read File interface, the response contains a field called &#39;Operation-Location&#39;. The &#39;Operation-Location&#39; field contains the URL that you must use for your &#39;GetReadOperationResult&#39; operation to access OCR results.​

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
    try {
      apiInstance.batchReadFile(imageUrl);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchReadFile");
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
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The service has accepted the request and will start processing later. |  * Operation-Location - URL to query for status of the operation. The operation ID will expire in 48 hours.  <br>  |
| **0** | Error response. |  -  |

<a id="getReadOperationResult"></a>
# **getReadOperationResult**
> ReadOperationResult getReadOperationResult(operationId)



This interface is used for getting OCR results of Read operation. The URL to this interface should be retrieved from &#39;Operation-Location&#39; field returned from Batch Read File interface.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operationId = "e56ffa6e-1ee4-4042-bc07-993db706c95f"; // String | Id of read operation returned in the response of the 'Batch Read File' interface.
    try {
      ReadOperationResult result = apiInstance.getReadOperationResult(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReadOperationResult");
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
| **operationId** | **String**| Id of read operation returned in the response of the &#39;Batch Read File&#39; interface. | |

### Return type

[**ReadOperationResult**](ReadOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the read operation status. |  -  |
| **0** | Error response. |  -  |

<a id="getTextOperationResult"></a>
# **getTextOperationResult**
> TextOperationResult getTextOperationResult(operationId)



This interface is used for getting text operation result. The URL to this interface should be retrieved from &#39;Operation-Location&#39; field returned from Recognize Text interface.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operationId = "49a36324-fc4b-4387-aa06-090cfbf0064f"; // String | Id of the text operation returned in the response of the 'Recognize Text'
    try {
      TextOperationResult result = apiInstance.getTextOperationResult(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getTextOperationResult");
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
| **operationId** | **String**| Id of the text operation returned in the response of the &#39;Recognize Text&#39; | |

### Return type

[**TextOperationResult**](TextOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the operation status. |  -  |
| **0** | Error response. |  -  |

<a id="recognizeText"></a>
# **recognizeText**
> recognizeText(mode, imageUrl)



Recognize Text operation. When you use the Recognize Text interface, the response contains a field called &#39;Operation-Location&#39;. The &#39;Operation-Location&#39; field contains the URL that you must use for your Get Recognize Text Operation Result operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://westcentralus.api.cognitive.microsoft.com/vision/v2.1");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mode = "Handwritten"; // String | Type of text to recognize.
    ImageUrl imageUrl = new ImageUrl(); // ImageUrl | A JSON document with a URL pointing to the image that is to be analyzed.
    try {
      apiInstance.recognizeText(mode, imageUrl);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#recognizeText");
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
| **mode** | **String**| Type of text to recognize. | [enum: Handwritten, Printed] |
| **imageUrl** | [**ImageUrl**](ImageUrl.md)| A JSON document with a URL pointing to the image that is to be analyzed. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The service has accepted the request and will start processing later. It will return Accepted immediately and include an &#39;Operation-Location&#39; header. Client side should further query the operation status using the URL specified in this header. The operation ID will expire in 48 hours. |  * Operation-Location - URL to query for status of the operation. The operation ID will expire in 48 hours.  <br>  |
| **0** | Error response. |  -  |

