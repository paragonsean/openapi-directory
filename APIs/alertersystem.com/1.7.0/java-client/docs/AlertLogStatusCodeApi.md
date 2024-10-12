# AlertLogStatusCodeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiAlertLogStatusCodeGetCollection**](AlertLogStatusCodeApi.md#apiAlertLogStatusCodeGetCollection) | **GET** /api/alert-log-status-code | Retrieves the collection of AlertLogStatusCode resources. |
| [**apiAlertLogStatusCodeIdGet**](AlertLogStatusCodeApi.md#apiAlertLogStatusCodeIdGet) | **GET** /api/alert-log-status-code/{id} | Retrieves a AlertLogStatusCode resource. |


<a id="apiAlertLogStatusCodeGetCollection"></a>
# **apiAlertLogStatusCodeGetCollection**
> List&lt;AlertLogStatusCodeGet&gt; apiAlertLogStatusCodeGetCollection(page, properties)

Retrieves the collection of AlertLogStatusCode resources.

Retrieves the collection of AlertLogStatusCode resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertLogStatusCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    AlertLogStatusCodeApi apiInstance = new AlertLogStatusCodeApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<AlertLogStatusCodeGet> result = apiInstance.apiAlertLogStatusCodeGetCollection(page, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertLogStatusCodeApi#apiAlertLogStatusCodeGetCollection");
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
| **page** | **Integer**| The collection page number | [optional] [default to 1] |
| **properties** | [**List&lt;String&gt;**](String.md)| Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty} | [optional] |

### Return type

[**List&lt;AlertLogStatusCodeGet&gt;**](AlertLogStatusCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | AlertLogStatusCode collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiAlertLogStatusCodeIdGet"></a>
# **apiAlertLogStatusCodeIdGet**
> AlertLogStatusCodeGet apiAlertLogStatusCodeIdGet(id)

Retrieves a AlertLogStatusCode resource.

Retrieves a AlertLogStatusCode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertLogStatusCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    AlertLogStatusCodeApi apiInstance = new AlertLogStatusCodeApi(defaultClient);
    String id = "id_example"; // String | AlertLogStatusCode identifier
    try {
      AlertLogStatusCodeGet result = apiInstance.apiAlertLogStatusCodeIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertLogStatusCodeApi#apiAlertLogStatusCodeIdGet");
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
| **id** | **String**| AlertLogStatusCode identifier | |

### Return type

[**AlertLogStatusCodeGet**](AlertLogStatusCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | AlertLogStatusCode resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

