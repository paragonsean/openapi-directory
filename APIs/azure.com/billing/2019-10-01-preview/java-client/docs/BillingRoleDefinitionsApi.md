# BillingRoleDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingRoleDefinitionsGetByBillingAccount**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleDefinitions/{billingRoleDefinitionName} |  |
| [**billingRoleDefinitionsGetByBillingProfile**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleDefinitions/{billingRoleDefinitionName} |  |
| [**billingRoleDefinitionsGetByInvoiceSection**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleDefinitions/{billingRoleDefinitionName} |  |
| [**billingRoleDefinitionsListByBillingAccount**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleDefinitions |  |
| [**billingRoleDefinitionsListByBillingProfile**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleDefinitions |  |
| [**billingRoleDefinitionsListByInvoiceSection**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleDefinitions |  |


<a id="billingRoleDefinitionsGetByBillingAccount"></a>
# **billingRoleDefinitionsGetByBillingAccount**
> BillingRoleDefinition billingRoleDefinitionsGetByBillingAccount(apiVersion, billingAccountName, billingRoleDefinitionName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
    try {
      BillingRoleDefinition result = apiInstance.billingRoleDefinitionsGetByBillingAccount(apiVersion, billingAccountName, billingRoleDefinitionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsGetByBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
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

<a id="billingRoleDefinitionsGetByBillingProfile"></a>
# **billingRoleDefinitionsGetByBillingProfile**
> BillingRoleDefinition billingRoleDefinitionsGetByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleDefinitionName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
    try {
      BillingRoleDefinition result = apiInstance.billingRoleDefinitionsGetByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleDefinitionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsGetByBillingProfile");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
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

<a id="billingRoleDefinitionsGetByInvoiceSection"></a>
# **billingRoleDefinitionsGetByInvoiceSection**
> BillingRoleDefinition billingRoleDefinitionsGetByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleDefinitionName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
    try {
      BillingRoleDefinition result = apiInstance.billingRoleDefinitionsGetByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleDefinitionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsGetByInvoiceSection");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
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

<a id="billingRoleDefinitionsListByBillingAccount"></a>
# **billingRoleDefinitionsListByBillingAccount**
> BillingRoleDefinitionListResult billingRoleDefinitionsListByBillingAccount(apiVersion, billingAccountName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    try {
      BillingRoleDefinitionListResult result = apiInstance.billingRoleDefinitionsListByBillingAccount(apiVersion, billingAccountName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsListByBillingAccount");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |

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

<a id="billingRoleDefinitionsListByBillingProfile"></a>
# **billingRoleDefinitionsListByBillingProfile**
> BillingRoleDefinitionListResult billingRoleDefinitionsListByBillingProfile(apiVersion, billingAccountName, billingProfileName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    try {
      BillingRoleDefinitionListResult result = apiInstance.billingRoleDefinitionsListByBillingProfile(apiVersion, billingAccountName, billingProfileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsListByBillingProfile");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
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

<a id="billingRoleDefinitionsListByInvoiceSection"></a>
# **billingRoleDefinitionsListByInvoiceSection**
> BillingRoleDefinitionListResult billingRoleDefinitionsListByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    try {
      BillingRoleDefinitionListResult result = apiInstance.billingRoleDefinitionsListByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleDefinitionsApi#billingRoleDefinitionsListByInvoiceSection");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
| **billingProfileName** | **String**| Billing Profile Id. | |
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

