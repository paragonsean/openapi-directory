# SociodemoApi

All URIs are relative to *https://developer.o2.cz/sociodemo/sandbox/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**age**](SociodemoApi.md#age) | **GET** /age/{location} | Presence in a location aggregated by age |
| [**gender**](SociodemoApi.md#gender) | **GET** /gender/{location} | Presence in a location aggregated by gender |


<a id="age"></a>
# **age**
> CountResult age(location, ageGroup, occurenceType, hour)

Presence in a location aggregated by age

Get count of people in a given location and an hour, aggregated by age.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SociodemoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.o2.cz/sociodemo/sandbox/api");

    SociodemoApi apiInstance = new SociodemoApi(defaultClient);
    String location = "127752"; // String | basic residential unit
    String ageGroup = "2"; // String | age-group specification (1: 8-18, 2: 19-25, 3: 26-35, 4: 36-55, 5: 56+)
    String occurenceType = "1"; // String | occurence type in the basic residential unit (1 - transit, 2 - visit)
    String hour = "10"; // String | time interval for the count aggregation (from 0 to 23)
    try {
      CountResult result = apiInstance.age(location, ageGroup, occurenceType, hour);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SociodemoApi#age");
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
| **location** | **String**| basic residential unit | |
| **ageGroup** | **String**| age-group specification (1: 8-18, 2: 19-25, 3: 26-35, 4: 36-55, 5: 56+) | |
| **occurenceType** | **String**| occurence type in the basic residential unit (1 - transit, 2 - visit) | |
| **hour** | **String**| time interval for the count aggregation (from 0 to 23) | |

### Return type

[**CountResult**](CountResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response with the requested content. |  -  |
| **204** | The request is valid, but the platform is not able to serve the data. The reason may be restriction (e.g. differential privacy) or no data were found. |  -  |
| **400** | Invalid request provided, missing or invalid parameter. |  -  |
| **500** | Internal server error. |  -  |

<a id="gender"></a>
# **gender**
> CountResult gender(location, g, occurenceType, hour)

Presence in a location aggregated by gender

Get count of people in a given location and an hour, aggregated by gender.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SociodemoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://developer.o2.cz/sociodemo/sandbox/api");

    SociodemoApi apiInstance = new SociodemoApi(defaultClient);
    String location = "127752"; // String | basic residential unit
    String g = "1"; // String | gender specification (1 - male, 2 - female)
    String occurenceType = "1"; // String | occurence type in the basic residential unit (1 - transit, 2 - visit)
    String hour = "10"; // String | time interval for the count aggregation (from 0 to 23)
    try {
      CountResult result = apiInstance.gender(location, g, occurenceType, hour);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SociodemoApi#gender");
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
| **location** | **String**| basic residential unit | |
| **g** | **String**| gender specification (1 - male, 2 - female) | |
| **occurenceType** | **String**| occurence type in the basic residential unit (1 - transit, 2 - visit) | |
| **hour** | **String**| time interval for the count aggregation (from 0 to 23) | |

### Return type

[**CountResult**](CountResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response with the requested content. |  -  |
| **204** | The request is valid, but the platform is not able to serve the data. The reason may be restriction (e.g. differential privacy) or no data were found. |  -  |
| **400** | Invalid request provided, missing or invalid parameter. |  -  |
| **500** | Internal server error. |  -  |

