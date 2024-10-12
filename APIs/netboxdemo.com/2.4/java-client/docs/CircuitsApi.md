# CircuitsApi

All URIs are relative to *http://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**circuitsChoicesList**](CircuitsApi.md#circuitsChoicesList) | **GET** /circuits/_choices/ |  |
| [**circuitsChoicesRead**](CircuitsApi.md#circuitsChoicesRead) | **GET** /circuits/_choices/{id}/ |  |
| [**circuitsCircuitTerminationsCreate**](CircuitsApi.md#circuitsCircuitTerminationsCreate) | **POST** /circuits/circuit-terminations/ |  |
| [**circuitsCircuitTerminationsDelete**](CircuitsApi.md#circuitsCircuitTerminationsDelete) | **DELETE** /circuits/circuit-terminations/{id}/ |  |
| [**circuitsCircuitTerminationsList**](CircuitsApi.md#circuitsCircuitTerminationsList) | **GET** /circuits/circuit-terminations/ |  |
| [**circuitsCircuitTerminationsPartialUpdate**](CircuitsApi.md#circuitsCircuitTerminationsPartialUpdate) | **PATCH** /circuits/circuit-terminations/{id}/ |  |
| [**circuitsCircuitTerminationsRead**](CircuitsApi.md#circuitsCircuitTerminationsRead) | **GET** /circuits/circuit-terminations/{id}/ |  |
| [**circuitsCircuitTerminationsUpdate**](CircuitsApi.md#circuitsCircuitTerminationsUpdate) | **PUT** /circuits/circuit-terminations/{id}/ |  |
| [**circuitsCircuitTypesCreate**](CircuitsApi.md#circuitsCircuitTypesCreate) | **POST** /circuits/circuit-types/ |  |
| [**circuitsCircuitTypesDelete**](CircuitsApi.md#circuitsCircuitTypesDelete) | **DELETE** /circuits/circuit-types/{id}/ |  |
| [**circuitsCircuitTypesList**](CircuitsApi.md#circuitsCircuitTypesList) | **GET** /circuits/circuit-types/ |  |
| [**circuitsCircuitTypesPartialUpdate**](CircuitsApi.md#circuitsCircuitTypesPartialUpdate) | **PATCH** /circuits/circuit-types/{id}/ |  |
| [**circuitsCircuitTypesRead**](CircuitsApi.md#circuitsCircuitTypesRead) | **GET** /circuits/circuit-types/{id}/ |  |
| [**circuitsCircuitTypesUpdate**](CircuitsApi.md#circuitsCircuitTypesUpdate) | **PUT** /circuits/circuit-types/{id}/ |  |
| [**circuitsCircuitsCreate**](CircuitsApi.md#circuitsCircuitsCreate) | **POST** /circuits/circuits/ |  |
| [**circuitsCircuitsDelete**](CircuitsApi.md#circuitsCircuitsDelete) | **DELETE** /circuits/circuits/{id}/ |  |
| [**circuitsCircuitsList**](CircuitsApi.md#circuitsCircuitsList) | **GET** /circuits/circuits/ |  |
| [**circuitsCircuitsPartialUpdate**](CircuitsApi.md#circuitsCircuitsPartialUpdate) | **PATCH** /circuits/circuits/{id}/ |  |
| [**circuitsCircuitsRead**](CircuitsApi.md#circuitsCircuitsRead) | **GET** /circuits/circuits/{id}/ |  |
| [**circuitsCircuitsUpdate**](CircuitsApi.md#circuitsCircuitsUpdate) | **PUT** /circuits/circuits/{id}/ |  |
| [**circuitsProvidersCreate**](CircuitsApi.md#circuitsProvidersCreate) | **POST** /circuits/providers/ |  |
| [**circuitsProvidersDelete**](CircuitsApi.md#circuitsProvidersDelete) | **DELETE** /circuits/providers/{id}/ |  |
| [**circuitsProvidersGraphs**](CircuitsApi.md#circuitsProvidersGraphs) | **GET** /circuits/providers/{id}/graphs/ |  |
| [**circuitsProvidersList**](CircuitsApi.md#circuitsProvidersList) | **GET** /circuits/providers/ |  |
| [**circuitsProvidersPartialUpdate**](CircuitsApi.md#circuitsProvidersPartialUpdate) | **PATCH** /circuits/providers/{id}/ |  |
| [**circuitsProvidersRead**](CircuitsApi.md#circuitsProvidersRead) | **GET** /circuits/providers/{id}/ |  |
| [**circuitsProvidersUpdate**](CircuitsApi.md#circuitsProvidersUpdate) | **PUT** /circuits/providers/{id}/ |  |


<a id="circuitsChoicesList"></a>
# **circuitsChoicesList**
> circuitsChoicesList()





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    try {
      apiInstance.circuitsChoicesList();
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsChoicesList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsChoicesRead"></a>
# **circuitsChoicesRead**
> circuitsChoicesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.circuitsChoicesRead(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsChoicesRead");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitTerminationsCreate"></a>
# **circuitsCircuitTerminationsCreate**
> CircuitTermination circuitsCircuitTerminationsCreate(writableCircuitTermination)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    WritableCircuitTermination writableCircuitTermination = new WritableCircuitTermination(); // WritableCircuitTermination | 
    try {
      CircuitTermination result = apiInstance.circuitsCircuitTerminationsCreate(writableCircuitTermination);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTerminationsCreate");
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
| **writableCircuitTermination** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | |

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="circuitsCircuitTerminationsDelete"></a>
# **circuitsCircuitTerminationsDelete**
> circuitsCircuitTerminationsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit termination.
    try {
      apiInstance.circuitsCircuitTerminationsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTerminationsDelete");
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
| **id** | **Integer**| A unique integer value identifying this circuit termination. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="circuitsCircuitTerminationsList"></a>
# **circuitsCircuitTerminationsList**
> CircuitsCircuitTerminationsList200Response circuitsCircuitTerminationsList(termSide, portSpeed, upstreamSpeed, xconnectId, q, circuitId, siteId, site, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    String termSide = "termSide_example"; // String | 
    BigDecimal portSpeed = new BigDecimal(78); // BigDecimal | 
    BigDecimal upstreamSpeed = new BigDecimal(78); // BigDecimal | 
    String xconnectId = "xconnectId_example"; // String | 
    String q = "q_example"; // String | 
    String circuitId = "circuitId_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      CircuitsCircuitTerminationsList200Response result = apiInstance.circuitsCircuitTerminationsList(termSide, portSpeed, upstreamSpeed, xconnectId, q, circuitId, siteId, site, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTerminationsList");
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
| **termSide** | **String**|  | [optional] |
| **portSpeed** | **BigDecimal**|  | [optional] |
| **upstreamSpeed** | **BigDecimal**|  | [optional] |
| **xconnectId** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **circuitId** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**CircuitsCircuitTerminationsList200Response**](CircuitsCircuitTerminationsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitTerminationsPartialUpdate"></a>
# **circuitsCircuitTerminationsPartialUpdate**
> CircuitTermination circuitsCircuitTerminationsPartialUpdate(id, writableCircuitTermination)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit termination.
    WritableCircuitTermination writableCircuitTermination = new WritableCircuitTermination(); // WritableCircuitTermination | 
    try {
      CircuitTermination result = apiInstance.circuitsCircuitTerminationsPartialUpdate(id, writableCircuitTermination);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTerminationsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this circuit termination. | |
| **writableCircuitTermination** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | |

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitTerminationsRead"></a>
# **circuitsCircuitTerminationsRead**
> CircuitTermination circuitsCircuitTerminationsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit termination.
    try {
      CircuitTermination result = apiInstance.circuitsCircuitTerminationsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTerminationsRead");
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
| **id** | **Integer**| A unique integer value identifying this circuit termination. | |

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitTerminationsUpdate"></a>
# **circuitsCircuitTerminationsUpdate**
> CircuitTermination circuitsCircuitTerminationsUpdate(id, writableCircuitTermination)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit termination.
    WritableCircuitTermination writableCircuitTermination = new WritableCircuitTermination(); // WritableCircuitTermination | 
    try {
      CircuitTermination result = apiInstance.circuitsCircuitTerminationsUpdate(id, writableCircuitTermination);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTerminationsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this circuit termination. | |
| **writableCircuitTermination** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | |

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitTypesCreate"></a>
# **circuitsCircuitTypesCreate**
> CircuitType circuitsCircuitTypesCreate(circuitType)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    CircuitType circuitType = new CircuitType(); // CircuitType | 
    try {
      CircuitType result = apiInstance.circuitsCircuitTypesCreate(circuitType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTypesCreate");
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
| **circuitType** | [**CircuitType**](CircuitType.md)|  | |

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="circuitsCircuitTypesDelete"></a>
# **circuitsCircuitTypesDelete**
> circuitsCircuitTypesDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit type.
    try {
      apiInstance.circuitsCircuitTypesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTypesDelete");
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
| **id** | **Integer**| A unique integer value identifying this circuit type. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="circuitsCircuitTypesList"></a>
# **circuitsCircuitTypesList**
> CircuitsCircuitTypesList200Response circuitsCircuitTypesList(name, slug, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      CircuitsCircuitTypesList200Response result = apiInstance.circuitsCircuitTypesList(name, slug, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTypesList");
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
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**CircuitsCircuitTypesList200Response**](CircuitsCircuitTypesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitTypesPartialUpdate"></a>
# **circuitsCircuitTypesPartialUpdate**
> CircuitType circuitsCircuitTypesPartialUpdate(id, circuitType)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit type.
    CircuitType circuitType = new CircuitType(); // CircuitType | 
    try {
      CircuitType result = apiInstance.circuitsCircuitTypesPartialUpdate(id, circuitType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTypesPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this circuit type. | |
| **circuitType** | [**CircuitType**](CircuitType.md)|  | |

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitTypesRead"></a>
# **circuitsCircuitTypesRead**
> CircuitType circuitsCircuitTypesRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit type.
    try {
      CircuitType result = apiInstance.circuitsCircuitTypesRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTypesRead");
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
| **id** | **Integer**| A unique integer value identifying this circuit type. | |

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitTypesUpdate"></a>
# **circuitsCircuitTypesUpdate**
> CircuitType circuitsCircuitTypesUpdate(id, circuitType)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit type.
    CircuitType circuitType = new CircuitType(); // CircuitType | 
    try {
      CircuitType result = apiInstance.circuitsCircuitTypesUpdate(id, circuitType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitTypesUpdate");
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
| **id** | **Integer**| A unique integer value identifying this circuit type. | |
| **circuitType** | [**CircuitType**](CircuitType.md)|  | |

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitsCreate"></a>
# **circuitsCircuitsCreate**
> Circuit circuitsCircuitsCreate(writableCircuit)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    WritableCircuit writableCircuit = new WritableCircuit(); // WritableCircuit | 
    try {
      Circuit result = apiInstance.circuitsCircuitsCreate(writableCircuit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitsCreate");
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
| **writableCircuit** | [**WritableCircuit**](WritableCircuit.md)|  | |

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="circuitsCircuitsDelete"></a>
# **circuitsCircuitsDelete**
> circuitsCircuitsDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit.
    try {
      apiInstance.circuitsCircuitsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitsDelete");
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
| **id** | **Integer**| A unique integer value identifying this circuit. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="circuitsCircuitsList"></a>
# **circuitsCircuitsList**
> CircuitsCircuitsList200Response circuitsCircuitsList(cid, installDate, commitRate, idIn, q, providerId, provider, typeId, type, status, tenantId, tenant, siteId, site, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    String cid = "cid_example"; // String | 
    String installDate = "installDate_example"; // String | 
    BigDecimal commitRate = new BigDecimal(78); // BigDecimal | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String provider = "provider_example"; // String | 
    String typeId = "typeId_example"; // String | 
    String type = "type_example"; // String | 
    String status = "status_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      CircuitsCircuitsList200Response result = apiInstance.circuitsCircuitsList(cid, installDate, commitRate, idIn, q, providerId, provider, typeId, type, status, tenantId, tenant, siteId, site, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitsList");
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
| **cid** | **String**|  | [optional] |
| **installDate** | **String**|  | [optional] |
| **commitRate** | **BigDecimal**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **providerId** | **String**|  | [optional] |
| **provider** | **String**|  | [optional] |
| **typeId** | **String**|  | [optional] |
| **type** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**CircuitsCircuitsList200Response**](CircuitsCircuitsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitsPartialUpdate"></a>
# **circuitsCircuitsPartialUpdate**
> Circuit circuitsCircuitsPartialUpdate(id, writableCircuit)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit.
    WritableCircuit writableCircuit = new WritableCircuit(); // WritableCircuit | 
    try {
      Circuit result = apiInstance.circuitsCircuitsPartialUpdate(id, writableCircuit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitsPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this circuit. | |
| **writableCircuit** | [**WritableCircuit**](WritableCircuit.md)|  | |

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitsRead"></a>
# **circuitsCircuitsRead**
> Circuit circuitsCircuitsRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit.
    try {
      Circuit result = apiInstance.circuitsCircuitsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitsRead");
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
| **id** | **Integer**| A unique integer value identifying this circuit. | |

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsCircuitsUpdate"></a>
# **circuitsCircuitsUpdate**
> Circuit circuitsCircuitsUpdate(id, writableCircuit)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this circuit.
    WritableCircuit writableCircuit = new WritableCircuit(); // WritableCircuit | 
    try {
      Circuit result = apiInstance.circuitsCircuitsUpdate(id, writableCircuit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsCircuitsUpdate");
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
| **id** | **Integer**| A unique integer value identifying this circuit. | |
| **writableCircuit** | [**WritableCircuit**](WritableCircuit.md)|  | |

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsProvidersCreate"></a>
# **circuitsProvidersCreate**
> Provider circuitsProvidersCreate(provider)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Provider provider = new Provider(); // Provider | 
    try {
      Provider result = apiInstance.circuitsProvidersCreate(provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsProvidersCreate");
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
| **provider** | [**Provider**](Provider.md)|  | |

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

<a id="circuitsProvidersDelete"></a>
# **circuitsProvidersDelete**
> circuitsProvidersDelete(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this provider.
    try {
      apiInstance.circuitsProvidersDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsProvidersDelete");
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
| **id** | **Integer**| A unique integer value identifying this provider. | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="circuitsProvidersGraphs"></a>
# **circuitsProvidersGraphs**
> Provider circuitsProvidersGraphs(id)



A convenience method for rendering graphs for a particular provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this provider.
    try {
      Provider result = apiInstance.circuitsProvidersGraphs(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsProvidersGraphs");
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
| **id** | **Integer**| A unique integer value identifying this provider. | |

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsProvidersList"></a>
# **circuitsProvidersList**
> CircuitsProvidersList200Response circuitsProvidersList(name, slug, asn, account, idIn, q, siteId, site, tag, limit, offset)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    BigDecimal asn = new BigDecimal(78); // BigDecimal | 
    String account = "account_example"; // String | 
    String idIn = "idIn_example"; // String | Multiple values may be separated by commas.
    String q = "q_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String tag = "tag_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      CircuitsProvidersList200Response result = apiInstance.circuitsProvidersList(name, slug, asn, account, idIn, q, siteId, site, tag, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsProvidersList");
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
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **asn** | **BigDecimal**|  | [optional] |
| **account** | **String**|  | [optional] |
| **idIn** | **String**| Multiple values may be separated by commas. | [optional] |
| **q** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **limit** | **Integer**| Number of results to return per page. | [optional] |
| **offset** | **Integer**| The initial index from which to return the results. | [optional] |

### Return type

[**CircuitsProvidersList200Response**](CircuitsProvidersList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsProvidersPartialUpdate"></a>
# **circuitsProvidersPartialUpdate**
> Provider circuitsProvidersPartialUpdate(id, provider)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this provider.
    Provider provider = new Provider(); // Provider | 
    try {
      Provider result = apiInstance.circuitsProvidersPartialUpdate(id, provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsProvidersPartialUpdate");
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
| **id** | **Integer**| A unique integer value identifying this provider. | |
| **provider** | [**Provider**](Provider.md)|  | |

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsProvidersRead"></a>
# **circuitsProvidersRead**
> Provider circuitsProvidersRead(id)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this provider.
    try {
      Provider result = apiInstance.circuitsProvidersRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsProvidersRead");
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
| **id** | **Integer**| A unique integer value identifying this provider. | |

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="circuitsProvidersUpdate"></a>
# **circuitsProvidersUpdate**
> Provider circuitsProvidersUpdate(id, provider)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CircuitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    Integer id = 56; // Integer | A unique integer value identifying this provider.
    Provider provider = new Provider(); // Provider | 
    try {
      Provider result = apiInstance.circuitsProvidersUpdate(id, provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CircuitsApi#circuitsProvidersUpdate");
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
| **id** | **Integer**| A unique integer value identifying this provider. | |
| **provider** | [**Provider**](Provider.md)|  | |

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

