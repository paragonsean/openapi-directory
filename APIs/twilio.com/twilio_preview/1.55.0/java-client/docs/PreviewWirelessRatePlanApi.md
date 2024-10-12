# PreviewWirelessRatePlanApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWirelessRatePlan**](PreviewWirelessRatePlanApi.md#createWirelessRatePlan) | **POST** /wireless/RatePlans |  |
| [**deleteWirelessRatePlan**](PreviewWirelessRatePlanApi.md#deleteWirelessRatePlan) | **DELETE** /wireless/RatePlans/{Sid} |  |
| [**fetchWirelessRatePlan**](PreviewWirelessRatePlanApi.md#fetchWirelessRatePlan) | **GET** /wireless/RatePlans/{Sid} |  |
| [**listWirelessRatePlan**](PreviewWirelessRatePlanApi.md#listWirelessRatePlan) | **GET** /wireless/RatePlans |  |
| [**updateWirelessRatePlan**](PreviewWirelessRatePlanApi.md#updateWirelessRatePlan) | **POST** /wireless/RatePlans/{Sid} |  |


<a id="createWirelessRatePlan"></a>
# **createWirelessRatePlan**
> PreviewWirelessRatePlan createWirelessRatePlan(commandsEnabled, dataEnabled, dataLimit, dataMetering, friendlyName, internationalRoaming, messagingEnabled, nationalRoamingEnabled, uniqueName, voiceEnabled)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessRatePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessRatePlanApi apiInstance = new PreviewWirelessRatePlanApi(defaultClient);
    Boolean commandsEnabled = true; // Boolean | 
    Boolean dataEnabled = true; // Boolean | 
    Integer dataLimit = 56; // Integer | 
    String dataMetering = "dataMetering_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    List<String> internationalRoaming = Arrays.asList(); // List<String> | 
    Boolean messagingEnabled = true; // Boolean | 
    Boolean nationalRoamingEnabled = true; // Boolean | 
    String uniqueName = "uniqueName_example"; // String | 
    Boolean voiceEnabled = true; // Boolean | 
    try {
      PreviewWirelessRatePlan result = apiInstance.createWirelessRatePlan(commandsEnabled, dataEnabled, dataLimit, dataMetering, friendlyName, internationalRoaming, messagingEnabled, nationalRoamingEnabled, uniqueName, voiceEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessRatePlanApi#createWirelessRatePlan");
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
| **commandsEnabled** | **Boolean**|  | [optional] |
| **dataEnabled** | **Boolean**|  | [optional] |
| **dataLimit** | **Integer**|  | [optional] |
| **dataMetering** | **String**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **internationalRoaming** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **messagingEnabled** | **Boolean**|  | [optional] |
| **nationalRoamingEnabled** | **Boolean**|  | [optional] |
| **uniqueName** | **String**|  | [optional] |
| **voiceEnabled** | **Boolean**|  | [optional] |

### Return type

[**PreviewWirelessRatePlan**](PreviewWirelessRatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteWirelessRatePlan"></a>
# **deleteWirelessRatePlan**
> deleteWirelessRatePlan(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessRatePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessRatePlanApi apiInstance = new PreviewWirelessRatePlanApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      apiInstance.deleteWirelessRatePlan(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessRatePlanApi#deleteWirelessRatePlan");
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
| **sid** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchWirelessRatePlan"></a>
# **fetchWirelessRatePlan**
> PreviewWirelessRatePlan fetchWirelessRatePlan(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessRatePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessRatePlanApi apiInstance = new PreviewWirelessRatePlanApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      PreviewWirelessRatePlan result = apiInstance.fetchWirelessRatePlan(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessRatePlanApi#fetchWirelessRatePlan");
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
| **sid** | **String**|  | |

### Return type

[**PreviewWirelessRatePlan**](PreviewWirelessRatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listWirelessRatePlan"></a>
# **listWirelessRatePlan**
> ListWirelessRatePlanResponse listWirelessRatePlan(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessRatePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessRatePlanApi apiInstance = new PreviewWirelessRatePlanApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListWirelessRatePlanResponse result = apiInstance.listWirelessRatePlan(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessRatePlanApi#listWirelessRatePlan");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListWirelessRatePlanResponse**](ListWirelessRatePlanResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateWirelessRatePlan"></a>
# **updateWirelessRatePlan**
> PreviewWirelessRatePlan updateWirelessRatePlan(sid, friendlyName, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewWirelessRatePlanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewWirelessRatePlanApi apiInstance = new PreviewWirelessRatePlanApi(defaultClient);
    String sid = "sid_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    String uniqueName = "uniqueName_example"; // String | 
    try {
      PreviewWirelessRatePlan result = apiInstance.updateWirelessRatePlan(sid, friendlyName, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewWirelessRatePlanApi#updateWirelessRatePlan");
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
| **sid** | **String**|  | |
| **friendlyName** | **String**|  | [optional] |
| **uniqueName** | **String**|  | [optional] |

### Return type

[**PreviewWirelessRatePlan**](PreviewWirelessRatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

