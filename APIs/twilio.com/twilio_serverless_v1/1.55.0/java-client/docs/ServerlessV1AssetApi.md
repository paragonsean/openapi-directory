# ServerlessV1AssetApi

All URIs are relative to *https://serverless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAsset**](ServerlessV1AssetApi.md#createAsset) | **POST** /v1/Services/{ServiceSid}/Assets |  |
| [**deleteAsset**](ServerlessV1AssetApi.md#deleteAsset) | **DELETE** /v1/Services/{ServiceSid}/Assets/{Sid} |  |
| [**fetchAsset**](ServerlessV1AssetApi.md#fetchAsset) | **GET** /v1/Services/{ServiceSid}/Assets/{Sid} |  |
| [**listAsset**](ServerlessV1AssetApi.md#listAsset) | **GET** /v1/Services/{ServiceSid}/Assets |  |
| [**updateAsset**](ServerlessV1AssetApi.md#updateAsset) | **POST** /v1/Services/{ServiceSid}/Assets/{Sid} |  |


<a id="createAsset"></a>
# **createAsset**
> ServerlessV1ServiceAsset createAsset(serviceSid, friendlyName)



Create a new Asset resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1AssetApi apiInstance = new ServerlessV1AssetApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Asset resource under.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.
    try {
      ServerlessV1ServiceAsset result = apiInstance.createAsset(serviceSid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1AssetApi#createAsset");
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
| **serviceSid** | **String**| The SID of the Service to create the Asset resource under. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters. | |

### Return type

[**ServerlessV1ServiceAsset**](ServerlessV1ServiceAsset.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteAsset"></a>
# **deleteAsset**
> deleteAsset(serviceSid, sid)



Delete an Asset resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1AssetApi apiInstance = new ServerlessV1AssetApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to delete the Asset resource from.
    String sid = "sid_example"; // String | The SID that identifies the Asset resource to delete.
    try {
      apiInstance.deleteAsset(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1AssetApi#deleteAsset");
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
| **serviceSid** | **String**| The SID of the Service to delete the Asset resource from. | |
| **sid** | **String**| The SID that identifies the Asset resource to delete. | |

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

<a id="fetchAsset"></a>
# **fetchAsset**
> ServerlessV1ServiceAsset fetchAsset(serviceSid, sid)



Retrieve a specific Asset resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1AssetApi apiInstance = new ServerlessV1AssetApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Asset resource from.
    String sid = "sid_example"; // String | The SID that identifies the Asset resource to fetch.
    try {
      ServerlessV1ServiceAsset result = apiInstance.fetchAsset(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1AssetApi#fetchAsset");
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
| **serviceSid** | **String**| The SID of the Service to fetch the Asset resource from. | |
| **sid** | **String**| The SID that identifies the Asset resource to fetch. | |

### Return type

[**ServerlessV1ServiceAsset**](ServerlessV1ServiceAsset.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAsset"></a>
# **listAsset**
> ListAssetResponse listAsset(serviceSid, pageSize, page, pageToken)



Retrieve a list of all Assets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1AssetApi apiInstance = new ServerlessV1AssetApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Asset resources from.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListAssetResponse result = apiInstance.listAsset(serviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1AssetApi#listAsset");
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
| **serviceSid** | **String**| The SID of the Service to read the Asset resources from. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListAssetResponse**](ListAssetResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateAsset"></a>
# **updateAsset**
> ServerlessV1ServiceAsset updateAsset(serviceSid, sid, friendlyName)



Update a specific Asset resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerlessV1AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://serverless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ServerlessV1AssetApi apiInstance = new ServerlessV1AssetApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the Service to update the Asset resource from.
    String sid = "sid_example"; // String | The SID that identifies the Asset resource to update.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters.
    try {
      ServerlessV1ServiceAsset result = apiInstance.updateAsset(serviceSid, sid, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerlessV1AssetApi#updateAsset");
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
| **serviceSid** | **String**| The SID of the Service to update the Asset resource from. | |
| **sid** | **String**| The SID that identifies the Asset resource to update. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the Asset resource. It can be a maximum of 255 characters. | |

### Return type

[**ServerlessV1ServiceAsset**](ServerlessV1ServiceAsset.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

