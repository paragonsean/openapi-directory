# AreaControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2Tier1ShortNameAreaAreasAreaIDGet**](AreaControllerApi.md#v2Tier1ShortNameAreaAreasAreaIDGet) | **GET** /v2/tier1/{shortName}/area/areas/{areaID} | Get a specific area given its unique Object ID (OID) |
| [**v2Tier1ShortNameAreaAreasGet**](AreaControllerApi.md#v2Tier1ShortNameAreaAreasGet) | **GET** /v2/tier1/{shortName}/area/areas | A collection of all the areas for a company |


<a id="v2Tier1ShortNameAreaAreasAreaIDGet"></a>
# **v2Tier1ShortNameAreaAreasAreaIDGet**
> AreaModel v2Tier1ShortNameAreaAreasAreaIDGet(shortName, areaID)

Get a specific area given its unique Object ID (OID)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AreaControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    AreaControllerApi apiInstance = new AreaControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String areaID = "areaID_example"; // String | The unique ID of the Area
    try {
      AreaModel result = apiInstance.v2Tier1ShortNameAreaAreasAreaIDGet(shortName, areaID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AreaControllerApi#v2Tier1ShortNameAreaAreasAreaIDGet");
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
| **areaID** | **String**| The unique ID of the Area | |

### Return type

[**AreaModel**](AreaModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier1ShortNameAreaAreasGet"></a>
# **v2Tier1ShortNameAreaAreasGet**
> AreaModelResults v2Tier1ShortNameAreaAreasGet(shortName, offset, count)

A collection of all the areas for a company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AreaControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    AreaControllerApi apiInstance = new AreaControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      AreaModelResults result = apiInstance.v2Tier1ShortNameAreaAreasGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AreaControllerApi#v2Tier1ShortNameAreaAreasGet");
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

[**AreaModelResults**](AreaModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

