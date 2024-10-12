# IssueCustomFieldValuesAppsApi

All URIs are relative to *https://your-domain.atlassian.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**updateCustomFieldValue**](IssueCustomFieldValuesAppsApi.md#updateCustomFieldValue) | **PUT** /rest/api/3/app/field/{fieldIdOrKey}/value | Update custom field value |
| [**updateMultipleCustomFieldValues**](IssueCustomFieldValuesAppsApi.md#updateMultipleCustomFieldValues) | **POST** /rest/api/3/app/field/value | Update custom fields |


<a id="updateCustomFieldValue"></a>
# **updateCustomFieldValue**
> Object updateCustomFieldValue(fieldIdOrKey, customFieldValueUpdateDetails, generateChangelog)

Update custom field value

Updates the value of a custom field on one or more issues. Custom fields can only be updated by the Forge app that created them.  **[Permissions](#permissions) required:** Only the app that created the custom field can update its values with this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueCustomFieldValuesAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://your-domain.atlassian.net");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IssueCustomFieldValuesAppsApi apiInstance = new IssueCustomFieldValuesAppsApi(defaultClient);
    String fieldIdOrKey = "fieldIdOrKey_example"; // String | The ID or key of the custom field. For example, `customfield_10010`.
    CustomFieldValueUpdateDetails customFieldValueUpdateDetails = new CustomFieldValueUpdateDetails(); // CustomFieldValueUpdateDetails | 
    Boolean generateChangelog = true; // Boolean | Whether to generate a changelog for this update.
    try {
      Object result = apiInstance.updateCustomFieldValue(fieldIdOrKey, customFieldValueUpdateDetails, generateChangelog);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueCustomFieldValuesAppsApi#updateCustomFieldValue");
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
| **fieldIdOrKey** | **String**| The ID or key of the custom field. For example, &#x60;customfield_10010&#x60;. | |
| **customFieldValueUpdateDetails** | [**CustomFieldValueUpdateDetails**](CustomFieldValueUpdateDetails.md)|  | |
| **generateChangelog** | **Boolean**| Whether to generate a changelog for this update. | [optional] [default to true] |

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Returned if the request is successful. |  -  |
| **400** | Returned if the request is invalid. |  -  |
| **403** | Returned if the request is not authenticated as the app that provided the field. |  -  |
| **404** | Returned if the field is not found. |  -  |

<a id="updateMultipleCustomFieldValues"></a>
# **updateMultipleCustomFieldValues**
> Object updateMultipleCustomFieldValues(multipleCustomFieldValuesUpdateDetails, generateChangelog)

Update custom fields

Updates the value of one or more custom fields on one or more issues. Combinations of custom field and issue should be unique within the request. Custom fields can only be updated by the Forge app that created them.  **[Permissions](#permissions) required:** Only the app that created the custom field can update its values with this operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueCustomFieldValuesAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://your-domain.atlassian.net");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    IssueCustomFieldValuesAppsApi apiInstance = new IssueCustomFieldValuesAppsApi(defaultClient);
    MultipleCustomFieldValuesUpdateDetails multipleCustomFieldValuesUpdateDetails = new MultipleCustomFieldValuesUpdateDetails(); // MultipleCustomFieldValuesUpdateDetails | 
    Boolean generateChangelog = true; // Boolean | Whether to generate a changelog for this update.
    try {
      Object result = apiInstance.updateMultipleCustomFieldValues(multipleCustomFieldValuesUpdateDetails, generateChangelog);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueCustomFieldValuesAppsApi#updateMultipleCustomFieldValues");
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
| **multipleCustomFieldValuesUpdateDetails** | [**MultipleCustomFieldValuesUpdateDetails**](MultipleCustomFieldValuesUpdateDetails.md)|  | |
| **generateChangelog** | **Boolean**| Whether to generate a changelog for this update. | [optional] [default to true] |

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Returned if the request is successful. |  -  |
| **400** | Returned if the request is invalid. |  -  |
| **403** | Returned if the request is not authenticated as the app that provided all the fields. |  -  |
| **404** | Returned if any field is not found. |  -  |

