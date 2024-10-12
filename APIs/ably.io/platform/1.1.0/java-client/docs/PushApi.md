# PushApi

All URIs are relative to *https://rest.ably.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deletePushDeviceDetails**](PushApi.md#deletePushDeviceDetails) | **DELETE** /push/channelSubscriptions | Delete a registered device&#39;s update token |
| [**getChannelsWithPushSubscribers**](PushApi.md#getChannelsWithPushSubscribers) | **GET** /push/channels | List all channels with at least one subscribed device |
| [**getPushDeviceDetails**](PushApi.md#getPushDeviceDetails) | **GET** /push/deviceRegistrations/{device_id} | Get a device registration |
| [**getPushSubscriptionsOnChannels**](PushApi.md#getPushSubscriptionsOnChannels) | **GET** /push/channelSubscriptions | List channel subscriptions |
| [**getRegisteredPushDevices**](PushApi.md#getRegisteredPushDevices) | **GET** /push/deviceRegistrations | List devices registered for receiving push notifications |
| [**patchPushDeviceDetails**](PushApi.md#patchPushDeviceDetails) | **PATCH** /push/deviceRegistrations/{device_id} | Update a device registration |
| [**publishPushNotificationToDevices**](PushApi.md#publishPushNotificationToDevices) | **POST** /push/publish | Publish a push notification to device(s) |
| [**putPushDeviceDetails**](PushApi.md#putPushDeviceDetails) | **PUT** /push/deviceRegistrations/{device_id} | Update a device registration |
| [**registerPushDevice**](PushApi.md#registerPushDevice) | **POST** /push/deviceRegistrations | Register a device for receiving push notifications |
| [**subscribePushDeviceToChannel**](PushApi.md#subscribePushDeviceToChannel) | **POST** /push/channelSubscriptions | Subscribe a device to a channel |
| [**unregisterAllPushDevices**](PushApi.md#unregisterAllPushDevices) | **DELETE** /push/deviceRegistrations | Unregister matching devices for push notifications |
| [**unregisterPushDevice**](PushApi.md#unregisterPushDevice) | **DELETE** /push/deviceRegistrations/{device_id} | Unregister a single device for push notifications |
| [**updatePushDeviceDetails**](PushApi.md#updatePushDeviceDetails) | **GET** /push/deviceRegistrations/{device_id}/resetUpdateToken | Reset a registered device&#39;s update token |


<a id="deletePushDeviceDetails"></a>
# **deletePushDeviceDetails**
> deletePushDeviceDetails(xAblyVersion, format, channel, deviceId, clientId)

Delete a registered device&#39;s update token

Delete a device details object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    String channel = "channel_example"; // String | Filter to restrict to subscriptions associated with that channel.
    String deviceId = "deviceId_example"; // String | Must be set when clientId is empty, cannot be used with clientId.
    String clientId = "clientId_example"; // String | Must be set when deviceId is empty, cannot be used with deviceId.
    try {
      apiInstance.deletePushDeviceDetails(xAblyVersion, format, channel, deviceId, clientId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#deletePushDeviceDetails");
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
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **channel** | **String**| Filter to restrict to subscriptions associated with that channel. | [optional] |
| **deviceId** | **String**| Must be set when clientId is empty, cannot be used with clientId. | [optional] |
| **clientId** | **String**| Must be set when deviceId is empty, cannot be used with deviceId. | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="getChannelsWithPushSubscribers"></a>
# **getChannelsWithPushSubscribers**
> List&lt;String&gt; getChannelsWithPushSubscribers(xAblyVersion, format)

List all channels with at least one subscribed device

Returns a paginated response of channel names.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    try {
      List<String> result = apiInstance.getChannelsWithPushSubscribers(xAblyVersion, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#getChannelsWithPushSubscribers");
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
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |

### Return type

**List&lt;String&gt;**

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="getPushDeviceDetails"></a>
# **getPushDeviceDetails**
> DeviceDetails getPushDeviceDetails(deviceId, xAblyVersion, format)

Get a device registration

Get the full details of a device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Device's ID.
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    try {
      DeviceDetails result = apiInstance.getPushDeviceDetails(deviceId, xAblyVersion, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#getPushDeviceDetails");
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
| **deviceId** | **String**| Device&#39;s ID. | |
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="getPushSubscriptionsOnChannels"></a>
# **getPushSubscriptionsOnChannels**
> DeviceDetails getPushSubscriptionsOnChannels(xAblyVersion, format, channel, deviceId, clientId, limit)

List channel subscriptions

Get a list of push notification subscriptions to channels.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    String channel = "channel_example"; // String | Filter to restrict to subscriptions associated with that channel.
    String deviceId = "deviceId_example"; // String | Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId.
    String clientId = "clientId_example"; // String | Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId.
    Integer limit = 100; // Integer | The maximum number of records to return.
    try {
      DeviceDetails result = apiInstance.getPushSubscriptionsOnChannels(xAblyVersion, format, channel, deviceId, clientId, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#getPushSubscriptionsOnChannels");
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
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **channel** | **String**| Filter to restrict to subscriptions associated with that channel. | [optional] |
| **deviceId** | **String**| Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId. | [optional] |
| **clientId** | **String**| Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId. | [optional] |
| **limit** | **Integer**| The maximum number of records to return. | [optional] [default to 100] |

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="getRegisteredPushDevices"></a>
# **getRegisteredPushDevices**
> DeviceDetails getRegisteredPushDevices(xAblyVersion, format, deviceId, clientId, limit)

List devices registered for receiving push notifications

List of device details of devices registed for push notifications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    String deviceId = "deviceId_example"; // String | Optional filter to restrict to devices associated with that deviceId.
    String clientId = "clientId_example"; // String | Optional filter to restrict to devices associated with that clientId.
    Integer limit = 100; // Integer | The maximum number of records to return.
    try {
      DeviceDetails result = apiInstance.getRegisteredPushDevices(xAblyVersion, format, deviceId, clientId, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#getRegisteredPushDevices");
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
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **deviceId** | **String**| Optional filter to restrict to devices associated with that deviceId. | [optional] |
| **clientId** | **String**| Optional filter to restrict to devices associated with that clientId. | [optional] |
| **limit** | **Integer**| The maximum number of records to return. | [optional] [default to 100] |

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="patchPushDeviceDetails"></a>
# **patchPushDeviceDetails**
> DeviceDetails patchPushDeviceDetails(deviceId, xAblyVersion, format, deviceDetails)

Update a device registration

Specific attributes of an existing registration can be updated. Only clientId, metadata and push.recipient are mutable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Device's ID.
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    DeviceDetails deviceDetails = new DeviceDetails(); // DeviceDetails | 
    try {
      DeviceDetails result = apiInstance.patchPushDeviceDetails(deviceId, xAblyVersion, format, deviceDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#patchPushDeviceDetails");
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
| **deviceId** | **String**| Device&#39;s ID. | |
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **deviceDetails** | [**DeviceDetails**](DeviceDetails.md)|  | [optional] |

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-msgpack, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="publishPushNotificationToDevices"></a>
# **publishPushNotificationToDevices**
> publishPushNotificationToDevices(xAblyVersion, format, publishPushNotificationToDevicesRequest)

Publish a push notification to device(s)

A convenience endpoint to deliver a push notification payload to a single device or set of devices identified by their client identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    PublishPushNotificationToDevicesRequest publishPushNotificationToDevicesRequest = new PublishPushNotificationToDevicesRequest(); // PublishPushNotificationToDevicesRequest | 
    try {
      apiInstance.publishPushNotificationToDevices(xAblyVersion, format, publishPushNotificationToDevicesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#publishPushNotificationToDevices");
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
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **publishPushNotificationToDevicesRequest** | [**PublishPushNotificationToDevicesRequest**](PublishPushNotificationToDevicesRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-msgpack, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="putPushDeviceDetails"></a>
# **putPushDeviceDetails**
> DeviceDetails putPushDeviceDetails(deviceId, xAblyVersion, format, deviceDetails)

Update a device registration

Device registrations can be upserted (the existing registration is replaced entirely) with a PUT operation. Only clientId, metadata and push.recipient are mutable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Device's ID.
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    DeviceDetails deviceDetails = new DeviceDetails(); // DeviceDetails | 
    try {
      DeviceDetails result = apiInstance.putPushDeviceDetails(deviceId, xAblyVersion, format, deviceDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#putPushDeviceDetails");
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
| **deviceId** | **String**| Device&#39;s ID. | |
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **deviceDetails** | [**DeviceDetails**](DeviceDetails.md)|  | [optional] |

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-msgpack, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="registerPushDevice"></a>
# **registerPushDevice**
> DeviceDetails registerPushDevice(xAblyVersion, format, deviceDetails)

Register a device for receiving push notifications

Register a device’s details, including the information necessary to deliver push notifications to it. Requires \&quot;push-admin\&quot; capability.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    DeviceDetails deviceDetails = new DeviceDetails(); // DeviceDetails | 
    try {
      DeviceDetails result = apiInstance.registerPushDevice(xAblyVersion, format, deviceDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#registerPushDevice");
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
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **deviceDetails** | [**DeviceDetails**](DeviceDetails.md)|  | [optional] |

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-msgpack
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="subscribePushDeviceToChannel"></a>
# **subscribePushDeviceToChannel**
> subscribePushDeviceToChannel(xAblyVersion, format, subscribePushDeviceToChannelRequest)

Subscribe a device to a channel

Subscribe either a single device or all devices associated with a client ID to receive push notifications from messages sent to a channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    SubscribePushDeviceToChannelRequest subscribePushDeviceToChannelRequest = new SubscribePushDeviceToChannelRequest(); // SubscribePushDeviceToChannelRequest | 
    try {
      apiInstance.subscribePushDeviceToChannel(xAblyVersion, format, subscribePushDeviceToChannelRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#subscribePushDeviceToChannel");
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
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **subscribePushDeviceToChannelRequest** | [**SubscribePushDeviceToChannelRequest**](SubscribePushDeviceToChannelRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-msgpack, application/x-www-form-urlencoded
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="unregisterAllPushDevices"></a>
# **unregisterAllPushDevices**
> unregisterAllPushDevices(xAblyVersion, format, deviceId, clientId)

Unregister matching devices for push notifications

Unregisters devices. All their subscriptions for receiving push notifications through channels will also be deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    String deviceId = "deviceId_example"; // String | Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId.
    String clientId = "clientId_example"; // String | Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId.
    try {
      apiInstance.unregisterAllPushDevices(xAblyVersion, format, deviceId, clientId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#unregisterAllPushDevices");
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
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |
| **deviceId** | **String**| Optional filter to restrict to devices associated with that deviceId. Cannot be used with clientId. | [optional] |
| **clientId** | **String**| Optional filter to restrict to devices associated with that clientId. Cannot be used with deviceId. | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="unregisterPushDevice"></a>
# **unregisterPushDevice**
> unregisterPushDevice(deviceId, xAblyVersion, format)

Unregister a single device for push notifications

Unregisters a single device by its device ID. All its subscriptions for receiving push notifications through channels will also be deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Device's ID.
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    try {
      apiInstance.unregisterPushDevice(deviceId, xAblyVersion, format);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#unregisterPushDevice");
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
| **deviceId** | **String**| Device&#39;s ID. | |
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

<a id="updatePushDeviceDetails"></a>
# **updatePushDeviceDetails**
> DeviceDetails updatePushDeviceDetails(deviceId, xAblyVersion, format)

Reset a registered device&#39;s update token

Gets an updated device details object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PushApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.ably.io");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PushApi apiInstance = new PushApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Device's ID.
    String xAblyVersion = "xAblyVersion_example"; // String | The version of the API you wish to use.
    String format = "json"; // String | The response format you would like
    try {
      DeviceDetails result = apiInstance.updatePushDeviceDetails(deviceId, xAblyVersion, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PushApi#updatePushDeviceDetails");
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
| **deviceId** | **String**| Device&#39;s ID. | |
| **xAblyVersion** | **String**| The version of the API you wish to use. | [optional] |
| **format** | **String**| The response format you would like | [optional] [enum: json, jsonp, msgpack, html] |

### Return type

[**DeviceDetails**](DeviceDetails.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/x-msgpack, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | OK |  -  |
| **0** | Error |  * x-ably-errorcode -  <br>  * x-ably-errormessage -  <br>  * x-ably-serverid -  <br>  |

