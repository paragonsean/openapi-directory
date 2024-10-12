# InvoiceSectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**invoiceSectionsCreate**](InvoiceSectionsApi.md#invoiceSectionsCreate) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections |  |
| [**invoiceSectionsElevateToBillingProfile**](InvoiceSectionsApi.md#invoiceSectionsElevateToBillingProfile) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/elevate |  |
| [**invoiceSectionsGet**](InvoiceSectionsApi.md#invoiceSectionsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName} |  |
| [**invoiceSectionsListByBillingAccountName**](InvoiceSectionsApi.md#invoiceSectionsListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections |  |
| [**invoiceSectionsListByBillingProfileName**](InvoiceSectionsApi.md#invoiceSectionsListByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections |  |
| [**invoiceSectionsListByCreateSubscriptionPermission**](InvoiceSectionsApi.md#invoiceSectionsListByCreateSubscriptionPermission) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/listInvoiceSectionsWithCreateSubscriptionPermission |  |
| [**invoiceSectionsUpdate**](InvoiceSectionsApi.md#invoiceSectionsUpdate) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName} |  |


<a id="invoiceSectionsCreate"></a>
# **invoiceSectionsCreate**
> InvoiceSection invoiceSectionsCreate(apiVersion, billingAccountName, parameters)



The operation to create a InvoiceSection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    InvoiceSectionCreationRequest parameters = new InvoiceSectionCreationRequest(); // InvoiceSectionCreationRequest | Parameters supplied to the Create InvoiceSection operation.
    try {
      InvoiceSection result = apiInstance.invoiceSectionsCreate(apiVersion, billingAccountName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsCreate");
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
| **parameters** | [**InvoiceSectionCreationRequest**](InvoiceSectionCreationRequest.md)| Parameters supplied to the Create InvoiceSection operation. | |

### Return type

[**InvoiceSection**](InvoiceSection.md)

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

<a id="invoiceSectionsElevateToBillingProfile"></a>
# **invoiceSectionsElevateToBillingProfile**
> invoiceSectionsElevateToBillingProfile(billingAccountName, invoiceSectionName)



Elevates the caller&#39;s access to match their billing profile access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    try {
      apiInstance.invoiceSectionsElevateToBillingProfile(billingAccountName, invoiceSectionName);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsElevateToBillingProfile");
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
| **billingAccountName** | **String**| Billing Account Id. | |
| **invoiceSectionName** | **String**| InvoiceSection Id. | |

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
| **204** | Elevated the caller&#39;s access to the invoice section. |  -  |
| **0** | Unexpected error. |  -  |

<a id="invoiceSectionsGet"></a>
# **invoiceSectionsGet**
> InvoiceSection invoiceSectionsGet(apiVersion, billingAccountName, invoiceSectionName, $expand)



Get the InvoiceSection by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    String $expand = "$expand_example"; // String | May be used to expand the billingProfiles.
    try {
      InvoiceSection result = apiInstance.invoiceSectionsGet(apiVersion, billingAccountName, invoiceSectionName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsGet");
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
| **$expand** | **String**| May be used to expand the billingProfiles. | [optional] |

### Return type

[**InvoiceSection**](InvoiceSection.md)

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

<a id="invoiceSectionsListByBillingAccountName"></a>
# **invoiceSectionsListByBillingAccountName**
> InvoiceSectionListResult invoiceSectionsListByBillingAccountName(apiVersion, billingAccountName, $expand)



Lists all invoice sections for which a user has access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String $expand = "$expand_example"; // String | May be used to expand the billingProfiles.
    try {
      InvoiceSectionListResult result = apiInstance.invoiceSectionsListByBillingAccountName(apiVersion, billingAccountName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsListByBillingAccountName");
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
| **$expand** | **String**| May be used to expand the billingProfiles. | [optional] |

### Return type

[**InvoiceSectionListResult**](InvoiceSectionListResult.md)

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

<a id="invoiceSectionsListByBillingProfileName"></a>
# **invoiceSectionsListByBillingProfileName**
> InvoiceSectionListResult invoiceSectionsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName)



Lists all invoice sections under a billing profile for which a user has access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
    try {
      InvoiceSectionListResult result = apiInstance.invoiceSectionsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsListByBillingProfileName");
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

[**InvoiceSectionListResult**](InvoiceSectionListResult.md)

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

<a id="invoiceSectionsListByCreateSubscriptionPermission"></a>
# **invoiceSectionsListByCreateSubscriptionPermission**
> InvoiceSectionListResult invoiceSectionsListByCreateSubscriptionPermission(apiVersion, billingAccountName, $expand)



Lists all invoiceSections with create subscription permission for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String $expand = "$expand_example"; // String | May be used to expand the billingProfiles.
    try {
      InvoiceSectionListResult result = apiInstance.invoiceSectionsListByCreateSubscriptionPermission(apiVersion, billingAccountName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsListByCreateSubscriptionPermission");
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
| **$expand** | **String**| May be used to expand the billingProfiles. | [optional] |

### Return type

[**InvoiceSectionListResult**](InvoiceSectionListResult.md)

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

<a id="invoiceSectionsUpdate"></a>
# **invoiceSectionsUpdate**
> InvoiceSection invoiceSectionsUpdate(apiVersion, billingAccountName, invoiceSectionName, parameters)



The operation to update a InvoiceSection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceSectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    InvoiceSectionsApi apiInstance = new InvoiceSectionsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    String billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
    String invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
    InvoiceSection parameters = new InvoiceSection(); // InvoiceSection | Parameters supplied to the Create InvoiceSection operation.
    try {
      InvoiceSection result = apiInstance.invoiceSectionsUpdate(apiVersion, billingAccountName, invoiceSectionName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceSectionsApi#invoiceSectionsUpdate");
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
| **parameters** | [**InvoiceSection**](InvoiceSection.md)| Parameters supplied to the Create InvoiceSection operation. | |

### Return type

[**InvoiceSection**](InvoiceSection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted. InvoiceSection update is in progress. |  * Retry-After - The amount of delay to use while the status of the operation is checked. The value is expressed in seconds. <br>  * Location - Location URI to poll for result. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

