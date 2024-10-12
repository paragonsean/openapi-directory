# GroupApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createGroup**](GroupApi.md#createGroup) | **POST** /group | Create a group |
| [**fetchGroup**](GroupApi.md#fetchGroup) | **GET** /group/{id} | Get a group |
| [**fetchGroups**](GroupApi.md#fetchGroups) | **GET** /group | List groups |


<a id="createGroup"></a>
# **createGroup**
> CreateGroupResponse createGroup(createGroupRequest)

Create a group

Create a group record.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    GroupApi apiInstance = new GroupApi(defaultClient);
    CreateGroupRequest createGroupRequest = new CreateGroupRequest(); // CreateGroupRequest | 
    try {
      CreateGroupResponse result = apiInstance.createGroup(createGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#createGroup");
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
| **createGroupRequest** | [**CreateGroupRequest**](CreateGroupRequest.md)|  | |

### Return type

[**CreateGroupResponse**](CreateGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

<a id="fetchGroup"></a>
# **fetchGroup**
> FetchGroupResponse fetchGroup(id)

Get a group

Get a group record by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String id = "id_example"; // String | Group identifier
    try {
      FetchGroupResponse result = apiInstance.fetchGroup(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#fetchGroup");
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
| **id** | **String**| Group identifier | |

### Return type

[**FetchGroupResponse**](FetchGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="fetchGroups"></a>
# **fetchGroups**
> FetchGroupsResponse fetchGroups(filterOrganization, filterName)

List groups

Get a list of groups matching the specified filters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    GroupApi apiInstance = new GroupApi(defaultClient);
    String filterOrganization = "filterOrganization_example"; // String | Organization identifier
    String filterName = "filterName_example"; // String | Group name
    try {
      FetchGroupsResponse result = apiInstance.fetchGroups(filterOrganization, filterName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupApi#fetchGroups");
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
| **filterOrganization** | **String**| Organization identifier | |
| **filterName** | **String**| Group name | [optional] |

### Return type

[**FetchGroupsResponse**](FetchGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

