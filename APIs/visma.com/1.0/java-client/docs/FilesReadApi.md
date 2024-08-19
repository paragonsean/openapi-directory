# FilesReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fileDataGetDataForFile**](FilesReadApi.md#fileDataGetDataForFile) | **GET** /v1/files/{guid}/filedata | Get file data by ID. |
| [**filesGetFile**](FilesReadApi.md#filesGetFile) | **GET** /v1/files/{guid} | Get file by ID. |
| [**filesGetInvoiceFile**](FilesReadApi.md#filesGetInvoiceFile) | **GET** /v1/invoicefiles/{guid} | Get invoice file by ID. |
| [**filesGetInvoiceFiles**](FilesReadApi.md#filesGetInvoiceFiles) | **GET** /v1/invoices/{invoiceGuid}/files | Get all files of a invoice by its id. |
| [**filesGetProjectFile**](FilesReadApi.md#filesGetProjectFile) | **GET** /v1/projectfiles/{guid} | Get project file by ID. |
| [**filesGetProjectFiles**](FilesReadApi.md#filesGetProjectFiles) | **GET** /v1/projects/{projectGuid}/files | Get all files of a project by its id. |
| [**filesGetTravelExpenseFile**](FilesReadApi.md#filesGetTravelExpenseFile) | **GET** /v1/projecttravelexpensefiles/{guid} | Get travel expense file by ID. |
| [**filesGetTravelExpenseFiles**](FilesReadApi.md#filesGetTravelExpenseFiles) | **GET** /v1/projecttravelexpenses/{projectTravelExpenseGuid}/files | Get all files of a travel expense by its id. |
| [**filesGetUsersTravelExpensesFiles**](FilesReadApi.md#filesGetUsersTravelExpensesFiles) | **GET** /v1/users/{userGuid}/travelexpensesfiles | Get all files of all travel expenses of the user. |
| [**keywordsGetFileKeywords**](FilesReadApi.md#keywordsGetFileKeywords) | **GET** /v1/files/{fileGuid}/keywords | Get all the keywords for file. |
| [**pdfGetInvoicePdf**](FilesReadApi.md#pdfGetInvoicePdf) | **GET** /v1/invoices/{guid}/pdf | Get an invoice PDF. |
| [**pdfGetTravelReimbursementPdf**](FilesReadApi.md#pdfGetTravelReimbursementPdf) | **GET** /v1/travelreimbursements/{guid}/pdf | Get a travel reimbursement PDF. |


<a id="fileDataGetDataForFile"></a>
# **fileDataGetDataForFile**
> File fileDataGetDataForFile(guid)

Get file data by ID.

Returns binary data, which contains content with type given in Content-Type header.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the file.
    try {
      File result = apiInstance.fileDataGetDataForFile(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#fileDataGetDataForFile");
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
| **guid** | **String**| GUID used to get the file. | |

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
| **200** | Get file data by ID |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="filesGetFile"></a>
# **filesGetFile**
> FileModel filesGetFile(guid, includeDataInResponse)

Get file by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the file.
    Boolean includeDataInResponse = false; // Boolean | Is data included in response as base64 string.
    try {
      FileModel result = apiInstance.filesGetFile(guid, includeDataInResponse);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#filesGetFile");
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
| **guid** | **String**| GUID used to get the file. | |
| **includeDataInResponse** | **Boolean**| Is data included in response as base64 string. | [optional] [default to false] |

### Return type

[**FileModel**](FileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="filesGetInvoiceFile"></a>
# **filesGetInvoiceFile**
> InvoiceFileModel filesGetInvoiceFile(guid)

Get invoice file by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the invoice file.
    try {
      InvoiceFileModel result = apiInstance.filesGetInvoiceFile(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#filesGetInvoiceFile");
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
| **guid** | **String**| GUID used to get the invoice file. | |

### Return type

[**InvoiceFileModel**](InvoiceFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | InvoiceFile. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="filesGetInvoiceFiles"></a>
# **filesGetInvoiceFiles**
> List&lt;InvoiceFileModel&gt; filesGetInvoiceFiles(invoiceGuid, firstRow, rowCount)

Get all files of a invoice by its id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String invoiceGuid = "invoiceGuid_example"; // String | GUID of the invoice used to get the files.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch.
    try {
      List<InvoiceFileModel> result = apiInstance.filesGetInvoiceFiles(invoiceGuid, firstRow, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#filesGetInvoiceFiles");
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
| **invoiceGuid** | **String**| GUID of the invoice used to get the files. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch. | [optional] |

### Return type

[**List&lt;InvoiceFileModel&gt;**](InvoiceFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | InvoiceFile. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="filesGetProjectFile"></a>
# **filesGetProjectFile**
> ProjectFileModel filesGetProjectFile(guid)

Get project file by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the project file.
    try {
      ProjectFileModel result = apiInstance.filesGetProjectFile(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#filesGetProjectFile");
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
| **guid** | **String**| GUID used to get the project file. | |

### Return type

[**ProjectFileModel**](ProjectFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProposalFile. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="filesGetProjectFiles"></a>
# **filesGetProjectFiles**
> List&lt;ProjectFileModel&gt; filesGetProjectFiles(projectGuid, firstRow, rowCount, sortings)

Get all files of a project by its id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String projectGuid = "projectGuid_example"; // String | GUID of the project used to get the files.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
    try {
      List<ProjectFileModel> result = apiInstance.filesGetProjectFiles(projectGuid, firstRow, rowCount, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#filesGetProjectFiles");
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
| **projectGuid** | **String**| GUID of the project used to get the files. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch. | [optional] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] |

### Return type

[**List&lt;ProjectFileModel&gt;**](ProjectFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="filesGetTravelExpenseFile"></a>
# **filesGetTravelExpenseFile**
> ProjectTravelExpenseFileModel filesGetTravelExpenseFile(guid)

Get travel expense file by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String guid = "guid_example"; // String | GUID used to get the travel expense file.
    try {
      ProjectTravelExpenseFileModel result = apiInstance.filesGetTravelExpenseFile(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#filesGetTravelExpenseFile");
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
| **guid** | **String**| GUID used to get the travel expense file. | |

### Return type

[**ProjectTravelExpenseFileModel**](ProjectTravelExpenseFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | InvoiceFile. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="filesGetTravelExpenseFiles"></a>
# **filesGetTravelExpenseFiles**
> List&lt;ProjectTravelExpenseFileModel&gt; filesGetTravelExpenseFiles(projectTravelExpenseGuid, firstRow, rowCount)

Get all files of a travel expense by its id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String projectTravelExpenseGuid = "projectTravelExpenseGuid_example"; // String | GUID of the travel expense used to get the files.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch.
    try {
      List<ProjectTravelExpenseFileModel> result = apiInstance.filesGetTravelExpenseFiles(projectTravelExpenseGuid, firstRow, rowCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#filesGetTravelExpenseFiles");
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
| **projectTravelExpenseGuid** | **String**| GUID of the travel expense used to get the files. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch. | [optional] |

### Return type

[**List&lt;ProjectTravelExpenseFileModel&gt;**](ProjectTravelExpenseFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TravelExpenseFile. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="filesGetUsersTravelExpensesFiles"></a>
# **filesGetUsersTravelExpensesFiles**
> List&lt;ProjectTravelExpenseFileModel&gt; filesGetUsersTravelExpensesFiles(userGuid, firstRow, rowCount, startDate, endDate)

Get all files of all travel expenses of the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String userGuid = "userGuid_example"; // String | GUID of the user used to get the files attached to travel expenses.
    Integer firstRow = 56; // Integer | Optional: first row to fetch. Default 0 = first row.
    Integer rowCount = 56; // Integer | Optional: How many rows to fetch.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Optional: Start date to from which to check travel expenses.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Optional: End date to check for availability until travel expenses.
    try {
      List<ProjectTravelExpenseFileModel> result = apiInstance.filesGetUsersTravelExpensesFiles(userGuid, firstRow, rowCount, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#filesGetUsersTravelExpensesFiles");
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
| **userGuid** | **String**| GUID of the user used to get the files attached to travel expenses. | |
| **firstRow** | **Integer**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] |
| **rowCount** | **Integer**| Optional: How many rows to fetch. | [optional] |
| **startDate** | **OffsetDateTime**| Optional: Start date to from which to check travel expenses. | [optional] |
| **endDate** | **OffsetDateTime**| Optional: End date to check for availability until travel expenses. | [optional] |

### Return type

[**List&lt;ProjectTravelExpenseFileModel&gt;**](ProjectTravelExpenseFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TravelExpenseFile. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="keywordsGetFileKeywords"></a>
# **keywordsGetFileKeywords**
> List&lt;FileKeywordModel&gt; keywordsGetFileKeywords(fileGuid, active, sortings)

Get all the keywords for file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String fileGuid = "fileGuid_example"; // String | ID of the file for which keywords are requested.
    Boolean active = true; // Boolean | If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
    List<KeyValuePairOfStringAndSortDirection> sortings = Arrays.asList(); // List<KeyValuePairOfStringAndSortDirection> | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Keyword&sortings[0].value=Desc\".
    try {
      List<FileKeywordModel> result = apiInstance.keywordsGetFileKeywords(fileGuid, active, sortings);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#keywordsGetFileKeywords");
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
| **fileGuid** | **String**| ID of the file for which keywords are requested. | |
| **active** | **Boolean**| If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords. | [optional] |
| **sortings** | [**List&lt;KeyValuePairOfStringAndSortDirection&gt;**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] |

### Return type

[**List&lt;FileKeywordModel&gt;**](FileKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Keywords. |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="pdfGetInvoicePdf"></a>
# **pdfGetInvoicePdf**
> File pdfGetInvoicePdf(guid, invoiceType, pdfGetOptions)

Get an invoice PDF.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String guid = "guid_example"; // String | The invoice GUID.
    InvoiceType invoiceType = InvoiceType.fromValue("Invoice"); // InvoiceType | Optional: type of invoice.
    InvoicePdfGetOptions pdfGetOptions = InvoicePdfGetOptions.fromValue("All"); // InvoicePdfGetOptions | Optional: what to include in the PDF. Defaults to InvoicePdfGetOptions.All.
    try {
      File result = apiInstance.pdfGetInvoicePdf(guid, invoiceType, pdfGetOptions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#pdfGetInvoicePdf");
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
| **invoiceType** | [**InvoiceType**](.md)| Optional: type of invoice. | [optional] [enum: Invoice, Reminder] |
| **pdfGetOptions** | [**InvoicePdfGetOptions**](.md)| Optional: what to include in the PDF. Defaults to InvoicePdfGetOptions.All. | [optional] [enum: All, InvoiceOnly, AttachmentAndBreakdown] |

### Return type

[**File**](File.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get an invoice PDF |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

<a id="pdfGetTravelReimbursementPdf"></a>
# **pdfGetTravelReimbursementPdf**
> File pdfGetTravelReimbursementPdf(guid)

Get a travel reimbursement PDF.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilesReadApi;

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

    FilesReadApi apiInstance = new FilesReadApi(defaultClient);
    String guid = "guid_example"; // String | The travel reimbursement GUID.
    try {
      File result = apiInstance.pdfGetTravelReimbursementPdf(guid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilesReadApi#pdfGetTravelReimbursementPdf");
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
| **guid** | **String**| The travel reimbursement GUID. | |

### Return type

[**File**](File.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get a travel reimbursement PDF |  -  |
| **404** | Resource not found |  -  |
| **0** | Default error response |  -  |

