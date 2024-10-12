# CategoriesApi

All URIs are relative to *https://demo.pims.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAllCategories**](CategoriesApi.md#fetchAllCategories) | **GET** /categories | Find all categories |
| [**fetchAllEventsCategories**](CategoriesApi.md#fetchAllEventsCategories) | **GET** /events/{event_id}/categories | Find all categories for one event |
| [**fetchOneCategory**](CategoriesApi.md#fetchOneCategory) | **GET** /categories/{category_id} | Get one category by ID |
| [**fetchOneEventCategory**](CategoriesApi.md#fetchOneEventCategory) | **GET** /events/{event_id}/categories/{category_id} | Get one event category by ID |


<a id="fetchAllCategories"></a>
# **fetchAllCategories**
> List&lt;CategoriesEntity&gt; fetchAllCategories(label, showIgnored, sort, pageSize, acceptLanguage)

Find all categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String label = "label_example"; // String | Find only the categories whose label/short label contains this value.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the categories which are not ignored. If set to `true`, show all categories.
    String sort = "label"; // String | Sort the categories in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      List<CategoriesEntity> result = apiInstance.fetchAllCategories(label, showIgnored, sort, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#fetchAllCategories");
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
| **label** | **String**| Find only the categories whose label/short label contains this value. | [optional] |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the categories which are not ignored. If set to &#x60;true&#x60;, show all categories. | [optional] [default to false] |
| **sort** | **String**| Sort the categories in the corresponding order. | [optional] [default to order] [enum: label, -label, order, -order] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**List&lt;CategoriesEntity&gt;**](CategoriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of categories |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchAllEventsCategories"></a>
# **fetchAllEventsCategories**
> List&lt;EventsCategoriesEntity&gt; fetchAllEventsCategories(eventId, showIgnored, pageSize)

Find all categories for one event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the [event-]categories/[event-]price ranges which are not ignored. If set to `true`, show everything.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    try {
      List<EventsCategoriesEntity> result = apiInstance.fetchAllEventsCategories(eventId, showIgnored, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#fetchAllEventsCategories");
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
| **eventId** | **Integer**| ID of the targeted event. | |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |

### Return type

[**List&lt;EventsCategoriesEntity&gt;**](EventsCategoriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of events categories |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOneCategory"></a>
# **fetchOneCategory**
> CategoriesEntity fetchOneCategory(categoryId, acceptLanguage)

Get one category by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    Integer categoryId = 56; // Integer | ID of the targeted category.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      CategoriesEntity result = apiInstance.fetchOneCategory(categoryId, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#fetchOneCategory");
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
| **categoryId** | **Integer**| ID of the targeted category. | |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**CategoriesEntity**](CategoriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one category |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOneEventCategory"></a>
# **fetchOneEventCategory**
> EventsCategoriesEntity fetchOneEventCategory(eventId, categoryId, showIgnored)

Get one event category by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    BigDecimal categoryId = new BigDecimal(78); // BigDecimal | ID of the targeted event category.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the embedded [event-]price ranges which are not ignored. If set to `true`, show everything.
    try {
      EventsCategoriesEntity result = apiInstance.fetchOneEventCategory(eventId, categoryId, showIgnored);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#fetchOneEventCategory");
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
| **eventId** | **Integer**| ID of the targeted event. | |
| **categoryId** | **BigDecimal**| ID of the targeted event category. | |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the embedded [event-]price ranges which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false] |

### Return type

[**EventsCategoriesEntity**](EventsCategoriesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one event category |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |

