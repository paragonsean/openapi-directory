# WebhooksApi

All URIs are relative to *https://app.billbee.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**webHookManagementDelete**](WebhooksApi.md#webHookManagementDelete) | **DELETE** /api/v1/webhooks/{id} | Deletes an existing WebHook registration. |
| [**webHookManagementDeleteAll**](WebhooksApi.md#webHookManagementDeleteAll) | **DELETE** /api/v1/webhooks | Deletes all existing WebHook registrations. |
| [**webHookManagementGet**](WebhooksApi.md#webHookManagementGet) | **GET** /api/v1/webhooks | Gets all registered WebHooks for a given user. |
| [**webHookManagementGetFilters**](WebhooksApi.md#webHookManagementGetFilters) | **GET** /api/v1/webhooks/filters | Returns a list of all known filters you can use to register webhooks |
| [**webHookManagementLookup**](WebhooksApi.md#webHookManagementLookup) | **GET** /api/v1/webhooks/{id} | Looks up a registered WebHook with the given {id} for a given user. |
| [**webHookManagementPost**](WebhooksApi.md#webHookManagementPost) | **POST** /api/v1/webhooks | Registers a new WebHook for a given user. |
| [**webHookManagementPut**](WebhooksApi.md#webHookManagementPut) | **PUT** /api/v1/webhooks/{id} | Updates an existing WebHook registration. |


<a id="webHookManagementDelete"></a>
# **webHookManagementDelete**
> Object webHookManagementDelete(id)

Deletes an existing WebHook registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String id = "id_example"; // String | The WebHook ID.
    try {
      Object result = apiInstance.webHookManagementDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webHookManagementDelete");
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
| **id** | **String**| The WebHook ID. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webHookManagementDeleteAll"></a>
# **webHookManagementDeleteAll**
> Object webHookManagementDeleteAll()

Deletes all existing WebHook registrations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    try {
      Object result = apiInstance.webHookManagementDeleteAll();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webHookManagementDeleteAll");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webHookManagementGet"></a>
# **webHookManagementGet**
> List&lt;RechnungsdruckWebAppControllersApiWebHookApiModel&gt; webHookManagementGet()

Gets all registered WebHooks for a given user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    try {
      List<RechnungsdruckWebAppControllersApiWebHookApiModel> result = apiInstance.webHookManagementGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webHookManagementGet");
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

[**List&lt;RechnungsdruckWebAppControllersApiWebHookApiModel&gt;**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webHookManagementGetFilters"></a>
# **webHookManagementGetFilters**
> Object webHookManagementGetFilters()

Returns a list of all known filters you can use to register webhooks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    try {
      Object result = apiInstance.webHookManagementGetFilters();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webHookManagementGetFilters");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webHookManagementLookup"></a>
# **webHookManagementLookup**
> RechnungsdruckWebAppControllersApiWebHookApiModel webHookManagementLookup(id)

Looks up a registered WebHook with the given {id} for a given user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      RechnungsdruckWebAppControllersApiWebHookApiModel result = apiInstance.webHookManagementLookup(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webHookManagementLookup");
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

[**RechnungsdruckWebAppControllersApiWebHookApiModel**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webHookManagementPost"></a>
# **webHookManagementPost**
> RechnungsdruckWebAppControllersApiWebHookApiModel webHookManagementPost(rechnungsdruckWebAppControllersApiWebHookApiModel)

Registers a new WebHook for a given user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    RechnungsdruckWebAppControllersApiWebHookApiModel rechnungsdruckWebAppControllersApiWebHookApiModel = new RechnungsdruckWebAppControllersApiWebHookApiModel(); // RechnungsdruckWebAppControllersApiWebHookApiModel | The webhook to create. Attach ?noecho to the uri to prevent echo test.
    try {
      RechnungsdruckWebAppControllersApiWebHookApiModel result = apiInstance.webHookManagementPost(rechnungsdruckWebAppControllersApiWebHookApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webHookManagementPost");
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
| **rechnungsdruckWebAppControllersApiWebHookApiModel** | [**RechnungsdruckWebAppControllersApiWebHookApiModel**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)| The webhook to create. Attach ?noecho to the uri to prevent echo test. | |

### Return type

[**RechnungsdruckWebAppControllersApiWebHookApiModel**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="webHookManagementPut"></a>
# **webHookManagementPut**
> RechnungsdruckWebAppControllersApiWebHookApiModel webHookManagementPut(id, rechnungsdruckWebAppControllersApiWebHookApiModel)

Updates an existing WebHook registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.billbee.io");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String id = "id_example"; // String | The WebHook ID.
    RechnungsdruckWebAppControllersApiWebHookApiModel rechnungsdruckWebAppControllersApiWebHookApiModel = new RechnungsdruckWebAppControllersApiWebHookApiModel(); // RechnungsdruckWebAppControllersApiWebHookApiModel | The new webhook to use.
    try {
      RechnungsdruckWebAppControllersApiWebHookApiModel result = apiInstance.webHookManagementPut(id, rechnungsdruckWebAppControllersApiWebHookApiModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webHookManagementPut");
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
| **id** | **String**| The WebHook ID. | |
| **rechnungsdruckWebAppControllersApiWebHookApiModel** | [**RechnungsdruckWebAppControllersApiWebHookApiModel**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)| The new webhook to use. | |

### Return type

[**RechnungsdruckWebAppControllersApiWebHookApiModel**](RechnungsdruckWebAppControllersApiWebHookApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

