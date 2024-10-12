# BlueprintApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blueprintsCreateOrUpdate**](BlueprintApi.md#blueprintsCreateOrUpdate) | **PUT** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName} |  |
| [**blueprintsDelete**](BlueprintApi.md#blueprintsDelete) | **DELETE** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName} |  |
| [**blueprintsGet**](BlueprintApi.md#blueprintsGet) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName} |  |
| [**blueprintsList**](BlueprintApi.md#blueprintsList) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints |  |


<a id="blueprintsCreateOrUpdate"></a>
# **blueprintsCreateOrUpdate**
> Blueprint blueprintsCreateOrUpdate(apiVersion, managementGroupName, blueprintName, blueprint)



Create or update Blueprint definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlueprintApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlueprintApi apiInstance = new BlueprintApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    Blueprint blueprint = new Blueprint(); // Blueprint | Blueprint definition.
    try {
      Blueprint result = apiInstance.blueprintsCreateOrUpdate(apiVersion, managementGroupName, blueprintName, blueprint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlueprintApi#blueprintsCreateOrUpdate");
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
| **apiVersion** | **String**| Client Api Version. | |
| **managementGroupName** | **String**| ManagementGroup where blueprint stores. | |
| **blueprintName** | **String**| name of the blueprint. | |
| **blueprint** | [**Blueprint**](Blueprint.md)| Blueprint definition. | |

### Return type

[**Blueprint**](Blueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created -- Blueprint definition saved. |  -  |

<a id="blueprintsDelete"></a>
# **blueprintsDelete**
> Blueprint blueprintsDelete(apiVersion, managementGroupName, blueprintName)



Delete a blueprint definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlueprintApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlueprintApi apiInstance = new BlueprintApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    try {
      Blueprint result = apiInstance.blueprintsDelete(apiVersion, managementGroupName, blueprintName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlueprintApi#blueprintsDelete");
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
| **apiVersion** | **String**| Client Api Version. | |
| **managementGroupName** | **String**| ManagementGroup where blueprint stores. | |
| **blueprintName** | **String**| name of the blueprint. | |

### Return type

[**Blueprint**](Blueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- blueprint definition deleted |  -  |
| **204** | no content |  -  |

<a id="blueprintsGet"></a>
# **blueprintsGet**
> Blueprint blueprintsGet(apiVersion, managementGroupName, blueprintName)



Get a blueprint definition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlueprintApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlueprintApi apiInstance = new BlueprintApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    String blueprintName = "blueprintName_example"; // String | name of the blueprint.
    try {
      Blueprint result = apiInstance.blueprintsGet(apiVersion, managementGroupName, blueprintName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlueprintApi#blueprintsGet");
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
| **apiVersion** | **String**| Client Api Version. | |
| **managementGroupName** | **String**| ManagementGroup where blueprint stores. | |
| **blueprintName** | **String**| name of the blueprint. | |

### Return type

[**Blueprint**](Blueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- blueprint definition retrieved. |  -  |

<a id="blueprintsList"></a>
# **blueprintsList**
> BlueprintList blueprintsList(apiVersion, managementGroupName)



List Blueprint definitions within a Management Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlueprintApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlueprintApi apiInstance = new BlueprintApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
    try {
      BlueprintList result = apiInstance.blueprintsList(apiVersion, managementGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlueprintApi#blueprintsList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **managementGroupName** | **String**| ManagementGroup where blueprint stores. | |

### Return type

[**BlueprintList**](BlueprintList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- retrieved Blueprints in this ManagementGroup. |  -  |

