# SmartDetectorAlertRulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**smartDetectorAlertRulesCreateOrUpdate**](SmartDetectorAlertRulesApi.md#smartDetectorAlertRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{alertRuleName} |  |
| [**smartDetectorAlertRulesDelete**](SmartDetectorAlertRulesApi.md#smartDetectorAlertRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{alertRuleName} |  |
| [**smartDetectorAlertRulesGet**](SmartDetectorAlertRulesApi.md#smartDetectorAlertRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.alertsManagement/smartDetectorAlertRules/{alertRuleName} |  |
| [**smartDetectorAlertRulesList**](SmartDetectorAlertRulesApi.md#smartDetectorAlertRulesList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.alertsManagement/smartDetectorAlertRules |  |
| [**smartDetectorAlertRulesListByResourceGroup**](SmartDetectorAlertRulesApi.md#smartDetectorAlertRulesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.alertsManagement/smartDetectorAlertRules |  |


<a id="smartDetectorAlertRulesCreateOrUpdate"></a>
# **smartDetectorAlertRulesCreateOrUpdate**
> AlertRule smartDetectorAlertRulesCreateOrUpdate(subscriptionId, resourceGroupName, alertRuleName, apiVersion, parameters)



Create or update a Smart Detector alert rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmartDetectorAlertRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SmartDetectorAlertRulesApi apiInstance = new SmartDetectorAlertRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String alertRuleName = "alertRuleName_example"; // String | The name of the alert rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    AlertRule parameters = new AlertRule(); // AlertRule | Parameters supplied to the operation.
    try {
      AlertRule result = apiInstance.smartDetectorAlertRulesCreateOrUpdate(subscriptionId, resourceGroupName, alertRuleName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmartDetectorAlertRulesApi#smartDetectorAlertRulesCreateOrUpdate");
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
| **subscriptionId** | **String**| The Azure subscription id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **alertRuleName** | **String**| The name of the alert rule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **parameters** | [**AlertRule**](AlertRule.md)| Parameters supplied to the operation. | |

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to update a Smart Detector alert rule. |  -  |
| **201** | Successful request to create a Smart Detector alert rule. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="smartDetectorAlertRulesDelete"></a>
# **smartDetectorAlertRulesDelete**
> smartDetectorAlertRulesDelete(subscriptionId, resourceGroupName, alertRuleName, apiVersion)



Delete an existing Smart Detector alert rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmartDetectorAlertRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SmartDetectorAlertRulesApi apiInstance = new SmartDetectorAlertRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String alertRuleName = "alertRuleName_example"; // String | The name of the alert rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.smartDetectorAlertRulesDelete(subscriptionId, resourceGroupName, alertRuleName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmartDetectorAlertRulesApi#smartDetectorAlertRulesDelete");
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
| **subscriptionId** | **String**| The Azure subscription id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **alertRuleName** | **String**| The name of the alert rule. | |
| **apiVersion** | **String**| Client Api Version. | |

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
| **200** | Successful request to delete a Smart Detector alert rule. |  -  |
| **204** | The Smart Detector alert rule does not exist. It may have already been deleted. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="smartDetectorAlertRulesGet"></a>
# **smartDetectorAlertRulesGet**
> AlertRule smartDetectorAlertRulesGet(subscriptionId, resourceGroupName, alertRuleName, apiVersion, expandDetector)



Get a specific Smart Detector alert rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmartDetectorAlertRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SmartDetectorAlertRulesApi apiInstance = new SmartDetectorAlertRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String alertRuleName = "alertRuleName_example"; // String | The name of the alert rule.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    Boolean expandDetector = true; // Boolean | Indicates if Smart Detector should be expanded.
    try {
      AlertRule result = apiInstance.smartDetectorAlertRulesGet(subscriptionId, resourceGroupName, alertRuleName, apiVersion, expandDetector);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmartDetectorAlertRulesApi#smartDetectorAlertRulesGet");
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
| **subscriptionId** | **String**| The Azure subscription id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **alertRuleName** | **String**| The name of the alert rule. | |
| **apiVersion** | **String**| Client Api Version. | |
| **expandDetector** | **Boolean**| Indicates if Smart Detector should be expanded. | [optional] |

### Return type

[**AlertRule**](AlertRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get Smart Detector alert rule. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="smartDetectorAlertRulesList"></a>
# **smartDetectorAlertRulesList**
> AlertRulesList smartDetectorAlertRulesList(subscriptionId, apiVersion)



List all the existing Smart Detector alert rules within the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmartDetectorAlertRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SmartDetectorAlertRulesApi apiInstance = new SmartDetectorAlertRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription id.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      AlertRulesList result = apiInstance.smartDetectorAlertRulesList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmartDetectorAlertRulesApi#smartDetectorAlertRulesList");
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
| **subscriptionId** | **String**| The Azure subscription id. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**AlertRulesList**](AlertRulesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to list Smart Detector alert rules. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="smartDetectorAlertRulesListByResourceGroup"></a>
# **smartDetectorAlertRulesListByResourceGroup**
> AlertRulesList smartDetectorAlertRulesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



List all the existing Smart Detector alert rules within the subscription and resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SmartDetectorAlertRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    SmartDetectorAlertRulesApi apiInstance = new SmartDetectorAlertRulesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      AlertRulesList result = apiInstance.smartDetectorAlertRulesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SmartDetectorAlertRulesApi#smartDetectorAlertRulesListByResourceGroup");
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
| **subscriptionId** | **String**| The Azure subscription id. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**AlertRulesList**](AlertRulesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to list Smart Detector alert rules. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

