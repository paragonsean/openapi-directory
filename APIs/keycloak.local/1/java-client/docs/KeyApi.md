# KeyApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmKeysGet**](KeyApi.md#realmKeysGet) | **GET** /{realm}/keys |  |


<a id="realmKeysGet"></a>
# **realmKeysGet**
> KeysMetadataRepresentation realmKeysGet(realm)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    KeyApi apiInstance = new KeyApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      KeysMetadataRepresentation result = apiInstance.realmKeysGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KeyApi#realmKeysGet");
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
| **realm** | **String**| realm name (not id!) | |

### Return type

[**KeysMetadataRepresentation**](KeysMetadataRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

