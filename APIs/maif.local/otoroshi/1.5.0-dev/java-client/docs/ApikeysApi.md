# ApikeysApi

All URIs are relative to *http://otoroshi-api.oto.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allApiKeys**](ApikeysApi.md#allApiKeys) | **GET** /api/apikeys | Get all api keys |
| [**apiKey**](ApikeysApi.md#apiKey) | **GET** /api/services/{serviceId}/apikeys/{clientId} | Get an api key |
| [**apiKeyFromGroup**](ApikeysApi.md#apiKeyFromGroup) | **GET** /api/groups/{groupId}/apikeys/{clientId} | Get an api key |
| [**apiKeyFromGroupQuotas**](ApikeysApi.md#apiKeyFromGroupQuotas) | **GET** /api/groups/{groupId}/apikeys/{clientId}/quotas | Get the quota state of an api key |
| [**apiKeyGroup**](ApikeysApi.md#apiKeyGroup) | **GET** /api/services/{serviceId}/apikeys/{clientId}/group | Get the group of an api key |
| [**apiKeyQuotas**](ApikeysApi.md#apiKeyQuotas) | **GET** /api/services/{serviceId}/apikeys/{clientId}/quotas | Get the quota state of an api key |
| [**apiKeys**](ApikeysApi.md#apiKeys) | **GET** /api/services/{serviceId}/apikeys | Get all api keys for the group of a service |
| [**apiKeysFromGroup**](ApikeysApi.md#apiKeysFromGroup) | **GET** /api/groups/{groupId}/apikeys | Get all api keys for the group of a service |
| [**createApiKey**](ApikeysApi.md#createApiKey) | **POST** /api/services/{serviceId}/apikeys | Create a new api key for a service |
| [**createApiKeyFromGroup**](ApikeysApi.md#createApiKeyFromGroup) | **POST** /api/groups/{groupId}/apikeys | Create a new api key for a group |
| [**deleteApiKey**](ApikeysApi.md#deleteApiKey) | **DELETE** /api/services/{serviceId}/apikeys/{clientId} | Delete an api key |
| [**deleteApiKeyFromGroup**](ApikeysApi.md#deleteApiKeyFromGroup) | **DELETE** /api/groups/{groupId}/apikeys/{clientId} | Delete an api key |
| [**patchApiKey**](ApikeysApi.md#patchApiKey) | **PATCH** /api/services/{serviceId}/apikeys/{clientId} | Update an api key with a diff |
| [**patchApiKeyFromGroup**](ApikeysApi.md#patchApiKeyFromGroup) | **PATCH** /api/groups/{groupId}/apikeys/{clientId} | Update an api key with a diff |
| [**resetApiKeyFromGroupQuotas**](ApikeysApi.md#resetApiKeyFromGroupQuotas) | **DELETE** /api/groups/{groupId}/apikeys/{clientId}/quotas | Reset the quota state of an api key |
| [**resetApiKeyQuotas**](ApikeysApi.md#resetApiKeyQuotas) | **DELETE** /api/services/{serviceId}/apikeys/{clientId}/quotas | Reset the quota state of an api key |
| [**updateApiKey**](ApikeysApi.md#updateApiKey) | **PUT** /api/services/{serviceId}/apikeys/{clientId} | Update an api key |
| [**updateApiKeyFromGroup**](ApikeysApi.md#updateApiKeyFromGroup) | **PUT** /api/groups/{groupId}/apikeys/{clientId} | Update an api key |


<a id="allApiKeys"></a>
# **allApiKeys**
> List&lt;ApiKey&gt; allApiKeys()

Get all api keys

Get all api keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    try {
      List<ApiKey> result = apiInstance.allApiKeys();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#allApiKeys");
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

[**List&lt;ApiKey&gt;**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="apiKey"></a>
# **apiKey**
> ApiKey apiKey(serviceId, clientId)

Get an api key

Get an api key for a specified service descriptor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The api key service id
    String clientId = "clientId_example"; // String | the api key id
    try {
      ApiKey result = apiInstance.apiKey(serviceId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#apiKey");
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
| **serviceId** | **String**| The api key service id | |
| **clientId** | **String**| the api key id | |

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="apiKeyFromGroup"></a>
# **apiKeyFromGroup**
> ApiKey apiKeyFromGroup(groupId, clientId)

Get an api key

Get an api key for a specified service group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String groupId = "groupId_example"; // String | The api key group id
    String clientId = "clientId_example"; // String | the api key id
    try {
      ApiKey result = apiInstance.apiKeyFromGroup(groupId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#apiKeyFromGroup");
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
| **groupId** | **String**| The api key group id | |
| **clientId** | **String**| the api key id | |

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="apiKeyFromGroupQuotas"></a>
# **apiKeyFromGroupQuotas**
> Quotas apiKeyFromGroupQuotas(groupId, clientId)

Get the quota state of an api key

Get the quota state of an api key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String groupId = "groupId_example"; // String | The api key group id
    String clientId = "clientId_example"; // String | the api key id
    try {
      Quotas result = apiInstance.apiKeyFromGroupQuotas(groupId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#apiKeyFromGroupQuotas");
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
| **groupId** | **String**| The api key group id | |
| **clientId** | **String**| the api key id | |

### Return type

[**Quotas**](Quotas.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="apiKeyGroup"></a>
# **apiKeyGroup**
> Group apiKeyGroup(serviceId, clientId)

Get the group of an api key

Get the group of an api key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The api key service id
    String clientId = "clientId_example"; // String | the api key id
    try {
      Group result = apiInstance.apiKeyGroup(serviceId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#apiKeyGroup");
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
| **serviceId** | **String**| The api key service id | |
| **clientId** | **String**| the api key id | |

### Return type

[**Group**](Group.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="apiKeyQuotas"></a>
# **apiKeyQuotas**
> Quotas apiKeyQuotas(serviceId, clientId)

Get the quota state of an api key

Get the quota state of an api key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The api key service id
    String clientId = "clientId_example"; // String | the api key id
    try {
      Quotas result = apiInstance.apiKeyQuotas(serviceId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#apiKeyQuotas");
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
| **serviceId** | **String**| The api key service id | |
| **clientId** | **String**| the api key id | |

### Return type

[**Quotas**](Quotas.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="apiKeys"></a>
# **apiKeys**
> List&lt;ApiKey&gt; apiKeys(serviceId)

Get all api keys for the group of a service

Get all api keys for the group of a service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The api key service id
    try {
      List<ApiKey> result = apiInstance.apiKeys(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#apiKeys");
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
| **serviceId** | **String**| The api key service id | |

### Return type

[**List&lt;ApiKey&gt;**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="apiKeysFromGroup"></a>
# **apiKeysFromGroup**
> List&lt;ApiKey&gt; apiKeysFromGroup(groupId)

Get all api keys for the group of a service

Get all api keys for the group of a service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String groupId = "groupId_example"; // String | The api key group id
    try {
      List<ApiKey> result = apiInstance.apiKeysFromGroup(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#apiKeysFromGroup");
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
| **groupId** | **String**| The api key group id | |

### Return type

[**List&lt;ApiKey&gt;**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="createApiKey"></a>
# **createApiKey**
> ApiKey createApiKey(serviceId, apiKey)

Create a new api key for a service



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The api key service id
    ApiKey apiKey = new ApiKey(); // ApiKey | 
    try {
      ApiKey result = apiInstance.createApiKey(serviceId, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#createApiKey");
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
| **serviceId** | **String**| The api key service id | |
| **apiKey** | [**ApiKey**](ApiKey.md)|  | [optional] |

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="createApiKeyFromGroup"></a>
# **createApiKeyFromGroup**
> ApiKey createApiKeyFromGroup(groupId, apiKey)

Create a new api key for a group

Create a new api key for a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String groupId = "groupId_example"; // String | The api key group id
    ApiKey apiKey = new ApiKey(); // ApiKey | 
    try {
      ApiKey result = apiInstance.createApiKeyFromGroup(groupId, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#createApiKeyFromGroup");
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
| **groupId** | **String**| The api key group id | |
| **apiKey** | [**ApiKey**](ApiKey.md)|  | [optional] |

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="deleteApiKey"></a>
# **deleteApiKey**
> Deleted deleteApiKey(serviceId, clientId)

Delete an api key

Delete an api key for a specified service descriptor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The api key service id
    String clientId = "clientId_example"; // String | the api key id
    try {
      Deleted result = apiInstance.deleteApiKey(serviceId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#deleteApiKey");
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
| **serviceId** | **String**| The api key service id | |
| **clientId** | **String**| the api key id | |

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="deleteApiKeyFromGroup"></a>
# **deleteApiKeyFromGroup**
> Deleted deleteApiKeyFromGroup(groupId, clientId)

Delete an api key

Delete an api key for a specified service group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String groupId = "groupId_example"; // String | The api key group id
    String clientId = "clientId_example"; // String | the api key id
    try {
      Deleted result = apiInstance.deleteApiKeyFromGroup(groupId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#deleteApiKeyFromGroup");
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
| **groupId** | **String**| The api key group id | |
| **clientId** | **String**| the api key id | |

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="patchApiKey"></a>
# **patchApiKey**
> ApiKey patchApiKey(serviceId, clientId, patchInner)

Update an api key with a diff

Update an api key for a specified service descriptor with a diff

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The api key service id
    String clientId = "clientId_example"; // String | the api key id
    List<PatchInner> patchInner = Arrays.asList(); // List<PatchInner> | 
    try {
      ApiKey result = apiInstance.patchApiKey(serviceId, clientId, patchInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#patchApiKey");
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
| **serviceId** | **String**| The api key service id | |
| **clientId** | **String**| the api key id | |
| **patchInner** | [**List&lt;PatchInner&gt;**](PatchInner.md)|  | [optional] |

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="patchApiKeyFromGroup"></a>
# **patchApiKeyFromGroup**
> ApiKey patchApiKeyFromGroup(groupId, clientId, patchInner)

Update an api key with a diff

Update an api key for a specified service descriptor with a diff

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String groupId = "groupId_example"; // String | The api key group id
    String clientId = "clientId_example"; // String | the api key id
    List<PatchInner> patchInner = Arrays.asList(); // List<PatchInner> | 
    try {
      ApiKey result = apiInstance.patchApiKeyFromGroup(groupId, clientId, patchInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#patchApiKeyFromGroup");
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
| **groupId** | **String**| The api key group id | |
| **clientId** | **String**| the api key id | |
| **patchInner** | [**List&lt;PatchInner&gt;**](PatchInner.md)|  | [optional] |

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="resetApiKeyFromGroupQuotas"></a>
# **resetApiKeyFromGroupQuotas**
> Quotas resetApiKeyFromGroupQuotas(groupId, clientId)

Reset the quota state of an api key

Reset the quota state of an api key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String groupId = "groupId_example"; // String | The api key group id
    String clientId = "clientId_example"; // String | the api key id
    try {
      Quotas result = apiInstance.resetApiKeyFromGroupQuotas(groupId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#resetApiKeyFromGroupQuotas");
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
| **groupId** | **String**| The api key group id | |
| **clientId** | **String**| the api key id | |

### Return type

[**Quotas**](Quotas.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="resetApiKeyQuotas"></a>
# **resetApiKeyQuotas**
> Quotas resetApiKeyQuotas(serviceId, clientId)

Reset the quota state of an api key

Reset the quota state of an api key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The api key service id
    String clientId = "clientId_example"; // String | the api key id
    try {
      Quotas result = apiInstance.resetApiKeyQuotas(serviceId, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#resetApiKeyQuotas");
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
| **serviceId** | **String**| The api key service id | |
| **clientId** | **String**| the api key id | |

### Return type

[**Quotas**](Quotas.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="updateApiKey"></a>
# **updateApiKey**
> ApiKey updateApiKey(serviceId, clientId, apiKey)

Update an api key

Update an api key for a specified service descriptor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The api key service id
    String clientId = "clientId_example"; // String | the api key id
    ApiKey apiKey = new ApiKey(); // ApiKey | 
    try {
      ApiKey result = apiInstance.updateApiKey(serviceId, clientId, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#updateApiKey");
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
| **serviceId** | **String**| The api key service id | |
| **clientId** | **String**| the api key id | |
| **apiKey** | [**ApiKey**](ApiKey.md)|  | [optional] |

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

<a id="updateApiKeyFromGroup"></a>
# **updateApiKeyFromGroup**
> ApiKey updateApiKeyFromGroup(groupId, clientId, apiKey)

Update an api key

Update an api key for a specified service group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApikeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ApikeysApi apiInstance = new ApikeysApi(defaultClient);
    String groupId = "groupId_example"; // String | The api key group id
    String clientId = "clientId_example"; // String | the api key id
    ApiKey apiKey = new ApiKey(); // ApiKey | 
    try {
      ApiKey result = apiInstance.updateApiKeyFromGroup(groupId, clientId, apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApikeysApi#updateApiKeyFromGroup");
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
| **groupId** | **String**| The api key group id | |
| **clientId** | **String**| the api key id | |
| **apiKey** | [**ApiKey**](ApiKey.md)|  | [optional] |

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Bad resource format. Take another look to the swagger, or open an issue :) |  -  |
| **401** | You have to provide an Api Key. Api Key can be passed with &#39;Otoroshi-Client-Id&#39; and &#39;Otoroshi-Client-Secret&#39; headers, or use basic http authentication |  -  |
| **404** | Resource not found or does not exist |  -  |

