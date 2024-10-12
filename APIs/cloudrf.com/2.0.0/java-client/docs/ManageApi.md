# ManageApi

All URIs are relative to *https://api.cloudrf.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addClutter**](ManageApi.md#addClutter) | **POST** /clutter/add | Upload clutter data as GeoJSON |
| [**callList**](ManageApi.md#callList) | **GET** /archive/list | List calculations from your archive |
| [**delete**](ManageApi.md#delete) | **GET** /archive/delete | Delete a calculation from the database. |
| [**deleteNetwork**](ManageApi.md#deleteNetwork) | **GET** /archive/delete/network | Delete an entire network |
| [**export**](ManageApi.md#export) | **GET** /archive/export | Export a calculation in a GIS file format |


<a id="addClutter"></a>
# **addClutter**
> addClutter(addClutterRequest)

Upload clutter data as GeoJSON

Upload GeoJSON lineString and polygon features to your account. The height property is in metres and the material code / type / attenuation are.. 1 Trees – 0.25,2Trees + 0.5,3 Timber – 1.0,4 Timber + 1.5,5 Brick –  1.5,6 Brick + 2.0,7 Concrete – 3.0,8 Concrete + 4.0,9 Metal 6.0

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloudrf.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ManageApi apiInstance = new ManageApi(defaultClient);
    AddClutterRequest addClutterRequest = new AddClutterRequest(); // AddClutterRequest | 
    try {
      apiInstance.addClutter(addClutterRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#addClutter");
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
| **addClutterRequest** | [**AddClutterRequest**](AddClutterRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request OK |  -  |

<a id="callList"></a>
# **callList**
> callList(n, e, s, w)

List calculations from your archive

List your area and path calculations, sorted by time and limited to the last few hundred. To fetch all for a given network append a &#39;net&#39; filter with the network name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloudrf.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ManageApi apiInstance = new ManageApi(defaultClient);
    Float n = 3.4F; // Float | North bounding box
    Float e = 3.4F; // Float | East bounding box
    Float s = 3.4F; // Float | South bounding box
    Float w = 3.4F; // Float | West bounding box
    try {
      apiInstance.callList(n, e, s, w);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#callList");
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
| **n** | **Float**| North bounding box | [optional] |
| **e** | **Float**| East bounding box | [optional] |
| **s** | **Float**| South bounding box | [optional] |
| **w** | **Float**| West bounding box | [optional] |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request OK |  -  |

<a id="delete"></a>
# **delete**
> delete(cid)

Delete a calculation from the database.

Warning! you could lose data. This function will delete the entry from the database and the file from the disk. Accidental deletion can be reversed by contacting support with biscuits who maintain an offsite backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloudrf.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ManageApi apiInstance = new ManageApi(defaultClient);
    Integer cid = 56; // Integer | Unique calculation ID number
    try {
      apiInstance.delete(cid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#delete");
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
| **cid** | **Integer**| Unique calculation ID number | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request OK |  -  |

<a id="deleteNetwork"></a>
# **deleteNetwork**
> deleteNetwork(nid)

Delete an entire network

Warning! you could lose data. This function will delete the entry from the database and the file from the disk. Accidental deletion can be reversed by contacting support with biscuits who maintain an offsite backup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloudrf.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String nid = "nid_example"; // String | Network name
    try {
      apiInstance.deleteNetwork(nid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#deleteNetwork");
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
| **nid** | **String**| Network name | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request OK |  -  |

<a id="export"></a>
# **export**
> export(_file, fmt)

Export a calculation in a GIS file format

Download your data in a format suitable for a third party viewer like Google Earth or ESRI Arcmap.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloudrf.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ManageApi apiInstance = new ManageApi(defaultClient);
    String _file = "_file_example"; // String | Calculation file name
    String fmt = "kml"; // String | Raster/Vector file format: KML, KMZ, SHP, GeoTIFF
    try {
      apiInstance.export(_file, fmt);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManageApi#export");
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
| **_file** | **String**| Calculation file name | |
| **fmt** | **String**| Raster/Vector file format: KML, KMZ, SHP, GeoTIFF | [enum: kml, kml, kmzppa, shp, tiff] |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request OK |  -  |

