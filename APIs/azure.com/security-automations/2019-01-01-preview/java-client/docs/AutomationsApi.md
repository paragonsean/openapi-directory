# AutomationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**automationsCreateOrUpdate**](AutomationsApi.md#automationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/automations/{automationName} |  |
| [**automationsDelete**](AutomationsApi.md#automationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/automations/{automationName} |  |
| [**automationsGet**](AutomationsApi.md#automationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/automations/{automationName} |  |
| [**automationsList**](AutomationsApi.md#automationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/automations |  |
| [**automationsListByResourceGroup**](AutomationsApi.md#automationsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/automations |  |
| [**automationsValidate**](AutomationsApi.md#automationsValidate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/automations/{automationName}/validate |  |


<a id="automationsCreateOrUpdate"></a>
# **automationsCreateOrUpdate**
> Automation automationsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, automationName, automation)



Creates or updates a security automation. If a security automation is already created and a subsequent request is issued for the same automation id, then it will be updated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutomationsApi apiInstance = new AutomationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String automationName = "automationName_example"; // String | The security automation name.
    Automation automation = new Automation(); // Automation | The security automation resource
    try {
      Automation result = apiInstance.automationsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, automationName, automation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationsApi#automationsCreateOrUpdate");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **automationName** | **String**| The security automation name. | |
| **automation** | [**Automation**](Automation.md)| The security automation resource | |

### Return type

[**Automation**](Automation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Error response that describes why the operation failed. |  -  |

<a id="automationsDelete"></a>
# **automationsDelete**
> automationsDelete(apiVersion, subscriptionId, resourceGroupName, automationName)



Deletes a security automation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutomationsApi apiInstance = new AutomationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String automationName = "automationName_example"; // String | The security automation name.
    try {
      apiInstance.automationsDelete(apiVersion, subscriptionId, resourceGroupName, automationName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationsApi#automationsDelete");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **automationName** | **String**| The security automation name. | |

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
| **0** | Error response that describes why the operation failed. |  -  |

<a id="automationsGet"></a>
# **automationsGet**
> Automation automationsGet(apiVersion, subscriptionId, resourceGroupName, automationName)



Retrieves information about the model of a security automation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutomationsApi apiInstance = new AutomationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String automationName = "automationName_example"; // String | The security automation name.
    try {
      Automation result = apiInstance.automationsGet(apiVersion, subscriptionId, resourceGroupName, automationName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationsApi#automationsGet");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **automationName** | **String**| The security automation name. | |

### Return type

[**Automation**](Automation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response that describes why the operation failed. |  -  |

<a id="automationsList"></a>
# **automationsList**
> AutomationList automationsList(apiVersion, subscriptionId)



Lists all the security automations in the specified subscription. Use the &#39;nextLink&#39; property in the response to get the next page of security automations for the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutomationsApi apiInstance = new AutomationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    try {
      AutomationList result = apiInstance.automationsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationsApi#automationsList");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |

### Return type

[**AutomationList**](AutomationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response that describes why the operation failed. |  -  |

<a id="automationsListByResourceGroup"></a>
# **automationsListByResourceGroup**
> AutomationList automationsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Lists all the security automations in the specified resource group. Use the &#39;nextLink&#39; property in the response to get the next page of security automations for the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutomationsApi apiInstance = new AutomationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    try {
      AutomationList result = apiInstance.automationsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationsApi#automationsListByResourceGroup");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |

### Return type

[**AutomationList**](AutomationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response that describes why the operation failed. |  -  |

<a id="automationsValidate"></a>
# **automationsValidate**
> AutomationValidationStatus automationsValidate(apiVersion, subscriptionId, resourceGroupName, automationName, automation)



Validates the security automation model before create or update. Any validation errors are returned to the client.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AutomationsApi apiInstance = new AutomationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
    String automationName = "automationName_example"; // String | The security automation name.
    Automation automation = new Automation(); // Automation | The security automation resource
    try {
      AutomationValidationStatus result = apiInstance.automationsValidate(apiVersion, subscriptionId, resourceGroupName, automationName, automation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationsApi#automationsValidate");
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
| **apiVersion** | **String**| API version for the operation | |
| **subscriptionId** | **String**| Azure subscription ID | |
| **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | |
| **automationName** | **String**| The security automation name. | |
| **automation** | [**Automation**](Automation.md)| The security automation resource | |

### Return type

[**AutomationValidationStatus**](AutomationValidationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response that describes why the operation failed. |  -  |

