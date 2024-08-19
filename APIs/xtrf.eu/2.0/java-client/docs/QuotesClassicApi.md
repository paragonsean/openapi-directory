# QuotesClassicApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createLanguageCombination1**](QuotesClassicApi.md#createLanguageCombination1) | **POST** /quotes/{quoteId}/languageCombinations | Creates a new language combination for a given quote without creating a task. |
| [**createPayable1**](QuotesClassicApi.md#createPayable1) | **POST** /quotes/{quoteId}/finance/payables | Adds a payable. |
| [**createReceivable1**](QuotesClassicApi.md#createReceivable1) | **POST** /quotes/{quoteId}/finance/receivables | Adds a receivable. |
| [**createTask1**](QuotesClassicApi.md#createTask1) | **POST** /quotes/{quoteId}/tasks | Creates a new task for a given quote. |
| [**delete13**](QuotesClassicApi.md#delete13) | **DELETE** /quotes/{quoteId} | Removes a quote. |
| [**deletePayable1**](QuotesClassicApi.md#deletePayable1) | **DELETE** /quotes/{quoteId}/finance/payables/{payableId} | Deletes a payable. |
| [**deleteReceivable1**](QuotesClassicApi.md#deleteReceivable1) | **DELETE** /quotes/{quoteId}/finance/receivables/{receivableId} | Deletes a receivable. |
| [**getAllIds7**](QuotesClassicApi.md#getAllIds7) | **GET** /quotes/ids | Returns quotes&#39; internal identifiers. |
| [**getById8**](QuotesClassicApi.md#getById8) | **GET** /quotes/{quoteId} | Returns quote details. |
| [**getCustomFields6**](QuotesClassicApi.md#getCustomFields6) | **GET** /quotes/{quoteId}/customFields | Returns custom fields of a given quote. |
| [**getDates2**](QuotesClassicApi.md#getDates2) | **GET** /quotes/{quoteId}/dates | Returns dates of a given quote. |
| [**getFinance1**](QuotesClassicApi.md#getFinance1) | **GET** /quotes/{quoteId}/finance | Returns finance of a given quote. |
| [**getInstructions1**](QuotesClassicApi.md#getInstructions1) | **GET** /quotes/{quoteId}/instructions | Returns instructions of a given quote. |
| [**send1**](QuotesClassicApi.md#send1) | **POST** /quotes/{quoteId}/confirmation/send | Sends a quote for customer confirmation. |
| [**start**](QuotesClassicApi.md#start) | **POST** /quotes/{quoteId}/start | Starts a quote. |
| [**updateCustomFields4**](QuotesClassicApi.md#updateCustomFields4) | **PUT** /quotes/{quoteId}/customFields | Updates custom fields of a given quote. |
| [**updateInstructions2**](QuotesClassicApi.md#updateInstructions2) | **PUT** /quotes/{quoteId}/instructions | Updates instructions of a given quote. |
| [**updatePayable1**](QuotesClassicApi.md#updatePayable1) | **PUT** /quotes/{quoteId}/finance/payables/{payableId} | Updates a payable. |
| [**updateReceivable1**](QuotesClassicApi.md#updateReceivable1) | **PUT** /quotes/{quoteId}/finance/receivables/{receivableId} | Updates a receivable. |


<a id="createLanguageCombination1"></a>
# **createLanguageCombination1**
> CommonLanguageCombinationDTO createLanguageCombination1(quoteId, commonLanguageCombinationDTO)

Creates a new language combination for a given quote without creating a task.

Creates a new language combination for a given quote without creating a task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    CommonLanguageCombinationDTO commonLanguageCombinationDTO = new CommonLanguageCombinationDTO(); // CommonLanguageCombinationDTO | Created a new language combination for a given quote without creating a task.
    try {
      CommonLanguageCombinationDTO result = apiInstance.createLanguageCombination1(quoteId, commonLanguageCombinationDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#createLanguageCombination1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **commonLanguageCombinationDTO** | [**CommonLanguageCombinationDTO**](CommonLanguageCombinationDTO.md)| Created a new language combination for a given quote without creating a task. | |

### Return type

[**CommonLanguageCombinationDTO**](CommonLanguageCombinationDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="createPayable1"></a>
# **createPayable1**
> PayableDTO createPayable1(quoteId, payableCreateDTO)

Adds a payable.

Adds a payable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    PayableCreateDTO payableCreateDTO = new PayableCreateDTO(); // PayableCreateDTO | Adds a payable.
    try {
      PayableDTO result = apiInstance.createPayable1(quoteId, payableCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#createPayable1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **payableCreateDTO** | [**PayableCreateDTO**](PayableCreateDTO.md)| Adds a payable. | |

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="createReceivable1"></a>
# **createReceivable1**
> ReceivableDTO createReceivable1(quoteId, receivableCreateDTO)

Adds a receivable.

Adds a receivable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    ReceivableCreateDTO receivableCreateDTO = new ReceivableCreateDTO(); // ReceivableCreateDTO | Adds a receivable.
    try {
      ReceivableDTO result = apiInstance.createReceivable1(quoteId, receivableCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#createReceivable1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **receivableCreateDTO** | [**ReceivableCreateDTO**](ReceivableCreateDTO.md)| Adds a receivable. | |

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="createTask1"></a>
# **createTask1**
> TaskDTO createTask1(quoteId, taskDTO)

Creates a new task for a given quote.

Creates a new task for a given quote. Required fields are presented in the example.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    TaskDTO taskDTO = new TaskDTO(); // TaskDTO | Updated custom fields of a given quote.
    try {
      TaskDTO result = apiInstance.createTask1(quoteId, taskDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#createTask1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **taskDTO** | [**TaskDTO**](TaskDTO.md)| Updated custom fields of a given quote. | |

### Return type

[**TaskDTO**](TaskDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="delete13"></a>
# **delete13**
> delete13(quoteId)

Removes a quote.

Removes a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      apiInstance.delete13(quoteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#delete13");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="deletePayable1"></a>
# **deletePayable1**
> deletePayable1(quoteId, payableId)

Deletes a payable.

Deletes a payable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quoteId's internal identifier
    Long payableId = 56L; // Long | payable's internal identifier
    try {
      apiInstance.deletePayable1(quoteId, payableId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#deletePayable1");
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
| **quoteId** | **String**| quoteId&#39;s internal identifier | |
| **payableId** | **Long**| payable&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="deleteReceivable1"></a>
# **deleteReceivable1**
> deleteReceivable1(quoteId, receivableId)

Deletes a receivable.

Deletes a receivable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quoteId's internal identifier
    Long receivableId = 56L; // Long | receivable's internal identifier
    try {
      apiInstance.deleteReceivable1(quoteId, receivableId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#deleteReceivable1");
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
| **quoteId** | **String**| quoteId&#39;s internal identifier | |
| **receivableId** | **Long**| receivable&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="getAllIds7"></a>
# **getAllIds7**
> List&lt;Integer&gt; getAllIds7(updatedSince)

Returns quotes&#39; internal identifiers.

Returns quotes&#39; internal identifiers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    Long updatedSince = 56L; // Long | only quotes modified since this timestamp
    try {
      List<Integer> result = apiInstance.getAllIds7(updatedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#getAllIds7");
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
| **updatedSince** | **Long**| only quotes modified since this timestamp | [optional] |

### Return type

**List&lt;Integer&gt;**

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getById8"></a>
# **getById8**
> QuoteDTOv1 getById8(quoteId, embed)

Returns quote details.

Returns quote details. If the specified quote ID refers to Smart Quote, 400 Bad Request is returned instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    String embed = "embed_example"; // String | list of adittional fields which should be embedded in the response (ie. tasks)
    try {
      QuoteDTOv1 result = apiInstance.getById8(quoteId, embed);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#getById8");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **embed** | **String**| list of adittional fields which should be embedded in the response (ie. tasks) | [optional] |

### Return type

[**QuoteDTOv1**](QuoteDTOv1.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getCustomFields6"></a>
# **getCustomFields6**
> List&lt;CustomFieldDTO&gt; getCustomFields6(quoteId)

Returns custom fields of a given quote.

Returns custom fields of a given quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      List<CustomFieldDTO> result = apiInstance.getCustomFields6(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#getCustomFields6");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

[**List&lt;CustomFieldDTO&gt;**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getDates2"></a>
# **getDates2**
> QuoteDatesDTO getDates2(quoteId)

Returns dates of a given quote.

Returns dates of a given quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      QuoteDatesDTO result = apiInstance.getDates2(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#getDates2");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

[**QuoteDatesDTO**](QuoteDatesDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getFinance1"></a>
# **getFinance1**
> FinanceDTO getFinance1(quoteId)

Returns finance of a given quote.

Returns finance of a given quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      FinanceDTO result = apiInstance.getFinance1(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#getFinance1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

[**FinanceDTO**](FinanceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getInstructions1"></a>
# **getInstructions1**
> InstructionsDTO getInstructions1(quoteId)

Returns instructions of a given quote.

Returns instructions of a given quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      InstructionsDTO result = apiInstance.getInstructions1(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#getInstructions1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

[**InstructionsDTO**](InstructionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="send1"></a>
# **send1**
> send1(quoteId)

Sends a quote for customer confirmation.

Sends a quote for customer confirmation. Quote status is changed to SENT and a document is sent to the customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      apiInstance.send1(quoteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#send1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="start"></a>
# **start**
> start(quoteId)

Starts a quote.

Starts a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      apiInstance.start(quoteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#start");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateCustomFields4"></a>
# **updateCustomFields4**
> List&lt;CustomFieldDTO&gt; updateCustomFields4(quoteId, customFieldDTO)

Updates custom fields of a given quote.

Updates custom fields of a given quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    List<CustomFieldDTO> customFieldDTO = new CustomFieldDTO(); // List<CustomFieldDTO> | Updated custom fields of a given quote.
    try {
      List<CustomFieldDTO> result = apiInstance.updateCustomFields4(quoteId, customFieldDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#updateCustomFields4");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **customFieldDTO** | [**List&lt;CustomFieldDTO&gt;**](CustomFieldDTO.md)| Updated custom fields of a given quote. | |

### Return type

[**List&lt;CustomFieldDTO&gt;**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateInstructions2"></a>
# **updateInstructions2**
> InstructionsDTO updateInstructions2(quoteId, instructionsDTO)

Updates instructions of a given quote.

Updates instructions of a given quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    InstructionsDTO instructionsDTO = new InstructionsDTO(); // InstructionsDTO | Updated instructions of a given project.
    try {
      InstructionsDTO result = apiInstance.updateInstructions2(quoteId, instructionsDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#updateInstructions2");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **instructionsDTO** | [**InstructionsDTO**](InstructionsDTO.md)| Updated instructions of a given project. | |

### Return type

[**InstructionsDTO**](InstructionsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updatePayable1"></a>
# **updatePayable1**
> PayableDTO updatePayable1(quoteId, payableId, payableDTO)

Updates a payable.

Updates a payable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    Long payableId = 56L; // Long | payable's internal identifier
    PayableDTO payableDTO = new PayableDTO(); // PayableDTO | Updates a payable.
    try {
      PayableDTO result = apiInstance.updatePayable1(quoteId, payableId, payableDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#updatePayable1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **payableId** | **Long**| payable&#39;s internal identifier | |
| **payableDTO** | [**PayableDTO**](PayableDTO.md)| Updates a payable. | |

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateReceivable1"></a>
# **updateReceivable1**
> ReceivableDTO updateReceivable1(quoteId, receivableId, receivableDTO)

Updates a receivable.

Updates a receivable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesClassicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesClassicApi apiInstance = new QuotesClassicApi(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    Long receivableId = 56L; // Long | receivable's internal identifier
    ReceivableDTO receivableDTO = new ReceivableDTO(); // ReceivableDTO | Updates a receivable.
    try {
      ReceivableDTO result = apiInstance.updateReceivable1(quoteId, receivableId, receivableDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesClassicApi#updateReceivable1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **receivableId** | **Long**| receivable&#39;s internal identifier | |
| **receivableDTO** | [**ReceivableDTO**](ReceivableDTO.md)| Updates a receivable. | |

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

