# DefaultApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analyzeLayoutAsync**](DefaultApi.md#analyzeLayoutAsync) | **POST** /layout/analyze | Analyze Layout |
| [**analyzeReceiptAsync**](DefaultApi.md#analyzeReceiptAsync) | **POST** /prebuilt/receipt/analyze | Analyze Receipt |
| [**analyzeWithCustomModel**](DefaultApi.md#analyzeWithCustomModel) | **POST** /custom/models/{modelId}/analyze | Analyze Form |
| [**deleteCustomModel**](DefaultApi.md#deleteCustomModel) | **DELETE** /custom/models/{modelId} | Delete Custom Model |
| [**getAnalyzeFormResult**](DefaultApi.md#getAnalyzeFormResult) | **GET** /custom/models/{modelId}/analyzeResults/{resultId} | Get Analyze Form Result |
| [**getAnalyzeLayoutResult**](DefaultApi.md#getAnalyzeLayoutResult) | **GET** /layout/analyzeResults/{resultId} | Get Analyze Layout Result |
| [**getAnalyzeReceiptResult**](DefaultApi.md#getAnalyzeReceiptResult) | **GET** /prebuilt/receipt/analyzeResults/{resultId} | Get Analyze Receipt Result |
| [**getCustomModel**](DefaultApi.md#getCustomModel) | **GET** /custom/models/{modelId} | Get Custom Model |
| [**getCustomModels**](DefaultApi.md#getCustomModels) | **GET** /custom/models | List Custom Models |
| [**trainCustomModelAsync**](DefaultApi.md#trainCustomModelAsync) | **POST** /custom/models | Train Custom Model |


<a id="analyzeLayoutAsync"></a>
# **analyzeLayoutAsync**
> analyzeLayoutAsync(fileStream)

Analyze Layout

Extract text and layout information from a given document. The input document must be of one of the supported content types - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39; or &#39;image/tiff&#39;. Alternatively, use &#39;application/json&#39; type to specify the location (Uri or local path) of the document to be analyzed.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Object fileStream = null; // Object | .json, .pdf, .jpg, .png or .tiff type file stream.
    try {
      apiInstance.analyzeLayoutAsync(fileStream);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyzeLayoutAsync");
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
| **fileStream** | **Object**| .json, .pdf, .jpg, .png or .tiff type file stream. | [optional] |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/pdf, application/json, image/jpeg, image/png, image/tiff
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request is queued successfully. |  * Operation-Location - URL containing the resultId used to track the progress and obtain the result of the analyze operation. <br>  |
| **0** | Response entity accompanying non-successful responses containing additional details about the error. |  -  |

<a id="analyzeReceiptAsync"></a>
# **analyzeReceiptAsync**
> analyzeReceiptAsync(includeTextDetails, fileStream)

Analyze Receipt

Extract field text and semantic values from a given receipt document. The input document must be of one of the supported content types - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39; or &#39;image/tiff&#39;. Alternatively, use &#39;application/json&#39; type to specify the location (Uri or local path) of the document to be analyzed.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean includeTextDetails = false; // Boolean | Include text lines and element references in the result.
    Object fileStream = null; // Object | .json, .pdf, .jpg, .png or .tiff type file stream.
    try {
      apiInstance.analyzeReceiptAsync(includeTextDetails, fileStream);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyzeReceiptAsync");
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
| **includeTextDetails** | **Boolean**| Include text lines and element references in the result. | [optional] [default to false] |
| **fileStream** | **Object**| .json, .pdf, .jpg, .png or .tiff type file stream. | [optional] |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/pdf, application/json, image/jpeg, image/png, image/tiff
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request is queued successfully. |  * Operation-Location - URL containing the resultId used to track the progress and obtain the result of the analyze operation. <br>  |
| **0** | Response entity accompanying non-successful responses containing additional details about the error. |  -  |

<a id="analyzeWithCustomModel"></a>
# **analyzeWithCustomModel**
> analyzeWithCustomModel(modelId, includeTextDetails, fileStream)

Analyze Form

Extract key-value pairs, tables, and semantic values from a given document. The input document must be of one of the supported content types - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39; or &#39;image/tiff&#39;. Alternatively, use &#39;application/json&#39; type to specify the location (Uri or local path) of the document to be analyzed.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID modelId = UUID.randomUUID(); // UUID | Model identifier.
    Boolean includeTextDetails = false; // Boolean | Include text lines and element references in the result.
    Object fileStream = null; // Object | .json, .pdf, .jpg, .png or .tiff type file stream.
    try {
      apiInstance.analyzeWithCustomModel(modelId, includeTextDetails, fileStream);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#analyzeWithCustomModel");
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
| **modelId** | **UUID**| Model identifier. | |
| **includeTextDetails** | **Boolean**| Include text lines and element references in the result. | [optional] [default to false] |
| **fileStream** | **Object**| .json, .pdf, .jpg, .png or .tiff type file stream. | [optional] |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/pdf, application/json, image/jpeg, image/png, image/tiff
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Request is queued successfully. |  * Operation-Location - URL containing the resultId used to track the progress and obtain the result of the analyze operation. <br>  |
| **0** | Response entity accompanying non-successful responses containing additional details about the error. |  -  |

<a id="deleteCustomModel"></a>
# **deleteCustomModel**
> deleteCustomModel(modelId)

Delete Custom Model

Mark model for deletion. Model artifacts will be permanently removed within a predetermined period.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID modelId = UUID.randomUUID(); // UUID | Model identifier.
    try {
      apiInstance.deleteCustomModel(modelId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteCustomModel");
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
| **modelId** | **UUID**| Model identifier. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully marked model for deletion. Model artifacts will be removed within a predefined time period. |  -  |
| **0** | Response entity accompanying non-successful responses containing additional details about the error. |  -  |

<a id="getAnalyzeFormResult"></a>
# **getAnalyzeFormResult**
> AnalyzeOperationResult getAnalyzeFormResult(modelId, resultId)

Get Analyze Form Result

Obtain current status and the result of the analyze form operation.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID modelId = UUID.randomUUID(); // UUID | Model identifier.
    UUID resultId = UUID.randomUUID(); // UUID | Analyze operation result identifier.
    try {
      AnalyzeOperationResult result = apiInstance.getAnalyzeFormResult(modelId, resultId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAnalyzeFormResult");
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
| **modelId** | **UUID**| Model identifier. | |
| **resultId** | **UUID**| Analyze operation result identifier. | |

### Return type

[**AnalyzeOperationResult**](AnalyzeOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Response entity accompanying non-successful responses containing additional details about the error. |  -  |

<a id="getAnalyzeLayoutResult"></a>
# **getAnalyzeLayoutResult**
> AnalyzeOperationResult getAnalyzeLayoutResult(resultId)

Get Analyze Layout Result

Track the progress and obtain the result of the analyze layout operation

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID resultId = UUID.randomUUID(); // UUID | Analyze operation result identifier.
    try {
      AnalyzeOperationResult result = apiInstance.getAnalyzeLayoutResult(resultId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAnalyzeLayoutResult");
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
| **resultId** | **UUID**| Analyze operation result identifier. | |

### Return type

[**AnalyzeOperationResult**](AnalyzeOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Response entity accompanying non-successful responses containing additional details about the error. |  -  |

<a id="getAnalyzeReceiptResult"></a>
# **getAnalyzeReceiptResult**
> AnalyzeOperationResult getAnalyzeReceiptResult(resultId)

Get Analyze Receipt Result

Track the progress and obtain the result of the analyze receipt operation.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID resultId = UUID.randomUUID(); // UUID | Analyze operation result identifier.
    try {
      AnalyzeOperationResult result = apiInstance.getAnalyzeReceiptResult(resultId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAnalyzeReceiptResult");
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
| **resultId** | **UUID**| Analyze operation result identifier. | |

### Return type

[**AnalyzeOperationResult**](AnalyzeOperationResult.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Response entity accompanying non-successful responses containing additional details about the error. |  -  |

<a id="getCustomModel"></a>
# **getCustomModel**
> Model getCustomModel(modelId, includeKeys)

Get Custom Model

Get detailed information about a custom model.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UUID modelId = UUID.randomUUID(); // UUID | Model identifier.
    Boolean includeKeys = false; // Boolean | Include list of extracted keys in model information.
    try {
      Model result = apiInstance.getCustomModel(modelId, includeKeys);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCustomModel");
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
| **modelId** | **UUID**| Model identifier. | |
| **includeKeys** | **Boolean**| Include list of extracted keys in model information. | [optional] [default to false] |

### Return type

[**Model**](Model.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Response entity accompanying non-successful responses containing additional details about the error. |  -  |

<a id="getCustomModels"></a>
# **getCustomModels**
> Models getCustomModels(op)

List Custom Models

Get information about all custom models

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String op = "full"; // String | Specify whether to return summary or full list of models.
    try {
      Models result = apiInstance.getCustomModels(op);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCustomModels");
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
| **op** | **String**| Specify whether to return summary or full list of models. | [optional] [default to full] [enum: full, summary] |

### Return type

[**Models**](Models.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Response entity accompanying non-successful responses containing additional details about the error. |  -  |

<a id="trainCustomModelAsync"></a>
# **trainCustomModelAsync**
> trainCustomModelAsync(trainRequest)

Train Custom Model

Create and train a custom model. The request must include a source parameter that is either an externally accessible Azure storage blob container Uri (preferably a Shared Access Signature Uri) or valid path to a data folder in a locally mounted drive. When local paths are specified, they must follow the Linux/Unix path format and be an absolute path rooted to the input mount configuration setting value e.g., if &#39;{Mounts:Input}&#39; configuration setting value is &#39;/input&#39; then a valid source path would be &#39;/input/contosodataset&#39;. All data to be trained is expected to be under the source folder or sub folders under it. Models are trained using documents that are of the following content type - &#39;application/pdf&#39;, &#39;image/jpeg&#39;, &#39;image/png&#39;, &#39;image/tiff&#39;. Other type of content is ignored.

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
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    TrainRequest trainRequest = new TrainRequest(); // TrainRequest | Training request parameters.
    try {
      apiInstance.trainCustomModelAsync(trainRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#trainCustomModelAsync");
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
| **trainRequest** | [**TrainRequest**](TrainRequest.md)| Training request parameters. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Request is queued successfully. |  * Location - Location and ID of the model being trained. The status of model training is specified in the status property at the model location. <br>  |
| **0** | Response entity accompanying non-successful responses containing additional details about the error. |  -  |

