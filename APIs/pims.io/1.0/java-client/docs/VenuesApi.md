# VenuesApi

All URIs are relative to *https://demo.pims.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAllVenues**](VenuesApi.md#fetchAllVenues) | **GET** /venues | Find all venues |
| [**fetchOneVenue**](VenuesApi.md#fetchOneVenue) | **GET** /venues/{venue_id} | Get one venue by ID |


<a id="fetchAllVenues"></a>
# **fetchAllVenues**
> List&lt;VenuesEntity&gt; fetchAllVenues(label, city, countryCode, type, sort, pageSize, acceptLanguage)

Find all venues

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VenuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    VenuesApi apiInstance = new VenuesApi(defaultClient);
    String label = "label_example"; // String | Find only the venues whose label contains this value.
    String city = "city_example"; // String | Find only the venues whose city contains this value.
    String countryCode = "countryCode_example"; // String | Find only the venues whose country_code is equal to this value.
    String type = "SAL"; // String | Find only the venues whose type is equal to this value.
    String sort = "label"; // String | Sort the venues in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      List<VenuesEntity> result = apiInstance.fetchAllVenues(label, city, countryCode, type, sort, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VenuesApi#fetchAllVenues");
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
| **label** | **String**| Find only the venues whose label contains this value. | [optional] |
| **city** | **String**| Find only the venues whose city contains this value. | [optional] |
| **countryCode** | **String**| Find only the venues whose country_code is equal to this value. | [optional] |
| **type** | **String**| Find only the venues whose type is equal to this value. | [optional] [enum: SAL, FES] |
| **sort** | **String**| Sort the venues in the corresponding order. | [optional] [default to label] [enum: label, -label, city, -city, country, -country] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**List&lt;VenuesEntity&gt;**](VenuesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of venues |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOneVenue"></a>
# **fetchOneVenue**
> VenuesEntity fetchOneVenue(venueId, acceptLanguage)

Get one venue by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VenuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    VenuesApi apiInstance = new VenuesApi(defaultClient);
    Integer venueId = 56; // Integer | ID of the targeted venue.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      VenuesEntity result = apiInstance.fetchOneVenue(venueId, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VenuesApi#fetchOneVenue");
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
| **venueId** | **Integer**| ID of the targeted venue. | |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**VenuesEntity**](VenuesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one venue |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |

