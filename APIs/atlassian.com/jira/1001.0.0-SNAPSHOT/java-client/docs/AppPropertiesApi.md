# AppPropertiesApi

All URIs are relative to *https://your-domain.atlassian.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addonPropertiesResourceDeleteAddonPropertyDelete**](AppPropertiesApi.md#addonPropertiesResourceDeleteAddonPropertyDelete) | **DELETE** /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey} | Delete app property |
| [**addonPropertiesResourceGetAddonPropertiesGet**](AppPropertiesApi.md#addonPropertiesResourceGetAddonPropertiesGet) | **GET** /rest/atlassian-connect/1/addons/{addonKey}/properties | Get app properties |
| [**addonPropertiesResourceGetAddonPropertyGet**](AppPropertiesApi.md#addonPropertiesResourceGetAddonPropertyGet) | **GET** /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey} | Get app property |
| [**addonPropertiesResourcePutAddonPropertyPut**](AppPropertiesApi.md#addonPropertiesResourcePutAddonPropertyPut) | **PUT** /rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey} | Set app property |


<a id="addonPropertiesResourceDeleteAddonPropertyDelete"></a>
# **addonPropertiesResourceDeleteAddonPropertyDelete**
> addonPropertiesResourceDeleteAddonPropertyDelete(addonKey, propertyKey)

Delete app property

Deletes an app&#39;s property.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://your-domain.atlassian.net");

    AppPropertiesApi apiInstance = new AppPropertiesApi(defaultClient);
    String addonKey = "addonKey_example"; // String | The key of the app, as defined in its descriptor.
    String propertyKey = "propertyKey_example"; // String | The key of the property.
    try {
      apiInstance.addonPropertiesResourceDeleteAddonPropertyDelete(addonKey, propertyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPropertiesApi#addonPropertiesResourceDeleteAddonPropertyDelete");
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
| **addonKey** | **String**| The key of the app, as defined in its descriptor. | |
| **propertyKey** | **String**| The key of the property. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Returned if the request is successful. |  -  |
| **400** | Returned if the property key is longer than 127 characters. |  -  |
| **401** | Returned if the authentication credentials are incorrect or missing. |  -  |
| **404** | Returned if the property is not found or doesn&#39;t belong to the app. |  -  |

<a id="addonPropertiesResourceGetAddonPropertiesGet"></a>
# **addonPropertiesResourceGetAddonPropertiesGet**
> PropertyKeys addonPropertiesResourceGetAddonPropertiesGet(addonKey)

Get app properties

Gets all the properties of an app.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request. Additionally, Forge apps published on the Marketplace can access properties of Connect apps they were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://your-domain.atlassian.net");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppPropertiesApi apiInstance = new AppPropertiesApi(defaultClient);
    String addonKey = "addonKey_example"; // String | The key of the app, as defined in its descriptor.
    try {
      PropertyKeys result = apiInstance.addonPropertiesResourceGetAddonPropertiesGet(addonKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPropertiesApi#addonPropertiesResourceGetAddonPropertiesGet");
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
| **addonKey** | **String**| The key of the app, as defined in its descriptor. | |

### Return type

[**PropertyKeys**](PropertyKeys.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the request is successful. |  -  |
| **401** | Returned if the authentication credentials are incorrect or missing. |  -  |

<a id="addonPropertiesResourceGetAddonPropertyGet"></a>
# **addonPropertiesResourceGetAddonPropertyGet**
> EntityProperty addonPropertiesResourceGetAddonPropertyGet(addonKey, propertyKey)

Get app property

Returns the key and value of an app&#39;s property.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request. Additionally, Forge apps published on the Marketplace can access properties of Connect apps they were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://your-domain.atlassian.net");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    AppPropertiesApi apiInstance = new AppPropertiesApi(defaultClient);
    String addonKey = "addonKey_example"; // String | The key of the app, as defined in its descriptor.
    String propertyKey = "propertyKey_example"; // String | The key of the property.
    try {
      EntityProperty result = apiInstance.addonPropertiesResourceGetAddonPropertyGet(addonKey, propertyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPropertiesApi#addonPropertiesResourceGetAddonPropertyGet");
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
| **addonKey** | **String**| The key of the app, as defined in its descriptor. | |
| **propertyKey** | **String**| The key of the property. | |

### Return type

[**EntityProperty**](EntityProperty.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the request is successful. |  -  |
| **400** | Returned if the property key is longer than 127 characters. |  -  |
| **401** | Returned if the authentication credentials are incorrect or missing. |  -  |
| **404** | Returned if the property is not found or doesn&#39;t belong to the app. |  -  |

<a id="addonPropertiesResourcePutAddonPropertyPut"></a>
# **addonPropertiesResourcePutAddonPropertyPut**
> OperationMessage addonPropertiesResourcePutAddonPropertyPut(addonKey, propertyKey, body)

Set app property

Sets the value of an app&#39;s property. Use this resource to store custom data for your app.  The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppPropertiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://your-domain.atlassian.net");

    AppPropertiesApi apiInstance = new AppPropertiesApi(defaultClient);
    String addonKey = "addonKey_example"; // String | The key of the app, as defined in its descriptor.
    String propertyKey = "propertyKey_example"; // String | The key of the property.
    Object body = null; // Object | 
    try {
      OperationMessage result = apiInstance.addonPropertiesResourcePutAddonPropertyPut(addonKey, propertyKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppPropertiesApi#addonPropertiesResourcePutAddonPropertyPut");
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
| **addonKey** | **String**| The key of the app, as defined in its descriptor. | |
| **propertyKey** | **String**| The key of the property. | |
| **body** | **Object**|  | |

### Return type

[**OperationMessage**](OperationMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the property is updated. |  -  |
| **201** | Returned is the property is created. |  -  |
| **400** | Returned if:   * the property key is longer than 127 characters.   * the value is not valid JSON.   * the value is longer than 32768 characters. |  -  |
| **401** | Returned if the authentication credentials are incorrect or missing. |  -  |

