# NotificationChannelsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**notificationChannelsCreateOrUpdate**](NotificationChannelsApi.md#notificationChannelsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/notificationchannels/{name} |  |
| [**notificationChannelsDelete**](NotificationChannelsApi.md#notificationChannelsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/notificationchannels/{name} |  |
| [**notificationChannelsGet**](NotificationChannelsApi.md#notificationChannelsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/notificationchannels/{name} |  |
| [**notificationChannelsList**](NotificationChannelsApi.md#notificationChannelsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/notificationchannels |  |
| [**notificationChannelsNotify**](NotificationChannelsApi.md#notificationChannelsNotify) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/notificationchannels/{name}/notify |  |
| [**notificationChannelsUpdate**](NotificationChannelsApi.md#notificationChannelsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/notificationchannels/{name} |  |


<a id="notificationChannelsCreateOrUpdate"></a>
# **notificationChannelsCreateOrUpdate**
> NotificationChannel notificationChannelsCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, notificationChannel)



Create or replace an existing notificationChannel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationChannelsApi apiInstance = new NotificationChannelsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the notificationChannel.
    String apiVersion = "2016-05-15"; // String | Client API version.
    NotificationChannel notificationChannel = new NotificationChannel(); // NotificationChannel | A notification.
    try {
      NotificationChannel result = apiInstance.notificationChannelsCreateOrUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, notificationChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationChannelsApi#notificationChannelsCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the notificationChannel. | |
| **apiVersion** | **String**| Client API version. | [default to 2016-05-15] |
| **notificationChannel** | [**NotificationChannel**](NotificationChannel.md)| A notification. | |

### Return type

[**NotificationChannel**](NotificationChannel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | BadRequest |  -  |

<a id="notificationChannelsDelete"></a>
# **notificationChannelsDelete**
> notificationChannelsDelete(subscriptionId, resourceGroupName, labName, name, apiVersion)



Delete notification channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationChannelsApi apiInstance = new NotificationChannelsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the notificationChannel.
    String apiVersion = "2016-05-15"; // String | Client API version.
    try {
      apiInstance.notificationChannelsDelete(subscriptionId, resourceGroupName, labName, name, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationChannelsApi#notificationChannelsDelete");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the notificationChannel. | |
| **apiVersion** | **String**| Client API version. | [default to 2016-05-15] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **0** | BadRequest |  -  |

<a id="notificationChannelsGet"></a>
# **notificationChannelsGet**
> NotificationChannel notificationChannelsGet(subscriptionId, resourceGroupName, labName, name, apiVersion, $expand)



Get notification channels.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationChannelsApi apiInstance = new NotificationChannelsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the notificationChannel.
    String apiVersion = "2016-05-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=webHookUrl)'
    try {
      NotificationChannel result = apiInstance.notificationChannelsGet(subscriptionId, resourceGroupName, labName, name, apiVersion, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationChannelsApi#notificationChannelsGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the notificationChannel. | |
| **apiVersion** | **String**| Client API version. | [default to 2016-05-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;webHookUrl)&#39; | [optional] |

### Return type

[**NotificationChannel**](NotificationChannel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="notificationChannelsList"></a>
# **notificationChannelsList**
> ResponseWithContinuationNotificationChannel notificationChannelsList(subscriptionId, resourceGroupName, labName, apiVersion, $expand, $filter, $top, $orderby)



List notification channels in a given lab.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationChannelsApi apiInstance = new NotificationChannelsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String apiVersion = "2016-05-15"; // String | Client API version.
    String $expand = "$expand_example"; // String | Specify the $expand query. Example: 'properties($select=webHookUrl)'
    String $filter = "$filter_example"; // String | The filter to apply to the operation.
    Integer $top = 56; // Integer | The maximum number of resources to return from the operation.
    String $orderby = "$orderby_example"; // String | The ordering expression for the results, using OData notation.
    try {
      ResponseWithContinuationNotificationChannel result = apiInstance.notificationChannelsList(subscriptionId, resourceGroupName, labName, apiVersion, $expand, $filter, $top, $orderby);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationChannelsApi#notificationChannelsList");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **apiVersion** | **String**| Client API version. | [default to 2016-05-15] |
| **$expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;webHookUrl)&#39; | [optional] |
| **$filter** | **String**| The filter to apply to the operation. | [optional] |
| **$top** | **Integer**| The maximum number of resources to return from the operation. | [optional] |
| **$orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] |

### Return type

[**ResponseWithContinuationNotificationChannel**](ResponseWithContinuationNotificationChannel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="notificationChannelsNotify"></a>
# **notificationChannelsNotify**
> notificationChannelsNotify(subscriptionId, resourceGroupName, labName, name, apiVersion, notifyParameters)



Send notification to provided channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationChannelsApi apiInstance = new NotificationChannelsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the notificationChannel.
    String apiVersion = "2016-05-15"; // String | Client API version.
    NotifyParameters notifyParameters = new NotifyParameters(); // NotifyParameters | Properties for generating a Notification.
    try {
      apiInstance.notificationChannelsNotify(subscriptionId, resourceGroupName, labName, name, apiVersion, notifyParameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationChannelsApi#notificationChannelsNotify");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the notificationChannel. | |
| **apiVersion** | **String**| Client API version. | [default to 2016-05-15] |
| **notifyParameters** | [**NotifyParameters**](NotifyParameters.md)| Properties for generating a Notification. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

<a id="notificationChannelsUpdate"></a>
# **notificationChannelsUpdate**
> NotificationChannel notificationChannelsUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, notificationChannel)



Modify properties of notification channels.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotificationChannelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    NotificationChannelsApi apiInstance = new NotificationChannelsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the notificationChannel.
    String apiVersion = "2016-05-15"; // String | Client API version.
    NotificationChannelFragment notificationChannel = new NotificationChannelFragment(); // NotificationChannelFragment | A notification.
    try {
      NotificationChannel result = apiInstance.notificationChannelsUpdate(subscriptionId, resourceGroupName, labName, name, apiVersion, notificationChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotificationChannelsApi#notificationChannelsUpdate");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the notificationChannel. | |
| **apiVersion** | **String**| Client API version. | [default to 2016-05-15] |
| **notificationChannel** | [**NotificationChannelFragment**](NotificationChannelFragment.md)| A notification. | |

### Return type

[**NotificationChannel**](NotificationChannel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

