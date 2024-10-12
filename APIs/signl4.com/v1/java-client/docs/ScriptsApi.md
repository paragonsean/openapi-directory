# ScriptsApi

All URIs are relative to *https://connect.signl4.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scriptsInstancesGet**](ScriptsApi.md#scriptsInstancesGet) | **GET** /scripts/instances | Returns all script instances of the SIGNL4 team |
| [**scriptsInstancesInstanceIdDataPut**](ScriptsApi.md#scriptsInstancesInstanceIdDataPut) | **PUT** /scripts/instances/{instanceId}/data | Updates custom data of a given script instance which includes its display name. |
| [**scriptsInstancesInstanceIdDelete**](ScriptsApi.md#scriptsInstancesInstanceIdDelete) | **DELETE** /scripts/instances/{instanceId} | Deletes a script instance. |
| [**scriptsInstancesInstanceIdDisablePost**](ScriptsApi.md#scriptsInstancesInstanceIdDisablePost) | **POST** /scripts/instances/{instanceId}/disable | Disables a given script instance. |
| [**scriptsInstancesInstanceIdEnablePost**](ScriptsApi.md#scriptsInstancesInstanceIdEnablePost) | **POST** /scripts/instances/{instanceId}/enable | Enables a script instance. |
| [**scriptsInstancesInstanceIdGet**](ScriptsApi.md#scriptsInstancesInstanceIdGet) | **GET** /scripts/instances/{instanceId} | Returns all information about a given script instance which includes its runtime status. |
| [**scriptsInstancesInstanceIdPut**](ScriptsApi.md#scriptsInstancesInstanceIdPut) | **PUT** /scripts/instances/{instanceId} | Updates a given script instance, typically used for updating the configuration of a script. |
| [**scriptsInstancesPost**](ScriptsApi.md#scriptsInstancesPost) | **POST** /scripts/instances | Creates a new script instance in the in the SIGNL4 team. |
| [**scriptsInventoryGet**](ScriptsApi.md#scriptsInventoryGet) | **GET** /scripts/inventory | Returns all available inventory scripts which can be added to a SIGNL4 subscription. |
| [**scriptsInventoryParsedGet**](ScriptsApi.md#scriptsInventoryParsedGet) | **GET** /scripts/inventory/parsed | Returns all inventory scripts. |
| [**scriptsInventoryParsedScriptIdGet**](ScriptsApi.md#scriptsInventoryParsedScriptIdGet) | **GET** /scripts/inventory/parsed/{scriptId} | Returns an inventory script by its id. |


<a id="scriptsInstancesGet"></a>
# **scriptsInstancesGet**
> List&lt;ScriptInstanceDetails&gt; scriptsInstancesGet(teamId)

Returns all script instances of the SIGNL4 team

Returns all script instances in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String teamId = "teamId_example"; // String | 
    try {
      List<ScriptInstanceDetails> result = apiInstance.scriptsInstancesGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#scriptsInstancesGet");
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
| **teamId** | **String**|  | [optional] |

### Return type

[**List&lt;ScriptInstanceDetails&gt;**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |

<a id="scriptsInstancesInstanceIdDataPut"></a>
# **scriptsInstancesInstanceIdDataPut**
> ScriptInstanceDetails scriptsInstancesInstanceIdDataPut(instanceId, scriptInstanceCustomUserData)

Updates custom data of a given script instance which includes its display name.

Updates the specified script instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String instanceId = "instanceId_example"; // String | InstanceId of the script to be updated.
    ScriptInstanceCustomUserData scriptInstanceCustomUserData = new ScriptInstanceCustomUserData(); // ScriptInstanceCustomUserData | Script instance to be updated.
    try {
      ScriptInstanceDetails result = apiInstance.scriptsInstancesInstanceIdDataPut(instanceId, scriptInstanceCustomUserData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#scriptsInstancesInstanceIdDataPut");
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
| **instanceId** | **String**| InstanceId of the script to be updated. | |
| **scriptInstanceCustomUserData** | [**ScriptInstanceCustomUserData**](ScriptInstanceCustomUserData.md)| Script instance to be updated. | [optional] |

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | An internal error has occurred during instance creation. |  -  |

<a id="scriptsInstancesInstanceIdDelete"></a>
# **scriptsInstancesInstanceIdDelete**
> scriptsInstancesInstanceIdDelete(instanceId)

Deletes a script instance.

Gets the script instance specified by the passed instance id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String instanceId = "instanceId_example"; // String | Instance Id of script instance to be returned.
    try {
      apiInstance.scriptsInstancesInstanceIdDelete(instanceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#scriptsInstancesInstanceIdDelete");
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
| **instanceId** | **String**| Instance Id of script instance to be returned. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database or in memory. |  -  |

<a id="scriptsInstancesInstanceIdDisablePost"></a>
# **scriptsInstancesInstanceIdDisablePost**
> ScriptInstanceDetails scriptsInstancesInstanceIdDisablePost(instanceId)

Disables a given script instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String instanceId = "instanceId_example"; // String | Id of the instance to be disabled.
    try {
      ScriptInstanceDetails result = apiInstance.scriptsInstancesInstanceIdDisablePost(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#scriptsInstancesInstanceIdDisablePost");
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
| **instanceId** | **String**| Id of the instance to be disabled. | |

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="scriptsInstancesInstanceIdEnablePost"></a>
# **scriptsInstancesInstanceIdEnablePost**
> ScriptInstanceDetails scriptsInstancesInstanceIdEnablePost(instanceId)

Enables a script instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String instanceId = "instanceId_example"; // String | Id of the instance to be enabled.
    try {
      ScriptInstanceDetails result = apiInstance.scriptsInstancesInstanceIdEnablePost(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#scriptsInstancesInstanceIdEnablePost");
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
| **instanceId** | **String**| Id of the instance to be enabled. | |

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

<a id="scriptsInstancesInstanceIdGet"></a>
# **scriptsInstancesInstanceIdGet**
> ScriptInstanceDetails scriptsInstancesInstanceIdGet(instanceId)

Returns all information about a given script instance which includes its runtime status.

Gets the script instance specified by the passed instance id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String instanceId = "instanceId_example"; // String | Instance Id of script instance to be returned.
    try {
      ScriptInstanceDetails result = apiInstance.scriptsInstancesInstanceIdGet(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#scriptsInstancesInstanceIdGet");
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
| **instanceId** | **String**| Instance Id of script instance to be returned. | |

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database or in memory. |  -  |

<a id="scriptsInstancesInstanceIdPut"></a>
# **scriptsInstancesInstanceIdPut**
> ScriptInstanceDetails scriptsInstancesInstanceIdPut(instanceId, scriptInstanceDetails)

Updates a given script instance, typically used for updating the configuration of a script.

Updates the specified script instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String instanceId = "instanceId_example"; // String | InstanceId of the script to be updated.
    ScriptInstanceDetails scriptInstanceDetails = new ScriptInstanceDetails(); // ScriptInstanceDetails | Script instance to be updated.
    try {
      ScriptInstanceDetails result = apiInstance.scriptsInstancesInstanceIdPut(instanceId, scriptInstanceDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#scriptsInstancesInstanceIdPut");
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
| **instanceId** | **String**| InstanceId of the script to be updated. | |
| **scriptInstanceDetails** | [**ScriptInstanceDetails**](ScriptInstanceDetails.md)| Script instance to be updated. | [optional] |

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | An internal error has occurred during instance creation. |  -  |

<a id="scriptsInstancesPost"></a>
# **scriptsInstancesPost**
> ScriptInstanceDetails scriptsInstancesPost(scriptInstanceDetails)

Creates a new script instance in the in the SIGNL4 team.

Creates a new script instance of the script specified in the request body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    ScriptInstanceDetails scriptInstanceDetails = new ScriptInstanceDetails(); // ScriptInstanceDetails | Script instance to be created.
    try {
      ScriptInstanceDetails result = apiInstance.scriptsInstancesPost(scriptInstanceDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#scriptsInstancesPost");
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
| **scriptInstanceDetails** | [**ScriptInstanceDetails**](ScriptInstanceDetails.md)| Script instance to be created. | [optional] |

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Existing script instance was updated as specified in body. |  -  |
| **201** | New script instance was updated as specified in body. |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | An internal error has occurred during instance creation. |  -  |

<a id="scriptsInventoryGet"></a>
# **scriptsInventoryGet**
> List&lt;InventoryScriptInfo&gt; scriptsInventoryGet()

Returns all available inventory scripts which can be added to a SIGNL4 subscription.

Returns all available inventory scripts which can be added to a SIGNL4 subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    try {
      List<InventoryScriptInfo> result = apiInstance.scriptsInventoryGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#scriptsInventoryGet");
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

[**List&lt;InventoryScriptInfo&gt;**](InventoryScriptInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **500** | An internal error orccurred while loading all inventory scripts. |  -  |

<a id="scriptsInventoryParsedGet"></a>
# **scriptsInventoryParsedGet**
> List&lt;InventoryScriptInfo&gt; scriptsInventoryParsedGet(language)

Returns all inventory scripts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String language = "language_example"; // String | 
    try {
      List<InventoryScriptInfo> result = apiInstance.scriptsInventoryParsedGet(language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#scriptsInventoryParsedGet");
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
| **language** | **String**|  | [optional] |

### Return type

[**List&lt;InventoryScriptInfo&gt;**](InventoryScriptInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **500** | Server Error |  -  |

<a id="scriptsInventoryParsedScriptIdGet"></a>
# **scriptsInventoryParsedScriptIdGet**
> ScriptInstanceDetails scriptsInventoryParsedScriptIdGet(scriptId, language)

Returns an inventory script by its id.

Gets the script specified by the passed script id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScriptsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ScriptsApi apiInstance = new ScriptsApi(defaultClient);
    String scriptId = "scriptId_example"; // String | The Id of the script to be returned.
    String language = "language_example"; // String | 
    try {
      ScriptInstanceDetails result = apiInstance.scriptsInventoryParsedScriptIdGet(scriptId, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScriptsApi#scriptsInventoryParsedScriptIdGet");
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
| **scriptId** | **String**| The Id of the script to be returned. | |
| **language** | **String**|  | [optional] |

### Return type

[**ScriptInstanceDetails**](ScriptInstanceDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database or in memory. |  -  |

