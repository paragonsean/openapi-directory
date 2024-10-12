# BillingRoleAssignmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingRoleAssignmentsAddByBillingAccountName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByBillingAccountName) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/createBillingRoleAssignment |  |
| [**billingRoleAssignmentsAddByBillingProfileName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByBillingProfileName) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/createBillingRoleAssignment |  |
| [**billingRoleAssignmentsAddByInvoiceSectionName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByInvoiceSectionName) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/createBillingRoleAssignment |  |
| [**billingRoleAssignmentsDeleteByBillingAccountName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByBillingAccountName) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsDeleteByBillingProfileName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByBillingProfileName) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsDeleteByInvoiceSectionName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByInvoiceSectionName) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsGetByBillingAccount**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsGetByBillingProfileName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsGetByInvoiceSectionName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByInvoiceSectionName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsListByBillingAccountName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/billingRoleAssignments |  |
| [**billingRoleAssignmentsListByBillingProfileName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/billingRoleAssignments |  |
| [**billingRoleAssignmentsListByInvoiceSectionName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByInvoiceSectionName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/billingRoleAssignments |  |


<a id="billingRoleAssignmentsAddByBillingAccountName"></a>
# **billingRoleAssignmentsAddByBillingAccountName**
> BillingRoleAssignmentListResult billingRoleAssignmentsAddByBillingAccountName(apiVersion, billingAccountName, parameters)



The operation to add a role assignment to a billing account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    BillingRoleAssignmentPayload parameters = new BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsAddByBillingAccountName(apiVersion, billingAccountName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsAddByBillingAccountName");
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
| **parameters** | [**BillingRoleAssignmentPayload**](BillingRoleAssignmentPayload.md)| Parameters supplied to add a role assignment. | |

### Return type

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Role assignment is successfully created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="billingRoleAssignmentsAddByBillingProfileName"></a>
# **billingRoleAssignmentsAddByBillingProfileName**
> BillingRoleAssignmentListResult billingRoleAssignmentsAddByBillingProfileName(apiVersion, billingAccountName, billingProfileName, parameters)



The operation to add a role assignment to a billing profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    BillingRoleAssignmentPayload parameters = new BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsAddByBillingProfileName(apiVersion, billingAccountName, billingProfileName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsAddByBillingProfileName");
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
| **parameters** | [**BillingRoleAssignmentPayload**](BillingRoleAssignmentPayload.md)| Parameters supplied to add a role assignment. | |

### Return type

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Role assignment is successfully created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="billingRoleAssignmentsAddByInvoiceSectionName"></a>
# **billingRoleAssignmentsAddByInvoiceSectionName**
> BillingRoleAssignmentListResult billingRoleAssignmentsAddByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, parameters)



The operation to add a role assignment to a invoice Section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    BillingRoleAssignmentPayload parameters = new BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsAddByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsAddByInvoiceSectionName");
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
| **parameters** | [**BillingRoleAssignmentPayload**](BillingRoleAssignmentPayload.md)| Parameters supplied to add a role assignment. | |

### Return type

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Role assignment is successfully created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="billingRoleAssignmentsDeleteByBillingAccountName"></a>
# **billingRoleAssignmentsDeleteByBillingAccountName**
> BillingRoleAssignment billingRoleAssignmentsDeleteByBillingAccountName(apiVersion, billingAccountName, billingRoleAssignmentName)



Delete the role assignment on this billing account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
    try {
      BillingRoleAssignment result = apiInstance.billingRoleAssignmentsDeleteByBillingAccountName(apiVersion, billingAccountName, billingRoleAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsDeleteByBillingAccountName");
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
| **billingRoleAssignmentName** | **String**| role assignment id. | |

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

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

<a id="billingRoleAssignmentsDeleteByBillingProfileName"></a>
# **billingRoleAssignmentsDeleteByBillingProfileName**
> BillingRoleAssignment billingRoleAssignmentsDeleteByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName)



Delete the role assignment on this Billing Profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
    try {
      BillingRoleAssignment result = apiInstance.billingRoleAssignmentsDeleteByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsDeleteByBillingProfileName");
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
| **billingRoleAssignmentName** | **String**| role assignment id. | |

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

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

<a id="billingRoleAssignmentsDeleteByInvoiceSectionName"></a>
# **billingRoleAssignmentsDeleteByInvoiceSectionName**
> BillingRoleAssignment billingRoleAssignmentsDeleteByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleAssignmentName)



Delete the role assignment on the invoice Section

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
    try {
      BillingRoleAssignment result = apiInstance.billingRoleAssignmentsDeleteByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsDeleteByInvoiceSectionName");
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
| **billingRoleAssignmentName** | **String**| role assignment id. | |

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

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

<a id="billingRoleAssignmentsGetByBillingAccount"></a>
# **billingRoleAssignmentsGetByBillingAccount**
> BillingRoleAssignment billingRoleAssignmentsGetByBillingAccount(apiVersion, billingAccountName, billingRoleAssignmentName)



Get the role assignment for the caller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
    try {
      BillingRoleAssignment result = apiInstance.billingRoleAssignmentsGetByBillingAccount(apiVersion, billingAccountName, billingRoleAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsGetByBillingAccount");
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
| **billingRoleAssignmentName** | **String**| role assignment id. | |

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

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

<a id="billingRoleAssignmentsGetByBillingProfileName"></a>
# **billingRoleAssignmentsGetByBillingProfileName**
> BillingRoleAssignment billingRoleAssignmentsGetByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName)



Get the role assignment for the caller on the Billing Profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
    try {
      BillingRoleAssignment result = apiInstance.billingRoleAssignmentsGetByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsGetByBillingProfileName");
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
| **billingRoleAssignmentName** | **String**| role assignment id. | |

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

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

<a id="billingRoleAssignmentsGetByInvoiceSectionName"></a>
# **billingRoleAssignmentsGetByInvoiceSectionName**
> BillingRoleAssignment billingRoleAssignmentsGetByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleAssignmentName)



Get the role assignment for the caller on the invoice Section

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
    try {
      BillingRoleAssignment result = apiInstance.billingRoleAssignmentsGetByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsGetByInvoiceSectionName");
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
| **billingRoleAssignmentName** | **String**| role assignment id. | |

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

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

<a id="billingRoleAssignmentsListByBillingAccountName"></a>
# **billingRoleAssignmentsListByBillingAccountName**
> BillingRoleAssignmentListResult billingRoleAssignmentsListByBillingAccountName(apiVersion, billingAccountName)



Get the role assignments on the Billing Account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsListByBillingAccountName(apiVersion, billingAccountName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsListByBillingAccountName");
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

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

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

<a id="billingRoleAssignmentsListByBillingProfileName"></a>
# **billingRoleAssignmentsListByBillingProfileName**
> BillingRoleAssignmentListResult billingRoleAssignmentsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName)



Get the role assignments on the Billing Profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsListByBillingProfileName");
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

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

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

<a id="billingRoleAssignmentsListByInvoiceSectionName"></a>
# **billingRoleAssignmentsListByInvoiceSectionName**
> BillingRoleAssignmentListResult billingRoleAssignmentsListByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName)



Get the role assignments on the invoice Section

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingRoleAssignmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingRoleAssignmentsApi apiInstance = new BillingRoleAssignmentsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsListByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsListByInvoiceSectionName");
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

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

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

