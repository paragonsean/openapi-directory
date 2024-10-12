# InformationProtectionPoliciesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**informationProtectionPoliciesCreateOrUpdate**](InformationProtectionPoliciesApi.md#informationProtectionPoliciesCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.Security/informationProtectionPolicies/{informationProtectionPolicyName} |  |
| [**informationProtectionPoliciesGet**](InformationProtectionPoliciesApi.md#informationProtectionPoliciesGet) | **GET** /{scope}/providers/Microsoft.Security/informationProtectionPolicies/{informationProtectionPolicyName} |  |
| [**informationProtectionPoliciesList**](InformationProtectionPoliciesApi.md#informationProtectionPoliciesList) | **GET** /{scope}/providers/Microsoft.Security/informationProtectionPolicies |  |


<a id="informationProtectionPoliciesCreateOrUpdate"></a>
# **informationProtectionPoliciesCreateOrUpdate**
> InformationProtectionPolicy informationProtectionPoliciesCreateOrUpdate(apiVersion, scope, informationProtectionPolicyName)



Details of the information protection policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InformationProtectionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InformationProtectionPoliciesApi apiInstance = new InformationProtectionPoliciesApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String scope = "scope_example"; // String | Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    String informationProtectionPolicyName = "effective"; // String | Name of the information protection policy.
    try {
      InformationProtectionPolicy result = apiInstance.informationProtectionPoliciesCreateOrUpdate(apiVersion, scope, informationProtectionPolicyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InformationProtectionPoliciesApi#informationProtectionPoliciesCreateOrUpdate");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **scope** | **String**| Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName). | |
| **informationProtectionPolicyName** | **String**| Name of the information protection policy. | [enum: effective, custom] |

### Return type

[**InformationProtectionPolicy**](InformationProtectionPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="informationProtectionPoliciesGet"></a>
# **informationProtectionPoliciesGet**
> InformationProtectionPolicy informationProtectionPoliciesGet(apiVersion, scope, informationProtectionPolicyName)



Details of the information protection policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InformationProtectionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InformationProtectionPoliciesApi apiInstance = new InformationProtectionPoliciesApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String scope = "scope_example"; // String | Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    String informationProtectionPolicyName = "effective"; // String | Name of the information protection policy.
    try {
      InformationProtectionPolicy result = apiInstance.informationProtectionPoliciesGet(apiVersion, scope, informationProtectionPolicyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InformationProtectionPoliciesApi#informationProtectionPoliciesGet");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **scope** | **String**| Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName). | |
| **informationProtectionPolicyName** | **String**| Name of the information protection policy. | [enum: effective, custom] |

### Return type

[**InformationProtectionPolicy**](InformationProtectionPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="informationProtectionPoliciesList"></a>
# **informationProtectionPoliciesList**
> InformationProtectionPolicyList informationProtectionPoliciesList(apiVersion, scope)



Information protection policies of a specific management group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InformationProtectionPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InformationProtectionPoliciesApi apiInstance = new InformationProtectionPoliciesApi(defaultClient);
    String apiVersion = "2017-08-01-preview"; // String | API version for the operation
    String scope = "scope_example"; // String | Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName).
    try {
      InformationProtectionPolicyList result = apiInstance.informationProtectionPoliciesList(apiVersion, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InformationProtectionPoliciesApi#informationProtectionPoliciesList");
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
| **apiVersion** | **String**| API version for the operation | [enum: 2017-08-01-preview] |
| **scope** | **String**| Scope of the query, can be subscription (/subscriptions/0b06d9ea-afe6-4779-bd59-30e5c2d9d13f) or management group (/providers/Microsoft.Management/managementGroups/mgName). | |

### Return type

[**InformationProtectionPolicyList**](InformationProtectionPolicyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

