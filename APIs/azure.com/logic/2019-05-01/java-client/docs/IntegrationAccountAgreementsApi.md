# IntegrationAccountAgreementsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationAccountAgreementsCreateOrUpdate**](IntegrationAccountAgreementsApi.md#integrationAccountAgreementsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/agreements/{agreementName} |  |
| [**integrationAccountAgreementsDelete**](IntegrationAccountAgreementsApi.md#integrationAccountAgreementsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/agreements/{agreementName} |  |
| [**integrationAccountAgreementsGet**](IntegrationAccountAgreementsApi.md#integrationAccountAgreementsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/agreements/{agreementName} |  |
| [**integrationAccountAgreementsList**](IntegrationAccountAgreementsApi.md#integrationAccountAgreementsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/agreements |  |
| [**integrationAccountAgreementsListContentCallbackUrl**](IntegrationAccountAgreementsApi.md#integrationAccountAgreementsListContentCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/agreements/{agreementName}/listContentCallbackUrl |  |


<a id="integrationAccountAgreementsCreateOrUpdate"></a>
# **integrationAccountAgreementsCreateOrUpdate**
> IntegrationAccountAgreement integrationAccountAgreementsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion, agreement)



Creates or updates an integration account agreement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountAgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountAgreementsApi apiInstance = new IntegrationAccountAgreementsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String agreementName = "agreementName_example"; // String | The integration account agreement name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationAccountAgreement agreement = new IntegrationAccountAgreement(); // IntegrationAccountAgreement | The integration account agreement.
    try {
      IntegrationAccountAgreement result = apiInstance.integrationAccountAgreementsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion, agreement);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountAgreementsApi#integrationAccountAgreementsCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **agreementName** | **String**| The integration account agreement name. | |
| **apiVersion** | **String**| The API version. | |
| **agreement** | [**IntegrationAccountAgreement**](IntegrationAccountAgreement.md)| The integration account agreement. | |

### Return type

[**IntegrationAccountAgreement**](IntegrationAccountAgreement.md)

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
| **0** | Error response describing why the operation failed. |  -  |

<a id="integrationAccountAgreementsDelete"></a>
# **integrationAccountAgreementsDelete**
> integrationAccountAgreementsDelete(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion)



Deletes an integration account agreement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountAgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountAgreementsApi apiInstance = new IntegrationAccountAgreementsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String agreementName = "agreementName_example"; // String | The integration account agreement name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationAccountAgreementsDelete(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountAgreementsApi#integrationAccountAgreementsDelete");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **agreementName** | **String**| The integration account agreement name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="integrationAccountAgreementsGet"></a>
# **integrationAccountAgreementsGet**
> IntegrationAccountAgreement integrationAccountAgreementsGet(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion)



Gets an integration account agreement.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountAgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountAgreementsApi apiInstance = new IntegrationAccountAgreementsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String agreementName = "agreementName_example"; // String | The integration account agreement name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationAccountAgreement result = apiInstance.integrationAccountAgreementsGet(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountAgreementsApi#integrationAccountAgreementsGet");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **agreementName** | **String**| The integration account agreement name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationAccountAgreement**](IntegrationAccountAgreement.md)

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

<a id="integrationAccountAgreementsList"></a>
# **integrationAccountAgreementsList**
> IntegrationAccountAgreementListResult integrationAccountAgreementsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top, $filter)



Gets a list of integration account agreements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountAgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountAgreementsApi apiInstance = new IntegrationAccountAgreementsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Options for filters include: AgreementType.
    try {
      IntegrationAccountAgreementListResult result = apiInstance.integrationAccountAgreementsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountAgreementsApi#integrationAccountAgreementsList");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |
| **$filter** | **String**| The filter to apply on the operation. Options for filters include: AgreementType. | [optional] |

### Return type

[**IntegrationAccountAgreementListResult**](IntegrationAccountAgreementListResult.md)

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

<a id="integrationAccountAgreementsListContentCallbackUrl"></a>
# **integrationAccountAgreementsListContentCallbackUrl**
> WorkflowTriggerCallbackUrl integrationAccountAgreementsListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion, listContentCallbackUrl)



Get the content callback url.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountAgreementsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountAgreementsApi apiInstance = new IntegrationAccountAgreementsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String agreementName = "agreementName_example"; // String | The integration account agreement name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    GetCallbackUrlParameters listContentCallbackUrl = new GetCallbackUrlParameters(); // GetCallbackUrlParameters | 
    try {
      WorkflowTriggerCallbackUrl result = apiInstance.integrationAccountAgreementsListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, agreementName, apiVersion, listContentCallbackUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountAgreementsApi#integrationAccountAgreementsListContentCallbackUrl");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **agreementName** | **String**| The integration account agreement name. | |
| **apiVersion** | **String**| The API version. | |
| **listContentCallbackUrl** | [**GetCallbackUrlParameters**](GetCallbackUrlParameters.md)|  | |

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

