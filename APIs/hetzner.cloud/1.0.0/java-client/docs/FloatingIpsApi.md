# FloatingIpsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**floatingIpsGet**](FloatingIpsApi.md#floatingIpsGet) | **GET** /floating_ips | Get all Floating IPs |
| [**floatingIpsIdDelete**](FloatingIpsApi.md#floatingIpsIdDelete) | **DELETE** /floating_ips/{id} | Delete a Floating IP |
| [**floatingIpsIdGet**](FloatingIpsApi.md#floatingIpsIdGet) | **GET** /floating_ips/{id} | Get a Floating IP |
| [**floatingIpsIdPut**](FloatingIpsApi.md#floatingIpsIdPut) | **PUT** /floating_ips/{id} | Update a Floating IP |
| [**floatingIpsPost**](FloatingIpsApi.md#floatingIpsPost) | **POST** /floating_ips | Create a Floating IP |


<a id="floatingIpsGet"></a>
# **floatingIpsGet**
> FloatingIpsGet200Response floatingIpsGet(name, labelSelector, sort)

Get all Floating IPs

Returns all Floating IP objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloatingIpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FloatingIpsApi apiInstance = new FloatingIpsApi(defaultClient);
    String name = "name_example"; // String | Can be used to filter Floating IPs by their name. The response will only contain the Floating IP matching the specified name.
    String labelSelector = "labelSelector_example"; // String | Can be used to filter Floating IPs by labels. The response will only contain Floating IPs matching the label selector.
    String sort = "id"; // String | Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc
    try {
      FloatingIpsGet200Response result = apiInstance.floatingIpsGet(name, labelSelector, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloatingIpsApi#floatingIpsGet");
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
| **name** | **String**| Can be used to filter Floating IPs by their name. The response will only contain the Floating IP matching the specified name. | [optional] |
| **labelSelector** | **String**| Can be used to filter Floating IPs by labels. The response will only contain Floating IPs matching the label selector. | [optional] |
| **sort** | **String**| Can be used multiple times. Choices id id:asc id:desc created created:asc created:desc | [optional] [enum: id, id:asc, id:desc, created, created:asc, created:desc] |

### Return type

[**FloatingIpsGet200Response**](FloatingIpsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;floating_ips&#x60; key in the reply contains an array of Floating IP objects with this structure |  -  |

<a id="floatingIpsIdDelete"></a>
# **floatingIpsIdDelete**
> floatingIpsIdDelete(id)

Delete a Floating IP

Deletes a Floating IP. If it is currently assigned to a Server it will automatically get unassigned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloatingIpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FloatingIpsApi apiInstance = new FloatingIpsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Floating IP
    try {
      apiInstance.floatingIpsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloatingIpsApi#floatingIpsIdDelete");
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
| **id** | **Integer**| ID of the Floating IP | |

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
| **204** | Floating IP deleted |  -  |

<a id="floatingIpsIdGet"></a>
# **floatingIpsIdGet**
> FloatingIpsIdGet200Response floatingIpsIdGet(id)

Get a Floating IP

Returns a specific Floating IP object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloatingIpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FloatingIpsApi apiInstance = new FloatingIpsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Floating IP
    try {
      FloatingIpsIdGet200Response result = apiInstance.floatingIpsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloatingIpsApi#floatingIpsIdGet");
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
| **id** | **Integer**| ID of the Floating IP | |

### Return type

[**FloatingIpsIdGet200Response**](FloatingIpsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;floating_ip&#x60; key in the reply contains a Floating IP object with this structure |  -  |

<a id="floatingIpsIdPut"></a>
# **floatingIpsIdPut**
> FloatingIpsIdGet200Response floatingIpsIdPut(id, updateFloatingIPRequest)

Update a Floating IP

Updates the description or labels of a Floating IP. Also note that when updating labels, the Floating IP’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloatingIpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FloatingIpsApi apiInstance = new FloatingIpsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Floating IP
    UpdateFloatingIPRequest updateFloatingIPRequest = new UpdateFloatingIPRequest(); // UpdateFloatingIPRequest | 
    try {
      FloatingIpsIdGet200Response result = apiInstance.floatingIpsIdPut(id, updateFloatingIPRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloatingIpsApi#floatingIpsIdPut");
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
| **id** | **Integer**| ID of the Floating IP | |
| **updateFloatingIPRequest** | [**UpdateFloatingIPRequest**](UpdateFloatingIPRequest.md)|  | [optional] |

### Return type

[**FloatingIpsIdGet200Response**](FloatingIpsIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;floating_ip&#x60; key in the reply contains the modified Floating IP object with the new description |  -  |

<a id="floatingIpsPost"></a>
# **floatingIpsPost**
> FloatingIpsPost201Response floatingIpsPost(createFloatingIPRequest)

Create a Floating IP

Creates a new Floating IP assigned to a Server. If you want to create a Floating IP that is not bound to a Server, you need to provide the &#x60;home_location&#x60; key instead of &#x60;server&#x60;. This can be either the ID or the name of the Location this IP shall be created in. Note that a Floating IP can be assigned to a Server in any Location later on. For optimal routing it is advised to use the Floating IP in the same Location it was created in.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloatingIpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FloatingIpsApi apiInstance = new FloatingIpsApi(defaultClient);
    CreateFloatingIPRequest createFloatingIPRequest = new CreateFloatingIPRequest(); // CreateFloatingIPRequest | The `type` argument is required while `home_location` and `server` are mutually exclusive.
    try {
      FloatingIpsPost201Response result = apiInstance.floatingIpsPost(createFloatingIPRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloatingIpsApi#floatingIpsPost");
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
| **createFloatingIPRequest** | [**CreateFloatingIPRequest**](CreateFloatingIPRequest.md)| The &#x60;type&#x60; argument is required while &#x60;home_location&#x60; and &#x60;server&#x60; are mutually exclusive. | [optional] |

### Return type

[**FloatingIpsPost201Response**](FloatingIpsPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;floating_ip&#x60; key in the reply contains the object that was just created |  -  |

