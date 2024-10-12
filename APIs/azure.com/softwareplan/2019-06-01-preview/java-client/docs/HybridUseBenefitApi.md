# HybridUseBenefitApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hybridUseBenefitCreate**](HybridUseBenefitApi.md#hybridUseBenefitCreate) | **PUT** /{scope}/providers/Microsoft.SoftwarePlan/hybridUseBenefits/{planId} |  |
| [**hybridUseBenefitDelete**](HybridUseBenefitApi.md#hybridUseBenefitDelete) | **DELETE** /{scope}/providers/Microsoft.SoftwarePlan/hybridUseBenefits/{planId} |  |
| [**hybridUseBenefitGet**](HybridUseBenefitApi.md#hybridUseBenefitGet) | **GET** /{scope}/providers/Microsoft.SoftwarePlan/hybridUseBenefits/{planId} |  |
| [**hybridUseBenefitUpdate**](HybridUseBenefitApi.md#hybridUseBenefitUpdate) | **PATCH** /{scope}/providers/Microsoft.SoftwarePlan/hybridUseBenefits/{planId} |  |


<a id="hybridUseBenefitCreate"></a>
# **hybridUseBenefitCreate**
> HybridUseBenefitModel hybridUseBenefitCreate(scope, planId, apiVersion, body)



Create a new hybrid use benefit under a given scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridUseBenefitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridUseBenefitApi apiInstance = new HybridUseBenefitApi(defaultClient);
    String scope = "scope_example"; // String | The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    String planId = "planId_example"; // String | This is a unique identifier for a plan. Should be a guid.
    String apiVersion = "apiVersion_example"; // String | The api-version to be used by the service
    HybridUseBenefitModel body = new HybridUseBenefitModel(); // HybridUseBenefitModel | Request body for creating a hybrid use benefit
    try {
      HybridUseBenefitModel result = apiInstance.hybridUseBenefitCreate(scope, planId, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridUseBenefitApi#hybridUseBenefitCreate");
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
| **scope** | **String**| The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now | |
| **planId** | **String**| This is a unique identifier for a plan. Should be a guid. | |
| **apiVersion** | **String**| The api-version to be used by the service | |
| **body** | [**HybridUseBenefitModel**](HybridUseBenefitModel.md)| Request body for creating a hybrid use benefit | |

### Return type

[**HybridUseBenefitModel**](HybridUseBenefitModel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - returns the plan that is created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hybridUseBenefitDelete"></a>
# **hybridUseBenefitDelete**
> hybridUseBenefitDelete(scope, planId, apiVersion)



Deletes a given plan ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridUseBenefitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridUseBenefitApi apiInstance = new HybridUseBenefitApi(defaultClient);
    String scope = "scope_example"; // String | The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    String planId = "planId_example"; // String | This is a unique identifier for a plan. Should be a guid.
    String apiVersion = "apiVersion_example"; // String | The api-version to be used by the service
    try {
      apiInstance.hybridUseBenefitDelete(scope, planId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridUseBenefitApi#hybridUseBenefitDelete");
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
| **scope** | **String**| The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now | |
| **planId** | **String**| This is a unique identifier for a plan. Should be a guid. | |
| **apiVersion** | **String**| The api-version to be used by the service | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - successfully deleted the given plan |  -  |
| **204** | OK - there was no plan to delete |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hybridUseBenefitGet"></a>
# **hybridUseBenefitGet**
> HybridUseBenefitModel hybridUseBenefitGet(scope, planId, apiVersion)



Gets a given plan ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridUseBenefitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridUseBenefitApi apiInstance = new HybridUseBenefitApi(defaultClient);
    String scope = "scope_example"; // String | The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    String planId = "planId_example"; // String | This is a unique identifier for a plan. Should be a guid.
    String apiVersion = "apiVersion_example"; // String | The api-version to be used by the service
    try {
      HybridUseBenefitModel result = apiInstance.hybridUseBenefitGet(scope, planId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridUseBenefitApi#hybridUseBenefitGet");
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
| **scope** | **String**| The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now | |
| **planId** | **String**| This is a unique identifier for a plan. Should be a guid. | |
| **apiVersion** | **String**| The api-version to be used by the service | |

### Return type

[**HybridUseBenefitModel**](HybridUseBenefitModel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - returns the plan that is created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hybridUseBenefitUpdate"></a>
# **hybridUseBenefitUpdate**
> HybridUseBenefitModel hybridUseBenefitUpdate(scope, planId, apiVersion, body)



Updates an existing hybrid use benefit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridUseBenefitApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridUseBenefitApi apiInstance = new HybridUseBenefitApi(defaultClient);
    String scope = "scope_example"; // String | The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    String planId = "planId_example"; // String | This is a unique identifier for a plan. Should be a guid.
    String apiVersion = "apiVersion_example"; // String | The api-version to be used by the service
    HybridUseBenefitModel body = new HybridUseBenefitModel(); // HybridUseBenefitModel | Request body for creating a hybrid use benefit
    try {
      HybridUseBenefitModel result = apiInstance.hybridUseBenefitUpdate(scope, planId, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridUseBenefitApi#hybridUseBenefitUpdate");
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
| **scope** | **String**| The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now | |
| **planId** | **String**| This is a unique identifier for a plan. Should be a guid. | |
| **apiVersion** | **String**| The api-version to be used by the service | |
| **body** | [**HybridUseBenefitModel**](HybridUseBenefitModel.md)| Request body for creating a hybrid use benefit | |

### Return type

[**HybridUseBenefitModel**](HybridUseBenefitModel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - successfully updated the given hybrid use benefit |  -  |
| **0** | Error response describing why the operation failed. |  -  |

