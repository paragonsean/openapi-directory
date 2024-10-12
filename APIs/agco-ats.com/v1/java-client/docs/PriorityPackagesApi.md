# PriorityPackagesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**priorityPackagesDeletePriorityPackages**](PriorityPackagesApi.md#priorityPackagesDeletePriorityPackages) | **DELETE** /api/v2/PriorityPackages/{ID} | Delete a Priority Package for a Client. |
| [**priorityPackagesGetPriorityPackage**](PriorityPackagesApi.md#priorityPackagesGetPriorityPackage) | **GET** /api/v2/PriorityPackages/{ID} | Get a Priority Packages for a Client. |
| [**priorityPackagesGetPriorityPackages**](PriorityPackagesApi.md#priorityPackagesGetPriorityPackages) | **GET** /api/v2/PriorityPackages | Get a list of Priority Packages by Client. |
| [**priorityPackagesPostPriorityPackages**](PriorityPackagesApi.md#priorityPackagesPostPriorityPackages) | **POST** /api/v2/PriorityPackages | Add a Priority Package for a Client. |


<a id="priorityPackagesDeletePriorityPackages"></a>
# **priorityPackagesDeletePriorityPackages**
> priorityPackagesDeletePriorityPackages(ID)

Delete a Priority Package for a Client.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriorityPackagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PriorityPackagesApi apiInstance = new PriorityPackagesApi(defaultClient);
    String ID = "ID_example"; // String | The Priority Package ID
    try {
      apiInstance.priorityPackagesDeletePriorityPackages(ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriorityPackagesApi#priorityPackagesDeletePriorityPackages");
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
| **ID** | **String**| The Priority Package ID | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="priorityPackagesGetPriorityPackage"></a>
# **priorityPackagesGetPriorityPackage**
> UpdateSystemModelsPriorityPackage priorityPackagesGetPriorityPackage(ID)

Get a Priority Packages for a Client.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriorityPackagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PriorityPackagesApi apiInstance = new PriorityPackagesApi(defaultClient);
    String ID = "ID_example"; // String | The Priority Package ID
    try {
      UpdateSystemModelsPriorityPackage result = apiInstance.priorityPackagesGetPriorityPackage(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriorityPackagesApi#priorityPackagesGetPriorityPackage");
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
| **ID** | **String**| The Priority Package ID | |

### Return type

[**UpdateSystemModelsPriorityPackage**](UpdateSystemModelsPriorityPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="priorityPackagesGetPriorityPackages"></a>
# **priorityPackagesGetPriorityPackages**
> APIPagedResponseUpdateSystemModelsPriorityPackage priorityPackagesGetPriorityPackages(clientID, status, limit, offset)

Get a list of Priority Packages by Client.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriorityPackagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PriorityPackagesApi apiInstance = new PriorityPackagesApi(defaultClient);
    String clientID = "clientID_example"; // String | Optional. Filter priority packages by ClientID.
    String status = "Active"; // String | Optional. Filter returned packages by status. By default only active packages will be returned.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsPriorityPackage result = apiInstance.priorityPackagesGetPriorityPackages(clientID, status, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriorityPackagesApi#priorityPackagesGetPriorityPackages");
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
| **clientID** | **String**| Optional. Filter priority packages by ClientID. | [optional] |
| **status** | **String**| Optional. Filter returned packages by status. By default only active packages will be returned. | [optional] [enum: Active, Completed, All] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsPriorityPackage**](APIPagedResponseUpdateSystemModelsPriorityPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="priorityPackagesPostPriorityPackages"></a>
# **priorityPackagesPostPriorityPackages**
> String priorityPackagesPostPriorityPackages(updateSystemModelsPriorityPackage)

Add a Priority Package for a Client.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriorityPackagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PriorityPackagesApi apiInstance = new PriorityPackagesApi(defaultClient);
    UpdateSystemModelsPriorityPackage updateSystemModelsPriorityPackage = new UpdateSystemModelsPriorityPackage(); // UpdateSystemModelsPriorityPackage | The PriorityPackage to add
    try {
      String result = apiInstance.priorityPackagesPostPriorityPackages(updateSystemModelsPriorityPackage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriorityPackagesApi#priorityPackagesPostPriorityPackages");
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
| **updateSystemModelsPriorityPackage** | [**UpdateSystemModelsPriorityPackage**](UpdateSystemModelsPriorityPackage.md)| The PriorityPackage to add | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

