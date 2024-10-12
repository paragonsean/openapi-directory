# BundlesApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteBundlesId**](BundlesApi.md#deleteBundlesId) | **DELETE** /bundles/{id} | Delete Bundle |
| [**getBundles**](BundlesApi.md#getBundles) | **GET** /bundles | List Bundles |
| [**getBundlesId**](BundlesApi.md#getBundlesId) | **GET** /bundles/{id} | Show Bundle |
| [**patchBundlesId**](BundlesApi.md#patchBundlesId) | **PATCH** /bundles/{id} | Update Bundle |
| [**postBundles**](BundlesApi.md#postBundles) | **POST** /bundles | Create Bundle |
| [**postBundlesIdShare**](BundlesApi.md#postBundlesIdShare) | **POST** /bundles/{id}/share | Send email(s) with a link to bundle |


<a id="deleteBundlesId"></a>
# **deleteBundlesId**
> deleteBundlesId(id)

Delete Bundle

Delete Bundle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    Integer id = 56; // Integer | Bundle ID.
    try {
      apiInstance.deleteBundlesId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#deleteBundlesId");
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
| **id** | **Integer**| Bundle ID. | |

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
| **204** | No body. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getBundles"></a>
# **getBundles**
> List&lt;BundleEntity&gt; getBundles(userId, cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq)

List Bundles

List Bundles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[created_at]=desc`). Valid fields are `created_at` and `code`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `created_at`.
    Object filterGt = null; // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `created_at`.
    Object filterGteq = null; // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `created_at`.
    Object filterLt = null; // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `created_at`.
    Object filterLteq = null; // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `created_at`.
    try {
      List<BundleEntity> result = apiInstance.getBundles(userId, cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#getBundles");
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
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[created_at]&#x3D;desc&#x60;). Valid fields are &#x60;created_at&#x60; and &#x60;code&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] |
| **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] |
| **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] |
| **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] |
| **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] |

### Return type

[**List&lt;BundleEntity&gt;**](BundleEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Bundles objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getBundlesId"></a>
# **getBundlesId**
> BundleEntity getBundlesId(id)

Show Bundle

Show Bundle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    Integer id = 56; // Integer | Bundle ID.
    try {
      BundleEntity result = apiInstance.getBundlesId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#getBundlesId");
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
| **id** | **Integer**| Bundle ID. | |

### Return type

[**BundleEntity**](BundleEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Bundles object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="patchBundlesId"></a>
# **patchBundlesId**
> BundleEntity patchBundlesId(id, clickwrapId, code, description, dontSeparateSubmissionsByFolder, expiresAt, formFieldSetId, inboxId, maxUses, note, password, pathTemplate, paths, permissions, previewOnly, requireRegistration, requireShareRecipient, sendEmailReceiptToUploader, skipCompany, skipEmail, skipName, watermarkAttachmentDelete, watermarkAttachmentFile)

Update Bundle

Update Bundle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    Integer id = 56; // Integer | Bundle ID.
    Integer clickwrapId = 56; // Integer | ID of the clickwrap to use with this bundle.
    String code = "code_example"; // String | Bundle code.  This code forms the end part of the Public URL.
    String description = "description_example"; // String | Public description
    Boolean dontSeparateSubmissionsByFolder = true; // Boolean | Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required.
    OffsetDateTime expiresAt = OffsetDateTime.now(); // OffsetDateTime | Bundle expiration date/time
    Integer formFieldSetId = 56; // Integer | Id of Form Field Set to use with this bundle
    Integer inboxId = 56; // Integer | ID of the associated inbox, if available.
    Integer maxUses = 56; // Integer | Maximum number of times bundle can be accessed
    String note = "note_example"; // String | Bundle internal note
    String password = "password_example"; // String | Password for this bundle.
    String pathTemplate = "pathTemplate_example"; // String | Template for creating submission subfolders. Can use the uploader's name, email address, ip, company, and any custom form data.
    List<String> paths = Arrays.asList(); // List<String> | A list of paths to include in this bundle.
    String permissions = "read"; // String | Permissions that apply to Folders in this Share Link.
    Boolean previewOnly = true; // Boolean | Restrict users to previewing files only?
    Boolean requireRegistration = true; // Boolean | Show a registration page that captures the downloader's name and email address?
    Boolean requireShareRecipient = true; // Boolean | Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI?
    Boolean sendEmailReceiptToUploader = true; // Boolean | Send delivery receipt to the uploader. Note: For writable share only
    Boolean skipCompany = true; // Boolean | BundleRegistrations can be saved without providing company?
    Boolean skipEmail = true; // Boolean | BundleRegistrations can be saved without providing email?
    Boolean skipName = true; // Boolean | BundleRegistrations can be saved without providing name?
    Boolean watermarkAttachmentDelete = true; // Boolean | If true, will delete the file stored in watermark_attachment
    File watermarkAttachmentFile = new File("/path/to/file"); // File | Preview watermark image applied to all bundle items.
    try {
      BundleEntity result = apiInstance.patchBundlesId(id, clickwrapId, code, description, dontSeparateSubmissionsByFolder, expiresAt, formFieldSetId, inboxId, maxUses, note, password, pathTemplate, paths, permissions, previewOnly, requireRegistration, requireShareRecipient, sendEmailReceiptToUploader, skipCompany, skipEmail, skipName, watermarkAttachmentDelete, watermarkAttachmentFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#patchBundlesId");
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
| **id** | **Integer**| Bundle ID. | |
| **clickwrapId** | **Integer**| ID of the clickwrap to use with this bundle. | [optional] |
| **code** | **String**| Bundle code.  This code forms the end part of the Public URL. | [optional] |
| **description** | **String**| Public description | [optional] |
| **dontSeparateSubmissionsByFolder** | **Boolean**| Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required. | [optional] |
| **expiresAt** | **OffsetDateTime**| Bundle expiration date/time | [optional] |
| **formFieldSetId** | **Integer**| Id of Form Field Set to use with this bundle | [optional] |
| **inboxId** | **Integer**| ID of the associated inbox, if available. | [optional] |
| **maxUses** | **Integer**| Maximum number of times bundle can be accessed | [optional] |
| **note** | **String**| Bundle internal note | [optional] |
| **password** | **String**| Password for this bundle. | [optional] |
| **pathTemplate** | **String**| Template for creating submission subfolders. Can use the uploader&#39;s name, email address, ip, company, and any custom form data. | [optional] |
| **paths** | [**List&lt;String&gt;**](String.md)| A list of paths to include in this bundle. | [optional] |
| **permissions** | **String**| Permissions that apply to Folders in this Share Link. | [optional] [enum: read, write, read_write, full, none, preview_only] |
| **previewOnly** | **Boolean**| Restrict users to previewing files only? | [optional] |
| **requireRegistration** | **Boolean**| Show a registration page that captures the downloader&#39;s name and email address? | [optional] |
| **requireShareRecipient** | **Boolean**| Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI? | [optional] |
| **sendEmailReceiptToUploader** | **Boolean**| Send delivery receipt to the uploader. Note: For writable share only | [optional] |
| **skipCompany** | **Boolean**| BundleRegistrations can be saved without providing company? | [optional] |
| **skipEmail** | **Boolean**| BundleRegistrations can be saved without providing email? | [optional] |
| **skipName** | **Boolean**| BundleRegistrations can be saved without providing name? | [optional] |
| **watermarkAttachmentDelete** | **Boolean**| If true, will delete the file stored in watermark_attachment | [optional] |
| **watermarkAttachmentFile** | **File**| Preview watermark image applied to all bundle items. | [optional] |

### Return type

[**BundleEntity**](BundleEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Bundles object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postBundles"></a>
# **postBundles**
> BundleEntity postBundles(paths, clickwrapId, code, description, dontSeparateSubmissionsByFolder, expiresAt, formFieldSetId, inboxId, maxUses, note, password, pathTemplate, permissions, previewOnly, requireRegistration, requireShareRecipient, sendEmailReceiptToUploader, skipCompany, skipEmail, skipName, userId, watermarkAttachmentFile)

Create Bundle

Create Bundle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    List<String> paths = Arrays.asList(); // List<String> | A list of paths to include in this bundle.
    Integer clickwrapId = 56; // Integer | ID of the clickwrap to use with this bundle.
    String code = "code_example"; // String | Bundle code.  This code forms the end part of the Public URL.
    String description = "description_example"; // String | Public description
    Boolean dontSeparateSubmissionsByFolder = true; // Boolean | Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required.
    OffsetDateTime expiresAt = OffsetDateTime.now(); // OffsetDateTime | Bundle expiration date/time
    Integer formFieldSetId = 56; // Integer | Id of Form Field Set to use with this bundle
    Integer inboxId = 56; // Integer | ID of the associated inbox, if available.
    Integer maxUses = 56; // Integer | Maximum number of times bundle can be accessed
    String note = "note_example"; // String | Bundle internal note
    String password = "password_example"; // String | Password for this bundle.
    String pathTemplate = "pathTemplate_example"; // String | Template for creating submission subfolders. Can use the uploader's name, email address, ip, company, and any custom form data.
    String permissions = "read"; // String | Permissions that apply to Folders in this Share Link.
    Boolean previewOnly = true; // Boolean | Restrict users to previewing files only?
    Boolean requireRegistration = true; // Boolean | Show a registration page that captures the downloader's name and email address?
    Boolean requireShareRecipient = true; // Boolean | Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI?
    Boolean sendEmailReceiptToUploader = true; // Boolean | Send delivery receipt to the uploader. Note: For writable share only
    Boolean skipCompany = true; // Boolean | BundleRegistrations can be saved without providing company?
    Boolean skipEmail = true; // Boolean | BundleRegistrations can be saved without providing email?
    Boolean skipName = true; // Boolean | BundleRegistrations can be saved without providing name?
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    File watermarkAttachmentFile = new File("/path/to/file"); // File | Preview watermark image applied to all bundle items.
    try {
      BundleEntity result = apiInstance.postBundles(paths, clickwrapId, code, description, dontSeparateSubmissionsByFolder, expiresAt, formFieldSetId, inboxId, maxUses, note, password, pathTemplate, permissions, previewOnly, requireRegistration, requireShareRecipient, sendEmailReceiptToUploader, skipCompany, skipEmail, skipName, userId, watermarkAttachmentFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#postBundles");
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
| **paths** | [**List&lt;String&gt;**](String.md)| A list of paths to include in this bundle. | |
| **clickwrapId** | **Integer**| ID of the clickwrap to use with this bundle. | [optional] |
| **code** | **String**| Bundle code.  This code forms the end part of the Public URL. | [optional] |
| **description** | **String**| Public description | [optional] |
| **dontSeparateSubmissionsByFolder** | **Boolean**| Do not create subfolders for files uploaded to this share. Note: there are subtle security pitfalls with allowing anonymous uploads from multiple users to live in the same folder. We strongly discourage use of this option unless absolutely required. | [optional] |
| **expiresAt** | **OffsetDateTime**| Bundle expiration date/time | [optional] |
| **formFieldSetId** | **Integer**| Id of Form Field Set to use with this bundle | [optional] |
| **inboxId** | **Integer**| ID of the associated inbox, if available. | [optional] |
| **maxUses** | **Integer**| Maximum number of times bundle can be accessed | [optional] |
| **note** | **String**| Bundle internal note | [optional] |
| **password** | **String**| Password for this bundle. | [optional] |
| **pathTemplate** | **String**| Template for creating submission subfolders. Can use the uploader&#39;s name, email address, ip, company, and any custom form data. | [optional] |
| **permissions** | **String**| Permissions that apply to Folders in this Share Link. | [optional] [enum: read, write, read_write, full, none, preview_only] |
| **previewOnly** | **Boolean**| Restrict users to previewing files only? | [optional] |
| **requireRegistration** | **Boolean**| Show a registration page that captures the downloader&#39;s name and email address? | [optional] |
| **requireShareRecipient** | **Boolean**| Only allow access to recipients who have explicitly received the share via an email sent through the Files.com UI? | [optional] |
| **sendEmailReceiptToUploader** | **Boolean**| Send delivery receipt to the uploader. Note: For writable share only | [optional] |
| **skipCompany** | **Boolean**| BundleRegistrations can be saved without providing company? | [optional] |
| **skipEmail** | **Boolean**| BundleRegistrations can be saved without providing email? | [optional] |
| **skipName** | **Boolean**| BundleRegistrations can be saved without providing name? | [optional] |
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |
| **watermarkAttachmentFile** | **File**| Preview watermark image applied to all bundle items. | [optional] |

### Return type

[**BundleEntity**](BundleEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Bundles object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postBundlesIdShare"></a>
# **postBundlesIdShare**
> postBundlesIdShare(id, note, recipients, to)

Send email(s) with a link to bundle

Send email(s) with a link to bundle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    Integer id = 56; // Integer | Bundle ID.
    String note = "note_example"; // String | Note to include in email.
    List<Object> recipients = null; // List<Object> | A list of recipients to share this bundle with. Required unless `to` is used.
    List<String> to = Arrays.asList(); // List<String> | A list of email addresses to share this bundle with. Required unless `recipients` is used.
    try {
      apiInstance.postBundlesIdShare(id, note, recipients, to);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#postBundlesIdShare");
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
| **id** | **Integer**| Bundle ID. | |
| **note** | **String**| Note to include in email. | [optional] |
| **recipients** | [**List&lt;Object&gt;**](Object.md)| A list of recipients to share this bundle with. Required unless &#x60;to&#x60; is used. | [optional] |
| **to** | [**List&lt;String&gt;**](String.md)| A list of email addresses to share this bundle with. Required unless &#x60;recipients&#x60; is used. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No body. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

