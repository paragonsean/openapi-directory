# DatacentersApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**datacentersGet**](DatacentersApi.md#datacentersGet) | **GET** /datacenters | Get all Datacenters |
| [**datacentersIdGet**](DatacentersApi.md#datacentersIdGet) | **GET** /datacenters/{id} | Get a Datacenter |


<a id="datacentersGet"></a>
# **datacentersGet**
> DatacentersGet200Response datacentersGet(name)

Get all Datacenters

Returns all Datacenter objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatacentersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    DatacentersApi apiInstance = new DatacentersApi(defaultClient);
    String name = "name_example"; // String | Can be used to filter Datacenters by their name. The response will only contain the Datacenter matching the specified name. When the name does not match the Datacenter name format, an `invalid_input` error is returned.
    try {
      DatacentersGet200Response result = apiInstance.datacentersGet(name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatacentersApi#datacentersGet");
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
| **name** | **String**| Can be used to filter Datacenters by their name. The response will only contain the Datacenter matching the specified name. When the name does not match the Datacenter name format, an &#x60;invalid_input&#x60; error is returned. | [optional] |

### Return type

[**DatacentersGet200Response**](DatacentersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The reply contains the &#x60;datacenters&#x60; and &#x60;recommendation&#x60; keys |  -  |

<a id="datacentersIdGet"></a>
# **datacentersIdGet**
> DatacentersIdGet200Response datacentersIdGet(id)

Get a Datacenter

Returns a specific Datacenter object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatacentersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    DatacentersApi apiInstance = new DatacentersApi(defaultClient);
    Integer id = 56; // Integer | ID of Datacenter
    try {
      DatacentersIdGet200Response result = apiInstance.datacentersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatacentersApi#datacentersIdGet");
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
| **id** | **Integer**| ID of Datacenter | |

### Return type

[**DatacentersIdGet200Response**](DatacentersIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;datacenter&#x60; key in the reply contains a Datacenter object with this structure |  -  |

