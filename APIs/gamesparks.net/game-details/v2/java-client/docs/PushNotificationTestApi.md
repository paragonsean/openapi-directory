# PushNotificationTestApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**testPushAmazonNotificationsUsingPOST**](PushNotificationTestApi.md#testPushAmazonNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/amazon | testPushAmazonNotifications |
| [**testPushAppleDevNotificationsUsingPOST**](PushNotificationTestApi.md#testPushAppleDevNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/apple/development | testPushAppleDevNotifications |
| [**testPushAppleProdNotificationsUsingPOST**](PushNotificationTestApi.md#testPushAppleProdNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/apple/production | testPushAppleProdNotifications |
| [**testPushGoogleNotificationsUsingPOST**](PushNotificationTestApi.md#testPushGoogleNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/google | testPushGoogleNotifications |
| [**testViberIntegrationNotificationsUsingPOST**](PushNotificationTestApi.md#testViberIntegrationNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/viber/integration | testViberIntegrationNotifications |
| [**testViberProductionNotificationsUsingPOST**](PushNotificationTestApi.md#testViberProductionNotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/viber/production | testViberProductionNotifications |
| [**testWindows8NotificationsUsingPOST**](PushNotificationTestApi.md#testWindows8NotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/microsoft/windows8 | testWindows8Notifications |
| [**testWindowsPhone8NotificationsUsingPOST**](PushNotificationTestApi.md#testWindowsPhone8NotificationsUsingPOST) | **POST** /restv2/game/{apiKey}/admin/pushNotifications/test/microsoft/windowsPhone8 | testWindowsPhone8Notifications |


<a id="testPushAmazonNotificationsUsingPOST"></a>
# **testPushAmazonNotificationsUsingPOST**
> PushNotificationTestSummaryListModel testPushAmazonNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testPushAmazonNotifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushNotificationTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    PushNotificationTestApi apiInstance = new PushNotificationTestApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    PushNotificationTestModel pushNotificationTestModel = new PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
    try {
      PushNotificationTestSummaryListModel result = apiInstance.testPushAmazonNotificationsUsingPOST(apiKey, pushNotificationTestModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushNotificationTestApi#testPushAmazonNotificationsUsingPOST");
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
| **apiKey** | **String**| apiKey | |
| **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | |

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="testPushAppleDevNotificationsUsingPOST"></a>
# **testPushAppleDevNotificationsUsingPOST**
> PushNotificationTestSummaryListModel testPushAppleDevNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testPushAppleDevNotifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushNotificationTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    PushNotificationTestApi apiInstance = new PushNotificationTestApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    PushNotificationTestModel pushNotificationTestModel = new PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
    try {
      PushNotificationTestSummaryListModel result = apiInstance.testPushAppleDevNotificationsUsingPOST(apiKey, pushNotificationTestModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushNotificationTestApi#testPushAppleDevNotificationsUsingPOST");
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
| **apiKey** | **String**| apiKey | |
| **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | |

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="testPushAppleProdNotificationsUsingPOST"></a>
# **testPushAppleProdNotificationsUsingPOST**
> PushNotificationTestSummaryListModel testPushAppleProdNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testPushAppleProdNotifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushNotificationTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    PushNotificationTestApi apiInstance = new PushNotificationTestApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    PushNotificationTestModel pushNotificationTestModel = new PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
    try {
      PushNotificationTestSummaryListModel result = apiInstance.testPushAppleProdNotificationsUsingPOST(apiKey, pushNotificationTestModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushNotificationTestApi#testPushAppleProdNotificationsUsingPOST");
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
| **apiKey** | **String**| apiKey | |
| **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | |

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="testPushGoogleNotificationsUsingPOST"></a>
# **testPushGoogleNotificationsUsingPOST**
> PushNotificationTestSummaryListModel testPushGoogleNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testPushGoogleNotifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushNotificationTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    PushNotificationTestApi apiInstance = new PushNotificationTestApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    PushNotificationTestModel pushNotificationTestModel = new PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
    try {
      PushNotificationTestSummaryListModel result = apiInstance.testPushGoogleNotificationsUsingPOST(apiKey, pushNotificationTestModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushNotificationTestApi#testPushGoogleNotificationsUsingPOST");
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
| **apiKey** | **String**| apiKey | |
| **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | |

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="testViberIntegrationNotificationsUsingPOST"></a>
# **testViberIntegrationNotificationsUsingPOST**
> PushNotificationTestSummaryListModel testViberIntegrationNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testViberIntegrationNotifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushNotificationTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    PushNotificationTestApi apiInstance = new PushNotificationTestApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    PushNotificationTestModel pushNotificationTestModel = new PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
    try {
      PushNotificationTestSummaryListModel result = apiInstance.testViberIntegrationNotificationsUsingPOST(apiKey, pushNotificationTestModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushNotificationTestApi#testViberIntegrationNotificationsUsingPOST");
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
| **apiKey** | **String**| apiKey | |
| **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | |

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="testViberProductionNotificationsUsingPOST"></a>
# **testViberProductionNotificationsUsingPOST**
> PushNotificationTestSummaryListModel testViberProductionNotificationsUsingPOST(apiKey, pushNotificationTestModel)

testViberProductionNotifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushNotificationTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    PushNotificationTestApi apiInstance = new PushNotificationTestApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    PushNotificationTestModel pushNotificationTestModel = new PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
    try {
      PushNotificationTestSummaryListModel result = apiInstance.testViberProductionNotificationsUsingPOST(apiKey, pushNotificationTestModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushNotificationTestApi#testViberProductionNotificationsUsingPOST");
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
| **apiKey** | **String**| apiKey | |
| **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | |

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="testWindows8NotificationsUsingPOST"></a>
# **testWindows8NotificationsUsingPOST**
> PushNotificationTestSummaryListModel testWindows8NotificationsUsingPOST(apiKey, pushNotificationTestModel)

testWindows8Notifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushNotificationTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    PushNotificationTestApi apiInstance = new PushNotificationTestApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    PushNotificationTestModel pushNotificationTestModel = new PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
    try {
      PushNotificationTestSummaryListModel result = apiInstance.testWindows8NotificationsUsingPOST(apiKey, pushNotificationTestModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushNotificationTestApi#testWindows8NotificationsUsingPOST");
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
| **apiKey** | **String**| apiKey | |
| **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | |

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="testWindowsPhone8NotificationsUsingPOST"></a>
# **testWindowsPhone8NotificationsUsingPOST**
> PushNotificationTestSummaryListModel testWindowsPhone8NotificationsUsingPOST(apiKey, pushNotificationTestModel)

testWindowsPhone8Notifications

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushNotificationTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    PushNotificationTestApi apiInstance = new PushNotificationTestApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    PushNotificationTestModel pushNotificationTestModel = new PushNotificationTestModel(); // PushNotificationTestModel | messageDetails
    try {
      PushNotificationTestSummaryListModel result = apiInstance.testWindowsPhone8NotificationsUsingPOST(apiKey, pushNotificationTestModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushNotificationTestApi#testWindowsPhone8NotificationsUsingPOST");
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
| **apiKey** | **String**| apiKey | |
| **pushNotificationTestModel** | [**PushNotificationTestModel**](PushNotificationTestModel.md)| messageDetails | |

### Return type

[**PushNotificationTestSummaryListModel**](PushNotificationTestSummaryListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

