# VolumesApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**attachVolume**](VolumesApi.md#attachVolume) | **POST** /volumes/{volumeId}/attach | Volume Attach |
| [**cloneVolume**](VolumesApi.md#cloneVolume) | **POST** /volumes/{volumeId}/clone | Volume Clone |
| [**createVolume**](VolumesApi.md#createVolume) | **POST** /volumes | Volume Create |
| [**deleteVolume**](VolumesApi.md#deleteVolume) | **DELETE** /volumes/{volumeId} | Volume Delete |
| [**detachVolume**](VolumesApi.md#detachVolume) | **POST** /volumes/{volumeId}/detach | Volume Detach |
| [**getVolume**](VolumesApi.md#getVolume) | **GET** /volumes/{volumeId} | Volume View |
| [**getVolumes**](VolumesApi.md#getVolumes) | **GET** /volumes | Volumes List |
| [**resizeVolume**](VolumesApi.md#resizeVolume) | **POST** /volumes/{volumeId}/resize | Volume Resize |
| [**updateVolume**](VolumesApi.md#updateVolume) | **PUT** /volumes/{volumeId} | Volume Update |


<a id="attachVolume"></a>
# **attachVolume**
> Volume attachVolume(volumeId, attachVolumeRequest)

Volume Attach

Attaches a Volume on your Account to an existing Linode on your Account. In order for this request to complete successfully, your User must have &#x60;read_only&#x60; or &#x60;read_write&#x60; permission to the Volume and &#x60;read_write&#x60; permission to the Linode. Additionally, the Volume and Linode must be located in the same Region. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    Integer volumeId = 56; // Integer | ID of the Volume to attach.
    AttachVolumeRequest attachVolumeRequest = new AttachVolumeRequest(); // AttachVolumeRequest | Volume to attach to a Linode.
    try {
      Volume result = apiInstance.attachVolume(volumeId, attachVolumeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#attachVolume");
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
| **volumeId** | **Integer**| ID of the Volume to attach. | |
| **attachVolumeRequest** | [**AttachVolumeRequest**](AttachVolumeRequest.md)| Volume to attach to a Linode. | |

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volume was attached to a Linode. |  -  |
| **0** | Error |  -  |

<a id="cloneVolume"></a>
# **cloneVolume**
> Volume cloneVolume(volumeId, cloneVolumeRequest)

Volume Clone

Creates a Volume on your Account. In order for this request to complete successfully, your User must have the &#x60;add_volumes&#x60; grant. The new Volume will have the same size and data as the source Volume. Creating a new Volume will incur a charge on your Account. * Only Volumes with a &#x60;status&#x60; of \&quot;active\&quot; can be cloned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    Integer volumeId = 56; // Integer | ID of the Volume to clone.
    CloneVolumeRequest cloneVolumeRequest = new CloneVolumeRequest(); // CloneVolumeRequest | The requested state your Volume will be cloned into.
    try {
      Volume result = apiInstance.cloneVolume(volumeId, cloneVolumeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#cloneVolume");
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
| **volumeId** | **Integer**| ID of the Volume to clone. | |
| **cloneVolumeRequest** | [**CloneVolumeRequest**](CloneVolumeRequest.md)| The requested state your Volume will be cloned into. | |

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Clone started. |  -  |
| **0** | Error |  -  |

<a id="createVolume"></a>
# **createVolume**
> Volume createVolume(createVolumeRequest)

Volume Create

Creates a Volume on your Account. In order for this to complete successfully, your User must have the &#x60;add_volumes&#x60; grant. Creating a new Volume will start accruing additional charges on your account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    CreateVolumeRequest createVolumeRequest = new CreateVolumeRequest(); // CreateVolumeRequest | The requested initial state of a new Volume.
    try {
      Volume result = apiInstance.createVolume(createVolumeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#createVolume");
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
| **createVolumeRequest** | [**CreateVolumeRequest**](CreateVolumeRequest.md)| The requested initial state of a new Volume. | |

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Creating Volume.  |  -  |
| **0** | Error |  -  |

<a id="deleteVolume"></a>
# **deleteVolume**
> Object deleteVolume(volumeId)

Volume Delete

Deletes a Volume you have permission to &#x60;read_write&#x60;.  * **Deleting a Volume is a destructive action and cannot be undone.**  * Deleting stops billing for the Volume. You will be billed for time used within the billing period the Volume was active.  * Volumes that are migrating cannot be deleted until the migration is finished. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    Integer volumeId = 56; // Integer | ID of the Volume to look up.
    try {
      Object result = apiInstance.deleteVolume(volumeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#deleteVolume");
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
| **volumeId** | **Integer**| ID of the Volume to look up. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volume deletion successful. |  -  |
| **0** | Error |  -  |

<a id="detachVolume"></a>
# **detachVolume**
> Object detachVolume(volumeId)

Volume Detach

Detaches a Volume on your Account from a Linode on your Account. In order for this request to complete successfully, your User must have &#x60;read_write&#x60; access to the Volume and &#x60;read_write&#x60; access to the Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    Integer volumeId = 56; // Integer | ID of the Volume to detach.
    try {
      Object result = apiInstance.detachVolume(volumeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#detachVolume");
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
| **volumeId** | **Integer**| ID of the Volume to detach. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volume was detached from a Linode. |  -  |
| **0** | Error |  -  |

<a id="getVolume"></a>
# **getVolume**
> Volume getVolume(volumeId, page, pageSize)

Volume View

Get information about a single Volume. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    Integer volumeId = 56; // Integer | ID of the Volume to look up.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      Volume result = apiInstance.getVolume(volumeId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#getVolume");
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
| **volumeId** | **Integer**| ID of the Volume to look up. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single Volume object. |  -  |
| **0** | Error |  -  |

<a id="getVolumes"></a>
# **getVolumes**
> GetLinodeVolumes200Response getVolumes(page, pageSize)

Volumes List

Returns a paginated list of Volumes you have permission to view. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetLinodeVolumes200Response result = apiInstance.getVolumes(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#getVolumes");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetLinodeVolumes200Response**](GetLinodeVolumes200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of all Volumes on your Account. |  -  |
| **0** | Error |  -  |

<a id="resizeVolume"></a>
# **resizeVolume**
> Volume resizeVolume(volumeId, resizeVolumeRequest)

Volume Resize

Resize an existing Volume on your Account. In order for this request to complete successfully, your User must have the &#x60;read_write&#x60; permissions to the Volume. * Volumes can only be resized up. * Only Volumes with a &#x60;status&#x60; of \&quot;active\&quot; can be resized. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    Integer volumeId = 56; // Integer | ID of the Volume to resize.
    ResizeVolumeRequest resizeVolumeRequest = new ResizeVolumeRequest(); // ResizeVolumeRequest | The requested size to increase your Volume to.
    try {
      Volume result = apiInstance.resizeVolume(volumeId, resizeVolumeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#resizeVolume");
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
| **volumeId** | **Integer**| ID of the Volume to resize. | |
| **resizeVolumeRequest** | [**ResizeVolumeRequest**](ResizeVolumeRequest.md)| The requested size to increase your Volume to. | |

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Volume resize started. |  -  |
| **0** | Error |  -  |

<a id="updateVolume"></a>
# **updateVolume**
> Volume updateVolume(volumeId, updateVolumeRequest)

Volume Update

Updates a Volume that you have permission to &#x60;read_write&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VolumesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    VolumesApi apiInstance = new VolumesApi(defaultClient);
    Integer volumeId = 56; // Integer | ID of the Volume to look up.
    UpdateVolumeRequest updateVolumeRequest = new UpdateVolumeRequest(); // UpdateVolumeRequest | If any updated field fails to pass validation, the Volume will not be updated. 
    try {
      Volume result = apiInstance.updateVolume(volumeId, updateVolumeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VolumesApi#updateVolume");
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
| **volumeId** | **Integer**| ID of the Volume to look up. | |
| **updateVolumeRequest** | [**UpdateVolumeRequest**](UpdateVolumeRequest.md)| If any updated field fails to pass validation, the Volume will not be updated.  | |

### Return type

[**Volume**](Volume.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated Volume. |  -  |
| **0** | Error |  -  |

