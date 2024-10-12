# DeployApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelSiteDeploy**](DeployApi.md#cancelSiteDeploy) | **POST** /deploys/{deploy_id}/cancel |  |
| [**createSiteDeploy**](DeployApi.md#createSiteDeploy) | **POST** /sites/{site_id}/deploys |  |
| [**deleteDeploy**](DeployApi.md#deleteDeploy) | **DELETE** /deploys/{deploy_id} |  |
| [**deleteSiteDeploy**](DeployApi.md#deleteSiteDeploy) | **DELETE** /sites/{site_id}/deploys/{deploy_id} |  |
| [**getDeploy**](DeployApi.md#getDeploy) | **GET** /deploys/{deploy_id} |  |
| [**getSiteDeploy**](DeployApi.md#getSiteDeploy) | **GET** /sites/{site_id}/deploys/{deploy_id} |  |
| [**listSiteDeploys**](DeployApi.md#listSiteDeploys) | **GET** /sites/{site_id}/deploys |  |
| [**lockDeploy**](DeployApi.md#lockDeploy) | **POST** /deploys/{deploy_id}/lock |  |
| [**restoreSiteDeploy**](DeployApi.md#restoreSiteDeploy) | **POST** /sites/{site_id}/deploys/{deploy_id}/restore |  |
| [**rollbackSiteDeploy**](DeployApi.md#rollbackSiteDeploy) | **PUT** /sites/{site_id}/rollback |  |
| [**unlockDeploy**](DeployApi.md#unlockDeploy) | **POST** /deploys/{deploy_id}/unlock |  |
| [**updateSiteDeploy**](DeployApi.md#updateSiteDeploy) | **PUT** /sites/{site_id}/deploys/{deploy_id} |  |


<a id="cancelSiteDeploy"></a>
# **cancelSiteDeploy**
> Deploy cancelSiteDeploy(deployId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String deployId = "deployId_example"; // String | 
    try {
      Deploy result = apiInstance.cancelSiteDeploy(deployId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#cancelSiteDeploy");
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
| **deployId** | **String**|  | |

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Cancelled |  -  |
| **0** | error |  -  |

<a id="createSiteDeploy"></a>
# **createSiteDeploy**
> Deploy createSiteDeploy(siteId, deploy, deployPreviews, production, state, branch, latestPublished, title)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    DeployFiles deploy = new DeployFiles(); // DeployFiles | 
    Boolean deployPreviews = true; // Boolean | 
    Boolean production = true; // Boolean | 
    String state = "new"; // String | 
    String branch = "branch_example"; // String | 
    Boolean latestPublished = true; // Boolean | 
    String title = "title_example"; // String | 
    try {
      Deploy result = apiInstance.createSiteDeploy(siteId, deploy, deployPreviews, production, state, branch, latestPublished, title);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#createSiteDeploy");
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
| **siteId** | **String**|  | |
| **deploy** | [**DeployFiles**](DeployFiles.md)|  | |
| **deployPreviews** | **Boolean**|  | [optional] |
| **production** | **Boolean**|  | [optional] |
| **state** | **String**|  | [optional] [enum: new, pending_review, accepted, rejected, enqueued, building, uploading, uploaded, preparing, prepared, processing, ready, error, retrying] |
| **branch** | **String**|  | [optional] |
| **latestPublished** | **Boolean**|  | [optional] |
| **title** | **String**|  | [optional] |

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="deleteDeploy"></a>
# **deleteDeploy**
> deleteDeploy(deployId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String deployId = "deployId_example"; // String | 
    try {
      apiInstance.deleteDeploy(deployId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#deleteDeploy");
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
| **deployId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | error |  -  |

<a id="deleteSiteDeploy"></a>
# **deleteSiteDeploy**
> deleteSiteDeploy(deployId, siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String deployId = "deployId_example"; // String | 
    String siteId = "siteId_example"; // String | 
    try {
      apiInstance.deleteSiteDeploy(deployId, siteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#deleteSiteDeploy");
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
| **deployId** | **String**|  | |
| **siteId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | error |  -  |

<a id="getDeploy"></a>
# **getDeploy**
> Deploy getDeploy(deployId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String deployId = "deployId_example"; // String | 
    try {
      Deploy result = apiInstance.getDeploy(deployId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#getDeploy");
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
| **deployId** | **String**|  | |

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="getSiteDeploy"></a>
# **getSiteDeploy**
> Deploy getSiteDeploy(siteId, deployId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String deployId = "deployId_example"; // String | 
    try {
      Deploy result = apiInstance.getSiteDeploy(siteId, deployId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#getSiteDeploy");
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
| **siteId** | **String**|  | |
| **deployId** | **String**|  | |

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="listSiteDeploys"></a>
# **listSiteDeploys**
> List&lt;Deploy&gt; listSiteDeploys(siteId, deployPreviews, production, state, branch, latestPublished, page, perPage)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    Boolean deployPreviews = true; // Boolean | 
    Boolean production = true; // Boolean | 
    String state = "new"; // String | 
    String branch = "branch_example"; // String | 
    Boolean latestPublished = true; // Boolean | 
    Integer page = 56; // Integer | 
    Integer perPage = 56; // Integer | 
    try {
      List<Deploy> result = apiInstance.listSiteDeploys(siteId, deployPreviews, production, state, branch, latestPublished, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#listSiteDeploys");
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
| **siteId** | **String**|  | |
| **deployPreviews** | **Boolean**|  | [optional] |
| **production** | **Boolean**|  | [optional] |
| **state** | **String**|  | [optional] [enum: new, pending_review, accepted, rejected, enqueued, building, uploading, uploaded, preparing, prepared, processing, ready, error, retrying] |
| **branch** | **String**|  | [optional] |
| **latestPublished** | **Boolean**|  | [optional] |
| **page** | **Integer**|  | [optional] |
| **perPage** | **Integer**|  | [optional] |

### Return type

[**List&lt;Deploy&gt;**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="lockDeploy"></a>
# **lockDeploy**
> Deploy lockDeploy(deployId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String deployId = "deployId_example"; // String | 
    try {
      Deploy result = apiInstance.lockDeploy(deployId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#lockDeploy");
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
| **deployId** | **String**|  | |

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="restoreSiteDeploy"></a>
# **restoreSiteDeploy**
> Deploy restoreSiteDeploy(siteId, deployId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String deployId = "deployId_example"; // String | 
    try {
      Deploy result = apiInstance.restoreSiteDeploy(siteId, deployId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#restoreSiteDeploy");
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
| **siteId** | **String**|  | |
| **deployId** | **String**|  | |

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | error |  -  |

<a id="rollbackSiteDeploy"></a>
# **rollbackSiteDeploy**
> rollbackSiteDeploy(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      apiInstance.rollbackSiteDeploy(siteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#rollbackSiteDeploy");
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
| **siteId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | error |  -  |

<a id="unlockDeploy"></a>
# **unlockDeploy**
> Deploy unlockDeploy(deployId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String deployId = "deployId_example"; // String | 
    try {
      Deploy result = apiInstance.unlockDeploy(deployId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#unlockDeploy");
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
| **deployId** | **String**|  | |

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="updateSiteDeploy"></a>
# **updateSiteDeploy**
> Deploy updateSiteDeploy(siteId, deployId, deploy)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeployApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    DeployApi apiInstance = new DeployApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String deployId = "deployId_example"; // String | 
    DeployFiles deploy = new DeployFiles(); // DeployFiles | 
    try {
      Deploy result = apiInstance.updateSiteDeploy(siteId, deployId, deploy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeployApi#updateSiteDeploy");
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
| **siteId** | **String**|  | |
| **deployId** | **String**|  | |
| **deploy** | [**DeployFiles**](DeployFiles.md)|  | |

### Return type

[**Deploy**](Deploy.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

