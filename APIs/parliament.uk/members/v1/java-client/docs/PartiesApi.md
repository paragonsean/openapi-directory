# PartiesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPartiesGetActiveHouseGet**](PartiesApi.md#apiPartiesGetActiveHouseGet) | **GET** /api/Parties/GetActive/{house} | Returns a list of current parties with at least one active member. |
| [**apiPartiesLordsByTypeForDateGet**](PartiesApi.md#apiPartiesLordsByTypeForDateGet) | **GET** /api/Parties/LordsByType/{forDate} | Returns the composition of the House of Lords by peerage type. |
| [**apiPartiesStateOfThePartiesHouseForDateGet**](PartiesApi.md#apiPartiesStateOfThePartiesHouseForDateGet) | **GET** /api/Parties/StateOfTheParties/{house}/{forDate} | Returns current state of parties |


<a id="apiPartiesGetActiveHouseGet"></a>
# **apiPartiesGetActiveHouseGet**
> PartyMembersServiceSearchResult apiPartiesGetActiveHouseGet(house)

Returns a list of current parties with at least one active member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PartiesApi apiInstance = new PartiesApi(defaultClient);
    House house = House.fromValue("1"); // House | Current parties by house
    try {
      PartyMembersServiceSearchResult result = apiInstance.apiPartiesGetActiveHouseGet(house);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartiesApi#apiPartiesGetActiveHouseGet");
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
| **house** | [**House**](.md)| Current parties by house | [enum: 1, 2] |

### Return type

[**PartyMembersServiceSearchResult**](PartyMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="apiPartiesLordsByTypeForDateGet"></a>
# **apiPartiesLordsByTypeForDateGet**
> LordsByTypeMembersServiceSearchResult apiPartiesLordsByTypeForDateGet(forDate)

Returns the composition of the House of Lords by peerage type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PartiesApi apiInstance = new PartiesApi(defaultClient);
    OffsetDateTime forDate = OffsetDateTime.now(); // OffsetDateTime | Composition of the Lords for date specified.
    try {
      LordsByTypeMembersServiceSearchResult result = apiInstance.apiPartiesLordsByTypeForDateGet(forDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartiesApi#apiPartiesLordsByTypeForDateGet");
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
| **forDate** | **OffsetDateTime**| Composition of the Lords for date specified. | |

### Return type

[**LordsByTypeMembersServiceSearchResult**](LordsByTypeMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="apiPartiesStateOfThePartiesHouseForDateGet"></a>
# **apiPartiesStateOfThePartiesHouseForDateGet**
> PartySeatCountMembersServiceSearchResult apiPartiesStateOfThePartiesHouseForDateGet(house, forDate)

Returns current state of parties

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PartiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PartiesApi apiInstance = new PartiesApi(defaultClient);
    House house = House.fromValue("1"); // House | State of parties in Commons or Lords.
    OffsetDateTime forDate = OffsetDateTime.now(); // OffsetDateTime | State of parties for the date specified
    try {
      PartySeatCountMembersServiceSearchResult result = apiInstance.apiPartiesStateOfThePartiesHouseForDateGet(house, forDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PartiesApi#apiPartiesStateOfThePartiesHouseForDateGet");
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
| **house** | [**House**](.md)| State of parties in Commons or Lords. | [enum: 1, 2] |
| **forDate** | **OffsetDateTime**| State of parties for the date specified | |

### Return type

[**PartySeatCountMembersServiceSearchResult**](PartySeatCountMembersServiceSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

