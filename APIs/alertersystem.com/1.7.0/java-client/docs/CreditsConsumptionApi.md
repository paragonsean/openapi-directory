# CreditsConsumptionApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCreditsConsumptionGetCollection**](CreditsConsumptionApi.md#apiCreditsConsumptionGetCollection) | **GET** /api/credits-consumption | Retrieves the collection of CreditsConsumption resources. |
| [**apiCreditsConsumptionIdGet**](CreditsConsumptionApi.md#apiCreditsConsumptionIdGet) | **GET** /api/credits-consumption/{id} | Retrieves a CreditsConsumption resource. |


<a id="apiCreditsConsumptionGetCollection"></a>
# **apiCreditsConsumptionGetCollection**
> List&lt;CreditsConsumptionGet&gt; apiCreditsConsumptionGetCollection(page, properties)

Retrieves the collection of CreditsConsumption resources.

Retrieves the collection of CreditsConsumption resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditsConsumptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    CreditsConsumptionApi apiInstance = new CreditsConsumptionApi(defaultClient);
    Integer page = 1; // Integer | The collection page number
    List<String> properties = Arrays.asList(); // List<String> | Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]={propertyName}&properties[]={anotherPropertyName}&properties[{nestedPropertyParent}][]={nestedProperty}
    try {
      List<CreditsConsumptionGet> result = apiInstance.apiCreditsConsumptionGetCollection(page, properties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditsConsumptionApi#apiCreditsConsumptionGetCollection");
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

[**List&lt;CreditsConsumptionGet&gt;**](CreditsConsumptionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CreditsConsumption collection |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="apiCreditsConsumptionIdGet"></a>
# **apiCreditsConsumptionIdGet**
> CreditsConsumptionGet apiCreditsConsumptionIdGet(id)

Retrieves a CreditsConsumption resource.

Retrieves a CreditsConsumption resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditsConsumptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    CreditsConsumptionApi apiInstance = new CreditsConsumptionApi(defaultClient);
    String id = "id_example"; // String | CreditsConsumption identifier
    try {
      CreditsConsumptionGet result = apiInstance.apiCreditsConsumptionIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditsConsumptionApi#apiCreditsConsumptionIdGet");
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
| **id** | **String**| CreditsConsumption identifier | |

### Return type

[**CreditsConsumptionGet**](CreditsConsumptionGet.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | CreditsConsumption resource |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **429** | Too many requests |  -  |

