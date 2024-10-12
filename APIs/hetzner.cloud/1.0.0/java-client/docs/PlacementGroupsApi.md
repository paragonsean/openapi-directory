# PlacementGroupsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**placementGroupsGet**](PlacementGroupsApi.md#placementGroupsGet) | **GET** /placement_groups | Get all PlacementGroups |
| [**placementGroupsIdDelete**](PlacementGroupsApi.md#placementGroupsIdDelete) | **DELETE** /placement_groups/{id} | Delete a PlacementGroup |
| [**placementGroupsIdGet**](PlacementGroupsApi.md#placementGroupsIdGet) | **GET** /placement_groups/{id} | Get a PlacementGroup |
| [**placementGroupsIdPut**](PlacementGroupsApi.md#placementGroupsIdPut) | **PUT** /placement_groups/{id} | Update a PlacementGroup |
| [**placementGroupsPost**](PlacementGroupsApi.md#placementGroupsPost) | **POST** /placement_groups | Create a PlacementGroup |


<a id="placementGroupsGet"></a>
# **placementGroupsGet**
> PlacementGroupsResponse placementGroupsGet(sort, name, labelSelector, type)

Get all PlacementGroups

Returns all PlacementGroup objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PlacementGroupsApi apiInstance = new PlacementGroupsApi(defaultClient);
    String sort = "id"; // String | Can be used multiple times.
    String name = "name_example"; // String | Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    String labelSelector = "labelSelector_example"; // String | Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    String type = "spread"; // String | Can be used multiple times. The response will only contain PlacementGroups matching the type.
    try {
      PlacementGroupsResponse result = apiInstance.placementGroupsGet(sort, name, labelSelector, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacementGroupsApi#placementGroupsGet");
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
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, name, name:asc, name:desc, created, created:asc, created:desc] |
| **name** | **String**| Can be used to filter resources by their name. The response will only contain the resources matching the specified name | [optional] |
| **labelSelector** | **String**| Can be used to filter resources by labels. The response will only contain resources matching the label selector. | [optional] |
| **type** | **String**| Can be used multiple times. The response will only contain PlacementGroups matching the type. | [optional] [enum: spread] |

### Return type

[**PlacementGroupsResponse**](PlacementGroupsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;placement_groups&#x60; key contains an array of PlacementGroup objects |  -  |

<a id="placementGroupsIdDelete"></a>
# **placementGroupsIdDelete**
> placementGroupsIdDelete(id)

Delete a PlacementGroup

Deletes a PlacementGroup.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PlacementGroupsApi apiInstance = new PlacementGroupsApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    try {
      apiInstance.placementGroupsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacementGroupsApi#placementGroupsIdDelete");
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
| **id** | **Integer**| ID of the resource | |

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
| **204** | PlacementGroup deleted |  -  |

<a id="placementGroupsIdGet"></a>
# **placementGroupsIdGet**
> PlacementGroupResponse placementGroupsIdGet(id)

Get a PlacementGroup

Gets a specific PlacementGroup object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PlacementGroupsApi apiInstance = new PlacementGroupsApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    try {
      PlacementGroupResponse result = apiInstance.placementGroupsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacementGroupsApi#placementGroupsIdGet");
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
| **id** | **Integer**| ID of the resource | |

### Return type

[**PlacementGroupResponse**](PlacementGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;placement_group&#x60; key contains a PlacementGroup object |  -  |

<a id="placementGroupsIdPut"></a>
# **placementGroupsIdPut**
> PlacementGroupResponse placementGroupsIdPut(id, updatePlacementGroupRequest)

Update a PlacementGroup

Updates the PlacementGroup properties.  Note that when updating labels, the PlacementGroup’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body.  Note: if the PlacementGroup object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PlacementGroupsApi apiInstance = new PlacementGroupsApi(defaultClient);
    Integer id = 56; // Integer | ID of the resource
    UpdatePlacementGroupRequest updatePlacementGroupRequest = new UpdatePlacementGroupRequest(); // UpdatePlacementGroupRequest | 
    try {
      PlacementGroupResponse result = apiInstance.placementGroupsIdPut(id, updatePlacementGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacementGroupsApi#placementGroupsIdPut");
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
| **id** | **Integer**| ID of the resource | |
| **updatePlacementGroupRequest** | [**UpdatePlacementGroupRequest**](UpdatePlacementGroupRequest.md)|  | [optional] |

### Return type

[**PlacementGroupResponse**](PlacementGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;certificate&#x60; key contains the PlacementGroup that was just updated |  -  |

<a id="placementGroupsPost"></a>
# **placementGroupsPost**
> CreatePlacementGroupResponse placementGroupsPost(createPlacementGroupRequest)

Create a PlacementGroup

Creates a new PlacementGroup. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlacementGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PlacementGroupsApi apiInstance = new PlacementGroupsApi(defaultClient);
    CreatePlacementGroupRequest createPlacementGroupRequest = new CreatePlacementGroupRequest(); // CreatePlacementGroupRequest | 
    try {
      CreatePlacementGroupResponse result = apiInstance.placementGroupsPost(createPlacementGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlacementGroupsApi#placementGroupsPost");
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
| **createPlacementGroupRequest** | [**CreatePlacementGroupRequest**](CreatePlacementGroupRequest.md)|  | [optional] |

### Return type

[**CreatePlacementGroupResponse**](CreatePlacementGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;PlacementGroup&#x60; key contains the PlacementGroup that was just created. |  -  |

