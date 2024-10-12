# NeosentryApi

All URIs are relative to *http://www.neowsapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveSentryRiskData**](NeosentryApi.md#retrieveSentryRiskData) | **GET** /rest/v1/neo/sentry | Retrieve Sentry (Impact Risk ) Near Earth Objects |
| [**retrieveSentryRiskDataById**](NeosentryApi.md#retrieveSentryRiskDataById) | **GET** /rest/v1/neo/sentry/{asteroid_id} | Retrieve Sentry (Impact Risk ) Near Earth Objectby ID  |


<a id="retrieveSentryRiskData"></a>
# **retrieveSentryRiskData**
> SentryObjectPagingDto retrieveSentryRiskData(isActive, page, size)

Retrieve Sentry (Impact Risk ) Near Earth Objects

Retrieves Near Earth Objects listed in the NASA sentry data set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NeosentryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.neowsapp.com");

    NeosentryApi apiInstance = new NeosentryApi(defaultClient);
    Boolean isActive = true; // Boolean | show current list of Sentry objects, or show removed Sentry objects
    Integer page = 0; // Integer | page
    Integer size = 50; // Integer | size
    try {
      SentryObjectPagingDto result = apiInstance.retrieveSentryRiskData(isActive, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NeosentryApi#retrieveSentryRiskData");
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
| **isActive** | **Boolean**| show current list of Sentry objects, or show removed Sentry objects | [optional] [default to true] |
| **page** | **Integer**| page | [optional] [default to 0] |
| **size** | **Integer**| size | [optional] [default to 50] |

### Return type

[**SentryObjectPagingDto**](SentryObjectPagingDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="retrieveSentryRiskDataById"></a>
# **retrieveSentryRiskDataById**
> SentryImpactRiskObject retrieveSentryRiskDataById(asteroidId)

Retrieve Sentry (Impact Risk ) Near Earth Objectby ID 

Retrieves Sentry Near Earth Object by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NeosentryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.neowsapp.com");

    NeosentryApi apiInstance = new NeosentryApi(defaultClient);
    String asteroidId = "asteroidId_example"; // String | ID of NearEarth object.  ID can be SPK_ID, Asteroid des (designation) or Sentry ID
    try {
      SentryImpactRiskObject result = apiInstance.retrieveSentryRiskDataById(asteroidId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NeosentryApi#retrieveSentryRiskDataById");
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
| **asteroidId** | **String**| ID of NearEarth object.  ID can be SPK_ID, Asteroid des (designation) or Sentry ID | |

### Return type

[**SentryImpactRiskObject**](SentryImpactRiskObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

