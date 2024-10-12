# CircuitsApi

All URIs are relative to *https://netboxdemo.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> CircuitsCircuitTerminationsList200Response circuitsCircuitTerminationsList(termSide, portSpeed, upstreamSpeed, xconnectId, q, circuitId, siteId, site, termSideN, portSpeedN, portSpeedLte, portSpeedLt, portSpeedGte, portSpeedGt, upstreamSpeedN, upstreamSpeedLte, upstreamSpeedLt, upstreamSpeedGte, upstreamSpeedGt, xconnectIdN, xconnectIdIc, xconnectIdNic, xconnectIdIew, xconnectIdNiew, xconnectIdIsw, xconnectIdNisw, xconnectIdIe, xconnectIdNie, circuitIdN, siteIdN, siteN, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    String termSide = "termSide_example"; // String | 
    String portSpeed = "portSpeed_example"; // String | 
    String upstreamSpeed = "upstreamSpeed_example"; // String | 
    String xconnectId = "xconnectId_example"; // String | 
    String q = "q_example"; // String | 
    String circuitId = "circuitId_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String termSideN = "termSideN_example"; // String | 
    String portSpeedN = "portSpeedN_example"; // String | 
    String portSpeedLte = "portSpeedLte_example"; // String | 
    String portSpeedLt = "portSpeedLt_example"; // String | 
    String portSpeedGte = "portSpeedGte_example"; // String | 
    String portSpeedGt = "portSpeedGt_example"; // String | 
    String upstreamSpeedN = "upstreamSpeedN_example"; // String | 
    String upstreamSpeedLte = "upstreamSpeedLte_example"; // String | 
    String upstreamSpeedLt = "upstreamSpeedLt_example"; // String | 
    String upstreamSpeedGte = "upstreamSpeedGte_example"; // String | 
    String upstreamSpeedGt = "upstreamSpeedGt_example"; // String | 
    String xconnectIdN = "xconnectIdN_example"; // String | 
    String xconnectIdIc = "xconnectIdIc_example"; // String | 
    String xconnectIdNic = "xconnectIdNic_example"; // String | 
    String xconnectIdIew = "xconnectIdIew_example"; // String | 
    String xconnectIdNiew = "xconnectIdNiew_example"; // String | 
    String xconnectIdIsw = "xconnectIdIsw_example"; // String | 
    String xconnectIdNisw = "xconnectIdNisw_example"; // String | 
    String xconnectIdIe = "xconnectIdIe_example"; // String | 
    String xconnectIdNie = "xconnectIdNie_example"; // String | 
    String circuitIdN = "circuitIdN_example"; // String | 
    String siteIdN = "siteIdN_example"; // String | 
    String siteN = "siteN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      CircuitsCircuitTerminationsList200Response result = apiInstance.circuitsCircuitTerminationsList(termSide, portSpeed, upstreamSpeed, xconnectId, q, circuitId, siteId, site, termSideN, portSpeedN, portSpeedLte, portSpeedLt, portSpeedGte, portSpeedGt, upstreamSpeedN, upstreamSpeedLte, upstreamSpeedLt, upstreamSpeedGte, upstreamSpeedGt, xconnectIdN, xconnectIdIc, xconnectIdNic, xconnectIdIew, xconnectIdNiew, xconnectIdIsw, xconnectIdNisw, xconnectIdIe, xconnectIdNie, circuitIdN, siteIdN, siteN, limit, offset);
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
| **portSpeed** | **String**|  | [optional] |
| **upstreamSpeed** | **String**|  | [optional] |
| **xconnectId** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **circuitId** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **termSideN** | **String**|  | [optional] |
| **portSpeedN** | **String**|  | [optional] |
| **portSpeedLte** | **String**|  | [optional] |
| **portSpeedLt** | **String**|  | [optional] |
| **portSpeedGte** | **String**|  | [optional] |
| **portSpeedGt** | **String**|  | [optional] |
| **upstreamSpeedN** | **String**|  | [optional] |
| **upstreamSpeedLte** | **String**|  | [optional] |
| **upstreamSpeedLt** | **String**|  | [optional] |
| **upstreamSpeedGte** | **String**|  | [optional] |
| **upstreamSpeedGt** | **String**|  | [optional] |
| **xconnectIdN** | **String**|  | [optional] |
| **xconnectIdIc** | **String**|  | [optional] |
| **xconnectIdNic** | **String**|  | [optional] |
| **xconnectIdIew** | **String**|  | [optional] |
| **xconnectIdNiew** | **String**|  | [optional] |
| **xconnectIdIsw** | **String**|  | [optional] |
| **xconnectIdNisw** | **String**|  | [optional] |
| **xconnectIdIe** | **String**|  | [optional] |
| **xconnectIdNie** | **String**|  | [optional] |
| **circuitIdN** | **String**|  | [optional] |
| **siteIdN** | **String**|  | [optional] |
| **siteN** | **String**|  | [optional] |
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> CircuitsCircuitTypesList200Response circuitsCircuitTypesList(id, name, slug, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String q = "q_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String slugN = "slugN_example"; // String | 
    String slugIc = "slugIc_example"; // String | 
    String slugNic = "slugNic_example"; // String | 
    String slugIew = "slugIew_example"; // String | 
    String slugNiew = "slugNiew_example"; // String | 
    String slugIsw = "slugIsw_example"; // String | 
    String slugNisw = "slugNisw_example"; // String | 
    String slugIe = "slugIe_example"; // String | 
    String slugNie = "slugNie_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      CircuitsCircuitTypesList200Response result = apiInstance.circuitsCircuitTypesList(id, name, slug, q, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, limit, offset);
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **slugN** | **String**|  | [optional] |
| **slugIc** | **String**|  | [optional] |
| **slugNic** | **String**|  | [optional] |
| **slugIew** | **String**|  | [optional] |
| **slugNiew** | **String**|  | [optional] |
| **slugIsw** | **String**|  | [optional] |
| **slugNisw** | **String**|  | [optional] |
| **slugIe** | **String**|  | [optional] |
| **slugNie** | **String**|  | [optional] |
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> CircuitsCircuitsList200Response circuitsCircuitsList(id, cid, installDate, commitRate, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, providerId, provider, typeId, type, status, siteId, site, regionId, region, tag, idN, idLte, idLt, idGte, idGt, cidN, cidIc, cidNic, cidIew, cidNiew, cidIsw, cidNisw, cidIe, cidNie, installDateN, installDateLte, installDateLt, installDateGte, installDateGt, commitRateN, commitRateLte, commitRateLt, commitRateGte, commitRateGt, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, providerIdN, providerN, typeIdN, typeN, statusN, siteIdN, siteN, regionIdN, regionN, tagN, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    String id = "id_example"; // String | 
    String cid = "cid_example"; // String | 
    String installDate = "installDate_example"; // String | 
    String commitRate = "commitRate_example"; // String | 
    String tenantGroupId = "tenantGroupId_example"; // String | 
    String tenantGroup = "tenantGroup_example"; // String | 
    String tenantId = "tenantId_example"; // String | 
    String tenant = "tenant_example"; // String | 
    String created = "created_example"; // String | 
    String createdGte = "createdGte_example"; // String | 
    String createdLte = "createdLte_example"; // String | 
    String lastUpdated = "lastUpdated_example"; // String | 
    String lastUpdatedGte = "lastUpdatedGte_example"; // String | 
    String lastUpdatedLte = "lastUpdatedLte_example"; // String | 
    String q = "q_example"; // String | 
    String providerId = "providerId_example"; // String | 
    String provider = "provider_example"; // String | 
    String typeId = "typeId_example"; // String | 
    String type = "type_example"; // String | 
    String status = "status_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String regionId = "regionId_example"; // String | 
    String region = "region_example"; // String | 
    String tag = "tag_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String cidN = "cidN_example"; // String | 
    String cidIc = "cidIc_example"; // String | 
    String cidNic = "cidNic_example"; // String | 
    String cidIew = "cidIew_example"; // String | 
    String cidNiew = "cidNiew_example"; // String | 
    String cidIsw = "cidIsw_example"; // String | 
    String cidNisw = "cidNisw_example"; // String | 
    String cidIe = "cidIe_example"; // String | 
    String cidNie = "cidNie_example"; // String | 
    String installDateN = "installDateN_example"; // String | 
    String installDateLte = "installDateLte_example"; // String | 
    String installDateLt = "installDateLt_example"; // String | 
    String installDateGte = "installDateGte_example"; // String | 
    String installDateGt = "installDateGt_example"; // String | 
    String commitRateN = "commitRateN_example"; // String | 
    String commitRateLte = "commitRateLte_example"; // String | 
    String commitRateLt = "commitRateLt_example"; // String | 
    String commitRateGte = "commitRateGte_example"; // String | 
    String commitRateGt = "commitRateGt_example"; // String | 
    String tenantGroupIdN = "tenantGroupIdN_example"; // String | 
    String tenantGroupN = "tenantGroupN_example"; // String | 
    String tenantIdN = "tenantIdN_example"; // String | 
    String tenantN = "tenantN_example"; // String | 
    String providerIdN = "providerIdN_example"; // String | 
    String providerN = "providerN_example"; // String | 
    String typeIdN = "typeIdN_example"; // String | 
    String typeN = "typeN_example"; // String | 
    String statusN = "statusN_example"; // String | 
    String siteIdN = "siteIdN_example"; // String | 
    String siteN = "siteN_example"; // String | 
    String regionIdN = "regionIdN_example"; // String | 
    String regionN = "regionN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      CircuitsCircuitsList200Response result = apiInstance.circuitsCircuitsList(id, cid, installDate, commitRate, tenantGroupId, tenantGroup, tenantId, tenant, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, providerId, provider, typeId, type, status, siteId, site, regionId, region, tag, idN, idLte, idLt, idGte, idGt, cidN, cidIc, cidNic, cidIew, cidNiew, cidIsw, cidNisw, cidIe, cidNie, installDateN, installDateLte, installDateLt, installDateGte, installDateGt, commitRateN, commitRateLte, commitRateLt, commitRateGte, commitRateGt, tenantGroupIdN, tenantGroupN, tenantIdN, tenantN, providerIdN, providerN, typeIdN, typeN, statusN, siteIdN, siteN, regionIdN, regionN, tagN, limit, offset);
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
| **id** | **String**|  | [optional] |
| **cid** | **String**|  | [optional] |
| **installDate** | **String**|  | [optional] |
| **commitRate** | **String**|  | [optional] |
| **tenantGroupId** | **String**|  | [optional] |
| **tenantGroup** | **String**|  | [optional] |
| **tenantId** | **String**|  | [optional] |
| **tenant** | **String**|  | [optional] |
| **created** | **String**|  | [optional] |
| **createdGte** | **String**|  | [optional] |
| **createdLte** | **String**|  | [optional] |
| **lastUpdated** | **String**|  | [optional] |
| **lastUpdatedGte** | **String**|  | [optional] |
| **lastUpdatedLte** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **providerId** | **String**|  | [optional] |
| **provider** | **String**|  | [optional] |
| **typeId** | **String**|  | [optional] |
| **type** | **String**|  | [optional] |
| **status** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **regionId** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **cidN** | **String**|  | [optional] |
| **cidIc** | **String**|  | [optional] |
| **cidNic** | **String**|  | [optional] |
| **cidIew** | **String**|  | [optional] |
| **cidNiew** | **String**|  | [optional] |
| **cidIsw** | **String**|  | [optional] |
| **cidNisw** | **String**|  | [optional] |
| **cidIe** | **String**|  | [optional] |
| **cidNie** | **String**|  | [optional] |
| **installDateN** | **String**|  | [optional] |
| **installDateLte** | **String**|  | [optional] |
| **installDateLt** | **String**|  | [optional] |
| **installDateGte** | **String**|  | [optional] |
| **installDateGt** | **String**|  | [optional] |
| **commitRateN** | **String**|  | [optional] |
| **commitRateLte** | **String**|  | [optional] |
| **commitRateLt** | **String**|  | [optional] |
| **commitRateGte** | **String**|  | [optional] |
| **commitRateGt** | **String**|  | [optional] |
| **tenantGroupIdN** | **String**|  | [optional] |
| **tenantGroupN** | **String**|  | [optional] |
| **tenantIdN** | **String**|  | [optional] |
| **tenantN** | **String**|  | [optional] |
| **providerIdN** | **String**|  | [optional] |
| **providerN** | **String**|  | [optional] |
| **typeIdN** | **String**|  | [optional] |
| **typeN** | **String**|  | [optional] |
| **statusN** | **String**|  | [optional] |
| **siteIdN** | **String**|  | [optional] |
| **siteN** | **String**|  | [optional] |
| **regionIdN** | **String**|  | [optional] |
| **regionN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
> CircuitsProvidersList200Response circuitsProvidersList(id, name, slug, asn, account, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, regionId, region, siteId, site, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, asnN, asnLte, asnLt, asnGte, asnGt, accountN, accountIc, accountNic, accountIew, accountNiew, accountIsw, accountNisw, accountIe, accountNie, regionIdN, regionN, siteIdN, siteN, tagN, limit, offset)



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    CircuitsApi apiInstance = new CircuitsApi(defaultClient);
    String id = "id_example"; // String | 
    String name = "name_example"; // String | 
    String slug = "slug_example"; // String | 
    String asn = "asn_example"; // String | 
    String account = "account_example"; // String | 
    String created = "created_example"; // String | 
    String createdGte = "createdGte_example"; // String | 
    String createdLte = "createdLte_example"; // String | 
    String lastUpdated = "lastUpdated_example"; // String | 
    String lastUpdatedGte = "lastUpdatedGte_example"; // String | 
    String lastUpdatedLte = "lastUpdatedLte_example"; // String | 
    String q = "q_example"; // String | 
    String regionId = "regionId_example"; // String | 
    String region = "region_example"; // String | 
    String siteId = "siteId_example"; // String | 
    String site = "site_example"; // String | 
    String tag = "tag_example"; // String | 
    String idN = "idN_example"; // String | 
    String idLte = "idLte_example"; // String | 
    String idLt = "idLt_example"; // String | 
    String idGte = "idGte_example"; // String | 
    String idGt = "idGt_example"; // String | 
    String nameN = "nameN_example"; // String | 
    String nameIc = "nameIc_example"; // String | 
    String nameNic = "nameNic_example"; // String | 
    String nameIew = "nameIew_example"; // String | 
    String nameNiew = "nameNiew_example"; // String | 
    String nameIsw = "nameIsw_example"; // String | 
    String nameNisw = "nameNisw_example"; // String | 
    String nameIe = "nameIe_example"; // String | 
    String nameNie = "nameNie_example"; // String | 
    String slugN = "slugN_example"; // String | 
    String slugIc = "slugIc_example"; // String | 
    String slugNic = "slugNic_example"; // String | 
    String slugIew = "slugIew_example"; // String | 
    String slugNiew = "slugNiew_example"; // String | 
    String slugIsw = "slugIsw_example"; // String | 
    String slugNisw = "slugNisw_example"; // String | 
    String slugIe = "slugIe_example"; // String | 
    String slugNie = "slugNie_example"; // String | 
    String asnN = "asnN_example"; // String | 
    String asnLte = "asnLte_example"; // String | 
    String asnLt = "asnLt_example"; // String | 
    String asnGte = "asnGte_example"; // String | 
    String asnGt = "asnGt_example"; // String | 
    String accountN = "accountN_example"; // String | 
    String accountIc = "accountIc_example"; // String | 
    String accountNic = "accountNic_example"; // String | 
    String accountIew = "accountIew_example"; // String | 
    String accountNiew = "accountNiew_example"; // String | 
    String accountIsw = "accountIsw_example"; // String | 
    String accountNisw = "accountNisw_example"; // String | 
    String accountIe = "accountIe_example"; // String | 
    String accountNie = "accountNie_example"; // String | 
    String regionIdN = "regionIdN_example"; // String | 
    String regionN = "regionN_example"; // String | 
    String siteIdN = "siteIdN_example"; // String | 
    String siteN = "siteN_example"; // String | 
    String tagN = "tagN_example"; // String | 
    Integer limit = 56; // Integer | Number of results to return per page.
    Integer offset = 56; // Integer | The initial index from which to return the results.
    try {
      CircuitsProvidersList200Response result = apiInstance.circuitsProvidersList(id, name, slug, asn, account, created, createdGte, createdLte, lastUpdated, lastUpdatedGte, lastUpdatedLte, q, regionId, region, siteId, site, tag, idN, idLte, idLt, idGte, idGt, nameN, nameIc, nameNic, nameIew, nameNiew, nameIsw, nameNisw, nameIe, nameNie, slugN, slugIc, slugNic, slugIew, slugNiew, slugIsw, slugNisw, slugIe, slugNie, asnN, asnLte, asnLt, asnGte, asnGt, accountN, accountIc, accountNic, accountIew, accountNiew, accountIsw, accountNisw, accountIe, accountNie, regionIdN, regionN, siteIdN, siteN, tagN, limit, offset);
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
| **id** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **slug** | **String**|  | [optional] |
| **asn** | **String**|  | [optional] |
| **account** | **String**|  | [optional] |
| **created** | **String**|  | [optional] |
| **createdGte** | **String**|  | [optional] |
| **createdLte** | **String**|  | [optional] |
| **lastUpdated** | **String**|  | [optional] |
| **lastUpdatedGte** | **String**|  | [optional] |
| **lastUpdatedLte** | **String**|  | [optional] |
| **q** | **String**|  | [optional] |
| **regionId** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |
| **siteId** | **String**|  | [optional] |
| **site** | **String**|  | [optional] |
| **tag** | **String**|  | [optional] |
| **idN** | **String**|  | [optional] |
| **idLte** | **String**|  | [optional] |
| **idLt** | **String**|  | [optional] |
| **idGte** | **String**|  | [optional] |
| **idGt** | **String**|  | [optional] |
| **nameN** | **String**|  | [optional] |
| **nameIc** | **String**|  | [optional] |
| **nameNic** | **String**|  | [optional] |
| **nameIew** | **String**|  | [optional] |
| **nameNiew** | **String**|  | [optional] |
| **nameIsw** | **String**|  | [optional] |
| **nameNisw** | **String**|  | [optional] |
| **nameIe** | **String**|  | [optional] |
| **nameNie** | **String**|  | [optional] |
| **slugN** | **String**|  | [optional] |
| **slugIc** | **String**|  | [optional] |
| **slugNic** | **String**|  | [optional] |
| **slugIew** | **String**|  | [optional] |
| **slugNiew** | **String**|  | [optional] |
| **slugIsw** | **String**|  | [optional] |
| **slugNisw** | **String**|  | [optional] |
| **slugIe** | **String**|  | [optional] |
| **slugNie** | **String**|  | [optional] |
| **asnN** | **String**|  | [optional] |
| **asnLte** | **String**|  | [optional] |
| **asnLt** | **String**|  | [optional] |
| **asnGte** | **String**|  | [optional] |
| **asnGt** | **String**|  | [optional] |
| **accountN** | **String**|  | [optional] |
| **accountIc** | **String**|  | [optional] |
| **accountNic** | **String**|  | [optional] |
| **accountIew** | **String**|  | [optional] |
| **accountNiew** | **String**|  | [optional] |
| **accountIsw** | **String**|  | [optional] |
| **accountNisw** | **String**|  | [optional] |
| **accountIe** | **String**|  | [optional] |
| **accountNie** | **String**|  | [optional] |
| **regionIdN** | **String**|  | [optional] |
| **regionN** | **String**|  | [optional] |
| **siteIdN** | **String**|  | [optional] |
| **siteN** | **String**|  | [optional] |
| **tagN** | **String**|  | [optional] |
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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



Call to super to allow for caching

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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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
    defaultClient.setBasePath("https://netboxdemo.com/api");
    
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

