# DictionariesApi

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getActive**](DictionariesApi.md#getActive) | **GET** /dictionaries/active | Returns active dictionary entities for all types. |
| [**getActiveByType**](DictionariesApi.md#getActiveByType) | **GET** /dictionaries/{type}/active | Returns active values from a given dictionary. |
| [**getAll1**](DictionariesApi.md#getAll1) | **GET** /dictionaries/all | Returns dictionary entities for all types. Both active and not active ones. |
| [**getAll3**](DictionariesApi.md#getAll3) | **GET** /services/all | Returns services list |
| [**getAllActive**](DictionariesApi.md#getAllActive) | **GET** /services/active | Returns active services list |
| [**getAllByType**](DictionariesApi.md#getAllByType) | **GET** /dictionaries/{type}/all | Returns all values (both active and not active) from a given dictionary. |
| [**getByTypeAndId**](DictionariesApi.md#getByTypeAndId) | **GET** /dictionaries/{type}/{id} | Returns specific value from a given dictionary. |


<a id="getActive"></a>
# **getActive**
> ManyValuesPerTypeDTO getActive()

Returns active dictionary entities for all types.

Returns active dictionary entities for all types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DictionariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    DictionariesApi apiInstance = new DictionariesApi(defaultClient);
    try {
      ManyValuesPerTypeDTO result = apiInstance.getActive();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DictionariesApi#getActive");
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

[**ManyValuesPerTypeDTO**](ManyValuesPerTypeDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getActiveByType"></a>
# **getActiveByType**
> DictionaryEntity getActiveByType(type, nameEquals)

Returns active values from a given dictionary.

Returns active values from a given dictionary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DictionariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    DictionariesApi apiInstance = new DictionariesApi(defaultClient);
    String type = "type_example"; // String | dictionary type
    String nameEquals = "nameEquals_example"; // String | exact name of entity
    try {
      DictionaryEntity result = apiInstance.getActiveByType(type, nameEquals);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DictionariesApi#getActiveByType");
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
| **type** | **String**| dictionary type | |
| **nameEquals** | **String**| exact name of entity | [optional] |

### Return type

[**DictionaryEntity**](DictionaryEntity.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getAll1"></a>
# **getAll1**
> ManyValuesPerTypeDTO getAll1()

Returns dictionary entities for all types. Both active and not active ones.

&lt;div&gt;   &lt;p&gt;     XTRF holds many user-defined dictionaries (ie. countries).     Each dictionary contains a set of values (ie. Poland or Germany).     A default value may be defined for a dictionary.   &lt;/p&gt;   &lt;p&gt;     Dictionary values are identified using internal identifier which is constant and unique among other values from the same dictionary.     Please note that name used in dictionary values is presented in the locale of the current identity.     The same dictionary value can have different names, ie. \&quot;Poland\&quot; for one user, \&quot;Polska\&quot; for another one.   &lt;/p&gt;   &lt;p&gt;     Possible dictionary types with short explanation:     &lt;ul&gt;       &lt;li&gt;calculationUnit - predefined values of how to calculate the volume of work into the price&lt;/li&gt;       &lt;li&gt;category - labels to organize data on the platform&lt;/li&gt;       &lt;li&gt;country - list of countries used on the platform&lt;/li&gt;       &lt;li&gt;currency - currencies used in financial operations in the system&lt;/li&gt;       &lt;li&gt;industry - industry sectors which clients specialize in&lt;/li&gt;       &lt;li&gt;jobType - services offered by a company used in customized workflows&lt;/li&gt;       &lt;li&gt;language - list of languages and its values used on the platform&lt;/li&gt;       &lt;li&gt;leadSource - lead/recruitment places where new clients and vendors may be found&lt;/li&gt;       &lt;li&gt;personDepartment - departments in which contact person may be assigned to&lt;/li&gt;       &lt;li&gt;personPosition - positions in which user may be associated with&lt;/li&gt;       &lt;li&gt;province - states and provinces used in various documents on the platform&lt;/li&gt;       &lt;li&gt;specialization - list of specific qualifications required to perform a specific job in the task, for ex. medical, military&lt;/li&gt;     &lt;/ul&gt;   &lt;/p&gt; &lt;/div&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DictionariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    DictionariesApi apiInstance = new DictionariesApi(defaultClient);
    try {
      ManyValuesPerTypeDTO result = apiInstance.getAll1();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DictionariesApi#getAll1");
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

[**ManyValuesPerTypeDTO**](ManyValuesPerTypeDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getAll3"></a>
# **getAll3**
> ServiceDTO getAll3(nameEquals)

Returns services list

Returns workflows list. Both active and not active ones.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DictionariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    DictionariesApi apiInstance = new DictionariesApi(defaultClient);
    String nameEquals = "nameEquals_example"; // String | exact name of entity
    try {
      ServiceDTO result = apiInstance.getAll3(nameEquals);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DictionariesApi#getAll3");
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
| **nameEquals** | **String**| exact name of entity | [optional] |

### Return type

[**ServiceDTO**](ServiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getAllActive"></a>
# **getAllActive**
> ServiceDTO getAllActive(nameEquals)

Returns active services list

Returns active workflows list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DictionariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    DictionariesApi apiInstance = new DictionariesApi(defaultClient);
    String nameEquals = "nameEquals_example"; // String | exact name of entity
    try {
      ServiceDTO result = apiInstance.getAllActive(nameEquals);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DictionariesApi#getAllActive");
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
| **nameEquals** | **String**| exact name of entity | [optional] |

### Return type

[**ServiceDTO**](ServiceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getAllByType"></a>
# **getAllByType**
> DictionaryEntity getAllByType(type, nameEquals)

Returns all values (both active and not active) from a given dictionary.

Returns all values (both active and not active) from a given dictionary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DictionariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    DictionariesApi apiInstance = new DictionariesApi(defaultClient);
    String type = "type_example"; // String | dictionary type
    String nameEquals = "nameEquals_example"; // String | exact name of entity
    try {
      DictionaryEntity result = apiInstance.getAllByType(type, nameEquals);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DictionariesApi#getAllByType");
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
| **type** | **String**| dictionary type | |
| **nameEquals** | **String**| exact name of entity | [optional] |

### Return type

[**DictionaryEntity**](DictionaryEntity.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getByTypeAndId"></a>
# **getByTypeAndId**
> DictionaryEntity getByTypeAndId(type, id)

Returns specific value from a given dictionary.

Returns specific value from a given dictionary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DictionariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    DictionariesApi apiInstance = new DictionariesApi(defaultClient);
    String type = "type_example"; // String | dictionary type
    Long id = 56L; // Long | dictionary value identifier
    try {
      DictionaryEntity result = apiInstance.getByTypeAndId(type, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DictionariesApi#getByTypeAndId");
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
| **type** | **String**| dictionary type | |
| **id** | **Long**| dictionary value identifier | |

### Return type

[**DictionaryEntity**](DictionaryEntity.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.xtrf-v1+json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

