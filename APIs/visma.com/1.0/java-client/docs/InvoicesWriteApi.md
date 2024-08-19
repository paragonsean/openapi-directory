# InvoicesWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**invoiceRowsPatchInvoiceRow**](InvoicesWriteApi.md#invoiceRowsPatchInvoiceRow) | **PATCH** /v1/invoicerows/{guid} | Update (Patch) a invoice row or a part of it |
| [**invoiceSettingsPatchInvoiceSettings**](InvoicesWriteApi.md#invoiceSettingsPatchInvoiceSettings) | **PATCH** /v1/invoicesettings/{guid} | Update (Patch) invoice setting |
| [**invoicesPatchInvoice**](InvoicesWriteApi.md#invoicesPatchInvoice) | **PATCH** /v1/invoices/{guid} | Update (Patch) an invoice or a part of it |
| [**invoicesPostInvoiceCreation**](InvoicesWriteApi.md#invoicesPostInvoiceCreation) | **POST** /v1/invoices | Add an invoice to project(s) |
| [**projectInvoiceSettingsPatchProjectInvoiceSettings**](InvoicesWriteApi.md#projectInvoiceSettingsPatchProjectInvoiceSettings) | **PATCH** /v1/projectinvoicesettings/{guid} | Update (Patch) project invoice settings. |
| [**projectInvoiceSettingsPostProjectInvoiceSettings**](InvoicesWriteApi.md#projectInvoiceSettingsPostProjectInvoiceSettings) | **POST** /v1/projectinvoicesettings | Create a new project invoice settings. |


<a id="invoiceRowsPatchInvoiceRow"></a>
# **invoiceRowsPatchInvoiceRow**
> List&lt;InvoiceRowOutputModel&gt; invoiceRowsPatchInvoiceRow(guid, patchOperation)

Update (Patch) a invoice row or a part of it

If CostCenterNumber, SalesAccountNumber or RecurringSalesAccountNumber are changed and the invoice row is related to one or many ProjectFees or ProjectTravelExpenses, the values for those will also be updated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesWriteApi;

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

    InvoicesWriteApi apiInstance = new InvoicesWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the invoice row
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON Patch document of InvoiceRowModel
    try {
      List<InvoiceRowOutputModel> result = apiInstance.invoiceRowsPatchInvoiceRow(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesWriteApi#invoiceRowsPatchInvoiceRow");
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
| **guid** | **String**| ID of the invoice row | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON Patch document of InvoiceRowModel | [optional] |

### Return type

[**List&lt;InvoiceRowOutputModel&gt;**](InvoiceRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of updated invoice rows |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoiceSettingsPatchInvoiceSettings"></a>
# **invoiceSettingsPatchInvoiceSettings**
> InvoiceSettingsOutputModel invoiceSettingsPatchInvoiceSettings(guid, patchOperation)

Update (Patch) invoice setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesWriteApi;

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

    InvoicesWriteApi apiInstance = new InvoicesWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the invoice settings
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of InvoiceSettingsModel
    try {
      InvoiceSettingsOutputModel result = apiInstance.invoiceSettingsPatchInvoiceSettings(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesWriteApi#invoiceSettingsPatchInvoiceSettings");
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
| **guid** | **String**| ID of the invoice settings | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of InvoiceSettingsModel | [optional] |

### Return type

[**InvoiceSettingsOutputModel**](InvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | InvoiceSettingsOutputModel |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoicesPatchInvoice"></a>
# **invoicesPatchInvoice**
> List&lt;InvoiceOutputModel&gt; invoicesPatchInvoice(guid, patchOperation)

Update (Patch) an invoice or a part of it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesWriteApi;

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

    InvoicesWriteApi apiInstance = new InvoicesWriteApi(defaultClient);
    String guid = "guid_example"; // String | GUID of the invoice
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of InvoiceInputModel
    try {
      List<InvoiceOutputModel> result = apiInstance.invoicesPatchInvoice(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesWriteApi#invoicesPatchInvoice");
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
| **guid** | **String**| GUID of the invoice | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of InvoiceInputModel | [optional] |

### Return type

[**List&lt;InvoiceOutputModel&gt;**](InvoiceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list of invoices |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoicesPostInvoiceCreation"></a>
# **invoicesPostInvoiceCreation**
> List&lt;InvoiceOutputModel&gt; invoicesPostInvoiceCreation(createInvoiceModel)

Add an invoice to project(s)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesWriteApi;

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

    InvoicesWriteApi apiInstance = new InvoicesWriteApi(defaultClient);
    CreateInvoiceModel createInvoiceModel = new CreateInvoiceModel(); // CreateInvoiceModel | CreateInvoiceModel
    try {
      List<InvoiceOutputModel> result = apiInstance.invoicesPostInvoiceCreation(createInvoiceModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesWriteApi#invoicesPostInvoiceCreation");
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
| **createInvoiceModel** | [**CreateInvoiceModel**](CreateInvoiceModel.md)| CreateInvoiceModel | [optional] |

### Return type

[**List&lt;InvoiceOutputModel&gt;**](InvoiceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created invoice(s) |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectInvoiceSettingsPatchProjectInvoiceSettings"></a>
# **projectInvoiceSettingsPatchProjectInvoiceSettings**
> List&lt;ProjectInvoiceSettingsOutputModel&gt; projectInvoiceSettingsPatchProjectInvoiceSettings(guid, patchOperation)

Update (Patch) project invoice settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesWriteApi;

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

    InvoicesWriteApi apiInstance = new InvoicesWriteApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project invoice settings.
    List<PatchOperation> patchOperation = Arrays.asList(); // List<PatchOperation> | JSON patch document of ProjectInvoiceSettingsInputModel.
    try {
      List<ProjectInvoiceSettingsOutputModel> result = apiInstance.projectInvoiceSettingsPatchProjectInvoiceSettings(guid, patchOperation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesWriteApi#projectInvoiceSettingsPatchProjectInvoiceSettings");
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
| **guid** | **String**| ID of the project invoice settings. | |
| **patchOperation** | [**List&lt;PatchOperation&gt;**](PatchOperation.md)| JSON patch document of ProjectInvoiceSettingsInputModel. | [optional] |

### Return type

[**List&lt;ProjectInvoiceSettingsOutputModel&gt;**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project invoice settings. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectInvoiceSettingsPostProjectInvoiceSettings"></a>
# **projectInvoiceSettingsPostProjectInvoiceSettings**
> ProjectInvoiceSettingsOutputModel projectInvoiceSettingsPostProjectInvoiceSettings(projectInvoiceSettingsInputModel)

Create a new project invoice settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesWriteApi;

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

    InvoicesWriteApi apiInstance = new InvoicesWriteApi(defaultClient);
    ProjectInvoiceSettingsInputModel projectInvoiceSettingsInputModel = new ProjectInvoiceSettingsInputModel(); // ProjectInvoiceSettingsInputModel | Project invoice settings.
    try {
      ProjectInvoiceSettingsOutputModel result = apiInstance.projectInvoiceSettingsPostProjectInvoiceSettings(projectInvoiceSettingsInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesWriteApi#projectInvoiceSettingsPostProjectInvoiceSettings");
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
| **projectInvoiceSettingsInputModel** | [**ProjectInvoiceSettingsInputModel**](ProjectInvoiceSettingsInputModel.md)| Project invoice settings. | [optional] |

### Return type

[**ProjectInvoiceSettingsOutputModel**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created project invoice settings. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

