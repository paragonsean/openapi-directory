# DevicesApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**devicesCreateInstance**](DevicesApi.md#devicesCreateInstance) | **POST** /v1/devices |  |
| [**devicesGetCollection**](DevicesApi.md#devicesGetCollection) | **GET** /v1/devices |  |
| [**devicesGetInstance**](DevicesApi.md#devicesGetInstance) | **GET** /v1/devices/{id} |  |
| [**devicesUpdateInstance**](DevicesApi.md#devicesUpdateInstance) | **PATCH** /v1/devices/{id} |  |


<a id="devicesCreateInstance"></a>
# **devicesCreateInstance**
> DeviceResponse devicesCreateInstance(deviceCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    DeviceCreateRequest deviceCreateRequest = new DeviceCreateRequest(); // DeviceCreateRequest | Device representation
    try {
      DeviceResponse result = apiInstance.devicesCreateInstance(deviceCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesCreateInstance");
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
| **deviceCreateRequest** | [**DeviceCreateRequest**](DeviceCreateRequest.md)| Device representation | |

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single Device |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="devicesGetCollection"></a>
# **devicesGetCollection**
> DevicesResponse devicesGetCollection(filterName, filterPlatform, filterStatus, filterUdid, filterId, sort, fieldsDevices, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    List<String> filterName = Arrays.asList(); // List<String> | filter by attribute 'name'
    List<String> filterPlatform = Arrays.asList(); // List<String> | filter by attribute 'platform'
    List<String> filterStatus = Arrays.asList(); // List<String> | filter by attribute 'status'
    List<String> filterUdid = Arrays.asList(); // List<String> | filter by attribute 'udid'
    List<String> filterId = Arrays.asList(); // List<String> | filter by id(s)
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsDevices = Arrays.asList(); // List<String> | the fields to include for returned resources of type devices
    Integer limit = 56; // Integer | maximum resources per page
    try {
      DevicesResponse result = apiInstance.devicesGetCollection(filterName, filterPlatform, filterStatus, filterUdid, filterId, sort, fieldsDevices, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesGetCollection");
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
| **filterName** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;name&#39; | [optional] |
| **filterPlatform** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;platform&#39; | [optional] [enum: IOS, MAC_OS] |
| **filterStatus** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;status&#39; | [optional] [enum: ENABLED, DISABLED] |
| **filterUdid** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;udid&#39; | [optional] |
| **filterId** | [**List&lt;String&gt;**](String.md)| filter by id(s) | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: id, -id, name, -name, platform, -platform, status, -status, udid, -udid] |
| **fieldsDevices** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type devices | [optional] [enum: addedDate, deviceClass, model, name, platform, status, udid] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**DevicesResponse**](DevicesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Devices |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="devicesGetInstance"></a>
# **devicesGetInstance**
> DeviceResponse devicesGetInstance(id, fieldsDevices)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsDevices = Arrays.asList(); // List<String> | the fields to include for returned resources of type devices
    try {
      DeviceResponse result = apiInstance.devicesGetInstance(id, fieldsDevices);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesGetInstance");
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
| **id** | **String**| the id of the requested resource | |
| **fieldsDevices** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type devices | [optional] [enum: addedDate, deviceClass, model, name, platform, status, udid] |

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single Device |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="devicesUpdateInstance"></a>
# **devicesUpdateInstance**
> DeviceResponse devicesUpdateInstance(id, deviceUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    DeviceUpdateRequest deviceUpdateRequest = new DeviceUpdateRequest(); // DeviceUpdateRequest | Device representation
    try {
      DeviceResponse result = apiInstance.devicesUpdateInstance(id, deviceUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#devicesUpdateInstance");
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
| **id** | **String**| the id of the requested resource | |
| **deviceUpdateRequest** | [**DeviceUpdateRequest**](DeviceUpdateRequest.md)| Device representation | |

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single Device |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

