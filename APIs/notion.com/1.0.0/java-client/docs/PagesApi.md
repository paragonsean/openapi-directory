# PagesApi

All URIs are relative to *https://api.notion.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveAPage**](PagesApi.md#retrieveAPage) | **GET** /v1/pages/{id} | Retrieve a Page |
| [**retrieveAPagePropertyItem**](PagesApi.md#retrieveAPagePropertyItem) | **GET** /v1/pages/{page_id}/properties/{property_id} | Retrieve a Page Property Item |
| [**updatePageProperties**](PagesApi.md#updatePageProperties) | **PATCH** /v1/pages/{id} | Update Page properties  |


<a id="retrieveAPage"></a>
# **retrieveAPage**
> RetrieveAPage200Response retrieveAPage(id, notionVersion, )

Retrieve a Page

Retrieves a Page object using the ID in the request path. This endpoint exposes page properties, not page content. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String id = "{{PAGE_ID}}"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    String  = ""; // String | 
    try {
      RetrieveAPage200Response result = apiInstance.retrieveAPage(id, notionVersion, );
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#retrieveAPage");
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
| **notionVersion** | **String**|  | [optional] |
| **** | **String**|  | [optional] |

### Return type

[**RetrieveAPage200Response**](RetrieveAPage200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Retrieve a Page |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  |

<a id="retrieveAPagePropertyItem"></a>
# **retrieveAPagePropertyItem**
> RetrieveAPagePropertyItem200Response retrieveAPagePropertyItem(pageId, propertyId)

Retrieve a Page Property Item

Retrieve a Page Property Item

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String pageId = "{{PAGE_ID}}"; // String | 
    String propertyId = "propertyId_example"; // String | 
    try {
      RetrieveAPagePropertyItem200Response result = apiInstance.retrieveAPagePropertyItem(pageId, propertyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#retrieveAPagePropertyItem");
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
| **pageId** | **String**|  | |
| **propertyId** | **String**|  | |

### Return type

[**RetrieveAPagePropertyItem200Response**](RetrieveAPagePropertyItem200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Retrieve a Page Property Item |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  |

<a id="updatePageProperties"></a>
# **updatePageProperties**
> UpdatePageProperties200Response updatePageProperties(id, notionVersion, updatePagePropertiesRequest)

Update Page properties 

Updates a page by setting the values of any properties specified in the JSON body of the request. Properties not updated via parameters will remain unchanged. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    PagesApi apiInstance = new PagesApi(defaultClient);
    String id = "{{PAGE_ID}}"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    UpdatePagePropertiesRequest updatePagePropertiesRequest = new UpdatePagePropertiesRequest(); // UpdatePagePropertiesRequest | 
    try {
      UpdatePageProperties200Response result = apiInstance.updatePageProperties(id, notionVersion, updatePagePropertiesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PagesApi#updatePageProperties");
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
| **notionVersion** | **String**|  | [optional] |
| **updatePagePropertiesRequest** | [**UpdatePagePropertiesRequest**](UpdatePagePropertiesRequest.md)|  | [optional] |

### Return type

[**UpdatePageProperties200Response**](UpdatePageProperties200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Update Page properties |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  * cf-request-id -  <br>  |

