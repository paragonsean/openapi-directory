# InvoicesDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**invoiceRowsDeleteInvoiceRow**](InvoicesDeleteApi.md#invoiceRowsDeleteInvoiceRow) | **DELETE** /v1/invoicerows/{guid} | Deletes an invoice row |
| [**invoicesDeleteInvoice**](InvoicesDeleteApi.md#invoicesDeleteInvoice) | **DELETE** /v1/invoices/{guid} | Delete an invoice. |
| [**invoicesDeleteProjectFromInvoice**](InvoicesDeleteApi.md#invoicesDeleteProjectFromInvoice) | **DELETE** /v1/invoices/{guid}/projects/{projectGuid} | Delete a project from invoice. |
| [**projectInvoiceSettingsDeleteProjectInvoiceSettings**](InvoicesDeleteApi.md#projectInvoiceSettingsDeleteProjectInvoiceSettings) | **DELETE** /v1/projectinvoicesettings/{guid} | Delete an project invoice settings. |


<a id="invoiceRowsDeleteInvoiceRow"></a>
# **invoiceRowsDeleteInvoiceRow**
> invoiceRowsDeleteInvoiceRow(guid, setAsNonBillable)

Deletes an invoice row

Returns: No Content (204) if succeeded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesDeleteApi apiInstance = new InvoicesDeleteApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to delete the invoice row.
    Boolean setAsNonBillable = false; // Boolean | 
    try {
      apiInstance.invoiceRowsDeleteInvoiceRow(guid, setAsNonBillable);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesDeleteApi#invoiceRowsDeleteInvoiceRow");
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
| **guid** | **String**| GUID used to delete the invoice row. | |
| **setAsNonBillable** | **Boolean**|  | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoicesDeleteInvoice"></a>
# **invoicesDeleteInvoice**
> invoicesDeleteInvoice(guid)

Delete an invoice.

Returns: No Content (204) if succeeded. Not found (404) if cost center can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesDeleteApi apiInstance = new InvoicesDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the invoice to delete.
    try {
      apiInstance.invoicesDeleteInvoice(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesDeleteApi#invoicesDeleteInvoice");
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
| **guid** | **String**| ID for the invoice to delete. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoicesDeleteProjectFromInvoice"></a>
# **invoicesDeleteProjectFromInvoice**
> invoicesDeleteProjectFromInvoice(guid, projectGuid)

Delete a project from invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesDeleteApi apiInstance = new InvoicesDeleteApi(defaultClient);
    String guid = "guid_example"; // String | The invoice GUID.
    String projectGuid = "projectGuid_example"; // String | The project GUID.
    try {
      apiInstance.invoicesDeleteProjectFromInvoice(guid, projectGuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesDeleteApi#invoicesDeleteProjectFromInvoice");
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
| **guid** | **String**| The invoice GUID. | |
| **projectGuid** | **String**| The project GUID. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The updated invoice. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectInvoiceSettingsDeleteProjectInvoiceSettings"></a>
# **projectInvoiceSettingsDeleteProjectInvoiceSettings**
> projectInvoiceSettingsDeleteProjectInvoiceSettings(guid)

Delete an project invoice settings.

Returns: No Content (204) if succeeded. Not found (404) if project invoice settings can&#39;t be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.severa.visma.com/rest-api");
    
    // Configure API key authorization: ClientIdAuth
    ApiKeyAuth ClientIdAuth = (ApiKeyAuth) defaultClient.getAuthentication("ClientIdAuth");
    ClientIdAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ClientIdAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    InvoicesDeleteApi apiInstance = new InvoicesDeleteApi(defaultClient);
    String guid = "guid_example"; // String | ID for the project invoice settings to delete.
    try {
      apiInstance.projectInvoiceSettingsDeleteProjectInvoiceSettings(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesDeleteApi#projectInvoiceSettingsDeleteProjectInvoiceSettings");
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
| **guid** | **String**| ID for the project invoice settings to delete. | |

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

