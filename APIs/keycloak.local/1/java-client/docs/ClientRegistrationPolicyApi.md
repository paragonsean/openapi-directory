# ClientRegistrationPolicyApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmClientRegistrationPolicyProvidersGet**](ClientRegistrationPolicyApi.md#realmClientRegistrationPolicyProvidersGet) | **GET** /{realm}/client-registration-policy/providers | Base path for retrieve providers with the configProperties properly filled |


<a id="realmClientRegistrationPolicyProvidersGet"></a>
# **realmClientRegistrationPolicyProvidersGet**
> List&lt;ComponentTypeRepresentation&gt; realmClientRegistrationPolicyProvidersGet(realm)

Base path for retrieve providers with the configProperties properly filled

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientRegistrationPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientRegistrationPolicyApi apiInstance = new ClientRegistrationPolicyApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<ComponentTypeRepresentation> result = apiInstance.realmClientRegistrationPolicyProvidersGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientRegistrationPolicyApi#realmClientRegistrationPolicyProvidersGet");
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

[**List&lt;ComponentTypeRepresentation&gt;**](ComponentTypeRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

