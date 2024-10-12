# ContactApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBillingRecipients**](ContactApi.md#getBillingRecipients) | **GET** /v1/workgroups/{workgroup_id}/billingRecipients | List Billing Recipients |
| [**getContactList**](ContactApi.md#getContactList) | **GET** /v1/workgroups/{workgroup_id}/contacts | List the contacts |
| [**getContactUserInfo**](ContactApi.md#getContactUserInfo) | **GET** /v1/workgroups/{workgroup_id}/contacts/{user_id} | Contact Info |


<a id="getBillingRecipients"></a>
# **getBillingRecipients**
> ContactsListVO getBillingRecipients(workgroupId)

List Billing Recipients

List Billing Recipients

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ContactApi apiInstance = new ContactApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      ContactsListVO result = apiInstance.getBillingRecipients(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactApi#getBillingRecipients");
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
| **workgroupId** | **String**|  | |

### Return type

[**ContactsListVO**](ContactsListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getContactList"></a>
# **getContactList**
> ContactsListVO getContactList(workgroupId)

List the contacts

List the contacts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ContactApi apiInstance = new ContactApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      ContactsListVO result = apiInstance.getContactList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactApi#getContactList");
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
| **workgroupId** | **String**|  | |

### Return type

[**ContactsListVO**](ContactsListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

<a id="getContactUserInfo"></a>
# **getContactUserInfo**
> UserDetailsExpandVO getContactUserInfo(workgroupId, userId)

Contact Info

Contact Info

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContactApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    ContactApi apiInstance = new ContactApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      UserDetailsExpandVO result = apiInstance.getContactUserInfo(workgroupId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContactApi#getContactUserInfo");
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
| **workgroupId** | **String**|  | |
| **userId** | **String**|  | |

### Return type

[**UserDetailsExpandVO**](UserDetailsExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **404** | There are not any result matching your search condition |  -  |
| **500** | Internal server error |  -  |

