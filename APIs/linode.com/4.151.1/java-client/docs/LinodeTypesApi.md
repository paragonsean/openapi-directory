# LinodeTypesApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLinodeType**](LinodeTypesApi.md#getLinodeType) | **GET** /linode/types/{typeId} | Type View |
| [**getLinodeTypes**](LinodeTypesApi.md#getLinodeTypes) | **GET** /linode/types | Types List |


<a id="getLinodeType"></a>
# **getLinodeType**
> LinodeType getLinodeType(typeId)

Type View

Returns information about a specific Linode Type, including pricing and specifications. This is used when [creating](/docs/api/linode-instances/#linode-create) or [resizing](/docs/api/linode-instances/#linode-resize) Linodes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    LinodeTypesApi apiInstance = new LinodeTypesApi(defaultClient);
    String typeId = "typeId_example"; // String | The ID of the Linode Type to look up.
    try {
      LinodeType result = apiInstance.getLinodeType(typeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeTypesApi#getLinodeType");
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
| **typeId** | **String**| The ID of the Linode Type to look up. | |

### Return type

[**LinodeType**](LinodeType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single Linode Type. |  -  |
| **0** | Error |  -  |

<a id="getLinodeTypes"></a>
# **getLinodeTypes**
> GetLinodeTypes200Response getLinodeTypes()

Types List

Returns collection of Linode Types, including pricing and specifications for each Type. These are used when [creating](/docs/api/linode-instances/#linode-create) or [resizing](/docs/api/linode-instances/#linode-resize) Linodes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    LinodeTypesApi apiInstance = new LinodeTypesApi(defaultClient);
    try {
      GetLinodeTypes200Response result = apiInstance.getLinodeTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeTypesApi#getLinodeTypes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLinodeTypes200Response**](GetLinodeTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of Linode Types. |  -  |
| **0** | Error |  -  |

