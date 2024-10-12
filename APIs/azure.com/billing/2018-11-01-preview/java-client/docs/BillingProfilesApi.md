# BillingProfilesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billingProfilesCreate**](BillingProfilesApi.md#billingProfilesCreate) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles |  |
| [**billingProfilesGet**](BillingProfilesApi.md#billingProfilesGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName} |  |
| [**billingProfilesListByBillingAccountName**](BillingProfilesApi.md#billingProfilesListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles |  |
| [**billingProfilesUpdate**](BillingProfilesApi.md#billingProfilesUpdate) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName} |  |


<a id="billingProfilesCreate"></a>
# **billingProfilesCreate**
> BillingProfile billingProfilesCreate(apiVersion, billingAccountName, parameters)



The operation to create a BillingProfile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingProfilesApi apiInstance = new BillingProfilesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    BillingProfileCreationParameters parameters = new BillingProfileCreationParameters(); // BillingProfileCreationParameters | Parameters supplied to the Create BillingProfile operation.
    try {
      BillingProfile result = apiInstance.billingProfilesCreate(apiVersion, billingAccountName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingProfilesApi#billingProfilesCreate");
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
| **parameters** | [**BillingProfileCreationParameters**](BillingProfileCreationParameters.md)| Parameters supplied to the Create BillingProfile operation. | |

### Return type

[**BillingProfile**](BillingProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted |  * Retry-After - Recommends the retryable time after receiving this. <br>  * Azure-AsyncOperation - URI to poll for the operation status <br>  * Location - Location URI to poll for result. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="billingProfilesGet"></a>
# **billingProfilesGet**
> BillingProfile billingProfilesGet(apiVersion, billingAccountName, billingProfileName, $expand)



Get the billing profile by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingProfilesApi apiInstance = new BillingProfilesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    String $expand = "$expand_example"; // String | May be used to expand the invoiceSections.
    try {
      BillingProfile result = apiInstance.billingProfilesGet(apiVersion, billingAccountName, billingProfileName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingProfilesApi#billingProfilesGet");
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
| **$expand** | **String**| May be used to expand the invoiceSections. | [optional] |

### Return type

[**BillingProfile**](BillingProfile.md)

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

<a id="billingProfilesListByBillingAccountName"></a>
# **billingProfilesListByBillingAccountName**
> BillingProfileListResult billingProfilesListByBillingAccountName(apiVersion, billingAccountName, $expand)



Lists all billing profiles for a user which that user has access to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingProfilesApi apiInstance = new BillingProfilesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String $expand = "$expand_example"; // String | May be used to expand the invoiceSections.
    try {
      BillingProfileListResult result = apiInstance.billingProfilesListByBillingAccountName(apiVersion, billingAccountName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingProfilesApi#billingProfilesListByBillingAccountName");
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
| **$expand** | **String**| May be used to expand the invoiceSections. | [optional] |

### Return type

[**BillingProfileListResult**](BillingProfileListResult.md)

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

<a id="billingProfilesUpdate"></a>
# **billingProfilesUpdate**
> BillingProfile billingProfilesUpdate(apiVersion, billingAccountName, billingProfileName, parameters)



The operation to update a billing profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillingProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BillingProfilesApi apiInstance = new BillingProfilesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    BillingProfile parameters = new BillingProfile(); // BillingProfile | Parameters supplied to the update billing profile operation.
    try {
      BillingProfile result = apiInstance.billingProfilesUpdate(apiVersion, billingAccountName, billingProfileName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillingProfilesApi#billingProfilesUpdate");
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
| **parameters** | [**BillingProfile**](BillingProfile.md)| Parameters supplied to the update billing profile operation. | |

### Return type

[**BillingProfile**](BillingProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. Billing profile update is in progress. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * Location - Location URI to poll for result. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

