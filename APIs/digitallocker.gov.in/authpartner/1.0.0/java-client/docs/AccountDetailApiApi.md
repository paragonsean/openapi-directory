# AccountDetailApiApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountDetailAPIId**](AccountDetailApiApi.md#accountDetailAPIId) | **GET** /oauth2/1/user | Get User Details |


<a id="accountDetailAPIId"></a>
# **accountDetailAPIId**
> Sample5 accountDetailAPIId()

Get User Details

Client applications can call this API to get the DigiLocker Id, name, date of birth and gender of the account holder. An access token is required to call this API. The API will return the user details of the account with which the access token is linked. It is strongly recommended that the API can be called by client application only once after acquiring the access token. Since the user details do not change, the client application may store the values and use them when necessary than calling this API repeatedly.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountDetailApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountDetailApiApi apiInstance = new AccountDetailApiApi(defaultClient);
    try {
      Sample5 result = apiInstance.accountDetailAPIId();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountDetailApiApi#accountDetailAPIId");
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

[**Sample5**](Sample5.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **401** | Unauthorized error |  -  |
| **500** | Internal server error |  -  |

