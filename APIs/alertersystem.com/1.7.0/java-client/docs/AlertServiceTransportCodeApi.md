# AlertServiceTransportCodeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiAlertServiceTransportCodeGetCollection**](AlertServiceTransportCodeApi.md#apiAlertServiceTransportCodeGetCollection) | **GET** /api/alert-service-transport-code | Retrieves the collection of AlertServiceTransportCode resources. |
| [**apiAlertServiceTransportCodeIdGet**](AlertServiceTransportCodeApi.md#apiAlertServiceTransportCodeIdGet) | **GET** /api/alert-service-transport-code/{id} | Retrieves a AlertServiceTransportCode resource. |


<a id="apiAlertServiceTransportCodeGetCollection"></a>
# **apiAlertServiceTransportCodeGetCollection**
> List&lt;AlertServiceTransportCodeGet&gt; apiAlertServiceTransportCodeGetCollection(page, properties)

Retrieves the collection of AlertServiceTransportCode resources.

Retrieves the collection of AlertServiceTransportCode resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertServiceTransportCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    AlertServiceTransportCodeApi apiInstance = new AlertServiceTransportCodeApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<AlertServiceTransportCodeGet> result = apiInstance.apiAlertServiceTransportCodeGetCollection(page, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertServiceTransportCodeApi#apiAlertServiceTransportCodeGetCollection");
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

[**List&lt;AlertServiceTransportCodeGet&gt;**](AlertServiceTransportCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | AlertServiceTransportCode collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiAlertServiceTransportCodeIdGet"></a>
# **apiAlertServiceTransportCodeIdGet**
> AlertServiceTransportCodeGet apiAlertServiceTransportCodeIdGet(id)

Retrieves a AlertServiceTransportCode resource.

Retrieves a AlertServiceTransportCode resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AlertServiceTransportCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    AlertServiceTransportCodeApi apiInstance = new AlertServiceTransportCodeApi(defaultClient);
    String id = "id_example"; // String | AlertServiceTransportCode identifier
    try {
      AlertServiceTransportCodeGet result = apiInstance.apiAlertServiceTransportCodeIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AlertServiceTransportCodeApi#apiAlertServiceTransportCodeIdGet");
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
| **id** | **String**| AlertServiceTransportCode identifier | |

### Return type

[**AlertServiceTransportCodeGet**](AlertServiceTransportCodeGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | AlertServiceTransportCode resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

