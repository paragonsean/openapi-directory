# ExternalSubscriptionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**externalSubscriptionGet**](ExternalSubscriptionsApi.md#externalSubscriptionGet) | **GET** /providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName} |  |
| [**externalSubscriptionList**](ExternalSubscriptionsApi.md#externalSubscriptionList) | **GET** /providers/Microsoft.CostManagement/externalSubscriptions |  |
| [**externalSubscriptionListByExternalBillingAccount**](ExternalSubscriptionsApi.md#externalSubscriptionListByExternalBillingAccount) | **GET** /providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}/externalSubscriptions |  |
| [**externalSubscriptionListByManagementGroup**](ExternalSubscriptionsApi.md#externalSubscriptionListByManagementGroup) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/externalSubscriptions |  |
| [**externalSubscriptionUpdateManagementGroup**](ExternalSubscriptionsApi.md#externalSubscriptionUpdateManagementGroup) | **PUT** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName} |  |


<a id="externalSubscriptionGet"></a>
# **externalSubscriptionGet**
> ExternalSubscriptionDefinition externalSubscriptionGet(apiVersion, externalSubscriptionName, $expand)



Get an ExternalSubscription definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExternalSubscriptionsApi apiInstance = new ExternalSubscriptionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String externalSubscriptionName = "externalSubscriptionName_example"; // String | External Subscription Name. (eg 'aws-{UsageAccountId}')
    String $expand = "$expand_example"; // String | May be used to expand the collectionInfo property. By default, collectionInfo is not included.
    try {
      ExternalSubscriptionDefinition result = apiInstance.externalSubscriptionGet(apiVersion, externalSubscriptionName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalSubscriptionsApi#externalSubscriptionGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |
| **externalSubscriptionName** | **String**| External Subscription Name. (eg &#39;aws-{UsageAccountId}&#39;) | |
| **$expand** | **String**| May be used to expand the collectionInfo property. By default, collectionInfo is not included. | [optional] |

### Return type

[**ExternalSubscriptionDefinition**](ExternalSubscriptionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="externalSubscriptionList"></a>
# **externalSubscriptionList**
> ExternalSubscriptionDefinitionListResult externalSubscriptionList(apiVersion)



List all ExternalSubscription definitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExternalSubscriptionsApi apiInstance = new ExternalSubscriptionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    try {
      ExternalSubscriptionDefinitionListResult result = apiInstance.externalSubscriptionList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalSubscriptionsApi#externalSubscriptionList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |

### Return type

[**ExternalSubscriptionDefinitionListResult**](ExternalSubscriptionDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="externalSubscriptionListByExternalBillingAccount"></a>
# **externalSubscriptionListByExternalBillingAccount**
> ExternalSubscriptionDefinitionListResult externalSubscriptionListByExternalBillingAccount(apiVersion, externalBillingAccountName)



List all ExternalSubscriptions by ExternalBillingAccount definitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExternalSubscriptionsApi apiInstance = new ExternalSubscriptionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String externalBillingAccountName = "externalBillingAccountName_example"; // String | External Billing Account Name. (eg 'aws-{PayerAccountId}')
    try {
      ExternalSubscriptionDefinitionListResult result = apiInstance.externalSubscriptionListByExternalBillingAccount(apiVersion, externalBillingAccountName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalSubscriptionsApi#externalSubscriptionListByExternalBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |
| **externalBillingAccountName** | **String**| External Billing Account Name. (eg &#39;aws-{PayerAccountId}&#39;) | |

### Return type

[**ExternalSubscriptionDefinitionListResult**](ExternalSubscriptionDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="externalSubscriptionListByManagementGroup"></a>
# **externalSubscriptionListByManagementGroup**
> ExternalSubscriptionDefinitionListResult externalSubscriptionListByManagementGroup(apiVersion, managementGroupId, $recurse)



List all ExternalSubscription definitions for Management Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExternalSubscriptionsApi apiInstance = new ExternalSubscriptionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String managementGroupId = "managementGroupId_example"; // String | ManagementGroup ID
    Boolean $recurse = true; // Boolean | The $recurse=true query string parameter allows returning externalSubscriptions associated with the specified managementGroup, or any of its descendants.
    try {
      ExternalSubscriptionDefinitionListResult result = apiInstance.externalSubscriptionListByManagementGroup(apiVersion, managementGroupId, $recurse);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalSubscriptionsApi#externalSubscriptionListByManagementGroup");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |
| **managementGroupId** | **String**| ManagementGroup ID | |
| **$recurse** | **Boolean**| The $recurse&#x3D;true query string parameter allows returning externalSubscriptions associated with the specified managementGroup, or any of its descendants. | [optional] |

### Return type

[**ExternalSubscriptionDefinitionListResult**](ExternalSubscriptionDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="externalSubscriptionUpdateManagementGroup"></a>
# **externalSubscriptionUpdateManagementGroup**
> externalSubscriptionUpdateManagementGroup(apiVersion, managementGroupId, externalSubscriptionName)



Updates the management group of an ExternalSubscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalSubscriptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ExternalSubscriptionsApi apiInstance = new ExternalSubscriptionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String managementGroupId = "managementGroupId_example"; // String | ManagementGroup ID
    String externalSubscriptionName = "externalSubscriptionName_example"; // String | External Subscription Name. (eg 'aws-{UsageAccountId}')
    try {
      apiInstance.externalSubscriptionUpdateManagementGroup(apiVersion, managementGroupId, externalSubscriptionName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalSubscriptionsApi#externalSubscriptionUpdateManagementGroup");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |
| **managementGroupId** | **String**| ManagementGroup ID | |
| **externalSubscriptionName** | **String**| External Subscription Name. (eg &#39;aws-{UsageAccountId}&#39;) | |

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
| **204** | NoContent |  -  |
| **0** | Error response describing why the operation failed. |  -  |

