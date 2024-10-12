# EmailTemplatesApi

All URIs are relative to *https://rest.iad-01.braze.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listAvailableEmailTemplates_0**](EmailTemplatesApi.md#listAvailableEmailTemplates_0) | **GET** /templates/email/list | List Available Email Templates |
| [**seeEmailTemplateInformation_0**](EmailTemplatesApi.md#seeEmailTemplateInformation_0) | **GET** /templates/email/info | See Email Template Information |


<a id="listAvailableEmailTemplates_0"></a>
# **listAvailableEmailTemplates_0**
> listAvailableEmailTemplates_0(modifiedAfter, modifiedBefore, limit, offset)

List Available Email Templates

Use this endpoint to get a list of available templates in your Braze account.  Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates &amp; Media page. Braze provides two endpoints for creating and updating your email templates.  ### Successful Response Properties &#x60;&#x60;&#x60;json {   \&quot;count\&quot;: number of templates returned   \&quot;templates\&quot;: [template with the following properties]:     \&quot;email_template_id\&quot;: (string) your email template&#39;s API Identifier,     \&quot;template_name\&quot;: (string) the name of your email template,     \&quot;created_at\&quot;: (string, in ISO 8601),     \&quot;updated_at\&quot;: (string, in ISO 8601),     \&quot;tags\&quot;: (array of strings) tags appended to the template }   &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    EmailTemplatesApi apiInstance = new EmailTemplatesApi(defaultClient);
    String modifiedAfter = "2020-01-01T01:01:01.000000"; // String | (Optional) String in ISO 8601  Retrieve only templates updated at or after the given time.
    String modifiedBefore = "2020-02-01T01:01:01.000000"; // String | (Optional) String in ISO 8601  Retrieve only templates updated at or before the given time
    String limit = "1"; // String | (Optional) Positive Number  Maximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000.
    String offset = "0"; // String | (Optional) Positive Number  Number of templates to skip before returning rest of the templates that fit the search criteria.
    try {
      apiInstance.listAvailableEmailTemplates_0(modifiedAfter, modifiedBefore, limit, offset);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailTemplatesApi#listAvailableEmailTemplates_0");
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
| **modifiedAfter** | **String**| (Optional) String in ISO 8601  Retrieve only templates updated at or after the given time. | [optional] |
| **modifiedBefore** | **String**| (Optional) String in ISO 8601  Retrieve only templates updated at or before the given time | [optional] |
| **limit** | **String**| (Optional) Positive Number  Maximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000. | [optional] |
| **offset** | **String**| (Optional) Positive Number  Number of templates to skip before returning rest of the templates that fit the search criteria. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="seeEmailTemplateInformation_0"></a>
# **seeEmailTemplateInformation_0**
> seeEmailTemplateInformation_0(emailTemplateId)

See Email Template Information

Use to get information on your email templates.  Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates &amp; Media page. Braze provides two endpoints for creating and updating your email templates.  ### Request Components - [Template Identifier](https://www.braze.com/docs/api/identifier_types/)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmailTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    EmailTemplatesApi apiInstance = new EmailTemplatesApi(defaultClient);
    String emailTemplateId = "{{email_template_id}}"; // String | (Required) String  Your email template's API Identifier.
    try {
      apiInstance.seeEmailTemplateInformation_0(emailTemplateId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmailTemplatesApi#seeEmailTemplateInformation_0");
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
| **emailTemplateId** | **String**| (Required) String  Your email template&#39;s API Identifier. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

