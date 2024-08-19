# ProductDeploymentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productDeploymentsBootStrap**](ProductDeploymentsApi.md#productDeploymentsBootStrap) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/bootstrap |  |
| [**productDeploymentsDeploy**](ProductDeploymentsApi.md#productDeploymentsDeploy) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/deploy |  |
| [**productDeploymentsGet**](ProductDeploymentsApi.md#productDeploymentsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId} |  |
| [**productDeploymentsList**](ProductDeploymentsApi.md#productDeploymentsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments |  |
| [**productDeploymentsLock**](ProductDeploymentsApi.md#productDeploymentsLock) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/lock |  |
| [**productDeploymentsRemove**](ProductDeploymentsApi.md#productDeploymentsRemove) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/remove |  |
| [**productDeploymentsRotateSecrets**](ProductDeploymentsApi.md#productDeploymentsRotateSecrets) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/rotateSecrets |  |
| [**productDeploymentsUnlock**](ProductDeploymentsApi.md#productDeploymentsUnlock) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Deployment.Admin/locations/global/productDeployments/{productId}/unlock |  |


<a id="productDeploymentsBootStrap"></a>
# **productDeploymentsBootStrap**
> productDeploymentsBootStrap(subscriptionId, productId, apiVersion, bootstrapActionParameter)



Invokes bootstrap action on the product deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductDeploymentsApi apiInstance = new ProductDeploymentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String productId = "productId_example"; // String | The product identifier.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    ProductDeploymentsBootStrapRequest bootstrapActionParameter = new ProductDeploymentsBootStrapRequest(); // ProductDeploymentsBootStrapRequest | Represents bootstrap action parameter
    try {
      apiInstance.productDeploymentsBootStrap(subscriptionId, productId, apiVersion, bootstrapActionParameter);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDeploymentsApi#productDeploymentsBootStrap");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **productId** | **String**| The product identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |
| **bootstrapActionParameter** | [**ProductDeploymentsBootStrapRequest**](ProductDeploymentsBootStrapRequest.md)| Represents bootstrap action parameter | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **202** | ACCEPTED |  -  |

<a id="productDeploymentsDeploy"></a>
# **productDeploymentsDeploy**
> productDeploymentsDeploy(subscriptionId, productId, apiVersion, deployActionParameter)



Invokes deploy action on the product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductDeploymentsApi apiInstance = new ProductDeploymentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String productId = "productId_example"; // String | The product identifier.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    ProductDeploymentsDeployRequest deployActionParameter = new ProductDeploymentsDeployRequest(); // ProductDeploymentsDeployRequest | Represents bootstrap action parameter
    try {
      apiInstance.productDeploymentsDeploy(subscriptionId, productId, apiVersion, deployActionParameter);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDeploymentsApi#productDeploymentsDeploy");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **productId** | **String**| The product identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |
| **deployActionParameter** | [**ProductDeploymentsDeployRequest**](ProductDeploymentsDeployRequest.md)| Represents bootstrap action parameter | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **202** | ACCEPTED |  -  |

<a id="productDeploymentsGet"></a>
# **productDeploymentsGet**
> ProductDeploymentResourceEntity productDeploymentsGet(subscriptionId, apiVersion, productId)



Invokes bootstrap action on the product deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductDeploymentsApi apiInstance = new ProductDeploymentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    String productId = "productId_example"; // String | The product identifier.
    try {
      ProductDeploymentResourceEntity result = apiInstance.productDeploymentsGet(subscriptionId, apiVersion, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDeploymentsApi#productDeploymentsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |
| **productId** | **String**| The product identifier. | |

### Return type

[**ProductDeploymentResourceEntity**](ProductDeploymentResourceEntity.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **404** | NOT FOUND |  -  |

<a id="productDeploymentsList"></a>
# **productDeploymentsList**
> ProductDeploymentsList productDeploymentsList(subscriptionId, apiVersion)



Invokes bootstrap action on the product deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductDeploymentsApi apiInstance = new ProductDeploymentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    try {
      ProductDeploymentsList result = apiInstance.productDeploymentsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDeploymentsApi#productDeploymentsList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |

### Return type

[**ProductDeploymentsList**](ProductDeploymentsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |

<a id="productDeploymentsLock"></a>
# **productDeploymentsLock**
> productDeploymentsLock(subscriptionId, productId, apiVersion)



locks the product subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductDeploymentsApi apiInstance = new ProductDeploymentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String productId = "productId_example"; // String | The product identifier.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    try {
      apiInstance.productDeploymentsLock(subscriptionId, productId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDeploymentsApi#productDeploymentsLock");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **productId** | **String**| The product identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productDeploymentsRemove"></a>
# **productDeploymentsRemove**
> productDeploymentsRemove(subscriptionId, productId, apiVersion)



Invokes remove action on the product deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductDeploymentsApi apiInstance = new ProductDeploymentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String productId = "productId_example"; // String | The product identifier.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    try {
      apiInstance.productDeploymentsRemove(subscriptionId, productId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDeploymentsApi#productDeploymentsRemove");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **productId** | **String**| The product identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **202** | ACCEPTED |  -  |

<a id="productDeploymentsRotateSecrets"></a>
# **productDeploymentsRotateSecrets**
> productDeploymentsRotateSecrets(subscriptionId, productId, apiVersion)



Invokes rotate secrets action on the product deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductDeploymentsApi apiInstance = new ProductDeploymentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String productId = "productId_example"; // String | The product identifier.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    try {
      apiInstance.productDeploymentsRotateSecrets(subscriptionId, productId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDeploymentsApi#productDeploymentsRotateSecrets");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **productId** | **String**| The product identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | ACCEPTED |  -  |

<a id="productDeploymentsUnlock"></a>
# **productDeploymentsUnlock**
> productDeploymentsUnlock(subscriptionId, productId, apiVersion, unlockActionParameter)



Unlocks the product subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductDeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ProductDeploymentsApi apiInstance = new ProductDeploymentsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String productId = "productId_example"; // String | The product identifier.
    String apiVersion = "2019-01-01"; // String | Client API Version.
    ProductDeploymentsUnlockRequest unlockActionParameter = new ProductDeploymentsUnlockRequest(); // ProductDeploymentsUnlockRequest | Represents bootstrap action parameter
    try {
      apiInstance.productDeploymentsUnlock(subscriptionId, productId, apiVersion, unlockActionParameter);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductDeploymentsApi#productDeploymentsUnlock");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **productId** | **String**| The product identifier. | |
| **apiVersion** | **String**| Client API Version. | [default to 2019-01-01] |
| **unlockActionParameter** | [**ProductDeploymentsUnlockRequest**](ProductDeploymentsUnlockRequest.md)| Represents bootstrap action parameter | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

