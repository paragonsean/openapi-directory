# ComponentApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmComponentsGet**](ComponentApi.md#realmComponentsGet) | **GET** /{realm}/components |  |
| [**realmComponentsIdDelete**](ComponentApi.md#realmComponentsIdDelete) | **DELETE** /{realm}/components/{id} |  |
| [**realmComponentsIdGet**](ComponentApi.md#realmComponentsIdGet) | **GET** /{realm}/components/{id} |  |
| [**realmComponentsIdPut**](ComponentApi.md#realmComponentsIdPut) | **PUT** /{realm}/components/{id} |  |
| [**realmComponentsIdSubComponentTypesGet**](ComponentApi.md#realmComponentsIdSubComponentTypesGet) | **GET** /{realm}/components/{id}/sub-component-types | List of subcomponent types that are available to configure for a particular parent component. |
| [**realmComponentsPost**](ComponentApi.md#realmComponentsPost) | **POST** /{realm}/components |  |


<a id="realmComponentsGet"></a>
# **realmComponentsGet**
> List&lt;ComponentRepresentation&gt; realmComponentsGet(realm, name, parent, type)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComponentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ComponentApi apiInstance = new ComponentApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String name = "name_example"; // String | 
    String parent = "parent_example"; // String | 
    String type = "type_example"; // String | 
    try {
      List<ComponentRepresentation> result = apiInstance.realmComponentsGet(realm, name, parent, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComponentApi#realmComponentsGet");
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
| **name** | **String**|  | [optional] |
| **parent** | **String**|  | [optional] |
| **type** | **String**|  | [optional] |

### Return type

[**List&lt;ComponentRepresentation&gt;**](ComponentRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmComponentsIdDelete"></a>
# **realmComponentsIdDelete**
> realmComponentsIdDelete(realm, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComponentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ComponentApi apiInstance = new ComponentApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    try {
      apiInstance.realmComponentsIdDelete(realm, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComponentApi#realmComponentsIdDelete");
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

<a id="realmComponentsIdGet"></a>
# **realmComponentsIdGet**
> ComponentRepresentation realmComponentsIdGet(realm, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComponentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ComponentApi apiInstance = new ComponentApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    try {
      ComponentRepresentation result = apiInstance.realmComponentsIdGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComponentApi#realmComponentsIdGet");
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

[**ComponentRepresentation**](ComponentRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmComponentsIdPut"></a>
# **realmComponentsIdPut**
> realmComponentsIdPut(realm, id, componentRepresentation)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComponentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ComponentApi apiInstance = new ComponentApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    ComponentRepresentation componentRepresentation = new ComponentRepresentation(); // ComponentRepresentation | 
    try {
      apiInstance.realmComponentsIdPut(realm, id, componentRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComponentApi#realmComponentsIdPut");
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
| **componentRepresentation** | [**ComponentRepresentation**](ComponentRepresentation.md)|  | |

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

<a id="realmComponentsIdSubComponentTypesGet"></a>
# **realmComponentsIdSubComponentTypesGet**
> List&lt;ComponentTypeRepresentation&gt; realmComponentsIdSubComponentTypesGet(realm, id, type)

List of subcomponent types that are available to configure for a particular parent component.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComponentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ComponentApi apiInstance = new ComponentApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    String type = "type_example"; // String | 
    try {
      List<ComponentTypeRepresentation> result = apiInstance.realmComponentsIdSubComponentTypesGet(realm, id, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComponentApi#realmComponentsIdSubComponentTypesGet");
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
| **type** | **String**|  | [optional] |

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

<a id="realmComponentsPost"></a>
# **realmComponentsPost**
> realmComponentsPost(realm, componentRepresentation)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComponentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ComponentApi apiInstance = new ComponentApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    ComponentRepresentation componentRepresentation = new ComponentRepresentation(); // ComponentRepresentation | 
    try {
      apiInstance.realmComponentsPost(realm, componentRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComponentApi#realmComponentsPost");
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
| **componentRepresentation** | [**ComponentRepresentation**](ComponentRepresentation.md)|  | |

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

