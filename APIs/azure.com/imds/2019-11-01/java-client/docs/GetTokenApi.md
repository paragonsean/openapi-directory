# GetTokenApi

All URIs are relative to *http://169.254.169.254/metadata*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**identityGetToken**](GetTokenApi.md#identityGetToken) | **GET** /identity/oauth2/token |  |


<a id="identityGetToken"></a>
# **identityGetToken**
> IdentityTokenResponse identityGetToken(metadata, resource, apiVersion, clientId, objectId, msiResId, authority, bypassCache)



Get a Token from Azure AD

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetTokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://169.254.169.254/metadata");
    
    // Configure HTTP basic authorization: basic_auth
    HttpBasicAuth basic_auth = (HttpBasicAuth) defaultClient.getAuthentication("basic_auth");
    basic_auth.setUsername("YOUR USERNAME");
    basic_auth.setPassword("YOUR PASSWORD");

    GetTokenApi apiInstance = new GetTokenApi(defaultClient);
    String metadata = "true"; // String | This must be set to 'true'.
    String resource = "resource_example"; // String | This is the urlencoded identifier URI of the sink resource for the requested Azure AD token. The resulting token contains the corresponding aud for this resource.
    String apiVersion = "2018-10-01"; // String | This is the API version to use.
    String clientId = "clientId_example"; // String | This identifies, by Azure AD client id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with object_id and msi_res_id.
    String objectId = "objectId_example"; // String | This identifies, by Azure AD object id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with client_id and msi_res_id.
    String msiResId = "msiResId_example"; // String | This identifies, by urlencoded ARM resource id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with client_id and object_id.
    String authority = "authority_example"; // String | This indicates the authority to request AAD tokens from. Defaults to the known authority of the identity to be used.
    String bypassCache = "true"; // String | If provided, the value must be 'true'. This indicates to the server that the token must be retrieved from Azure AD and cannot be retrieved from an internal cache.
    try {
      IdentityTokenResponse result = apiInstance.identityGetToken(metadata, resource, apiVersion, clientId, objectId, msiResId, authority, bypassCache);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetTokenApi#identityGetToken");
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
| **metadata** | **String**| This must be set to &#39;true&#39;. | [enum: true] |
| **resource** | **String**| This is the urlencoded identifier URI of the sink resource for the requested Azure AD token. The resulting token contains the corresponding aud for this resource. | |
| **apiVersion** | **String**| This is the API version to use. | [enum: 2018-10-01] |
| **clientId** | **String**| This identifies, by Azure AD client id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with object_id and msi_res_id. | [optional] |
| **objectId** | **String**| This identifies, by Azure AD object id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with client_id and msi_res_id. | [optional] |
| **msiResId** | **String**| This identifies, by urlencoded ARM resource id, a specific explicit identity to use when authenticating to Azure AD. Mutually exclusive with client_id and object_id. | [optional] |
| **authority** | **String**| This indicates the authority to request AAD tokens from. Defaults to the known authority of the identity to be used. | [optional] |
| **bypassCache** | **String**| If provided, the value must be &#39;true&#39;. This indicates to the server that the token must be retrieved from Azure AD and cannot be retrieved from an internal cache. | [optional] [enum: true] |

### Return type

[**IdentityTokenResponse**](IdentityTokenResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | Error response describing why the operation failed. |  * Www-Authenticate - This is the response header containing a challenge for the Basic scheme with a realm value <br>  |

