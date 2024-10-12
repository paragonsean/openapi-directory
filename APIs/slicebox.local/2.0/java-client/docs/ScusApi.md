# ScusApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scusGet**](ScusApi.md#scusGet) | **GET** /scus |  |
| [**scusIdDelete**](ScusApi.md#scusIdDelete) | **DELETE** /scus/{id} |  |
| [**scusIdSendPost**](ScusApi.md#scusIdSendPost) | **POST** /scus/{id}/send |  |
| [**scusPost**](ScusApi.md#scusPost) | **POST** /scus |  |


<a id="scusGet"></a>
# **scusGet**
> List&lt;Scu&gt; scusGet(startindex, count)



get a list of DICOM SCUs. Each SCU is a client for sending DICOM images to an SCP, e.g. a PACS system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ScusApi apiInstance = new ScusApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of SCUs
    Long count = 20L; // Long | size of returned slice of SCUs
    try {
      List<Scu> result = apiInstance.scusGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScusApi#scusGet");
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
| **startindex** | **Long**| start index of returned slice of SCUs | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of SCUs | [optional] [default to 20] |

### Return type

[**List&lt;Scu&gt;**](Scu.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of SCUs |  -  |

<a id="scusIdDelete"></a>
# **scusIdDelete**
> scusIdDelete(id)



remove the SCU corresponding to the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ScusApi apiInstance = new ScusApi(defaultClient);
    Long id = 56L; // Long | id of SCU to remove
    try {
      apiInstance.scusIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScusApi#scusIdDelete");
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
| **id** | **Long**| id of SCU to remove | |

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
| **204** | SCU removed |  -  |

<a id="scusIdSendPost"></a>
# **scusIdSendPost**
> scusIdSendPost(id, imageids)



send the images with the supplied image IDs to a DICOM SCP using the the SCU with the supplied scu ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ScusApi apiInstance = new ScusApi(defaultClient);
    Long id = 56L; // Long | id of SCU to use for sending
    List<Long> imageids = Arrays.asList(); // List<Long> | array of ids of images to send
    try {
      apiInstance.scusIdSendPost(id, imageids);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScusApi#scusIdSendPost");
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
| **id** | **Long**| id of SCU to use for sending | |
| **imageids** | [**List&lt;Long&gt;**](Long.md)| array of ids of images to send | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Series sent |  -  |
| **404** | Series not found or SCU not found |  -  |
| **502** | Receiving SCP host not available |  -  |

<a id="scusPost"></a>
# **scusPost**
> Scu scusPost(scu)



add a new SCU for sending DICOM images

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ScusApi apiInstance = new ScusApi(defaultClient);
    Scu scu = new Scu(); // Scu | SCU information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    try {
      Scu result = apiInstance.scusPost(scu);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScusApi#scusPost");
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
| **scu** | [**Scu**](Scu.md)| SCU information. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] |

### Return type

[**Scu**](Scu.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | the created SCU |  -  |
| **400** | Invalid port number or AE title |  -  |

