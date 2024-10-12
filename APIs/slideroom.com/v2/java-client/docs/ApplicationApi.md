# ApplicationApi

All URIs are relative to *https://api.slideroom.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationDeleteAttributesV2**](ApplicationApi.md#applicationDeleteAttributesV2) | **DELETE** /api/v2/application/{applicationId}/attributes | Deletes a custom attribute for an application. |
| [**applicationGetAttributeNamesV2**](ApplicationApi.md#applicationGetAttributeNamesV2) | **GET** /api/v2/application/attributes/names | Gets the custom application attributes used by the organization. |
| [**applicationGetAttributesV2**](ApplicationApi.md#applicationGetAttributesV2) | **GET** /api/v2/application/{applicationId}/attributes | Gets the custom attributes for an application. |
| [**applicationPostAttributesV2**](ApplicationApi.md#applicationPostAttributesV2) | **POST** /api/v2/application/{applicationId}/attributes | Updates the custom attributes for an application. API Import is available in the Advanced Plan. |
| [**applicationRequestExportByApplicationIdV2**](ApplicationApi.md#applicationRequestExportByApplicationIdV2) | **POST** /api/v2/application/{applicationId}/request-export | Requests the generation of a single application export file (tabular, pdf, zip). |
| [**applicationRequestExportV2**](ApplicationApi.md#applicationRequestExportV2) | **POST** /api/v2/application/request-export | Requests the generation of application export files (tabular, pdf, zip). |


<a id="applicationDeleteAttributesV2"></a>
# **applicationDeleteAttributesV2**
> String applicationDeleteAttributesV2(applicationId, name)

Deletes a custom attribute for an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.slideroom.com");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String applicationId = "applicationId_example"; // String | The ID of the application.
    String name = "name_example"; // String | The name of the attribute to be deleted.
    try {
      String result = apiInstance.applicationDeleteAttributesV2(applicationId, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationDeleteAttributesV2");
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
| **applicationId** | **String**| The ID of the application. | |
| **name** | **String**| The name of the attribute to be deleted. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="applicationGetAttributeNamesV2"></a>
# **applicationGetAttributeNamesV2**
> List&lt;String&gt; applicationGetAttributeNamesV2()

Gets the custom application attributes used by the organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.slideroom.com");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    try {
      List<String> result = apiInstance.applicationGetAttributeNamesV2();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationGetAttributeNamesV2");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="applicationGetAttributesV2"></a>
# **applicationGetAttributesV2**
> Map&lt;String, String&gt; applicationGetAttributesV2(applicationId)

Gets the custom attributes for an application.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.slideroom.com");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String applicationId = "applicationId_example"; // String | The ID of the application.
    try {
      Map<String, String> result = apiInstance.applicationGetAttributesV2(applicationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationGetAttributesV2");
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
| **applicationId** | **String**| The ID of the application. | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="applicationPostAttributesV2"></a>
# **applicationPostAttributesV2**
> String applicationPostAttributesV2(applicationId, data)

Updates the custom attributes for an application. API Import is available in the Advanced Plan.

This method only adds or updates attributes. Null values will be updated as nulls, but not deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.slideroom.com");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String applicationId = "applicationId_example"; // String | The ID of the application.
    Map<String, String> data = new HashMap(); // Map<String, String> | The name/value pairs of the attributes.
    try {
      String result = apiInstance.applicationPostAttributesV2(applicationId, data);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationPostAttributesV2");
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
| **applicationId** | **String**| The ID of the application. | |
| **data** | [**Map&lt;String, String&gt;**](String.md)| The name/value pairs of the attributes. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="applicationRequestExportByApplicationIdV2"></a>
# **applicationRequestExportByApplicationIdV2**
> RequestApplicationExportResultV2 applicationRequestExportByApplicationIdV2(applicationId, format, roundType, roundName, tabExport, pdfIncludeForms, pdfIncludeReferences, pdfIncludeMedia, pdfIncludeApplicantAttachments, pdfIncludeOrganizationAttachments, pdfIncludeRatings, pdfIncludeFullPageMedia, pdfIncludeHighlights, pdfIncludeComments, pdfIncludeCommonApp, zipOriginalMedia, zipIncludeForms, zipIncludeReferences, zipIncludeMedia, zipIncludeApplicantAttachments, zipIncludeOrganizationAttachments, zipIncludeRatings, zipIncludeComments, zipIncludeCommonApp, deliveryAccount, deliveryFolder)

Requests the generation of a single application export file (tabular, pdf, zip).

Exports are generated asynchronously within SlideRoom.  To retrieve the export file generated by this request, use the api/v#/export/{token} endpoint to check the progress/result of the generation process.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.slideroom.com");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String applicationId = "applicationId_example"; // String | The id of the application to export
    String format = "csv"; // String | 
    String roundType = "Assigned"; // String | 
    String roundName = "roundName_example"; // String | 
    String tabExport = "tabExport_example"; // String | 
    Boolean pdfIncludeForms = true; // Boolean | 
    Boolean pdfIncludeReferences = true; // Boolean | 
    Boolean pdfIncludeMedia = true; // Boolean | 
    Boolean pdfIncludeApplicantAttachments = true; // Boolean | 
    Boolean pdfIncludeOrganizationAttachments = true; // Boolean | 
    Boolean pdfIncludeRatings = true; // Boolean | 
    Boolean pdfIncludeFullPageMedia = true; // Boolean | 
    Boolean pdfIncludeHighlights = true; // Boolean | 
    Boolean pdfIncludeComments = true; // Boolean | 
    Boolean pdfIncludeCommonApp = true; // Boolean | 
    Boolean zipOriginalMedia = true; // Boolean | 
    Boolean zipIncludeForms = true; // Boolean | 
    Boolean zipIncludeReferences = true; // Boolean | 
    Boolean zipIncludeMedia = true; // Boolean | 
    Boolean zipIncludeApplicantAttachments = true; // Boolean | 
    Boolean zipIncludeOrganizationAttachments = true; // Boolean | 
    Boolean zipIncludeRatings = true; // Boolean | 
    Boolean zipIncludeComments = true; // Boolean | 
    Boolean zipIncludeCommonApp = true; // Boolean | 
    String deliveryAccount = "deliveryAccount_example"; // String | 
    String deliveryFolder = "deliveryFolder_example"; // String | 
    try {
      RequestApplicationExportResultV2 result = apiInstance.applicationRequestExportByApplicationIdV2(applicationId, format, roundType, roundName, tabExport, pdfIncludeForms, pdfIncludeReferences, pdfIncludeMedia, pdfIncludeApplicantAttachments, pdfIncludeOrganizationAttachments, pdfIncludeRatings, pdfIncludeFullPageMedia, pdfIncludeHighlights, pdfIncludeComments, pdfIncludeCommonApp, zipOriginalMedia, zipIncludeForms, zipIncludeReferences, zipIncludeMedia, zipIncludeApplicantAttachments, zipIncludeOrganizationAttachments, zipIncludeRatings, zipIncludeComments, zipIncludeCommonApp, deliveryAccount, deliveryFolder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationRequestExportByApplicationIdV2");
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
| **applicationId** | **String**| The id of the application to export | |
| **format** | **String**|  | [optional] [enum: csv, tsv, txt, tab, xlsx, pdf, zip, json] |
| **roundType** | **String**|  | [optional] [enum: Assigned, Current, Named, All] |
| **roundName** | **String**|  | [optional] |
| **tabExport** | **String**|  | [optional] |
| **pdfIncludeForms** | **Boolean**|  | [optional] |
| **pdfIncludeReferences** | **Boolean**|  | [optional] |
| **pdfIncludeMedia** | **Boolean**|  | [optional] |
| **pdfIncludeApplicantAttachments** | **Boolean**|  | [optional] |
| **pdfIncludeOrganizationAttachments** | **Boolean**|  | [optional] |
| **pdfIncludeRatings** | **Boolean**|  | [optional] |
| **pdfIncludeFullPageMedia** | **Boolean**|  | [optional] |
| **pdfIncludeHighlights** | **Boolean**|  | [optional] |
| **pdfIncludeComments** | **Boolean**|  | [optional] |
| **pdfIncludeCommonApp** | **Boolean**|  | [optional] |
| **zipOriginalMedia** | **Boolean**|  | [optional] |
| **zipIncludeForms** | **Boolean**|  | [optional] |
| **zipIncludeReferences** | **Boolean**|  | [optional] |
| **zipIncludeMedia** | **Boolean**|  | [optional] |
| **zipIncludeApplicantAttachments** | **Boolean**|  | [optional] |
| **zipIncludeOrganizationAttachments** | **Boolean**|  | [optional] |
| **zipIncludeRatings** | **Boolean**|  | [optional] |
| **zipIncludeComments** | **Boolean**|  | [optional] |
| **zipIncludeCommonApp** | **Boolean**|  | [optional] |
| **deliveryAccount** | **String**|  | [optional] |
| **deliveryFolder** | **String**|  | [optional] |

### Return type

[**RequestApplicationExportResultV2**](RequestApplicationExportResultV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **400** | Bad Request |  -  |

<a id="applicationRequestExportV2"></a>
# **applicationRequestExportV2**
> RequestApplicationExportResultV2 applicationRequestExportV2(format, roundType, roundName, tabExport, pdfIncludeForms, pdfIncludeReferences, pdfIncludeMedia, pdfIncludeApplicantAttachments, pdfIncludeOrganizationAttachments, pdfIncludeRatings, pdfIncludeFullPageMedia, pdfIncludeHighlights, pdfIncludeComments, pdfIncludeCommonApp, zipOriginalMedia, zipIncludeForms, zipIncludeReferences, zipIncludeMedia, zipIncludeApplicantAttachments, zipIncludeOrganizationAttachments, zipIncludeRatings, zipIncludeComments, zipIncludeCommonApp, deliveryAccount, deliveryFolder, since, pool, status, searchName, email)

Requests the generation of application export files (tabular, pdf, zip).

Exports are generated asynchronously within SlideRoom.  To retrieve the export file generated by this request, use the api/v#/export/{token} endpoint to check the progress/result of the generation process.  PDF and ZIP exports are available in the Advanced Plan.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.slideroom.com");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String format = "csv"; // String | 
    String roundType = "Assigned"; // String | 
    String roundName = "roundName_example"; // String | 
    String tabExport = "tabExport_example"; // String | 
    Boolean pdfIncludeForms = true; // Boolean | 
    Boolean pdfIncludeReferences = true; // Boolean | 
    Boolean pdfIncludeMedia = true; // Boolean | 
    Boolean pdfIncludeApplicantAttachments = true; // Boolean | 
    Boolean pdfIncludeOrganizationAttachments = true; // Boolean | 
    Boolean pdfIncludeRatings = true; // Boolean | 
    Boolean pdfIncludeFullPageMedia = true; // Boolean | 
    Boolean pdfIncludeHighlights = true; // Boolean | 
    Boolean pdfIncludeComments = true; // Boolean | 
    Boolean pdfIncludeCommonApp = true; // Boolean | 
    Boolean zipOriginalMedia = true; // Boolean | 
    Boolean zipIncludeForms = true; // Boolean | 
    Boolean zipIncludeReferences = true; // Boolean | 
    Boolean zipIncludeMedia = true; // Boolean | 
    Boolean zipIncludeApplicantAttachments = true; // Boolean | 
    Boolean zipIncludeOrganizationAttachments = true; // Boolean | 
    Boolean zipIncludeRatings = true; // Boolean | 
    Boolean zipIncludeComments = true; // Boolean | 
    Boolean zipIncludeCommonApp = true; // Boolean | 
    String deliveryAccount = "deliveryAccount_example"; // String | 
    String deliveryFolder = "deliveryFolder_example"; // String | 
    Integer since = 56; // Integer | 
    String pool = "All"; // String | 
    String status = "All"; // String | 
    String searchName = "searchName_example"; // String | 
    String email = "email_example"; // String | 
    try {
      RequestApplicationExportResultV2 result = apiInstance.applicationRequestExportV2(format, roundType, roundName, tabExport, pdfIncludeForms, pdfIncludeReferences, pdfIncludeMedia, pdfIncludeApplicantAttachments, pdfIncludeOrganizationAttachments, pdfIncludeRatings, pdfIncludeFullPageMedia, pdfIncludeHighlights, pdfIncludeComments, pdfIncludeCommonApp, zipOriginalMedia, zipIncludeForms, zipIncludeReferences, zipIncludeMedia, zipIncludeApplicantAttachments, zipIncludeOrganizationAttachments, zipIncludeRatings, zipIncludeComments, zipIncludeCommonApp, deliveryAccount, deliveryFolder, since, pool, status, searchName, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationRequestExportV2");
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
| **format** | **String**|  | [optional] [enum: csv, tsv, txt, tab, xlsx, pdf, zip, json] |
| **roundType** | **String**|  | [optional] [enum: Assigned, Current, Named, All] |
| **roundName** | **String**|  | [optional] |
| **tabExport** | **String**|  | [optional] |
| **pdfIncludeForms** | **Boolean**|  | [optional] |
| **pdfIncludeReferences** | **Boolean**|  | [optional] |
| **pdfIncludeMedia** | **Boolean**|  | [optional] |
| **pdfIncludeApplicantAttachments** | **Boolean**|  | [optional] |
| **pdfIncludeOrganizationAttachments** | **Boolean**|  | [optional] |
| **pdfIncludeRatings** | **Boolean**|  | [optional] |
| **pdfIncludeFullPageMedia** | **Boolean**|  | [optional] |
| **pdfIncludeHighlights** | **Boolean**|  | [optional] |
| **pdfIncludeComments** | **Boolean**|  | [optional] |
| **pdfIncludeCommonApp** | **Boolean**|  | [optional] |
| **zipOriginalMedia** | **Boolean**|  | [optional] |
| **zipIncludeForms** | **Boolean**|  | [optional] |
| **zipIncludeReferences** | **Boolean**|  | [optional] |
| **zipIncludeMedia** | **Boolean**|  | [optional] |
| **zipIncludeApplicantAttachments** | **Boolean**|  | [optional] |
| **zipIncludeOrganizationAttachments** | **Boolean**|  | [optional] |
| **zipIncludeRatings** | **Boolean**|  | [optional] |
| **zipIncludeComments** | **Boolean**|  | [optional] |
| **zipIncludeCommonApp** | **Boolean**|  | [optional] |
| **deliveryAccount** | **String**|  | [optional] |
| **deliveryFolder** | **String**|  | [optional] |
| **since** | **Integer**|  | [optional] |
| **pool** | **String**|  | [optional] [enum: All, Current, Archived, CommonAppSDS] |
| **status** | **String**|  | [optional] [enum: All, InProgress, Submitted] |
| **searchName** | **String**|  | [optional] |
| **email** | **String**|  | [optional] |

### Return type

[**RequestApplicationExportResultV2**](RequestApplicationExportResultV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

