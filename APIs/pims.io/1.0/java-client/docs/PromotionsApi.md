# PromotionsApi

All URIs are relative to *https://demo.pims.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAllEventsPromotions**](PromotionsApi.md#fetchAllEventsPromotions) | **GET** /events/{event_id}/promotions | Find all promotions for one event |
| [**fetchAllPromotions**](PromotionsApi.md#fetchAllPromotions) | **GET** /promotions | Find all promotions |
| [**fetchAllSeriesPromotions**](PromotionsApi.md#fetchAllSeriesPromotions) | **GET** /series/{series_id}/promotions | Find all promotions for one series |
| [**fetchOnePromotion**](PromotionsApi.md#fetchOnePromotion) | **GET** /promotions/{promotion_id} | Get one promotion by ID |


<a id="fetchAllEventsPromotions"></a>
# **fetchAllEventsPromotions**
> List&lt;PromotionsEntity&gt; fetchAllEventsPromotions(eventId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage)

Find all promotions for one event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    PromotionsApi apiInstance = new PromotionsApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    String label = "label_example"; // String | Find only the promotions whose label contains this value.
    LocalDate fromDate = LocalDate.now(); // LocalDate | Find only the promotions starting after this date.
    LocalDate toDate = LocalDate.now(); // LocalDate | Find only the promotions ending before this date.
    String type = "type_example"; // String | Find only the promotions whose type is equal to this value.
    String family = "family_example"; // String | Find only the promotions whose family is equal to this value.
    String sort = "date"; // String | Sort the promotions in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      List<PromotionsEntity> result = apiInstance.fetchAllEventsPromotions(eventId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsApi#fetchAllEventsPromotions");
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
| **label** | **String**| Find only the promotions whose label contains this value. | [optional] |
| **fromDate** | **LocalDate**| Find only the promotions starting after this date. | [optional] |
| **toDate** | **LocalDate**| Find only the promotions ending before this date. | [optional] |
| **type** | **String**| Find only the promotions whose type is equal to this value. | [optional] |
| **family** | **String**| Find only the promotions whose family is equal to this value. | [optional] |
| **sort** | **String**| Sort the promotions in the corresponding order. | [optional] [default to date] [enum: date, -date, total_cost, -total_cost] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**List&lt;PromotionsEntity&gt;**](PromotionsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of promotions |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchAllPromotions"></a>
# **fetchAllPromotions**
> List&lt;PromotionsEntity&gt; fetchAllPromotions(label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage)

Find all promotions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    PromotionsApi apiInstance = new PromotionsApi(defaultClient);
    String label = "label_example"; // String | Find only the promotions whose label contains this value.
    LocalDate fromDate = LocalDate.now(); // LocalDate | Find only the promotions starting after this date.
    LocalDate toDate = LocalDate.now(); // LocalDate | Find only the promotions ending before this date.
    String type = "type_example"; // String | Find only the promotions whose type is equal to this value.
    String family = "family_example"; // String | Find only the promotions whose family is equal to this value.
    String sort = "date"; // String | Sort the promotions in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      List<PromotionsEntity> result = apiInstance.fetchAllPromotions(label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsApi#fetchAllPromotions");
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
| **label** | **String**| Find only the promotions whose label contains this value. | [optional] |
| **fromDate** | **LocalDate**| Find only the promotions starting after this date. | [optional] |
| **toDate** | **LocalDate**| Find only the promotions ending before this date. | [optional] |
| **type** | **String**| Find only the promotions whose type is equal to this value. | [optional] |
| **family** | **String**| Find only the promotions whose family is equal to this value. | [optional] |
| **sort** | **String**| Sort the promotions in the corresponding order. | [optional] [default to date] [enum: date, -date, total_cost, -total_cost] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**List&lt;PromotionsEntity&gt;**](PromotionsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of promotions |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchAllSeriesPromotions"></a>
# **fetchAllSeriesPromotions**
> List&lt;PromotionsEntity&gt; fetchAllSeriesPromotions(seriesId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage)

Find all promotions for one series

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    PromotionsApi apiInstance = new PromotionsApi(defaultClient);
    Integer seriesId = 56; // Integer | ID of the targeted series.
    String label = "label_example"; // String | Find only the promotions whose label contains this value.
    LocalDate fromDate = LocalDate.now(); // LocalDate | Find only the promotions starting after this date.
    LocalDate toDate = LocalDate.now(); // LocalDate | Find only the promotions ending before this date.
    String type = "type_example"; // String | Find only the promotions whose type is equal to this value.
    String family = "family_example"; // String | Find only the promotions whose family is equal to this value.
    String sort = "date"; // String | Sort the promotions in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      List<PromotionsEntity> result = apiInstance.fetchAllSeriesPromotions(seriesId, label, fromDate, toDate, type, family, sort, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsApi#fetchAllSeriesPromotions");
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
| **seriesId** | **Integer**| ID of the targeted series. | |
| **label** | **String**| Find only the promotions whose label contains this value. | [optional] |
| **fromDate** | **LocalDate**| Find only the promotions starting after this date. | [optional] |
| **toDate** | **LocalDate**| Find only the promotions ending before this date. | [optional] |
| **type** | **String**| Find only the promotions whose type is equal to this value. | [optional] |
| **family** | **String**| Find only the promotions whose family is equal to this value. | [optional] |
| **sort** | **String**| Sort the promotions in the corresponding order. | [optional] [default to date] [enum: date, -date, total_cost, -total_cost] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**List&lt;PromotionsEntity&gt;**](PromotionsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of promotions |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOnePromotion"></a>
# **fetchOnePromotion**
> PromotionsEntity fetchOnePromotion(promotionId, acceptLanguage)

Get one promotion by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    PromotionsApi apiInstance = new PromotionsApi(defaultClient);
    Integer promotionId = 56; // Integer | ID of the targeted promotion.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      PromotionsEntity result = apiInstance.fetchOnePromotion(promotionId, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsApi#fetchOnePromotion");
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
| **promotionId** | **Integer**| ID of the targeted promotion. | |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**PromotionsEntity**](PromotionsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one promotion |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |

