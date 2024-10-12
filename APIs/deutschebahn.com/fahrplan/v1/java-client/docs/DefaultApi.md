# DefaultApi

All URIs are relative to *https://api.deutschebahn.com/freeplan/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**arrivalBoardIdGet**](DefaultApi.md#arrivalBoardIdGet) | **GET** /arrivalBoard/{id} | Get arrival board of a location |
| [**departureBoardIdGet**](DefaultApi.md#departureBoardIdGet) | **GET** /departureBoard/{id} | Get departure board of a location |
| [**journeyDetailsIdGet**](DefaultApi.md#journeyDetailsIdGet) | **GET** /journeyDetails/{id} | Get details about a single journey |
| [**locationNameGet**](DefaultApi.md#locationNameGet) | **GET** /location/{name} | Get location information |


<a id="arrivalBoardIdGet"></a>
# **arrivalBoardIdGet**
> BoardResponse arrivalBoardIdGet(id, date)

Get arrival board of a location

Get arrival board at a given location at a given daten and time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/freeplan/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Id of location. Use attribute 'id' from the result of 'location'
    String date = "date_example"; // String | Date and time in ISO-8601 format, yyyy-mm-ddThh:mm:ss, example: 2017-04-01 or 2017-04-01T10:30
    try {
      BoardResponse result = apiInstance.arrivalBoardIdGet(id, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#arrivalBoardIdGet");
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
| **id** | **String**| Id of location. Use attribute &#39;id&#39; from the result of &#39;location&#39; | |
| **date** | **String**| Date and time in ISO-8601 format, yyyy-mm-ddThh:mm:ss, example: 2017-04-01 or 2017-04-01T10:30 | |

### Return type

[**BoardResponse**](BoardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | arrival board |  -  |
| **400** | Invalid date/time specification. |  -  |
| **500** | Internal Server Error. |  -  |
| **503** | The service has been disabled temporarily. |  -  |

<a id="departureBoardIdGet"></a>
# **departureBoardIdGet**
> BoardResponse departureBoardIdGet(id, date)

Get departure board of a location

Get departure board at a given location at a given daten and time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/freeplan/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Id of a location. Use attribute 'id' from the result of 'location'
    String date = "date_example"; // String | Date and time in ISO-8601 format, yyyy-mm-ddThh:mm:ss, example: 2017-04-01 or 2017-04-01T10:30
    try {
      BoardResponse result = apiInstance.departureBoardIdGet(id, date);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#departureBoardIdGet");
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
| **id** | **String**| Id of a location. Use attribute &#39;id&#39; from the result of &#39;location&#39; | |
| **date** | **String**| Date and time in ISO-8601 format, yyyy-mm-ddThh:mm:ss, example: 2017-04-01 or 2017-04-01T10:30 | |

### Return type

[**BoardResponse**](BoardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | departure board |  -  |
| **400** | Invalid date/time specification. |  -  |
| **500** | Internal Server Error. |  -  |
| **503** | The service has been disabled temporarily. |  -  |

<a id="journeyDetailsIdGet"></a>
# **journeyDetailsIdGet**
> JourneyResponse journeyDetailsIdGet(id)

Get details about a single journey

Retrieve details of a journey. The id of journey should come from an arrival board or a departure board.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/freeplan/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | Id of a journey. Use attribute 'detailsId' from the result of  'arrivalBoard' or 'departureBoard'
    try {
      JourneyResponse result = apiInstance.journeyDetailsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#journeyDetailsIdGet");
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
| **id** | **String**| Id of a journey. Use attribute &#39;detailsId&#39; from the result of  &#39;arrivalBoard&#39; or &#39;departureBoard&#39; | |

### Return type

[**JourneyResponse**](JourneyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | journey details, locations of a journey |  -  |
| **500** | Internal Server Error. |  -  |
| **503** | The service has been disabled temporarily. |  -  |

<a id="locationNameGet"></a>
# **locationNameGet**
> LocationResponse locationNameGet(name)

Get location information

Get information about locations matching the given name or name fragment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.deutschebahn.com/freeplan/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | Name or name fragment of a location
    try {
      LocationResponse result = apiInstance.locationNameGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#locationNameGet");
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
| **name** | **String**| Name or name fragment of a location | |

### Return type

[**LocationResponse**](LocationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | location information |  -  |
| **500** | Internal Server Error. |  -  |
| **503** | The service has been disabled temporarily. |  -  |

