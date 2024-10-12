# CountyControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**countyControllerGetCountiesBranches**](CountyControllerApi.md#countyControllerGetCountiesBranches) | **GET** /v2/tier2/{shortName}/county/counties/{countyID}/branches | A collection of branches that manage a specific county |
| [**v2Tier2ShortNameCountyCountiesCountyIDGet**](CountyControllerApi.md#v2Tier2ShortNameCountyCountiesCountyIDGet) | **GET** /v2/tier2/{shortName}/county/counties/{countyID} | Get a specific county given its unique Object ID (OID) |
| [**v2Tier2ShortNameCountyCountiesGet**](CountyControllerApi.md#v2Tier2ShortNameCountyCountiesGet) | **GET** /v2/tier2/{shortName}/county/counties | A collection of all counties available for a company |


<a id="countyControllerGetCountiesBranches"></a>
# **countyControllerGetCountiesBranches**
> BranchModelResults countyControllerGetCountiesBranches(shortName, countyID, offset, count)

A collection of branches that manage a specific county

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    CountyControllerApi apiInstance = new CountyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String countyID = "countyID_example"; // String | The unique ID of the County
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      BranchModelResults result = apiInstance.countyControllerGetCountiesBranches(shortName, countyID, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountyControllerApi#countyControllerGetCountiesBranches");
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
| **shortName** | **String**| The unique client short-name | |
| **countyID** | **String**| The unique ID of the County | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**BranchModelResults**](BranchModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier2ShortNameCountyCountiesCountyIDGet"></a>
# **v2Tier2ShortNameCountyCountiesCountyIDGet**
> CountyModel v2Tier2ShortNameCountyCountiesCountyIDGet(shortName, countyID)

Get a specific county given its unique Object ID (OID)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    CountyControllerApi apiInstance = new CountyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String countyID = "countyID_example"; // String | The unique ID of the County
    try {
      CountyModel result = apiInstance.v2Tier2ShortNameCountyCountiesCountyIDGet(shortName, countyID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountyControllerApi#v2Tier2ShortNameCountyCountiesCountyIDGet");
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
| **shortName** | **String**| The unique client short-name | |
| **countyID** | **String**| The unique ID of the County | |

### Return type

[**CountyModel**](CountyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier2ShortNameCountyCountiesGet"></a>
# **v2Tier2ShortNameCountyCountiesGet**
> CountyModelResults v2Tier2ShortNameCountyCountiesGet(shortName, offset, count)

A collection of all counties available for a company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountyControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    CountyControllerApi apiInstance = new CountyControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      CountyModelResults result = apiInstance.v2Tier2ShortNameCountyCountiesGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountyControllerApi#v2Tier2ShortNameCountyCountiesGet");
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
| **shortName** | **String**| The unique client short-name | |
| **offset** | **Integer**| The index of the first item to return | |
| **count** | **Integer**| The maximum number of items to return (up to 1000 per request) | |

### Return type

[**CountyModelResults**](CountyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

