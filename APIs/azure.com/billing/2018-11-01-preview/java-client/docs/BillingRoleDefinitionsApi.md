# BillingRoleDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingRoleDefinitionsGetByBillingAccountName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/billingRoleDefinitions/{billingRoleDefinitionName} |  |
| [**billingRoleDefinitionsGetByBillingProfileName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/billingRoleDefinitions/{billingRoleDefinitionName} |  |
| [**billingRoleDefinitionsGetByInvoiceSectionName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByInvoiceSectionName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/billingRoleDefinitions/{billingRoleDefinitionName} |  |
| [**billingRoleDefinitionsListByBillingAccountName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/billingRoleDefinitions |  |
| [**billingRoleDefinitionsListByBillingProfileName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/billingRoleDefinitions |  |
| [**billingRoleDefinitionsListByInvoiceSectionName**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByInvoiceSectionName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/billingRoleDefinitions |  |


<a id="billingRoleDefinitionsGetByBillingAccountName"></a>
# **billingRoleDefinitionsGetByBillingAccountName**
> BillingRoleDefinition billingRoleDefinitionsGetByBillingAccountName(apiVersion, billingAccountName, billingRoleDefinitionName)



Gets the role definition for a role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleDefinitionsApi apiInstance = new BillingRoleDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
    try {
      BillingRoleDefinition result = apiInstance.billingRoleDefinitionsGetByBillingAccountName(apiVersion, billingAccountName, billingRoleDefinitionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsGetByBillingAccountName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **billingAccountName** | **String**| Billing Account Id. | |
| **billingRoleDefinitionName** | **String**| role definition id. | |

### Return type

[**BillingRoleDefinition**](BillingRoleDefinition.md)

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

<a id="billingRoleDefinitionsGetByBillingProfileName"></a>
# **billingRoleDefinitionsGetByBillingProfileName**
> BillingRoleDefinition billingRoleDefinitionsGetByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleDefinitionName)



Gets the role definition for a role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleDefinitionsApi apiInstance = new BillingRoleDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
    try {
      BillingRoleDefinition result = apiInstance.billingRoleDefinitionsGetByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleDefinitionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsGetByBillingProfileName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **billingAccountName** | **String**| Billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
| **billingRoleDefinitionName** | **String**| role definition id. | |

### Return type

[**BillingRoleDefinition**](BillingRoleDefinition.md)

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

<a id="billingRoleDefinitionsGetByInvoiceSectionName"></a>
# **billingRoleDefinitionsGetByInvoiceSectionName**
> BillingRoleDefinition billingRoleDefinitionsGetByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleDefinitionName)



Gets the role definition for a role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleDefinitionsApi apiInstance = new BillingRoleDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
    try {
      BillingRoleDefinition result = apiInstance.billingRoleDefinitionsGetByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleDefinitionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsGetByInvoiceSectionName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **billingAccountName** | **String**| Billing Account Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |
| **billingRoleDefinitionName** | **String**| role definition id. | |

### Return type

[**BillingRoleDefinition**](BillingRoleDefinition.md)

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

<a id="billingRoleDefinitionsListByBillingAccountName"></a>
# **billingRoleDefinitionsListByBillingAccountName**
> BillingRoleDefinitionListResult billingRoleDefinitionsListByBillingAccountName(apiVersion, billingAccountName)



Lists the role definition for a billing account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleDefinitionsApi apiInstance = new BillingRoleDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    try {
      BillingRoleDefinitionListResult result = apiInstance.billingRoleDefinitionsListByBillingAccountName(apiVersion, billingAccountName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsListByBillingAccountName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **billingAccountName** | **String**| Billing Account Id. | |

### Return type

[**BillingRoleDefinitionListResult**](BillingRoleDefinitionListResult.md)

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

<a id="billingRoleDefinitionsListByBillingProfileName"></a>
# **billingRoleDefinitionsListByBillingProfileName**
> BillingRoleDefinitionListResult billingRoleDefinitionsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName)



Lists the role definition for a Billing Profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleDefinitionsApi apiInstance = new BillingRoleDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    try {
      BillingRoleDefinitionListResult result = apiInstance.billingRoleDefinitionsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsListByBillingProfileName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **billingAccountName** | **String**| Billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |

### Return type

[**BillingRoleDefinitionListResult**](BillingRoleDefinitionListResult.md)

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

<a id="billingRoleDefinitionsListByInvoiceSectionName"></a>
# **billingRoleDefinitionsListByInvoiceSectionName**
> BillingRoleDefinitionListResult billingRoleDefinitionsListByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName)



Lists the role definition for an invoice Section

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleDefinitionsApi apiInstance = new BillingRoleDefinitionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    try {
      BillingRoleDefinitionListResult result = apiInstance.billingRoleDefinitionsListByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsListByInvoiceSectionName");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | |
| **billingAccountName** | **String**| Billing Account Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |

### Return type

[**BillingRoleDefinitionListResult**](BillingRoleDefinitionListResult.md)

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

