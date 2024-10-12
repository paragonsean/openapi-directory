# MyInfoApi

All URIs are relative to *http://example.com:80/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAutomaticInvitationList**](MyInfoApi.md#getAutomaticInvitationList) | **GET** /v1/workgroups/{workgroup_id}/automaticInvitations | List current user&#39;s automatic invitations info  |
| [**getTeamTemplateDetail**](MyInfoApi.md#getTeamTemplateDetail) | **GET** /v1/workgroups/{workgroup_id}/teamTemplates/{team_template_id} | Get current user&#39;s team template detal info  |
| [**getTeamTemplateList**](MyInfoApi.md#getTeamTemplateList) | **GET** /v1/workgroups/{workgroup_id}/teamTemplates | List current user&#39;s team templates info  |
| [**uploadProfileImage**](MyInfoApi.md#uploadProfileImage) | **POST** /v1/workgroups/{workgroup_id}/profileImage | Upload Profile Image.  A multipart/form-data request with a name \&quot;file\&quot; |


<a id="getAutomaticInvitationList"></a>
# **getAutomaticInvitationList**
> AutomaticInvitationsListVO getAutomaticInvitationList(workgroupId)

List current user&#39;s automatic invitations info 

List current user&#39;s automatic invitations info 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    MyInfoApi apiInstance = new MyInfoApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      AutomaticInvitationsListVO result = apiInstance.getAutomaticInvitationList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyInfoApi#getAutomaticInvitationList");
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

[**AutomaticInvitationsListVO**](AutomaticInvitationsListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **500** | Internal server error |  -  |

<a id="getTeamTemplateDetail"></a>
# **getTeamTemplateDetail**
> TeamTemplateExpandVO getTeamTemplateDetail(workgroupId, teamTemplateId)

Get current user&#39;s team template detal info 

Get current user&#39;s team template detal info 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    MyInfoApi apiInstance = new MyInfoApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    String teamTemplateId = "teamTemplateId_example"; // String | 
    try {
      TeamTemplateExpandVO result = apiInstance.getTeamTemplateDetail(workgroupId, teamTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyInfoApi#getTeamTemplateDetail");
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
| **teamTemplateId** | **String**|  | |

### Return type

[**TeamTemplateExpandVO**](TeamTemplateExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **500** | Internal server error |  -  |

<a id="getTeamTemplateList"></a>
# **getTeamTemplateList**
> TeamTemplateListVO getTeamTemplateList(workgroupId)

List current user&#39;s team templates info 

List current user&#39;s team templates info 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    MyInfoApi apiInstance = new MyInfoApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    try {
      TeamTemplateListVO result = apiInstance.getTeamTemplateList(workgroupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyInfoApi#getTeamTemplateList");
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

[**TeamTemplateListVO**](TeamTemplateListVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful retrieval |  -  |
| **500** | Internal server error |  -  |

<a id="uploadProfileImage"></a>
# **uploadProfileImage**
> ProfileImageVO uploadProfileImage(workgroupId, body)

Upload Profile Image.  A multipart/form-data request with a name \&quot;file\&quot;

Upload Profile Image.  A multipart/form-data request with a name \&quot;file\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MyInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://example.com:80/v1");

    MyInfoApi apiInstance = new MyInfoApi(defaultClient);
    String workgroupId = "workgroupId_example"; // String | 
    File body = new File("/path/to/file"); // File | 
    try {
      ProfileImageVO result = apiInstance.uploadProfileImage(workgroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MyInfoApi#uploadProfileImage");
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
| **body** | **File**|  | [optional] |

### Return type

[**ProfileImageVO**](ProfileImageVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
 - **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **500** | Internal server error |  -  |

