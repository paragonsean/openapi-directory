# ProtocolMappersApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmClientScopesId1ProtocolMappersModelsId2Delete**](ProtocolMappersApi.md#realmClientScopesId1ProtocolMappersModelsId2Delete) | **DELETE** /{realm}/client-scopes/{id1}/protocol-mappers/models/{id2} | Delete the mapper |
| [**realmClientScopesId1ProtocolMappersModelsId2Get**](ProtocolMappersApi.md#realmClientScopesId1ProtocolMappersModelsId2Get) | **GET** /{realm}/client-scopes/{id1}/protocol-mappers/models/{id2} | Get mapper by id |
| [**realmClientScopesId1ProtocolMappersModelsId2Put**](ProtocolMappersApi.md#realmClientScopesId1ProtocolMappersModelsId2Put) | **PUT** /{realm}/client-scopes/{id1}/protocol-mappers/models/{id2} | Update the mapper |
| [**realmClientScopesIdProtocolMappersAddModelsPost**](ProtocolMappersApi.md#realmClientScopesIdProtocolMappersAddModelsPost) | **POST** /{realm}/client-scopes/{id}/protocol-mappers/add-models | Create multiple mappers |
| [**realmClientScopesIdProtocolMappersModelsGet**](ProtocolMappersApi.md#realmClientScopesIdProtocolMappersModelsGet) | **GET** /{realm}/client-scopes/{id}/protocol-mappers/models | Get mappers |
| [**realmClientScopesIdProtocolMappersModelsPost**](ProtocolMappersApi.md#realmClientScopesIdProtocolMappersModelsPost) | **POST** /{realm}/client-scopes/{id}/protocol-mappers/models | Create a mapper |
| [**realmClientScopesIdProtocolMappersProtocolProtocolGet**](ProtocolMappersApi.md#realmClientScopesIdProtocolMappersProtocolProtocolGet) | **GET** /{realm}/client-scopes/{id}/protocol-mappers/protocol/{protocol} | Get mappers by name for a specific protocol |
| [**realmClientsId1ProtocolMappersModelsId2Delete**](ProtocolMappersApi.md#realmClientsId1ProtocolMappersModelsId2Delete) | **DELETE** /{realm}/clients/{id1}/protocol-mappers/models/{id2} | Delete the mapper |
| [**realmClientsId1ProtocolMappersModelsId2Get**](ProtocolMappersApi.md#realmClientsId1ProtocolMappersModelsId2Get) | **GET** /{realm}/clients/{id1}/protocol-mappers/models/{id2} | Get mapper by id |
| [**realmClientsId1ProtocolMappersModelsId2Put**](ProtocolMappersApi.md#realmClientsId1ProtocolMappersModelsId2Put) | **PUT** /{realm}/clients/{id1}/protocol-mappers/models/{id2} | Update the mapper |
| [**realmClientsIdProtocolMappersAddModelsPost**](ProtocolMappersApi.md#realmClientsIdProtocolMappersAddModelsPost) | **POST** /{realm}/clients/{id}/protocol-mappers/add-models | Create multiple mappers |
| [**realmClientsIdProtocolMappersModelsGet**](ProtocolMappersApi.md#realmClientsIdProtocolMappersModelsGet) | **GET** /{realm}/clients/{id}/protocol-mappers/models | Get mappers |
| [**realmClientsIdProtocolMappersModelsPost**](ProtocolMappersApi.md#realmClientsIdProtocolMappersModelsPost) | **POST** /{realm}/clients/{id}/protocol-mappers/models | Create a mapper |
| [**realmClientsIdProtocolMappersProtocolProtocolGet**](ProtocolMappersApi.md#realmClientsIdProtocolMappersProtocolProtocolGet) | **GET** /{realm}/clients/{id}/protocol-mappers/protocol/{protocol} | Get mappers by name for a specific protocol |


<a id="realmClientScopesId1ProtocolMappersModelsId2Delete"></a>
# **realmClientScopesId1ProtocolMappersModelsId2Delete**
> realmClientScopesId1ProtocolMappersModelsId2Delete(realm, id1, id2)

Delete the mapper

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id1 = "id1_example"; // String | 
    String id2 = "id2_example"; // String | 
    try {
      apiInstance.realmClientScopesId1ProtocolMappersModelsId2Delete(realm, id1, id2);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientScopesId1ProtocolMappersModelsId2Delete");
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
| **id1** | **String**|  | |
| **id2** | **String**|  | |

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

<a id="realmClientScopesId1ProtocolMappersModelsId2Get"></a>
# **realmClientScopesId1ProtocolMappersModelsId2Get**
> ProtocolMapperRepresentation realmClientScopesId1ProtocolMappersModelsId2Get(realm, id1, id2)

Get mapper by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id1 = "id1_example"; // String | 
    String id2 = "id2_example"; // String | 
    try {
      ProtocolMapperRepresentation result = apiInstance.realmClientScopesId1ProtocolMappersModelsId2Get(realm, id1, id2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientScopesId1ProtocolMappersModelsId2Get");
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
| **id1** | **String**|  | |
| **id2** | **String**|  | |

### Return type

[**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesId1ProtocolMappersModelsId2Put"></a>
# **realmClientScopesId1ProtocolMappersModelsId2Put**
> realmClientScopesId1ProtocolMappersModelsId2Put(realm, id1, id2, protocolMapperRepresentation)

Update the mapper

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id1 = "id1_example"; // String | 
    String id2 = "id2_example"; // String | 
    ProtocolMapperRepresentation protocolMapperRepresentation = new ProtocolMapperRepresentation(); // ProtocolMapperRepresentation | 
    try {
      apiInstance.realmClientScopesId1ProtocolMappersModelsId2Put(realm, id1, id2, protocolMapperRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientScopesId1ProtocolMappersModelsId2Put");
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
| **id1** | **String**|  | |
| **id2** | **String**|  | |
| **protocolMapperRepresentation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdProtocolMappersAddModelsPost"></a>
# **realmClientScopesIdProtocolMappersAddModelsPost**
> realmClientScopesIdProtocolMappersAddModelsPost(realm, id, protocolMapperRepresentation)

Create multiple mappers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    List<ProtocolMapperRepresentation> protocolMapperRepresentation = Arrays.asList(); // List<ProtocolMapperRepresentation> | 
    try {
      apiInstance.realmClientScopesIdProtocolMappersAddModelsPost(realm, id, protocolMapperRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientScopesIdProtocolMappersAddModelsPost");
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
| **id** | **String**| id of client scope (not name) | |
| **protocolMapperRepresentation** | [**List&lt;ProtocolMapperRepresentation&gt;**](ProtocolMapperRepresentation.md)|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdProtocolMappersModelsGet"></a>
# **realmClientScopesIdProtocolMappersModelsGet**
> List&lt;ProtocolMapperRepresentation&gt; realmClientScopesIdProtocolMappersModelsGet(realm, id)

Get mappers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    try {
      List<ProtocolMapperRepresentation> result = apiInstance.realmClientScopesIdProtocolMappersModelsGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientScopesIdProtocolMappersModelsGet");
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
| **id** | **String**| id of client scope (not name) | |

### Return type

[**List&lt;ProtocolMapperRepresentation&gt;**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdProtocolMappersModelsPost"></a>
# **realmClientScopesIdProtocolMappersModelsPost**
> realmClientScopesIdProtocolMappersModelsPost(realm, id, protocolMapperRepresentation)

Create a mapper

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    ProtocolMapperRepresentation protocolMapperRepresentation = new ProtocolMapperRepresentation(); // ProtocolMapperRepresentation | 
    try {
      apiInstance.realmClientScopesIdProtocolMappersModelsPost(realm, id, protocolMapperRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientScopesIdProtocolMappersModelsPost");
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
| **id** | **String**| id of client scope (not name) | |
| **protocolMapperRepresentation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdProtocolMappersProtocolProtocolGet"></a>
# **realmClientScopesIdProtocolMappersProtocolProtocolGet**
> List&lt;ProtocolMapperRepresentation&gt; realmClientScopesIdProtocolMappersProtocolProtocolGet(realm, id, protocol)

Get mappers by name for a specific protocol

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    String protocol = "protocol_example"; // String | 
    try {
      List<ProtocolMapperRepresentation> result = apiInstance.realmClientScopesIdProtocolMappersProtocolProtocolGet(realm, id, protocol);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientScopesIdProtocolMappersProtocolProtocolGet");
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
| **id** | **String**| id of client scope (not name) | |
| **protocol** | **String**|  | |

### Return type

[**List&lt;ProtocolMapperRepresentation&gt;**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsId1ProtocolMappersModelsId2Delete"></a>
# **realmClientsId1ProtocolMappersModelsId2Delete**
> realmClientsId1ProtocolMappersModelsId2Delete(realm, id1, id2)

Delete the mapper

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id1 = "id1_example"; // String | 
    String id2 = "id2_example"; // String | 
    try {
      apiInstance.realmClientsId1ProtocolMappersModelsId2Delete(realm, id1, id2);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientsId1ProtocolMappersModelsId2Delete");
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
| **id1** | **String**|  | |
| **id2** | **String**|  | |

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

<a id="realmClientsId1ProtocolMappersModelsId2Get"></a>
# **realmClientsId1ProtocolMappersModelsId2Get**
> ProtocolMapperRepresentation realmClientsId1ProtocolMappersModelsId2Get(realm, id1, id2)

Get mapper by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id1 = "id1_example"; // String | 
    String id2 = "id2_example"; // String | 
    try {
      ProtocolMapperRepresentation result = apiInstance.realmClientsId1ProtocolMappersModelsId2Get(realm, id1, id2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientsId1ProtocolMappersModelsId2Get");
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
| **id1** | **String**|  | |
| **id2** | **String**|  | |

### Return type

[**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsId1ProtocolMappersModelsId2Put"></a>
# **realmClientsId1ProtocolMappersModelsId2Put**
> realmClientsId1ProtocolMappersModelsId2Put(realm, id1, id2, protocolMapperRepresentation)

Update the mapper

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id1 = "id1_example"; // String | 
    String id2 = "id2_example"; // String | 
    ProtocolMapperRepresentation protocolMapperRepresentation = new ProtocolMapperRepresentation(); // ProtocolMapperRepresentation | 
    try {
      apiInstance.realmClientsId1ProtocolMappersModelsId2Put(realm, id1, id2, protocolMapperRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientsId1ProtocolMappersModelsId2Put");
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
| **id1** | **String**|  | |
| **id2** | **String**|  | |
| **protocolMapperRepresentation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdProtocolMappersAddModelsPost"></a>
# **realmClientsIdProtocolMappersAddModelsPost**
> realmClientsIdProtocolMappersAddModelsPost(realm, id, protocolMapperRepresentation)

Create multiple mappers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    List<ProtocolMapperRepresentation> protocolMapperRepresentation = Arrays.asList(); // List<ProtocolMapperRepresentation> | 
    try {
      apiInstance.realmClientsIdProtocolMappersAddModelsPost(realm, id, protocolMapperRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientsIdProtocolMappersAddModelsPost");
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
| **id** | **String**| id of client (not client-id) | |
| **protocolMapperRepresentation** | [**List&lt;ProtocolMapperRepresentation&gt;**](ProtocolMapperRepresentation.md)|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdProtocolMappersModelsGet"></a>
# **realmClientsIdProtocolMappersModelsGet**
> List&lt;ProtocolMapperRepresentation&gt; realmClientsIdProtocolMappersModelsGet(realm, id)

Get mappers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      List<ProtocolMapperRepresentation> result = apiInstance.realmClientsIdProtocolMappersModelsGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientsIdProtocolMappersModelsGet");
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
| **id** | **String**| id of client (not client-id) | |

### Return type

[**List&lt;ProtocolMapperRepresentation&gt;**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdProtocolMappersModelsPost"></a>
# **realmClientsIdProtocolMappersModelsPost**
> realmClientsIdProtocolMappersModelsPost(realm, id, protocolMapperRepresentation)

Create a mapper

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    ProtocolMapperRepresentation protocolMapperRepresentation = new ProtocolMapperRepresentation(); // ProtocolMapperRepresentation | 
    try {
      apiInstance.realmClientsIdProtocolMappersModelsPost(realm, id, protocolMapperRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientsIdProtocolMappersModelsPost");
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
| **id** | **String**| id of client (not client-id) | |
| **protocolMapperRepresentation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdProtocolMappersProtocolProtocolGet"></a>
# **realmClientsIdProtocolMappersProtocolProtocolGet**
> List&lt;ProtocolMapperRepresentation&gt; realmClientsIdProtocolMappersProtocolProtocolGet(realm, id, protocol)

Get mappers by name for a specific protocol

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProtocolMappersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ProtocolMappersApi apiInstance = new ProtocolMappersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String protocol = "protocol_example"; // String | 
    try {
      List<ProtocolMapperRepresentation> result = apiInstance.realmClientsIdProtocolMappersProtocolProtocolGet(realm, id, protocol);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProtocolMappersApi#realmClientsIdProtocolMappersProtocolProtocolGet");
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
| **id** | **String**| id of client (not client-id) | |
| **protocol** | **String**|  | |

### Return type

[**List&lt;ProtocolMapperRepresentation&gt;**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

