# InvoicesReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**finvoicesGetFinvoiceByInvoiceGuid**](InvoicesReadApi.md#finvoicesGetFinvoiceByInvoiceGuid) | **GET** /v1/invoices/{invoiceGuid}/finvoice |  |
| [**finvoicesGetFinvoicesByInvoiceStatus**](InvoicesReadApi.md#finvoicesGetFinvoicesByInvoiceStatus) | **GET** /v1/invoicestatuses/{invoiceStatusGuid}/finvoices |  |
| [**invoiceRowsGetInvoiceRow**](InvoicesReadApi.md#invoiceRowsGetInvoiceRow) | **GET** /v1/invoicerows/{guid} | Get invoice row by ID |
| [**invoiceRowsGetInvoiceRows**](InvoicesReadApi.md#invoiceRowsGetInvoiceRows) | **GET** /v1/invoicerows | Get invoice rows |
| [**invoiceRowsGetInvoiceRowsForInvoice**](InvoicesReadApi.md#invoiceRowsGetInvoiceRowsForInvoice) | **GET** /v1/invoices/{invoiceGuid}/invoicerows | Get Invoice rows for an invoice. |
| [**invoiceSettingsGetInvoiceSettings**](InvoicesReadApi.md#invoiceSettingsGetInvoiceSettings) | **GET** /v1/invoices/{invoiceGuid}/invoicesettings | Get invoice settings by invoice GUID |
| [**invoicesGetInvoice**](InvoicesReadApi.md#invoicesGetInvoice) | **GET** /v1/invoices/{guid} | Get invoice by ID |
| [**invoicesGetInvoices**](InvoicesReadApi.md#invoicesGetInvoices) | **GET** /v1/invoices | Get Invoices |
| [**projectFeesGetInvoiceProjectFees**](InvoicesReadApi.md#projectFeesGetInvoiceProjectFees) | **GET** /v1/invoices/{invoiceGuid}/projectfees | Get all the project fees on an invoice |
| [**projectFeesGetInvoiceRowProjectFees**](InvoicesReadApi.md#projectFeesGetInvoiceRowProjectFees) | **GET** /v1/invoicerows/{invoiceRowGuid}/projectfees | Get all the project fees on an invoice row |
| [**projectFeesGetUninvoicedProjectFeesForInvoice**](InvoicesReadApi.md#projectFeesGetUninvoicedProjectFeesForInvoice) | **GET** /v1/invoices/{invoiceGuid}/uninvoicedprojectfees | Get uninvoiced project fees available for invoice |
| [**projectInvoiceSettingsGetProjectInvoiceSetting**](InvoicesReadApi.md#projectInvoiceSettingsGetProjectInvoiceSetting) | **GET** /v1/projectinvoicesettings/{guid} | Get project invoice settings by ID. |
| [**projectInvoiceSettingsGetProjectInvoiceSettings**](InvoicesReadApi.md#projectInvoiceSettingsGetProjectInvoiceSettings) | **GET** /v1/projects/{projectGuid}/projectinvoicesettings | Get project invoice settings by project ID. |
| [**projectTravelExpensesGetInvoiceProjectTravelExpenses**](InvoicesReadApi.md#projectTravelExpensesGetInvoiceProjectTravelExpenses) | **GET** /v1/invoices/{invoiceGuid}/projecttravelexpenses | Get all the project travel expenses on an invoice |
| [**projectTravelExpensesGetInvoiceRowProjectTravelExpenses**](InvoicesReadApi.md#projectTravelExpensesGetInvoiceRowProjectTravelExpenses) | **GET** /v1/invoicerows/{invoiceRowGuid}/projecttravelexpenses | Get all the project travel expenses on an invoice row |
| [**projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice**](InvoicesReadApi.md#projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice) | **GET** /v1/invoices/{invoiceGuid}/uninvoicedprojecttravelexpenses | Get uninvoiced project travel expenses available for invoice |
| [**reimbursedProjectFeesGetInvoiceReimbursedProjectFees**](InvoicesReadApi.md#reimbursedProjectFeesGetInvoiceReimbursedProjectFees) | **GET** /v1/invoices/{invoiceGuid}/reimbursedprojectfees | Get all the project fees on an invoice |
| [**reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees**](InvoicesReadApi.md#reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees) | **GET** /v1/invoicerows/{invoiceRowGuid}/reimbursedprojectfees | Get all the project fees on an invoice row |
| [**reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses**](InvoicesReadApi.md#reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses) | **GET** /v1/invoices/{invoiceGuid}/reimbursedprojecttravelexpenses | Get all the project travel expenses on an invoice. |
| [**reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses**](InvoicesReadApi.md#reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses) | **GET** /v1/invoicerows/{invoiceRowGuid}/reimbursedprojecttravelexpenses | Get all the project travel expenses on an invoice row. |
| [**reimbursedWorkHoursGetInvoiceReimbursedWorkHours**](InvoicesReadApi.md#reimbursedWorkHoursGetInvoiceReimbursedWorkHours) | **GET** /v1/invoices/{invoiceGuid}/reimbursedworkhours | Get all reimbursed hours on an invoice. |
| [**reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours**](InvoicesReadApi.md#reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours) | **GET** /v1/invoicerows/{invoiceRowGuid}/reimbursedworkhours | Get all reimbursed hours on an invoice row. |
| [**workHoursGetInvoiceRowWorkHours**](InvoicesReadApi.md#workHoursGetInvoiceRowWorkHours) | **GET** /v1/invoicerows/{invoiceRowGuid}/workhours | Get all the work hours on an invoice row |
| [**workHoursGetInvoiceWorkHours**](InvoicesReadApi.md#workHoursGetInvoiceWorkHours) | **GET** /v1/invoices/{invoiceGuid}/workhours | Get all the work hours on an invoice |
| [**workHoursGetUninvoicedWorkHoursForInvoice**](InvoicesReadApi.md#workHoursGetUninvoicedWorkHoursForInvoice) | **GET** /v1/invoices/{invoiceGuid}/uninvoicedworkhours | Get uninvoiced work hours available for invoice |


<a id="finvoicesGetFinvoiceByInvoiceGuid"></a>
# **finvoicesGetFinvoiceByInvoiceGuid**
> File finvoicesGetFinvoiceByInvoiceGuid(invoiceGuid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | 
    try {
      File result = apiInstance.finvoicesGetFinvoiceByInvoiceGuid(invoiceGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#finvoicesGetFinvoiceByInvoiceGuid");
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
| **invoiceGuid** | **String**|  | |

### Return type

[**File**](File.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/soap+xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exports single invoice as Finvoice |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="finvoicesGetFinvoicesByInvoiceStatus"></a>
# **finvoicesGetFinvoicesByInvoiceStatus**
> File finvoicesGetFinvoicesByInvoiceStatus(invoiceStatusGuid)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceStatusGuid = "invoiceStatusGuid_example"; // String | 
    try {
      File result = apiInstance.finvoicesGetFinvoicesByInvoiceStatus(invoiceStatusGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#finvoicesGetFinvoicesByInvoiceStatus");
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
| **invoiceStatusGuid** | **String**|  | |

### Return type

[**File**](File.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Exports all invoices by invoice status as stream of multiple Finvoices |  -  |
| **403** | Addon required |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoiceRowsGetInvoiceRow"></a>
# **invoiceRowsGetInvoiceRow**
> InvoiceRowOutputModel invoiceRowsGetInvoiceRow(guid)

Get invoice row by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID of the invoice row.
    try {
      InvoiceRowOutputModel result = apiInstance.invoiceRowsGetInvoiceRow(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#invoiceRowsGetInvoiceRow");
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
| **guid** | **String**| GUID of the invoice row. | |

### Return type

[**InvoiceRowOutputModel**](InvoiceRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invoice row |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoiceRowsGetInvoiceRows"></a>
# **invoiceRowsGetInvoiceRows**
> List&lt;InvoiceRowOutputModel&gt; invoiceRowsGetInvoiceRows(pageToken, rowCount, changedSince)

Get invoice rows

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get invoice rows that have been added or changed after this date time (greater or equal).
    try {
      List<InvoiceRowOutputModel> result = apiInstance.invoiceRowsGetInvoiceRows(pageToken, rowCount, changedSince);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#invoiceRowsGetInvoiceRows");
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
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get invoice rows that have been added or changed after this date time (greater or equal). | [optional] |

### Return type

[**List&lt;InvoiceRowOutputModel&gt;**](InvoiceRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoiceRowsGetInvoiceRowsForInvoice"></a>
# **invoiceRowsGetInvoiceRowsForInvoice**
> List&lt;InvoiceRowOutputModel&gt; invoiceRowsGetInvoiceRowsForInvoice(invoiceGuid, pageToken, rowCount, rowType)

Get Invoice rows for an invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    InvoiceRowType rowType = InvoiceRowType.fromValue("FlatRate"); // InvoiceRowType | Optional: Type of the row. Either Hours or ProjectFees, Default all.
    try {
      List<InvoiceRowOutputModel> result = apiInstance.invoiceRowsGetInvoiceRowsForInvoice(invoiceGuid, pageToken, rowCount, rowType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#invoiceRowsGetInvoiceRowsForInvoice");
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
| **invoiceGuid** | **String**| ID of the invoice. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **rowType** | [**InvoiceRowType**](.md)| Optional: Type of the row. Either Hours or ProjectFees, Default all. | [optional] [enum: FlatRate, Hours, ProjectFees, TravelExpenses] |

### Return type

[**List&lt;InvoiceRowOutputModel&gt;**](InvoiceRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Invoice rows  |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoiceSettingsGetInvoiceSettings"></a>
# **invoiceSettingsGetInvoiceSettings**
> InvoiceSettingsOutputModel invoiceSettingsGetInvoiceSettings(invoiceGuid)

Get invoice settings by invoice GUID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | Invoice GUID used to get the invoice settings.
    try {
      InvoiceSettingsOutputModel result = apiInstance.invoiceSettingsGetInvoiceSettings(invoiceGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#invoiceSettingsGetInvoiceSettings");
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
| **invoiceGuid** | **String**| Invoice GUID used to get the invoice settings. | |

### Return type

[**InvoiceSettingsOutputModel**](InvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | InvoiceSettingsOutputModel |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoicesGetInvoice"></a>
# **invoicesGetInvoice**
> InvoiceOutputModel invoicesGetInvoice(guid)

Get invoice by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID of the invoice.
    try {
      InvoiceOutputModel result = apiInstance.invoicesGetInvoice(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#invoicesGetInvoice");
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
| **guid** | **String**| GUID of the invoice. | |

### Return type

[**InvoiceOutputModel**](InvoiceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="invoicesGetInvoices"></a>
# **invoicesGetInvoices**
> List&lt;InvoiceOutputModel&gt; invoicesGetInvoices(rowCount, pageToken, paymentDateStart, invoiceStatusGuids, projectGuids, projectOwnerGuids, projectBusinessUnitGuids, customerGuids, startDate, endDate, minimumTotalExcludingTax, maximumTotalExcludingTax, referenceNumbers, numbers, changedSince, salesPersonGuids, createdByUserGuids)

Get Invoices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    OffsetDateTime paymentDateStart = OffsetDateTime.now(); // OffsetDateTime | Optional: Get only invoices paid at this date or later. Default: Get invoices regardless of payment date.
    List<String> invoiceStatusGuids = Arrays.asList(); // List<String> | Optional: Get invoices with this status only. Default: all statuses.
    List<String> projectGuids = Arrays.asList(); // List<String> | Optional: ID of the project to get the invoices. If not provided, returns for all projects. Default all.
    List<String> projectOwnerGuids = Arrays.asList(); // List<String> | Optional: ID of the project manager to get the invoices for. If not provided, returns for all project managers. Default all.
    List<String> projectBusinessUnitGuids = Arrays.asList(); // List<String> | Optional: ID of the business unit of the project. If not provided, returns for all business units. Default all.
    List<String> customerGuids = Arrays.asList(); // List<String> | Optional: List of customer IDs. Get invoices for these customers.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Optional: starting date from which to get the invoices. Default all.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Optional: end date from which to get the invoices. Default all.
    Double minimumTotalExcludingTax = 3.4D; // Double | Optional: specifies minimum value for invoice total in organization currency.
    Double maximumTotalExcludingTax = 3.4D; // Double | Optional: specifies maximum value for invoice total in organization currency.
    List<String> referenceNumbers = Arrays.asList(); // List<String> | Optional: Invoice reference number. If not provided, returns invoices with any invoice reference number.
    List<Integer> numbers = Arrays.asList(); // List<Integer> | Optional: Invoice number. If not provided, returns invoices with any invoice number.
    OffsetDateTime changedSince = OffsetDateTime.now(); // OffsetDateTime | Optional: Get invoices that have been added or changed after this date time (greater or equal).
    List<String> salesPersonGuids = Arrays.asList(); // List<String> | Optional: ID of the salesperson to get the invoices for. If not provided, returns for all sales persons.
    List<String> createdByUserGuids = Arrays.asList(); // List<String> | Optional: ID of the user who created the invoice. If not provided, returns for all users.
    try {
      List<InvoiceOutputModel> result = apiInstance.invoicesGetInvoices(rowCount, pageToken, paymentDateStart, invoiceStatusGuids, projectGuids, projectOwnerGuids, projectBusinessUnitGuids, customerGuids, startDate, endDate, minimumTotalExcludingTax, maximumTotalExcludingTax, referenceNumbers, numbers, changedSince, salesPersonGuids, createdByUserGuids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#invoicesGetInvoices");
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
| **rowCount** | **Integer**| Optional: Number of rows to fetch. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **paymentDateStart** | **OffsetDateTime**| Optional: Get only invoices paid at this date or later. Default: Get invoices regardless of payment date. | [optional] |
| **invoiceStatusGuids** | [**List&lt;String&gt;**](String.md)| Optional: Get invoices with this status only. Default: all statuses. | [optional] |
| **projectGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the project to get the invoices. If not provided, returns for all projects. Default all. | [optional] |
| **projectOwnerGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the project manager to get the invoices for. If not provided, returns for all project managers. Default all. | [optional] |
| **projectBusinessUnitGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the business unit of the project. If not provided, returns for all business units. Default all. | [optional] |
| **customerGuids** | [**List&lt;String&gt;**](String.md)| Optional: List of customer IDs. Get invoices for these customers. | [optional] |
| **startDate** | **OffsetDateTime**| Optional: starting date from which to get the invoices. Default all. | [optional] |
| **endDate** | **OffsetDateTime**| Optional: end date from which to get the invoices. Default all. | [optional] |
| **minimumTotalExcludingTax** | **Double**| Optional: specifies minimum value for invoice total in organization currency. | [optional] |
| **maximumTotalExcludingTax** | **Double**| Optional: specifies maximum value for invoice total in organization currency. | [optional] |
| **referenceNumbers** | [**List&lt;String&gt;**](String.md)| Optional: Invoice reference number. If not provided, returns invoices with any invoice reference number. | [optional] |
| **numbers** | [**List&lt;Integer&gt;**](Integer.md)| Optional: Invoice number. If not provided, returns invoices with any invoice number. | [optional] |
| **changedSince** | **OffsetDateTime**| Optional: Get invoices that have been added or changed after this date time (greater or equal). | [optional] |
| **salesPersonGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the salesperson to get the invoices for. If not provided, returns for all sales persons. | [optional] |
| **createdByUserGuids** | [**List&lt;String&gt;**](String.md)| Optional: ID of the user who created the invoice. If not provided, returns for all users. | [optional] |

### Return type

[**List&lt;InvoiceOutputModel&gt;**](InvoiceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Invoices  |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectFeesGetInvoiceProjectFees"></a>
# **projectFeesGetInvoiceProjectFees**
> List&lt;ProjectFeeOutputModel&gt; projectFeesGetInvoiceProjectFees(invoiceGuid, pageToken, rowCount, productType)

Get all the project fees on an invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch.
    ProductType productType = ProductType.fromValue("FixedFees"); // ProductType | Optional: ProjectFee's product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting
    try {
      List<ProjectFeeOutputModel> result = apiInstance.projectFeesGetInvoiceProjectFees(invoiceGuid, pageToken, rowCount, productType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#projectFeesGetInvoiceProjectFees");
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
| **invoiceGuid** | **String**| ID of the invoice. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: Number of rows to fetch. | [optional] |
| **productType** | [**ProductType**](.md)| Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting | [optional] [enum: FixedFees, Materials, Subcontracting] |

### Return type

[**List&lt;ProjectFeeOutputModel&gt;**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectFees |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectFeesGetInvoiceRowProjectFees"></a>
# **projectFeesGetInvoiceRowProjectFees**
> List&lt;ProjectFeeOutputModel&gt; projectFeesGetInvoiceRowProjectFees(invoiceRowGuid, pageToken, rowCount, productType)

Get all the project fees on an invoice row

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch.
    ProductType productType = ProductType.fromValue("FixedFees"); // ProductType | Optional: ProjectFee's product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting
    try {
      List<ProjectFeeOutputModel> result = apiInstance.projectFeesGetInvoiceRowProjectFees(invoiceRowGuid, pageToken, rowCount, productType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#projectFeesGetInvoiceRowProjectFees");
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
| **invoiceRowGuid** | **String**| ID of the invoice row. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: Number of rows to fetch. | [optional] |
| **productType** | [**ProductType**](.md)| Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting | [optional] [enum: FixedFees, Materials, Subcontracting] |

### Return type

[**List&lt;ProjectFeeOutputModel&gt;**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectFees |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectFeesGetUninvoicedProjectFeesForInvoice"></a>
# **projectFeesGetUninvoicedProjectFeesForInvoice**
> List&lt;ProjectFeeOutputModel&gt; projectFeesGetUninvoicedProjectFeesForInvoice(invoiceGuid, pageToken, rowCount, isBillable)

Get uninvoiced project fees available for invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch.
    Boolean isBillable = true; // Boolean | Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    try {
      List<ProjectFeeOutputModel> result = apiInstance.projectFeesGetUninvoicedProjectFeesForInvoice(invoiceGuid, pageToken, rowCount, isBillable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#projectFeesGetUninvoicedProjectFeesForInvoice");
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
| **invoiceGuid** | **String**| ID of the invoice. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: Number of rows to fetch. | [optional] |
| **isBillable** | **Boolean**| Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] |

### Return type

[**List&lt;ProjectFeeOutputModel&gt;**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectFees |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectInvoiceSettingsGetProjectInvoiceSetting"></a>
# **projectInvoiceSettingsGetProjectInvoiceSetting**
> ProjectInvoiceSettingsOutputModel projectInvoiceSettingsGetProjectInvoiceSetting(guid)

Get project invoice settings by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String guid = "guid_example"; // String | ID of the project invoice settings.
    try {
      ProjectInvoiceSettingsOutputModel result = apiInstance.projectInvoiceSettingsGetProjectInvoiceSetting(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#projectInvoiceSettingsGetProjectInvoiceSetting");
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

### Return type

[**ProjectInvoiceSettingsOutputModel**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project invoice settings. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectInvoiceSettingsGetProjectInvoiceSettings"></a>
# **projectInvoiceSettingsGetProjectInvoiceSettings**
> List&lt;ProjectInvoiceSettingsOutputModel&gt; projectInvoiceSettingsGetProjectInvoiceSettings(projectGuid)

Get project invoice settings by project ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | ID of the project.
    try {
      List<ProjectInvoiceSettingsOutputModel> result = apiInstance.projectInvoiceSettingsGetProjectInvoiceSettings(projectGuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#projectInvoiceSettingsGetProjectInvoiceSettings");
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
| **projectGuid** | **String**| ID of the project. | |

### Return type

[**List&lt;ProjectInvoiceSettingsOutputModel&gt;**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project invoice settings. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTravelExpensesGetInvoiceProjectTravelExpenses"></a>
# **projectTravelExpensesGetInvoiceProjectTravelExpenses**
> List&lt;ProjectTravelExpenseOutputModel&gt; projectTravelExpensesGetInvoiceProjectTravelExpenses(invoiceGuid, pageToken, rowCount, expenseClass)

Get all the project travel expenses on an invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    ExpensesClass expenseClass = ExpensesClass.fromValue("Mileage"); // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    try {
      List<ProjectTravelExpenseOutputModel> result = apiInstance.projectTravelExpensesGetInvoiceProjectTravelExpenses(invoiceGuid, pageToken, rowCount, expenseClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#projectTravelExpensesGetInvoiceProjectTravelExpenses");
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
| **invoiceGuid** | **String**| ID of the invoice. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] [enum: Mileage, DailyAllowance, OtherTravelExpense] |

### Return type

[**List&lt;ProjectTravelExpenseOutputModel&gt;**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectTravelExpenseOutputModel |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTravelExpensesGetInvoiceRowProjectTravelExpenses"></a>
# **projectTravelExpensesGetInvoiceRowProjectTravelExpenses**
> List&lt;ProjectTravelExpenseOutputModel&gt; projectTravelExpensesGetInvoiceRowProjectTravelExpenses(invoiceRowGuid, pageToken, rowCount, expenseClass)

Get all the project travel expenses on an invoice row

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    ExpensesClass expenseClass = ExpensesClass.fromValue("Mileage"); // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    try {
      List<ProjectTravelExpenseOutputModel> result = apiInstance.projectTravelExpensesGetInvoiceRowProjectTravelExpenses(invoiceRowGuid, pageToken, rowCount, expenseClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#projectTravelExpensesGetInvoiceRowProjectTravelExpenses");
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
| **invoiceRowGuid** | **String**| ID of the invoice row. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] [enum: Mileage, DailyAllowance, OtherTravelExpense] |

### Return type

[**List&lt;ProjectTravelExpenseOutputModel&gt;**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectTravelExpenseOutputModel |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice"></a>
# **projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice**
> List&lt;ProjectTravelExpenseOutputModel&gt; projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice(invoiceGuid, isBillable, pageToken, rowCount, expenseClass)

Get uninvoiced project travel expenses available for invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
    Boolean isBillable = true; // Boolean | Optional: Filter the travel expenses. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    ExpensesClass expenseClass = ExpensesClass.fromValue("Mileage"); // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    try {
      List<ProjectTravelExpenseOutputModel> result = apiInstance.projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice(invoiceGuid, isBillable, pageToken, rowCount, expenseClass);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice");
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
| **invoiceGuid** | **String**| ID of the invoice. | |
| **isBillable** | **Boolean**| Optional: Filter the travel expenses. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] [enum: Mileage, DailyAllowance, OtherTravelExpense] |

### Return type

[**List&lt;ProjectTravelExpenseOutputModel&gt;**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectTravelExpenseOutputModel |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="reimbursedProjectFeesGetInvoiceReimbursedProjectFees"></a>
# **reimbursedProjectFeesGetInvoiceReimbursedProjectFees**
> List&lt;ReimbursedProjectFeeOutputModel&gt; reimbursedProjectFeesGetInvoiceReimbursedProjectFees(invoiceGuid, rowCount, pageToken)

Get all the project fees on an invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    try {
      List<ReimbursedProjectFeeOutputModel> result = apiInstance.reimbursedProjectFeesGetInvoiceReimbursedProjectFees(invoiceGuid, rowCount, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#reimbursedProjectFeesGetInvoiceReimbursedProjectFees");
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
| **invoiceGuid** | **String**| ID of the invoice. | |
| **rowCount** | **Integer**| Optional: Number of rows to fetch | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |

### Return type

[**List&lt;ReimbursedProjectFeeOutputModel&gt;**](ReimbursedProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ReimbursedProjectFee |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees"></a>
# **reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees**
> List&lt;ReimbursedProjectFeeOutputModel&gt; reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees(invoiceRowGuid, rowCount, pageToken)

Get all the project fees on an invoice row

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
    Integer rowCount = 56; // Integer | Optional: Number of rows to fetch
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    try {
      List<ReimbursedProjectFeeOutputModel> result = apiInstance.reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees(invoiceRowGuid, rowCount, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees");
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
| **invoiceRowGuid** | **String**| ID of the invoice row. | |
| **rowCount** | **Integer**| Optional: Number of rows to fetch | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |

### Return type

[**List&lt;ReimbursedProjectFeeOutputModel&gt;**](ReimbursedProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ReimbursedProjectFee |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses"></a>
# **reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses**
> List&lt;ReimbursedProjectTravelExpenseOutputModel&gt; reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses(invoiceGuid, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get all the project travel expenses on an invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    String textToSearch = ""; // String | Searched string: part of name or description.
    Boolean calculateRowCount = false; // Boolean | Optional. If true, calculates the total count of project fees. Default false.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
    try {
      List<ReimbursedProjectTravelExpenseOutputModel> result = apiInstance.reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses(invoiceGuid, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses");
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
| **invoiceGuid** | **String**| ID of the invoice. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |
| **textToSearch** | **String**| Searched string: part of name or description. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional. If true, calculates the total count of project fees. Default false. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;ReimbursedProjectTravelExpenseOutputModel&gt;**](ReimbursedProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ReimbursedProjectTravelExpenses. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses"></a>
# **reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses**
> List&lt;ReimbursedProjectTravelExpenseOutputModel&gt; reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses(invoiceRowGuid, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get all the project travel expenses on an invoice row.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
    Integer firstRow = 0; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default all.
    String textToSearch = ""; // String | Searched string: part of name or description.
    Boolean calculateRowCount = false; // Boolean | Optional. If true, calculates the total count of project fees. Default false.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
    try {
      List<ReimbursedProjectTravelExpenseOutputModel> result = apiInstance.reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses(invoiceRowGuid, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses");
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
| **invoiceRowGuid** | **String**| ID of the invoice row. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default all. | [optional] |
| **textToSearch** | **String**| Searched string: part of name or description. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional. If true, calculates the total count of project fees. Default false. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;ReimbursedProjectTravelExpenseOutputModel&gt;**](ReimbursedProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ReimbursedProjectTravelExpenses. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="reimbursedWorkHoursGetInvoiceReimbursedWorkHours"></a>
# **reimbursedWorkHoursGetInvoiceReimbursedWorkHours**
> List&lt;ReimbursedWorkHourOutputModel&gt; reimbursedWorkHoursGetInvoiceReimbursedWorkHours(invoiceGuid, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get all reimbursed hours on an invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from description or invoice description.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=DueDate&sortings[0].value=Asc&sortings[1].key=TotalIncludingTax&sortings[1].value=Desc\".
    try {
      List<ReimbursedWorkHourOutputModel> result = apiInstance.reimbursedWorkHoursGetInvoiceReimbursedWorkHours(invoiceGuid, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#reimbursedWorkHoursGetInvoiceReimbursedWorkHours");
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
| **invoiceGuid** | **String**| ID of the invoice. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from description or invoice description. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;DueDate&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;TotalIncludingTax&amp;sortings[1].value&#x3D;Desc\&quot;. | [optional] |

### Return type

[**List&lt;ReimbursedWorkHourOutputModel&gt;**](ReimbursedWorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ReimbursedWorkHour. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours"></a>
# **reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours**
> List&lt;ReimbursedWorkHourOutputModel&gt; reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours(invoiceRowGuid, firstRow, rowCount, textToSearch, calculateRowCount, sortings)

Get all reimbursed hours on an invoice row.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    String textToSearch = ""; // String | Optional: Text to search from description or invoice description.
    Boolean calculateRowCount = false; // Boolean | Optional: Calculate total number of rows.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=DueDate&sortings[0].value=Asc&sortings[1].key=TotalIncludingTax&sortings[1].value=Desc\".
    try {
      List<ReimbursedWorkHourOutputModel> result = apiInstance.reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours(invoiceRowGuid, firstRow, rowCount, textToSearch, calculateRowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours");
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
| **invoiceRowGuid** | **String**| ID of the invoice row. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |
| **textToSearch** | **String**| Optional: Text to search from description or invoice description. | [optional] [default to ] |
| **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;DueDate&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;TotalIncludingTax&amp;sortings[1].value&#x3D;Desc\&quot;. | [optional] |

### Return type

[**List&lt;ReimbursedWorkHourOutputModel&gt;**](ReimbursedWorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ReimbursedWorkHour. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workHoursGetInvoiceRowWorkHours"></a>
# **workHoursGetInvoiceRowWorkHours**
> List&lt;WorkHourOutputModel&gt; workHoursGetInvoiceRowWorkHours(invoiceRowGuid, pageToken, rowCount)

Get all the work hours on an invoice row

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    try {
      List<WorkHourOutputModel> result = apiInstance.workHoursGetInvoiceRowWorkHours(invoiceRowGuid, pageToken, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#workHoursGetInvoiceRowWorkHours");
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
| **invoiceRowGuid** | **String**| ID of the invoice row. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |

### Return type

[**List&lt;WorkHourOutputModel&gt;**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | WorkHours |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workHoursGetInvoiceWorkHours"></a>
# **workHoursGetInvoiceWorkHours**
> List&lt;WorkHourOutputModel&gt; workHoursGetInvoiceWorkHours(invoiceGuid, pageToken, rowCount)

Get all the work hours on an invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    try {
      List<WorkHourOutputModel> result = apiInstance.workHoursGetInvoiceWorkHours(invoiceGuid, pageToken, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#workHoursGetInvoiceWorkHours");
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
| **invoiceGuid** | **String**| ID of the invoice. | |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |

### Return type

[**List&lt;WorkHourOutputModel&gt;**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | WorkHours |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="workHoursGetUninvoicedWorkHoursForInvoice"></a>
# **workHoursGetUninvoicedWorkHoursForInvoice**
> List&lt;WorkHourOutputModel&gt; workHoursGetUninvoicedWorkHoursForInvoice(invoiceGuid, isBillable, pageToken, rowCount)

Get uninvoiced work hours available for invoice

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesReadApi;

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

    InvoicesReadApi apiInstance = new InvoicesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
    Boolean isBillable = true; // Boolean | Optional: Filter the work hours. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    String pageToken = "pageToken_example"; // String | Optional: page token to fetch the next page.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch, Default 20, maximum 100.
    try {
      List<WorkHourOutputModel> result = apiInstance.workHoursGetUninvoicedWorkHoursForInvoice(invoiceGuid, isBillable, pageToken, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesReadApi#workHoursGetUninvoicedWorkHoursForInvoice");
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
| **invoiceGuid** | **String**| ID of the invoice. | |
| **isBillable** | **Boolean**| Optional: Filter the work hours. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] |
| **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] |

### Return type

[**List&lt;WorkHourOutputModel&gt;**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | WorkHours |  * NextPageToken - Page token to fetch the next page <br>  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

