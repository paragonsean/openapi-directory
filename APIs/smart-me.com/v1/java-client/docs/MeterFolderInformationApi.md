# MeterFolderInformationApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**meterFolderInformationGet**](MeterFolderInformationApi.md#meterFolderInformationGet) | **GET** /api/MeterFolderInformation/{id} | Beta: Gets the General Information for a Meter or a Folder |
| [**meterFolderInformationPost**](MeterFolderInformationApi.md#meterFolderInformationPost) | **POST** /api/MeterFolderInformation | Sets the Name of a Meter or a Folder |


<a id="meterFolderInformationGet"></a>
# **meterFolderInformationGet**
> MeterFolderInformation meterFolderInformationGet(id)

Beta: Gets the General Information for a Meter or a Folder

Beta: Gets the General Information for a Meter or a Folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeterFolderInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    MeterFolderInformationApi apiInstance = new MeterFolderInformationApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      MeterFolderInformation result = apiInstance.meterFolderInformationGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeterFolderInformationApi#meterFolderInformationGet");
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
| **id** | **String**|  | |

### Return type

[**MeterFolderInformation**](MeterFolderInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="meterFolderInformationPost"></a>
# **meterFolderInformationPost**
> meterFolderInformationPost(meterFolderInformationToPost)

Sets the Name of a Meter or a Folder

Sets the Name of a Meter or a Folder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeterFolderInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    MeterFolderInformationApi apiInstance = new MeterFolderInformationApi(defaultClient);
    MeterFolderInformationToPost meterFolderInformationToPost = new MeterFolderInformationToPost(); // MeterFolderInformationToPost | 
    try {
      apiInstance.meterFolderInformationPost(meterFolderInformationToPost);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeterFolderInformationApi#meterFolderInformationPost");
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
| **meterFolderInformationToPost** | [**MeterFolderInformationToPost**](MeterFolderInformationToPost.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

