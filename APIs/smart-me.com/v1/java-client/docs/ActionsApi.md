# ActionsApi

All URIs are relative to *https://smart-me.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**actionsGet**](ActionsApi.md#actionsGet) | **GET** /api/Actions/{id} | Gets all available Actions of a Device |
| [**actionsPost**](ActionsApi.md#actionsPost) | **POST** /api/Actions | Set an action for the specified device. |


<a id="actionsGet"></a>
# **actionsGet**
> List&lt;ActionInformation&gt; actionsGet(id)

Gets all available Actions of a Device

Gets all available Actions of a Device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    String id = "id_example"; // String | The ID of the device
    try {
      List<ActionInformation> result = apiInstance.actionsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsGet");
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
| **id** | **String**| The ID of the device | |

### Return type

[**List&lt;ActionInformation&gt;**](ActionInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="actionsPost"></a>
# **actionsPost**
> actionsPost(actionToPost)

Set an action for the specified device.

Set an action for the specified device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://smart-me.com:443");

    ActionsApi apiInstance = new ActionsApi(defaultClient);
    ActionToPost actionToPost = new ActionToPost(); // ActionToPost | The Action Data
    try {
      apiInstance.actionsPost(actionToPost);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionsApi#actionsPost");
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
| **actionToPost** | [**ActionToPost**](ActionToPost.md)| The Action Data | |

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

