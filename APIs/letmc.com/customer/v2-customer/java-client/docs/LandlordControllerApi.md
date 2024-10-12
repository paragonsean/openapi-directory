# LandlordControllerApi

All URIs are relative to *https://live-api.letmc.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**landlordControllerCreateMaintenancePreference**](LandlordControllerApi.md#landlordControllerCreateMaintenancePreference) | **POST** /v2/customer/{shortName}/landlord/tenancy/maintenance/preference | Post tenancy maintenance preferences:- |
| [**landlordControllerGetAccounts**](LandlordControllerApi.md#landlordControllerGetAccounts) | **GET** /v2/customer/{shortName}/landlord/accounting | Get the accounting details for the landlord. |
| [**landlordControllerGetDocument**](LandlordControllerApi.md#landlordControllerGetDocument) | **GET** /v2/customer/{shortName}/landlord/document | Download a Document |
| [**landlordControllerGetInvetoryReport**](LandlordControllerApi.md#landlordControllerGetInvetoryReport) | **GET** /v2/customer/{shortName}/landlord/inventory | Generate a Inventory PDF for a tenancy |
| [**landlordControllerGetInvoice**](LandlordControllerApi.md#landlordControllerGetInvoice) | **GET** /v2/customer/{shortName}/landlord/invoice | Get an invoice pdf belonging to the landlord. |
| [**landlordControllerGetLandlordCrmEntries**](LandlordControllerApi.md#landlordControllerGetLandlordCrmEntries) | **GET** /v2/customer/{shortName}/landlord/landlordcrmentries | Retrieve landlord&#39;s CRM ID |
| [**landlordControllerGetMaintenanceJobs**](LandlordControllerApi.md#landlordControllerGetMaintenanceJobs) | **GET** /v2/customer/{shortName}/landlord/maintenance | Get Active maintenance jobs. |
| [**landlordControllerGetProfitLossReport**](LandlordControllerApi.md#landlordControllerGetProfitLossReport) | **GET** /v2/customer/{shortName}/landlord/profitloss | Generate a Profit and Loss Report |
| [**landlordControllerGetRentArrears**](LandlordControllerApi.md#landlordControllerGetRentArrears) | **GET** /v2/customer/{shortName}/landlord/rentarrears | Rent Arrears |
| [**landlordControllerGetSASReport**](LandlordControllerApi.md#landlordControllerGetSASReport) | **GET** /v2/customer/{shortName}/landlord/sas | Generate a Self Assessment Tax Report |
| [**landlordControllerGetSettings**](LandlordControllerApi.md#landlordControllerGetSettings) | **GET** /v2/customer/{shortName}/landlord/settings | Get contact details of all linked landlords. |
| [**landlordControllerGetSummaryDetails**](LandlordControllerApi.md#landlordControllerGetSummaryDetails) | **GET** /v2/customer/{shortName}/landlord/summary | Get the summary details for the landlord. |
| [**landlordControllerGetTenancy**](LandlordControllerApi.md#landlordControllerGetTenancy) | **GET** /v2/customer/{shortName}/landlord/tenancy | Get tenancy details. |
| [**landlordControllerGetTenancyAgreementReport**](LandlordControllerApi.md#landlordControllerGetTenancyAgreementReport) | **GET** /v2/customer/{shortName}/landlord/tenancyagreement | Generate a Tenancy Agreement Copy (PDF) |


<a id="landlordControllerCreateMaintenancePreference"></a>
# **landlordControllerCreateMaintenancePreference**
> String landlordControllerCreateMaintenancePreference(shortName, token, tenancyID, name, notes)

Post tenancy maintenance preferences:-

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    String tenancyID = "tenancyID_example"; // String | The Tenancy ID
    String name = "name_example"; // String | Name of the maintenance preference to add
    String notes = "notes_example"; // String | Notes of the maintenance preference to add
    try {
      String result = apiInstance.landlordControllerCreateMaintenancePreference(shortName, token, tenancyID, name, notes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerCreateMaintenancePreference");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |
| **tenancyID** | **String**| The Tenancy ID | |
| **name** | **String**| Name of the maintenance preference to add | |
| **notes** | **String**| Notes of the maintenance preference to add | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetAccounts"></a>
# **landlordControllerGetAccounts**
> LandlordAccountingModel landlordControllerGetAccounts(shortName, token)

Get the accounting details for the landlord.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    try {
      LandlordAccountingModel result = apiInstance.landlordControllerGetAccounts(shortName, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetAccounts");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |

### Return type

[**LandlordAccountingModel**](LandlordAccountingModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetDocument"></a>
# **landlordControllerGetDocument**
> Object landlordControllerGetDocument(shortName, token, ID)

Download a Document

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    String ID = "ID_example"; // String | The Document ID
    try {
      Object result = apiInstance.landlordControllerGetDocument(shortName, token, ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetDocument");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |
| **ID** | **String**| The Document ID | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetInvetoryReport"></a>
# **landlordControllerGetInvetoryReport**
> Object landlordControllerGetInvetoryReport(shortName, token, tenancyID)

Generate a Inventory PDF for a tenancy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    String tenancyID = "tenancyID_example"; // String | The Tenancy ID
    try {
      Object result = apiInstance.landlordControllerGetInvetoryReport(shortName, token, tenancyID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetInvetoryReport");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |
| **tenancyID** | **String**| The Tenancy ID | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetInvoice"></a>
# **landlordControllerGetInvoice**
> Object landlordControllerGetInvoice(shortName, token, invoiceID)

Get an invoice pdf belonging to the landlord.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    String invoiceID = "invoiceID_example"; // String | The invoice ID to load.
    try {
      Object result = apiInstance.landlordControllerGetInvoice(shortName, token, invoiceID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetInvoice");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |
| **invoiceID** | **String**| The invoice ID to load. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetLandlordCrmEntries"></a>
# **landlordControllerGetLandlordCrmEntries**
> List&lt;LandlordCrmEntry&gt; landlordControllerGetLandlordCrmEntries(shortName, token)

Retrieve landlord&#39;s CRM ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    try {
      List<LandlordCrmEntry> result = apiInstance.landlordControllerGetLandlordCrmEntries(shortName, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetLandlordCrmEntries");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |

### Return type

[**List&lt;LandlordCrmEntry&gt;**](LandlordCrmEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetMaintenanceJobs"></a>
# **landlordControllerGetMaintenanceJobs**
> LandlordMaintenanceModel landlordControllerGetMaintenanceJobs(shortName, token)

Get Active maintenance jobs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    try {
      LandlordMaintenanceModel result = apiInstance.landlordControllerGetMaintenanceJobs(shortName, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetMaintenanceJobs");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |

### Return type

[**LandlordMaintenanceModel**](LandlordMaintenanceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetProfitLossReport"></a>
# **landlordControllerGetProfitLossReport**
> LandlordProfitLossModel landlordControllerGetProfitLossReport(shortName, token)

Generate a Profit and Loss Report

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    try {
      LandlordProfitLossModel result = apiInstance.landlordControllerGetProfitLossReport(shortName, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetProfitLossReport");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |

### Return type

[**LandlordProfitLossModel**](LandlordProfitLossModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetRentArrears"></a>
# **landlordControllerGetRentArrears**
> LandlordRentArrearsModel landlordControllerGetRentArrears(shortName, token)

Rent Arrears

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    try {
      LandlordRentArrearsModel result = apiInstance.landlordControllerGetRentArrears(shortName, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetRentArrears");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |

### Return type

[**LandlordRentArrearsModel**](LandlordRentArrearsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetSASReport"></a>
# **landlordControllerGetSASReport**
> Object landlordControllerGetSASReport(shortName, token, yearEnd)

Generate a Self Assessment Tax Report

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    Integer yearEnd = 56; // Integer | The Tax Year End.
    try {
      Object result = apiInstance.landlordControllerGetSASReport(shortName, token, yearEnd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetSASReport");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |
| **yearEnd** | **Integer**| The Tax Year End. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetSettings"></a>
# **landlordControllerGetSettings**
> LandlordSettingsModel landlordControllerGetSettings(shortName, token)

Get contact details of all linked landlords.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    try {
      LandlordSettingsModel result = apiInstance.landlordControllerGetSettings(shortName, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetSettings");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |

### Return type

[**LandlordSettingsModel**](LandlordSettingsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetSummaryDetails"></a>
# **landlordControllerGetSummaryDetails**
> LandlordSummaryModel landlordControllerGetSummaryDetails(shortName, token)

Get the summary details for the landlord.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    try {
      LandlordSummaryModel result = apiInstance.landlordControllerGetSummaryDetails(shortName, token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetSummaryDetails");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |

### Return type

[**LandlordSummaryModel**](LandlordSummaryModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetTenancy"></a>
# **landlordControllerGetTenancy**
> LandlordTenancyModel landlordControllerGetTenancy(shortName, token, tenancyID)

Get tenancy details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    String tenancyID = "tenancyID_example"; // String | The Tenancy ID
    try {
      LandlordTenancyModel result = apiInstance.landlordControllerGetTenancy(shortName, token, tenancyID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetTenancy");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |
| **tenancyID** | **String**| The Tenancy ID | |

### Return type

[**LandlordTenancyModel**](LandlordTenancyModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="landlordControllerGetTenancyAgreementReport"></a>
# **landlordControllerGetTenancyAgreementReport**
> Object landlordControllerGetTenancyAgreementReport(shortName, token, tenancyID)

Generate a Tenancy Agreement Copy (PDF)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LandlordControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://live-api.letmc.com");

    LandlordControllerApi apiInstance = new LandlordControllerApi(defaultClient);
    String shortName = "shortName_example"; // String | The unique client short-name
    String token = "token_example"; // String | The login token returned from the /session POST call
    String tenancyID = "tenancyID_example"; // String | The Tenancy ID
    try {
      Object result = apiInstance.landlordControllerGetTenancyAgreementReport(shortName, token, tenancyID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LandlordControllerApi#landlordControllerGetTenancyAgreementReport");
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
| **shortName** | **String**| The unique client short-name | |
| **token** | **String**| The login token returned from the /session POST call | |
| **tenancyID** | **String**| The Tenancy ID | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

