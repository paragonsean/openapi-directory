# SshKeysApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSSHKey**](SshKeysApi.md#addSSHKey) | **POST** /ssh-keys | Create a new SSH Key |
| [**deleteSSHKey**](SshKeysApi.md#deleteSSHKey) | **DELETE** /ssh-keys/{id} | Delete an SSH Key |
| [**getSSHKey**](SshKeysApi.md#getSSHKey) | **GET** /ssh-keys/{id} | Get metadata for an SSH Key |
| [**getSSHKeysList**](SshKeysApi.md#getSSHKeysList) | **GET** /ssh-keys | Get metadata for a list of SSH Keys |


<a id="addSSHKey"></a>
# **addSSHKey**
> SSHKeyResponse addSSHKey(evApiKey, evAccessToken, addSSHKeyRequestBody)

Create a new SSH Key

Create a new SSH Key for a user. Provide the Public Key as formatted from the ssh-keygen command (openssh format or RFC-4716 format).  If you&#39;d prefer to let us generate your key automatically, you can log in to your account via the web portal and set up new keys via the SSH Keys page. 

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
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    SshKeysApi apiInstance = new SshKeysApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    AddSSHKeyRequestBody addSSHKeyRequestBody = new AddSSHKeyRequestBody(); // AddSSHKeyRequestBody | 
    try {
      SSHKeyResponse result = apiInstance.addSSHKey(evApiKey, evAccessToken, addSSHKeyRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshKeysApi#addSSHKey");
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
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **addSSHKeyRequestBody** | [**AddSSHKeyRequestBody**](AddSSHKeyRequestBody.md)|  | [optional] |

### Return type

[**SSHKeyResponse**](SSHKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="deleteSSHKey"></a>
# **deleteSSHKey**
> deleteSSHKey(id, evApiKey, evAccessToken)

Delete an SSH Key

Delete the specified SSH key. This will not delete or deactivate the user tied to the key.

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
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    SshKeysApi apiInstance = new SshKeysApi(defaultClient);
    String id = "id_example"; // String | 
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    try {
      apiInstance.deleteSSHKey(id, evApiKey, evAccessToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshKeysApi#deleteSSHKey");
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
| **id** | **String**|  | |
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |

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
| **200** | Successful Operation |  -  |

<a id="getSSHKey"></a>
# **getSSHKey**
> SSHKeyResponse getSSHKey(id, evApiKey, evAccessToken)

Get metadata for an SSH Key

Return the information for a single SSH Key

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
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    SshKeysApi apiInstance = new SshKeysApi(defaultClient);
    String id = "id_example"; // String | 
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    try {
      SSHKeyResponse result = apiInstance.getSSHKey(id, evApiKey, evAccessToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshKeysApi#getSSHKey");
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
| **id** | **String**|  | |
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |

### Return type

[**SSHKeyResponse**](SSHKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

<a id="getSSHKeysList"></a>
# **getSSHKeysList**
> SSHKeyCollectionResponse getSSHKeysList(evApiKey, evAccessToken, userId, limit, offset)

Get metadata for a list of SSH Keys

Returns a list of SSH Keys within the account. Can be filtered for a single user.

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
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    SshKeysApi apiInstance = new SshKeysApi(defaultClient);
    String evApiKey = "evApiKey_example"; // String | API key required to make the API call.
    String evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
    String userId = "userId_example"; // String |  Only return results for the given user ID. This is not the username, but the numeric ID of the user.
    Integer limit = 56; // Integer |  Limits the results by the given number. Cannot be set higher than 100.
    Integer offset = 56; // Integer |  Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list.
    try {
      SSHKeyCollectionResponse result = apiInstance.getSSHKeysList(evApiKey, evAccessToken, userId, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SshKeysApi#getSSHKeysList");
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
| **evApiKey** | **String**| API key required to make the API call. | |
| **evAccessToken** | **String**| Access token required to make the API call. | |
| **userId** | **String**|  Only return results for the given user ID. This is not the username, but the numeric ID of the user. | [optional] |
| **limit** | **Integer**|  Limits the results by the given number. Cannot be set higher than 100. | [optional] |
| **offset** | **Integer**|  Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list. | [optional] |

### Return type

[**SSHKeyCollectionResponse**](SSHKeyCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |

