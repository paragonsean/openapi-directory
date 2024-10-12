# UpdateSystemApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateSystemGetCachedFiles**](UpdateSystemApi.md#updateSystemGetCachedFiles) | **GET** /api/v2/Clients/{ClientID}/CachedFiles | Get a list of Cached Files installed on the client Machine. |
| [**updateSystemGetCheckin**](UpdateSystemApi.md#updateSystemGetCheckin) | **GET** /api/v2/UpdateSystem | Checks the Client ID into the Update System. |


<a id="updateSystemGetCachedFiles"></a>
# **updateSystemGetCachedFiles**
> List&lt;String&gt; updateSystemGetCachedFiles(clientID, expired)

Get a list of Cached Files installed on the client Machine.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateSystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateSystemApi apiInstance = new UpdateSystemApi(defaultClient);
    String clientID = "clientID_example"; // String | The ClientID of the Client
    Boolean expired = true; // Boolean | Only Expired Files (true|false)
    try {
      List<String> result = apiInstance.updateSystemGetCachedFiles(clientID, expired);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateSystemApi#updateSystemGetCachedFiles");
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
| **clientID** | **String**| The ClientID of the Client | |
| **expired** | **Boolean**| Only Expired Files (true|false) | |

### Return type

**List&lt;String&gt;**

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

<a id="updateSystemGetCheckin"></a>
# **updateSystemGetCheckin**
> UpdateSystemModelsCheckinResult updateSystemGetCheckin(clientID, preview, runAllInventories)

Checks the Client ID into the Update System.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UpdateSystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UpdateSystemApi apiInstance = new UpdateSystemApi(defaultClient);
    String clientID = "clientID_example"; // String | The Client ID to check-in.  If this is a new client ID it will be added to Clients.
    Boolean preview = true; // Boolean | Get Pkgs w\\o updating Datetimes(true|false)
    Boolean runAllInventories = true; // Boolean | Force return inventories. Defaults to false.
    try {
      UpdateSystemModelsCheckinResult result = apiInstance.updateSystemGetCheckin(clientID, preview, runAllInventories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UpdateSystemApi#updateSystemGetCheckin");
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
| **clientID** | **String**| The Client ID to check-in.  If this is a new client ID it will be added to Clients. | |
| **preview** | **Boolean**| Get Pkgs w\\o updating Datetimes(true|false) | |
| **runAllInventories** | **Boolean**| Force return inventories. Defaults to false. | [optional] |

### Return type

[**UpdateSystemModelsCheckinResult**](UpdateSystemModelsCheckinResult.md)

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

