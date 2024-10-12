# DeviceApi

All URIs are relative to *https://ioe2api.ijenko.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deviceAddFunctionality**](DeviceApi.md#deviceAddFunctionality) | **POST** /devices/{deviceId}/functionalities | Add dynamically a functionality |
| [**deviceGetMetadata**](DeviceApi.md#deviceGetMetadata) | **GET** /devices/{deviceId}/metadata | List metadata |
| [**deviceGetTags**](DeviceApi.md#deviceGetTags) | **GET** /devices/{deviceId}/tags | List tags |
| [**devicePatchMetadata**](DeviceApi.md#devicePatchMetadata) | **PATCH** /devices/{deviceId}/metadata | Modify metadata |
| [**devicePatchTags**](DeviceApi.md#devicePatchTags) | **PATCH** /devices/{deviceId}/tags | Modify tags |
| [**devicesGet**](DeviceApi.md#devicesGet) | **GET** /devices/{deviceId} | Information about a Device |
| [**devicesPatch**](DeviceApi.md#devicesPatch) | **PATCH** /devices/{deviceId} | Update a Device |
| [**placeDevices**](DeviceApi.md#placeDevices) | **GET** /places/{placeId}/devices | List of Devices |


<a id="deviceAddFunctionality"></a>
# **deviceAddFunctionality**
> FunctionalityCreated deviceAddFunctionality(deviceId, functionalityInfo)

Add dynamically a functionality

Add a *Functionality* to the device.  Required parameters are : - functionality class - endpoint  Each device class has its own restrictions on which Functionality classes can be added and on which endpoints. Only a few devices allow to add Functionalities.  |Device class|Functionality class|Endpoints| |------------|-------------------|---------| |MINT        |CurrentPeriod      |1,2,3    | |MINT        |ElectricityRates   |1,2,3    | |MINT        |GenericRate        |1,2,3    |  **Note**: requires full access to the *Account*. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    DeviceApi apiInstance = new DeviceApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique identifier of a *Device*.
    FunctionalityNew functionalityInfo = new FunctionalityNew(); // FunctionalityNew | 
    try {
      FunctionalityCreated result = apiInstance.deviceAddFunctionality(deviceId, functionalityInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceApi#deviceAddFunctionality");
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
| **deviceId** | **String**| Unique identifier of a *Device*. | |
| **functionalityInfo** | [**FunctionalityNew**](FunctionalityNew.md)|  | |

### Return type

[**FunctionalityCreated**](FunctionalityCreated.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | *Functionality* successfully created. |  * Location - Path of the Program created (&#x60;/programs/{id}&#x60;) <br>  |
| **403** | *Device* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="deviceGetMetadata"></a>
# **deviceGetMetadata**
> Map&lt;String, Object&gt; deviceGetMetadata(deviceId)

List metadata

Get the metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    DeviceApi apiInstance = new DeviceApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique identifier of a *Device*.
    try {
      Map<String, Object> result = apiInstance.deviceGetMetadata(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceApi#deviceGetMetadata");
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
| **deviceId** | **String**| Unique identifier of a *Device*. | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

<a id="deviceGetTags"></a>
# **deviceGetTags**
> Set&lt;String&gt; deviceGetTags(deviceId)

List tags

Get the tags of a *Device*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    DeviceApi apiInstance = new DeviceApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique identifier of a *Device*.
    try {
      Set<String> result = apiInstance.deviceGetTags(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceApi#deviceGetTags");
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
| **deviceId** | **String**| Unique identifier of a *Device*. | |

### Return type

**Set&lt;String&gt;**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

<a id="devicePatchMetadata"></a>
# **devicePatchMetadata**
> Map&lt;String, Object&gt; devicePatchMetadata(deviceId, metadataPatch)

Modify metadata

Modify the metadata. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    DeviceApi apiInstance = new DeviceApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique identifier of a *Device*.
    MetadataPatch metadataPatch = new MetadataPatch(); // MetadataPatch | Modifications to apply to the metadata of the resource. 
    try {
      Map<String, Object> result = apiInstance.devicePatchMetadata(deviceId, metadataPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceApi#devicePatchMetadata");
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
| **deviceId** | **String**| Unique identifier of a *Device*. | |
| **metadataPatch** | [**MetadataPatch**](MetadataPatch.md)| Modifications to apply to the metadata of the resource.  | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. The new metadata is returned. |  -  |
| **304** | Successful, but nothing changed. |  -  |
| **403** | *Device* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="devicePatchTags"></a>
# **devicePatchTags**
> Set&lt;String&gt; devicePatchTags(deviceId, tagsPatch)

Modify tags

Modify the tags of a *Device*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    DeviceApi apiInstance = new DeviceApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique identifier of a *Device*.
    TagsPatch tagsPatch = new TagsPatch(); // TagsPatch | Modifications to apply to the tags list of the resource. 
    try {
      Set<String> result = apiInstance.devicePatchTags(deviceId, tagsPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceApi#devicePatchTags");
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
| **deviceId** | **String**| Unique identifier of a *Device*. | |
| **tagsPatch** | [**TagsPatch**](TagsPatch.md)| Modifications to apply to the tags list of the resource.  | |

### Return type

**Set&lt;String&gt;**

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. The new list of tags is returned. |  -  |
| **304** | Successful, but nothing changed. |  -  |
| **403** | *Device* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="devicesGet"></a>
# **devicesGet**
> Device devicesGet(deviceId)

Information about a Device

Get information about a *Device*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    DeviceApi apiInstance = new DeviceApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique identifier of a *Device*.
    try {
      Device result = apiInstance.devicesGet(deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceApi#devicesGet");
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
| **deviceId** | **String**| Unique identifier of a *Device*. | |

### Return type

[**Device**](Device.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

<a id="devicesPatch"></a>
# **devicesPatch**
> devicesPatch(deviceId, devicePatch)

Update a Device

Modify information about a *Device*: its name. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    DeviceApi apiInstance = new DeviceApi(defaultClient);
    String deviceId = "deviceId_example"; // String | Unique identifier of a *Device*.
    DevicePatch devicePatch = new DevicePatch(); // DevicePatch | 
    try {
      apiInstance.devicesPatch(deviceId, devicePatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceApi#devicesPatch");
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
| **deviceId** | **String**| Unique identifier of a *Device*. | |
| **devicePatch** | [**DevicePatch**](DevicePatch.md)|  | |

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Modification successful. |  -  |
| **304** | Successful, but nothing changed. |  -  |
| **403** | *Device* doesn&#39;t exist or the requester doesn&#39;t have appropriate access to the *Place*.  |  -  |
| **0** | Other error. |  -  |

<a id="placeDevices"></a>
# **placeDevices**
> Set&lt;DeviceItem&gt; placeDevices(placeId, devices, embedMetadata)

List of Devices

Get the list of *Devices* available in this *Place*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeviceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    DeviceApi apiInstance = new DeviceApi(defaultClient);
    String placeId = "placeId_example"; // String | Unique identifier of a *Place*.
    String devices = "devices_example"; // String | Devices selector. Device tags or device classes or device ids or '*' for any. Multiple values are separated by '|' and interpreted as « OR ».
    List<String> embedMetadata = Arrays.asList(); // List<String> | Request to include the given keys of metadata in the response. If a key doesn't exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
    try {
      Set<DeviceItem> result = apiInstance.placeDevices(placeId, devices, embedMetadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeviceApi#placeDevices");
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
| **placeId** | **String**| Unique identifier of a *Place*. | |
| **devices** | **String**| Devices selector. Device tags or device classes or device ids or &#39;*&#39; for any. Multiple values are separated by &#39;|&#39; and interpreted as « OR ». | [optional] |
| **embedMetadata** | [**List&lt;String&gt;**](String.md)| Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources.  | [optional] |

### Return type

[**Set&lt;DeviceItem&gt;**](DeviceItem.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful. |  -  |
| **0** | Other error. |  -  |

