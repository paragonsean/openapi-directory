# BillingRoleAssignmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingRoleAssignmentsAddByBillingAccount**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByBillingAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/createBillingRoleAssignment |  |
| [**billingRoleAssignmentsAddByBillingProfile**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByBillingProfile) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/createBillingRoleAssignment |  |
| [**billingRoleAssignmentsAddByInvoiceSection**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByInvoiceSection) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/createBillingRoleAssignment |  |
| [**billingRoleAssignmentsDeleteByBillingAccount**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByBillingAccount) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsDeleteByBillingProfile**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByBillingProfile) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsDeleteByInvoiceSection**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByInvoiceSection) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsGetByBillingAccount**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsGetByBillingProfile**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsGetByInvoiceSection**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleAssignments/{billingRoleAssignmentName} |  |
| [**billingRoleAssignmentsListByBillingAccount**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments |  |
| [**billingRoleAssignmentsListByBillingProfile**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleAssignments |  |
| [**billingRoleAssignmentsListByInvoiceSection**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleAssignments |  |


<a id="billingRoleAssignmentsAddByBillingAccount"></a>
# **billingRoleAssignmentsAddByBillingAccount**
> BillingRoleAssignmentListResult billingRoleAssignmentsAddByBillingAccount(apiVersion, billingAccountName, parameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    BillingRoleAssignmentPayload parameters = new BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsAddByBillingAccount(apiVersion, billingAccountName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsAddByBillingAccount");
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

<a id="billingRoleAssignmentsAddByBillingProfile"></a>
# **billingRoleAssignmentsAddByBillingProfile**
> BillingRoleAssignmentListResult billingRoleAssignmentsAddByBillingProfile(apiVersion, billingAccountName, billingProfileName, parameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    BillingRoleAssignmentPayload parameters = new BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsAddByBillingProfile(apiVersion, billingAccountName, billingProfileName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsAddByBillingProfile");
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

<a id="billingRoleAssignmentsAddByInvoiceSection"></a>
# **billingRoleAssignmentsAddByInvoiceSection**
> BillingRoleAssignmentListResult billingRoleAssignmentsAddByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, parameters)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    BillingRoleAssignmentPayload parameters = new BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsAddByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsAddByInvoiceSection");
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

<a id="billingRoleAssignmentsDeleteByBillingAccount"></a>
# **billingRoleAssignmentsDeleteByBillingAccount**
> BillingRoleAssignment billingRoleAssignmentsDeleteByBillingAccount(apiVersion, billingAccountName, billingRoleAssignmentName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
    try {
      BillingRoleAssignment result = apiInstance.billingRoleAssignmentsDeleteByBillingAccount(apiVersion, billingAccountName, billingRoleAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsDeleteByBillingAccount");
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

<a id="billingRoleAssignmentsDeleteByBillingProfile"></a>
# **billingRoleAssignmentsDeleteByBillingProfile**
> BillingRoleAssignment billingRoleAssignmentsDeleteByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
    try {
      BillingRoleAssignment result = apiInstance.billingRoleAssignmentsDeleteByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsDeleteByBillingProfile");
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

<a id="billingRoleAssignmentsDeleteByInvoiceSection"></a>
# **billingRoleAssignmentsDeleteByInvoiceSection**
> BillingRoleAssignment billingRoleAssignmentsDeleteByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleAssignmentName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
    try {
      BillingRoleAssignment result = apiInstance.billingRoleAssignmentsDeleteByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsDeleteByInvoiceSection");
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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | |
| **billingAccountName** | **String**| billing Account Id. | |
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

<a id="billingRoleAssignmentsGetByBillingProfile"></a>
# **billingRoleAssignmentsGetByBillingProfile**
> BillingRoleAssignment billingRoleAssignmentsGetByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
    try {
      BillingRoleAssignment result = apiInstance.billingRoleAssignmentsGetByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsGetByBillingProfile");
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

<a id="billingRoleAssignmentsGetByInvoiceSection"></a>
# **billingRoleAssignmentsGetByInvoiceSection**
> BillingRoleAssignment billingRoleAssignmentsGetByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleAssignmentName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
    try {
      BillingRoleAssignment result = apiInstance.billingRoleAssignmentsGetByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleAssignmentName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsGetByInvoiceSection");
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

<a id="billingRoleAssignmentsListByBillingAccount"></a>
# **billingRoleAssignmentsListByBillingAccount**
> BillingRoleAssignmentListResult billingRoleAssignmentsListByBillingAccount(apiVersion, billingAccountName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsListByBillingAccount(apiVersion, billingAccountName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsListByBillingAccount");
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

<a id="billingRoleAssignmentsListByBillingProfile"></a>
# **billingRoleAssignmentsListByBillingProfile**
> BillingRoleAssignmentListResult billingRoleAssignmentsListByBillingProfile(apiVersion, billingAccountName, billingProfileName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsListByBillingProfile(apiVersion, billingAccountName, billingProfileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsListByBillingProfile");
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

<a id="billingRoleAssignmentsListByInvoiceSection"></a>
# **billingRoleAssignmentsListByInvoiceSection**
> BillingRoleAssignmentListResult billingRoleAssignmentsListByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName)



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
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    try {
      BillingRoleAssignmentListResult result = apiInstance.billingRoleAssignmentsListByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingRoleAssignmentsApi#billingRoleAssignmentsListByInvoiceSection");
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

