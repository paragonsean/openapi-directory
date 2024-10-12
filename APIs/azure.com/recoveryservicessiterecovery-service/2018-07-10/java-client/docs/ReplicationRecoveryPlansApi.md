# ReplicationRecoveryPlansApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicationRecoveryPlansCreate**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName} | Creates a recovery plan with the given details. |
| [**replicationRecoveryPlansDelete**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName} | Deletes the specified recovery plan. |
| [**replicationRecoveryPlansFailoverCommit**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansFailoverCommit) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/failoverCommit | Execute commit failover of the recovery plan. |
| [**replicationRecoveryPlansGet**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName} | Gets the requested recovery plan. |
| [**replicationRecoveryPlansList**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans | Gets the list of recovery plans. |
| [**replicationRecoveryPlansPlannedFailover**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansPlannedFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/plannedFailover | Execute planned failover of the recovery plan. |
| [**replicationRecoveryPlansReprotect**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansReprotect) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/reProtect | Execute reprotect of the recovery plan. |
| [**replicationRecoveryPlansTestFailover**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansTestFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/testFailover | Execute test failover of the recovery plan. |
| [**replicationRecoveryPlansTestFailoverCleanup**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansTestFailoverCleanup) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/testFailoverCleanup | Execute test failover cleanup of the recovery plan. |
| [**replicationRecoveryPlansUnplannedFailover**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansUnplannedFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName}/unplannedFailover | Execute unplanned failover of the recovery plan. |
| [**replicationRecoveryPlansUpdate**](ReplicationRecoveryPlansApi.md#replicationRecoveryPlansUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationRecoveryPlans/{recoveryPlanName} | Updates the given recovery plan. |


<a id="replicationRecoveryPlansCreate"></a>
# **replicationRecoveryPlansCreate**
> RecoveryPlan replicationRecoveryPlansCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Creates a recovery plan with the given details.

The operation to create a recovery plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryPlansApi apiInstance = new ReplicationRecoveryPlansApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
    CreateRecoveryPlanInput input = new CreateRecoveryPlanInput(); // CreateRecoveryPlanInput | Recovery Plan creation input.
    try {
      RecoveryPlan result = apiInstance.replicationRecoveryPlansCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryPlansApi#replicationRecoveryPlansCreate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **recoveryPlanName** | **String**| Recovery plan name. | |
| **input** | [**CreateRecoveryPlanInput**](CreateRecoveryPlanInput.md)| Recovery Plan creation input. | |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationRecoveryPlansDelete"></a>
# **replicationRecoveryPlansDelete**
> replicationRecoveryPlansDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName)

Deletes the specified recovery plan.

Delete a recovery plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryPlansApi apiInstance = new ReplicationRecoveryPlansApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
    try {
      apiInstance.replicationRecoveryPlansDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryPlansApi#replicationRecoveryPlansDelete");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **recoveryPlanName** | **String**| Recovery plan name. | |

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
| **202** | Accepted |  -  |
| **204** | NoContent |  -  |

<a id="replicationRecoveryPlansFailoverCommit"></a>
# **replicationRecoveryPlansFailoverCommit**
> RecoveryPlan replicationRecoveryPlansFailoverCommit(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName)

Execute commit failover of the recovery plan.

The operation to commit the fail over of a recovery plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryPlansApi apiInstance = new ReplicationRecoveryPlansApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
    try {
      RecoveryPlan result = apiInstance.replicationRecoveryPlansFailoverCommit(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryPlansApi#replicationRecoveryPlansFailoverCommit");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **recoveryPlanName** | **String**| Recovery plan name. | |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationRecoveryPlansGet"></a>
# **replicationRecoveryPlansGet**
> RecoveryPlan replicationRecoveryPlansGet(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName)

Gets the requested recovery plan.

Gets the details of the recovery plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryPlansApi apiInstance = new ReplicationRecoveryPlansApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String recoveryPlanName = "recoveryPlanName_example"; // String | Name of the recovery plan.
    try {
      RecoveryPlan result = apiInstance.replicationRecoveryPlansGet(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryPlansApi#replicationRecoveryPlansGet");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **recoveryPlanName** | **String**| Name of the recovery plan. | |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationRecoveryPlansList"></a>
# **replicationRecoveryPlansList**
> RecoveryPlanCollection replicationRecoveryPlansList(apiVersion, resourceName, resourceGroupName, subscriptionId)

Gets the list of recovery plans.

Lists the recovery plans in the vault.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryPlansApi apiInstance = new ReplicationRecoveryPlansApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    try {
      RecoveryPlanCollection result = apiInstance.replicationRecoveryPlansList(apiVersion, resourceName, resourceGroupName, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryPlansApi#replicationRecoveryPlansList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |

### Return type

[**RecoveryPlanCollection**](RecoveryPlanCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replicationRecoveryPlansPlannedFailover"></a>
# **replicationRecoveryPlansPlannedFailover**
> RecoveryPlan replicationRecoveryPlansPlannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Execute planned failover of the recovery plan.

The operation to start the planned failover of a recovery plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryPlansApi apiInstance = new ReplicationRecoveryPlansApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
    RecoveryPlanPlannedFailoverInput input = new RecoveryPlanPlannedFailoverInput(); // RecoveryPlanPlannedFailoverInput | Failover input.
    try {
      RecoveryPlan result = apiInstance.replicationRecoveryPlansPlannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryPlansApi#replicationRecoveryPlansPlannedFailover");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **recoveryPlanName** | **String**| Recovery plan name. | |
| **input** | [**RecoveryPlanPlannedFailoverInput**](RecoveryPlanPlannedFailoverInput.md)| Failover input. | |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationRecoveryPlansReprotect"></a>
# **replicationRecoveryPlansReprotect**
> RecoveryPlan replicationRecoveryPlansReprotect(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName)

Execute reprotect of the recovery plan.

The operation to reprotect(reverse replicate) a recovery plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryPlansApi apiInstance = new ReplicationRecoveryPlansApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
    try {
      RecoveryPlan result = apiInstance.replicationRecoveryPlansReprotect(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryPlansApi#replicationRecoveryPlansReprotect");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **recoveryPlanName** | **String**| Recovery plan name. | |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationRecoveryPlansTestFailover"></a>
# **replicationRecoveryPlansTestFailover**
> RecoveryPlan replicationRecoveryPlansTestFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Execute test failover of the recovery plan.

The operation to start the test failover of a recovery plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryPlansApi apiInstance = new ReplicationRecoveryPlansApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
    RecoveryPlanTestFailoverInput input = new RecoveryPlanTestFailoverInput(); // RecoveryPlanTestFailoverInput | Failover input.
    try {
      RecoveryPlan result = apiInstance.replicationRecoveryPlansTestFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryPlansApi#replicationRecoveryPlansTestFailover");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **recoveryPlanName** | **String**| Recovery plan name. | |
| **input** | [**RecoveryPlanTestFailoverInput**](RecoveryPlanTestFailoverInput.md)| Failover input. | |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationRecoveryPlansTestFailoverCleanup"></a>
# **replicationRecoveryPlansTestFailoverCleanup**
> RecoveryPlan replicationRecoveryPlansTestFailoverCleanup(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Execute test failover cleanup of the recovery plan.

The operation to cleanup test failover of a recovery plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryPlansApi apiInstance = new ReplicationRecoveryPlansApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
    RecoveryPlanTestFailoverCleanupInput input = new RecoveryPlanTestFailoverCleanupInput(); // RecoveryPlanTestFailoverCleanupInput | Test failover cleanup input.
    try {
      RecoveryPlan result = apiInstance.replicationRecoveryPlansTestFailoverCleanup(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryPlansApi#replicationRecoveryPlansTestFailoverCleanup");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **recoveryPlanName** | **String**| Recovery plan name. | |
| **input** | [**RecoveryPlanTestFailoverCleanupInput**](RecoveryPlanTestFailoverCleanupInput.md)| Test failover cleanup input. | |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationRecoveryPlansUnplannedFailover"></a>
# **replicationRecoveryPlansUnplannedFailover**
> RecoveryPlan replicationRecoveryPlansUnplannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Execute unplanned failover of the recovery plan.

The operation to start the failover of a recovery plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryPlansApi apiInstance = new ReplicationRecoveryPlansApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
    RecoveryPlanUnplannedFailoverInput input = new RecoveryPlanUnplannedFailoverInput(); // RecoveryPlanUnplannedFailoverInput | Failover input.
    try {
      RecoveryPlan result = apiInstance.replicationRecoveryPlansUnplannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryPlansApi#replicationRecoveryPlansUnplannedFailover");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **recoveryPlanName** | **String**| Recovery plan name. | |
| **input** | [**RecoveryPlanUnplannedFailoverInput**](RecoveryPlanUnplannedFailoverInput.md)| Failover input. | |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="replicationRecoveryPlansUpdate"></a>
# **replicationRecoveryPlansUpdate**
> RecoveryPlan replicationRecoveryPlansUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input)

Updates the given recovery plan.

The operation to update a recovery plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicationRecoveryPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ReplicationRecoveryPlansApi apiInstance = new ReplicationRecoveryPlansApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String resourceName = "resourceName_example"; // String | The name of the recovery services vault.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
    String subscriptionId = "subscriptionId_example"; // String | The subscription Id.
    String recoveryPlanName = "recoveryPlanName_example"; // String | Recovery plan name.
    UpdateRecoveryPlanInput input = new UpdateRecoveryPlanInput(); // UpdateRecoveryPlanInput | Update recovery plan input
    try {
      RecoveryPlan result = apiInstance.replicationRecoveryPlansUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, recoveryPlanName, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicationRecoveryPlansApi#replicationRecoveryPlansUpdate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **resourceName** | **String**| The name of the recovery services vault. | |
| **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | |
| **subscriptionId** | **String**| The subscription Id. | |
| **recoveryPlanName** | **String**| Recovery plan name. | |
| **input** | [**UpdateRecoveryPlanInput**](UpdateRecoveryPlanInput.md)| Update recovery plan input | |

### Return type

[**RecoveryPlan**](RecoveryPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

