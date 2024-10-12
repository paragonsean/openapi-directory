# SshKeysApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sshKeysGet**](SshKeysApi.md#sshKeysGet) | **GET** /ssh_keys | Get all SSH keys |
| [**sshKeysIdDelete**](SshKeysApi.md#sshKeysIdDelete) | **DELETE** /ssh_keys/{id} | Delete an SSH key |
| [**sshKeysIdGet**](SshKeysApi.md#sshKeysIdGet) | **GET** /ssh_keys/{id} | Get a SSH key |
| [**sshKeysIdPut**](SshKeysApi.md#sshKeysIdPut) | **PUT** /ssh_keys/{id} | Update an SSH key |
| [**sshKeysPost**](SshKeysApi.md#sshKeysPost) | **POST** /ssh_keys | Create an SSH key |


<a id="sshKeysGet"></a>
# **sshKeysGet**
> SshKeysGet200Response sshKeysGet(sort, name, fingerprint, labelSelector)

Get all SSH keys

Returns all SSH key objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    SshKeysApi apiInstance = new SshKeysApi(defaultClient);
    String sort = "id"; // String | Can be used multiple times.
    String name = "name_example"; // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    String fingerprint = "fingerprint_example"; // String | Can be used to filter SSH keys by their fingerprint. The response will only contain the SSH key matching the specified fingerprint.
    String labelSelector = "labelSelector_example"; // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    try {
      SshKeysGet200Response result = apiInstance.sshKeysGet(sort, name, fingerprint, labelSelector);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshKeysApi#sshKeysGet");
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
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, name, name:asc, name:desc] |
| **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] |
| **fingerprint** | **String**| Can be used to filter SSH keys by their fingerprint. The response will only contain the SSH key matching the specified fingerprint. | [optional] |
| **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] |

### Return type

[**SshKeysGet200Response**](SshKeysGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;ssh_keys&#x60; key in the reply contains an array of SSH key objects with this structure |  -  |

<a id="sshKeysIdDelete"></a>
# **sshKeysIdDelete**
> sshKeysIdDelete(id)

Delete an SSH key

Deletes an SSH key. It cannot be used anymore.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    SshKeysApi apiInstance = new SshKeysApi(defaultClient);
    String id = "id_example"; // String | ID of the SSH key
    try {
      apiInstance.sshKeysIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshKeysApi#sshKeysIdDelete");
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
| **id** | **String**| ID of the SSH key | |

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
| **204** | SSH key deleted |  -  |

<a id="sshKeysIdGet"></a>
# **sshKeysIdGet**
> SshKeysPost201Response sshKeysIdGet(id)

Get a SSH key

Returns a specific SSH key object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    SshKeysApi apiInstance = new SshKeysApi(defaultClient);
    Integer id = 56; // Integer | ID of the SSH key
    try {
      SshKeysPost201Response result = apiInstance.sshKeysIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshKeysApi#sshKeysIdGet");
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
| **id** | **Integer**| ID of the SSH key | |

### Return type

[**SshKeysPost201Response**](SshKeysPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;ssh_key&#x60; key in the reply contains an SSH key object with this structure |  -  |

<a id="sshKeysIdPut"></a>
# **sshKeysIdPut**
> SshKeysPost201Response sshKeysIdPut(id, sshKeysIdPutRequest)

Update an SSH key

Updates an SSH key. You can update an SSH key name and an SSH key labels.  Please note that when updating labels, the SSH key current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    SshKeysApi apiInstance = new SshKeysApi(defaultClient);
    String id = "id_example"; // String | ID of the SSH key
    SshKeysIdPutRequest sshKeysIdPutRequest = new SshKeysIdPutRequest(); // SshKeysIdPutRequest | 
    try {
      SshKeysPost201Response result = apiInstance.sshKeysIdPut(id, sshKeysIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshKeysApi#sshKeysIdPut");
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
| **id** | **String**| ID of the SSH key | |
| **sshKeysIdPutRequest** | [**SshKeysIdPutRequest**](SshKeysIdPutRequest.md)|  | [optional] |

### Return type

[**SshKeysPost201Response**](SshKeysPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;ssh_key&#x60; key in the reply contains the modified SSH key object with the new description |  -  |

<a id="sshKeysPost"></a>
# **sshKeysPost**
> SshKeysPost201Response sshKeysPost(sshKeysPostRequest)

Create an SSH key

Creates a new SSH key with the given &#x60;name&#x60; and &#x60;public_key&#x60;. Once an SSH key is created, it can be used in other calls such as creating Servers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SshKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    SshKeysApi apiInstance = new SshKeysApi(defaultClient);
    SshKeysPostRequest sshKeysPostRequest = new SshKeysPostRequest(); // SshKeysPostRequest | 
    try {
      SshKeysPost201Response result = apiInstance.sshKeysPost(sshKeysPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshKeysApi#sshKeysPost");
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
| **sshKeysPostRequest** | [**SshKeysPostRequest**](SshKeysPostRequest.md)|  | [optional] |

### Return type

[**SshKeysPost201Response**](SshKeysPost201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;ssh_key&#x60; key in the reply contains the object that was just created |  -  |

