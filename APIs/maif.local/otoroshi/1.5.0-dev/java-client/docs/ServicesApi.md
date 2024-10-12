# ServicesApi

All URIs are relative to *http://otoroshi-api.oto.tools*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allServices**](ServicesApi.md#allServices) | **GET** /api/services | Get all services |
| [**createService**](ServicesApi.md#createService) | **POST** /api/services | Create a new service descriptor |
| [**createServiceTemplate**](ServicesApi.md#createServiceTemplate) | **POST** /api/services/{serviceId}/template | Create a service descriptor error template |
| [**deleteService**](ServicesApi.md#deleteService) | **DELETE** /api/services/{serviceId} | Delete a service descriptor |
| [**deleteServiceTemplate**](ServicesApi.md#deleteServiceTemplate) | **DELETE** /api/services/{serviceId}/template | Delete a service descriptor error template |
| [**patchService**](ServicesApi.md#patchService) | **PATCH** /api/services/{serviceId} | Update a service descriptor with a diff |
| [**service**](ServicesApi.md#service) | **GET** /api/services/{serviceId} | Get a service descriptor |
| [**serviceAddTarget**](ServicesApi.md#serviceAddTarget) | **POST** /api/services/{serviceId}/targets | Add a target to a service descriptor |
| [**serviceDeleteTarget**](ServicesApi.md#serviceDeleteTarget) | **DELETE** /api/services/{serviceId}/targets | Delete a service descriptor target |
| [**serviceGroupServices**](ServicesApi.md#serviceGroupServices) | **GET** /api/groups/{serviceGroupId}/services | Get all services descriptor for a group |
| [**serviceTargets**](ServicesApi.md#serviceTargets) | **GET** /api/services/{serviceId}/targets | Get a service descriptor targets |
| [**serviceTemplate**](ServicesApi.md#serviceTemplate) | **GET** /api/services/{serviceId}/template | Get a service descriptor error template |
| [**updateService**](ServicesApi.md#updateService) | **PUT** /api/services/{serviceId} | Update a service descriptor |
| [**updateServiceTargets**](ServicesApi.md#updateServiceTargets) | **PATCH** /api/services/{serviceId}/targets | Update a service descriptor targets |
| [**updateServiceTemplate**](ServicesApi.md#updateServiceTemplate) | **PUT** /api/services/{serviceId}/template | Update an error template to a service descriptor |


<a id="allServices"></a>
# **allServices**
> List&lt;Service&gt; allServices()

Get all services

Get all services

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    try {
      List<Service> result = apiInstance.allServices();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#allServices");
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

[**List&lt;Service&gt;**](Service.md)

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

<a id="createService"></a>
# **createService**
> Service createService(service)

Create a new service descriptor

Create a new service descriptor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    Service service = new Service(); // Service | 
    try {
      Service result = apiInstance.createService(service);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#createService");
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
| **service** | [**Service**](Service.md)|  | [optional] |

### Return type

[**Service**](Service.md)

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

<a id="createServiceTemplate"></a>
# **createServiceTemplate**
> ErrorTemplate createServiceTemplate(serviceId, errorTemplate)

Create a service descriptor error template

Update a service descriptor targets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    ErrorTemplate errorTemplate = new ErrorTemplate(); // ErrorTemplate | 
    try {
      ErrorTemplate result = apiInstance.createServiceTemplate(serviceId, errorTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#createServiceTemplate");
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
| **serviceId** | **String**| The service id | |
| **errorTemplate** | [**ErrorTemplate**](ErrorTemplate.md)|  | [optional] |

### Return type

[**ErrorTemplate**](ErrorTemplate.md)

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

<a id="deleteService"></a>
# **deleteService**
> Deleted deleteService(serviceId)

Delete a service descriptor

Delete a service descriptor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    try {
      Deleted result = apiInstance.deleteService(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#deleteService");
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
| **serviceId** | **String**| The service id | |

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

<a id="deleteServiceTemplate"></a>
# **deleteServiceTemplate**
> Deleted deleteServiceTemplate(serviceId)

Delete a service descriptor error template

Delete a service descriptor error template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    try {
      Deleted result = apiInstance.deleteServiceTemplate(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#deleteServiceTemplate");
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
| **serviceId** | **String**| The service id | |

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

<a id="patchService"></a>
# **patchService**
> Service patchService(serviceId, patchInner)

Update a service descriptor with a diff

Update a service descriptor with a diff

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    List<PatchInner> patchInner = Arrays.asList(); // List<PatchInner> | 
    try {
      Service result = apiInstance.patchService(serviceId, patchInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#patchService");
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
| **serviceId** | **String**| The service id | |
| **patchInner** | [**List&lt;PatchInner&gt;**](PatchInner.md)|  | [optional] |

### Return type

[**Service**](Service.md)

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

<a id="service"></a>
# **service**
> Service service(serviceId)

Get a service descriptor

Get a service descriptor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    try {
      Service result = apiInstance.service(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#service");
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
| **serviceId** | **String**| The service id | |

### Return type

[**Service**](Service.md)

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

<a id="serviceAddTarget"></a>
# **serviceAddTarget**
> List&lt;Target&gt; serviceAddTarget(serviceId, target)

Add a target to a service descriptor

Add a target to a service descriptor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    Target target = new Target(); // Target | 
    try {
      List<Target> result = apiInstance.serviceAddTarget(serviceId, target);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#serviceAddTarget");
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
| **serviceId** | **String**| The service id | |
| **target** | [**Target**](Target.md)|  | [optional] |

### Return type

[**List&lt;Target&gt;**](Target.md)

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

<a id="serviceDeleteTarget"></a>
# **serviceDeleteTarget**
> List&lt;Target&gt; serviceDeleteTarget(serviceId)

Delete a service descriptor target

Delete a service descriptor target

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    try {
      List<Target> result = apiInstance.serviceDeleteTarget(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#serviceDeleteTarget");
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
| **serviceId** | **String**| The service id | |

### Return type

[**List&lt;Target&gt;**](Target.md)

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

<a id="serviceGroupServices"></a>
# **serviceGroupServices**
> List&lt;ApiKey&gt; serviceGroupServices(serviceGroupId)

Get all services descriptor for a group

Get all services descriptor for a group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceGroupId = "serviceGroupId_example"; // String | The service group id
    try {
      List<ApiKey> result = apiInstance.serviceGroupServices(serviceGroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#serviceGroupServices");
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
| **serviceGroupId** | **String**| The service group id | |

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

<a id="serviceTargets"></a>
# **serviceTargets**
> List&lt;Target&gt; serviceTargets(serviceId)

Get a service descriptor targets

Get a service descriptor targets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    try {
      List<Target> result = apiInstance.serviceTargets(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#serviceTargets");
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
| **serviceId** | **String**| The service id | |

### Return type

[**List&lt;Target&gt;**](Target.md)

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

<a id="serviceTemplate"></a>
# **serviceTemplate**
> ErrorTemplate serviceTemplate(serviceId)

Get a service descriptor error template

Get a service descriptor error template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    try {
      ErrorTemplate result = apiInstance.serviceTemplate(serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#serviceTemplate");
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
| **serviceId** | **String**| The service id | |

### Return type

[**ErrorTemplate**](ErrorTemplate.md)

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

<a id="updateService"></a>
# **updateService**
> Service updateService(serviceId, service)

Update a service descriptor

Update a service descriptor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    Service service = new Service(); // Service | 
    try {
      Service result = apiInstance.updateService(serviceId, service);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#updateService");
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
| **serviceId** | **String**| The service id | |
| **service** | [**Service**](Service.md)|  | [optional] |

### Return type

[**Service**](Service.md)

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

<a id="updateServiceTargets"></a>
# **updateServiceTargets**
> List&lt;Target&gt; updateServiceTargets(serviceId, patchInner)

Update a service descriptor targets

Update a service descriptor targets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    List<PatchInner> patchInner = Arrays.asList(); // List<PatchInner> | 
    try {
      List<Target> result = apiInstance.updateServiceTargets(serviceId, patchInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#updateServiceTargets");
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
| **serviceId** | **String**| The service id | |
| **patchInner** | [**List&lt;PatchInner&gt;**](PatchInner.md)|  | [optional] |

### Return type

[**List&lt;Target&gt;**](Target.md)

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

<a id="updateServiceTemplate"></a>
# **updateServiceTemplate**
> ErrorTemplate updateServiceTemplate(serviceId, errorTemplate)

Update an error template to a service descriptor

Update an error template to a service descriptor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://otoroshi-api.oto.tools");
    
    // Configure HTTP basic authorization: otoroshi_auth
    HttpBasicAuth otoroshi_auth = (HttpBasicAuth) defaultClient.getAuthentication("otoroshi_auth");
    otoroshi_auth.setUsername("YOUR USERNAME");
    otoroshi_auth.setPassword("YOUR PASSWORD");

    ServicesApi apiInstance = new ServicesApi(defaultClient);
    String serviceId = "serviceId_example"; // String | The service id
    ErrorTemplate errorTemplate = new ErrorTemplate(); // ErrorTemplate | 
    try {
      ErrorTemplate result = apiInstance.updateServiceTemplate(serviceId, errorTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServicesApi#updateServiceTemplate");
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
| **serviceId** | **String**| The service id | |
| **errorTemplate** | [**ErrorTemplate**](ErrorTemplate.md)|  | [optional] |

### Return type

[**ErrorTemplate**](ErrorTemplate.md)

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

