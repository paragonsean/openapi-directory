# ScpsApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scpsGet**](ScpsApi.md#scpsGet) | **GET** /scps |  |
| [**scpsIdDelete**](ScpsApi.md#scpsIdDelete) | **DELETE** /scps/{id} |  |
| [**scpsPost**](ScpsApi.md#scpsPost) | **POST** /scps |  |


<a id="scpsGet"></a>
# **scpsGet**
> List&lt;Scp&gt; scpsGet(startindex, count)



get a list of DICOM SCPs. Each SCP is a server for receiving DICOM images from e.g. a PACS system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ScpsApi apiInstance = new ScpsApi(defaultClient);
    Long startindex = 0L; // Long | start index of returned slice of SCPs
    Long count = 20L; // Long | size of returned slice of SCPs
    try {
      List<Scp> result = apiInstance.scpsGet(startindex, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScpsApi#scpsGet");
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
| **startindex** | **Long**| start index of returned slice of SCPs | [optional] [default to 0] |
| **count** | **Long**| size of returned slice of SCPs | [optional] [default to 20] |

### Return type

[**List&lt;Scp&gt;**](Scp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the list of SCPs |  -  |

<a id="scpsIdDelete"></a>
# **scpsIdDelete**
> scpsIdDelete(id)



shut down and remove the SCP corresponding to the supplied ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ScpsApi apiInstance = new ScpsApi(defaultClient);
    Long id = 56L; // Long | id of SCP to remove
    try {
      apiInstance.scpsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScpsApi#scpsIdDelete");
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
| **id** | **Long**| id of SCP to remove | |

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
| **204** | SCP removed |  -  |

<a id="scpsPost"></a>
# **scpsPost**
> Scp scpsPost(scp)



add a new SCP for receiving DICOM images

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    ScpsApi apiInstance = new ScpsApi(defaultClient);
    Scp scp = new Scp(); // Scp | SCP information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
    try {
      Scp result = apiInstance.scpsPost(scp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScpsApi#scpsPost");
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
| **scp** | [**Scp**](Scp.md)| SCP information. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] |

### Return type

[**Scp**](Scp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream, multipart/form-data
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | the created SCP |  -  |
| **400** | Invalid port number or AE title |  -  |

