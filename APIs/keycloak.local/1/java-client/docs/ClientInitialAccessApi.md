# ClientInitialAccessApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmClientsInitialAccessGet**](ClientInitialAccessApi.md#realmClientsInitialAccessGet) | **GET** /{realm}/clients-initial-access |  |
| [**realmClientsInitialAccessIdDelete**](ClientInitialAccessApi.md#realmClientsInitialAccessIdDelete) | **DELETE** /{realm}/clients-initial-access/{id} |  |
| [**realmClientsInitialAccessPost**](ClientInitialAccessApi.md#realmClientsInitialAccessPost) | **POST** /{realm}/clients-initial-access | Create a new initial access token. |


<a id="realmClientsInitialAccessGet"></a>
# **realmClientsInitialAccessGet**
> List&lt;ClientInitialAccessPresentation&gt; realmClientsInitialAccessGet(realm)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInitialAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientInitialAccessApi apiInstance = new ClientInitialAccessApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<ClientInitialAccessPresentation> result = apiInstance.realmClientsInitialAccessGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInitialAccessApi#realmClientsInitialAccessGet");
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

[**List&lt;ClientInitialAccessPresentation&gt;**](ClientInitialAccessPresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsInitialAccessIdDelete"></a>
# **realmClientsInitialAccessIdDelete**
> realmClientsInitialAccessIdDelete(realm, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInitialAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientInitialAccessApi apiInstance = new ClientInitialAccessApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    try {
      apiInstance.realmClientsInitialAccessIdDelete(realm, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInitialAccessApi#realmClientsInitialAccessIdDelete");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsInitialAccessPost"></a>
# **realmClientsInitialAccessPost**
> ClientInitialAccessPresentation realmClientsInitialAccessPost(realm, clientInitialAccessCreatePresentation)

Create a new initial access token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientInitialAccessApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientInitialAccessApi apiInstance = new ClientInitialAccessApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    ClientInitialAccessCreatePresentation clientInitialAccessCreatePresentation = new ClientInitialAccessCreatePresentation(); // ClientInitialAccessCreatePresentation | 
    try {
      ClientInitialAccessPresentation result = apiInstance.realmClientsInitialAccessPost(realm, clientInitialAccessCreatePresentation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientInitialAccessApi#realmClientsInitialAccessPost");
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
| **clientInitialAccessCreatePresentation** | [**ClientInitialAccessCreatePresentation**](ClientInitialAccessCreatePresentation.md)|  | |

### Return type

[**ClientInitialAccessPresentation**](ClientInitialAccessPresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

