# DefaultApi

All URIs are relative to *https://api.nexmo.com/v1/applications*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApplication**](DefaultApi.md#createApplication) | **POST** / | Create Application |
| [**deleteApplication**](DefaultApi.md#deleteApplication) | **DELETE** /{app_id} | Destroy Application |
| [**retrieveApplication**](DefaultApi.md#retrieveApplication) | **GET** /{app_id} | Retrieve Application |
| [**retrieveApplications**](DefaultApi.md#retrieveApplications) | **GET** / | Retrieve all Applications |
| [**updateApplication**](DefaultApi.md#updateApplication) | **PUT** /{app_id} | Update Application |


<a id="createApplication"></a>
# **createApplication**
> ApplicationCreated createApplication(createApplicationRequest)

Create Application

You use a &#x60;POST&#x60; request to create a new application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/applications");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateApplicationRequest createApplicationRequest = new CreateApplicationRequest(); // CreateApplicationRequest | 
    try {
      ApplicationCreated result = apiInstance.createApplication(createApplicationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createApplication");
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
| **createApplicationRequest** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | [optional] |

### Return type

[**ApplicationCreated**](ApplicationCreated.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteApplication"></a>
# **deleteApplication**
> deleteApplication(appId)

Destroy Application

You use a &#x60;DELETE&#x60; request to delete a single application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/applications");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | The ID allocated to your application by Nexmo.
    try {
      apiInstance.deleteApplication(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteApplication");
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
| **appId** | **String**| The ID allocated to your application by Nexmo. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |

<a id="retrieveApplication"></a>
# **retrieveApplication**
> Application retrieveApplication(apiKey, apiSecret, appId)

Retrieve Application

You use a &#x60;GET&#x60; request to retrieve details about a single application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/applications");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiKey = "apiKey_example"; // String | You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview)
    String apiSecret = "apiSecret_example"; // String | You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview)
    String appId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | The ID allocated to your application by Nexmo.
    try {
      Application result = apiInstance.retrieveApplication(apiKey, apiSecret, appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveApplication");
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
| **apiKey** | **String**| You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview) | |
| **apiSecret** | **String**| You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview) | |
| **appId** | **String**| The ID allocated to your application by Nexmo. | |

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="retrieveApplications"></a>
# **retrieveApplications**
> Applications retrieveApplications(apiKey, apiSecret, pageSize, pageIndex)

Retrieve all Applications

You use a &#x60;GET&#x60; request to retrieve details of all applications associated with your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/applications");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiKey = "apiKey_example"; // String | You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview)
    String apiSecret = "apiSecret_example"; // String | You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview)
    Integer pageSize = 10; // Integer | Set the number of items returned on each call to this endpoint. The default is 10 records.
    Integer pageIndex = 0; // Integer | Set the offset from the first page. The default value is `0`.
    try {
      Applications result = apiInstance.retrieveApplications(apiKey, apiSecret, pageSize, pageIndex);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#retrieveApplications");
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
| **apiKey** | **String**| You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview) | |
| **apiSecret** | **String**| You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview) | |
| **pageSize** | **Integer**| Set the number of items returned on each call to this endpoint. The default is 10 records. | [optional] [default to 10] |
| **pageIndex** | **Integer**| Set the offset from the first page. The default value is &#x60;0&#x60;. | [optional] [default to 0] |

### Return type

[**Applications**](Applications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateApplication"></a>
# **updateApplication**
> Application updateApplication(appId, updateApplicationRequest)

Update Application

You use a &#x60;PUT&#x60; request to update an existing application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/v1/applications");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | The ID allocated to your application by Nexmo.
    UpdateApplicationRequest updateApplicationRequest = new UpdateApplicationRequest(); // UpdateApplicationRequest | 
    try {
      Application result = apiInstance.updateApplication(appId, updateApplicationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateApplication");
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
| **appId** | **String**| The ID allocated to your application by Nexmo. | |
| **updateApplicationRequest** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | [optional] |

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

