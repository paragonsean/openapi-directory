# CredentialsApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateCredentialSecretUsingPOST**](CredentialsApi.md#updateCredentialSecretUsingPOST) | **POST** /restv2/game/{apiKey}/config/~credentials/{credentialName}/resetSecret | Resets the secret of a credential |


<a id="updateCredentialSecretUsingPOST"></a>
# **updateCredentialSecretUsingPOST**
> updateCredentialSecretUsingPOST(apiKey, credentialName)

Resets the secret of a credential

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    CredentialsApi apiInstance = new CredentialsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    String credentialName = "credentialName_example"; // String | credentialName
    try {
      apiInstance.updateCredentialSecretUsingPOST(apiKey, credentialName);
    } catch (ApiException e) {
      System.err.println("Exception when calling CredentialsApi#updateCredentialSecretUsingPOST");
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
| **apiKey** | **String**| apiKey | |
| **credentialName** | **String**| credentialName | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

