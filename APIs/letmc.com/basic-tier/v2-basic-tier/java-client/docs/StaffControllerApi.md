# StaffControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2Tier2ShortNameStaffStaffApplicationStaffIDGet**](StaffControllerApi.md#v2Tier2ShortNameStaffStaffApplicationStaffIDGet) | **GET** /v2/tier2/{shortName}/staff/staff/{applicationStaffID} | Get a specific application staff given its unique Object ID (OID) |
| [**v2Tier2ShortNameStaffStaffGet**](StaffControllerApi.md#v2Tier2ShortNameStaffStaffGet) | **GET** /v2/tier2/{shortName}/staff/staff | A collection of all the staff members linked to a specific company |


<a id="v2Tier2ShortNameStaffStaffApplicationStaffIDGet"></a>
# **v2Tier2ShortNameStaffStaffApplicationStaffIDGet**
> ApplicationStaffModel v2Tier2ShortNameStaffStaffApplicationStaffIDGet(shortName, applicationStaffID)

Get a specific application staff given its unique Object ID (OID)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaffControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    StaffControllerApi apiInstance = new StaffControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String applicationStaffID = "applicationStaffID_example"; // String | The unique ID of the ApplicationStaff
    try {
      ApplicationStaffModel result = apiInstance.v2Tier2ShortNameStaffStaffApplicationStaffIDGet(shortName, applicationStaffID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaffControllerApi#v2Tier2ShortNameStaffStaffApplicationStaffIDGet");
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
| **applicationStaffID** | **String**| The unique ID of the ApplicationStaff | |

### Return type

[**ApplicationStaffModel**](ApplicationStaffModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v2Tier2ShortNameStaffStaffGet"></a>
# **v2Tier2ShortNameStaffStaffGet**
> ApplicationStaffModelResults v2Tier2ShortNameStaffStaffGet(shortName, offset, count)

A collection of all the staff members linked to a specific company

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaffControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    StaffControllerApi apiInstance = new StaffControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    Integer offset = 56; // Integer | The index of the first item to return
    Integer count = 56; // Integer | The maximum number of items to return (up to 1000 per request)
    try {
      ApplicationStaffModelResults result = apiInstance.v2Tier2ShortNameStaffStaffGet(shortName, offset, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaffControllerApi#v2Tier2ShortNameStaffStaffGet");
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

[**ApplicationStaffModelResults**](ApplicationStaffModelResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

