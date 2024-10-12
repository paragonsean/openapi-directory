# CustomerGroupsApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCustomerGroup**](CustomerGroupsApi.md#createCustomerGroup) | **POST** /v2/customers/groups | CreateCustomerGroup |
| [**deleteCustomerGroup**](CustomerGroupsApi.md#deleteCustomerGroup) | **DELETE** /v2/customers/groups/{group_id} | DeleteCustomerGroup |
| [**listCustomerGroups**](CustomerGroupsApi.md#listCustomerGroups) | **GET** /v2/customers/groups | ListCustomerGroups |
| [**retrieveCustomerGroup**](CustomerGroupsApi.md#retrieveCustomerGroup) | **GET** /v2/customers/groups/{group_id} | RetrieveCustomerGroup |
| [**updateCustomerGroup**](CustomerGroupsApi.md#updateCustomerGroup) | **PUT** /v2/customers/groups/{group_id} | UpdateCustomerGroup |


<a id="createCustomerGroup"></a>
# **createCustomerGroup**
> CreateCustomerGroupResponse createCustomerGroup(createCustomerGroupRequest)

CreateCustomerGroup

Creates a new customer group for a business.  The request must include the &#x60;name&#x60; value of the group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomerGroupsApi apiInstance = new CustomerGroupsApi(defaultClient);
    CreateCustomerGroupRequest createCustomerGroupRequest = new CreateCustomerGroupRequest(); // CreateCustomerGroupRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateCustomerGroupResponse result = apiInstance.createCustomerGroup(createCustomerGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsApi#createCustomerGroup");
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
| **createCustomerGroupRequest** | [**CreateCustomerGroupRequest**](CreateCustomerGroupRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateCustomerGroupResponse**](CreateCustomerGroupResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="deleteCustomerGroup"></a>
# **deleteCustomerGroup**
> DeleteCustomerGroupResponse deleteCustomerGroup(groupId)

DeleteCustomerGroup

Deletes a customer group as identified by the &#x60;group_id&#x60; value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomerGroupsApi apiInstance = new CustomerGroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | The ID of the customer group to delete.
    try {
      DeleteCustomerGroupResponse result = apiInstance.deleteCustomerGroup(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsApi#deleteCustomerGroup");
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
| **groupId** | **String**| The ID of the customer group to delete. | |

### Return type

[**DeleteCustomerGroupResponse**](DeleteCustomerGroupResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listCustomerGroups"></a>
# **listCustomerGroups**
> ListCustomerGroupsResponse listCustomerGroups(cursor, limit)

ListCustomerGroups

Retrieves the list of customer groups of a business.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomerGroupsApi apiInstance = new CustomerGroupsApi(defaultClient);
    String cursor = "cursor_example"; // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    Integer limit = 56; // Integer | The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than 1 or greater than 50. The default value is 50.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    try {
      ListCustomerGroupsResponse result = apiInstance.listCustomerGroups(cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsApi#listCustomerGroups");
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
| **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] |
| **limit** | **Integer**| The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than 1 or greater than 50. The default value is 50.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination). | [optional] |

### Return type

[**ListCustomerGroupsResponse**](ListCustomerGroupsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="retrieveCustomerGroup"></a>
# **retrieveCustomerGroup**
> RetrieveCustomerGroupResponse retrieveCustomerGroup(groupId)

RetrieveCustomerGroup

Retrieves a specific customer group as identified by the &#x60;group_id&#x60; value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomerGroupsApi apiInstance = new CustomerGroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | The ID of the customer group to retrieve.
    try {
      RetrieveCustomerGroupResponse result = apiInstance.retrieveCustomerGroup(groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsApi#retrieveCustomerGroup");
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
| **groupId** | **String**| The ID of the customer group to retrieve. | |

### Return type

[**RetrieveCustomerGroupResponse**](RetrieveCustomerGroupResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="updateCustomerGroup"></a>
# **updateCustomerGroup**
> UpdateCustomerGroupResponse updateCustomerGroup(groupId, updateCustomerGroupRequest)

UpdateCustomerGroup

Updates a customer group as identified by the &#x60;group_id&#x60; value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CustomerGroupsApi apiInstance = new CustomerGroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | The ID of the customer group to update.
    UpdateCustomerGroupRequest updateCustomerGroupRequest = new UpdateCustomerGroupRequest(); // UpdateCustomerGroupRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      UpdateCustomerGroupResponse result = apiInstance.updateCustomerGroup(groupId, updateCustomerGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerGroupsApi#updateCustomerGroup");
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
| **groupId** | **String**| The ID of the customer group to update. | |
| **updateCustomerGroupRequest** | [**UpdateCustomerGroupRequest**](UpdateCustomerGroupRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**UpdateCustomerGroupResponse**](UpdateCustomerGroupResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

