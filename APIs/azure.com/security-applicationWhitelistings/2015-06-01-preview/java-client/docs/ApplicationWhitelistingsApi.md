# ApplicationWhitelistingsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**adaptiveApplicationControlsGet**](ApplicationWhitelistingsApi.md#adaptiveApplicationControlsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/applicationWhitelistings/{groupName} |  |
| [**adaptiveApplicationControlsList**](ApplicationWhitelistingsApi.md#adaptiveApplicationControlsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/applicationWhitelistings |  |
| [**adaptiveApplicationControlsPut**](ApplicationWhitelistingsApi.md#adaptiveApplicationControlsPut) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/applicationWhitelistings/{groupName} |  |


<a id="adaptiveApplicationControlsGet"></a>
# **adaptiveApplicationControlsGet**
> AppWhitelistingGroup adaptiveApplicationControlsGet(subscriptionId, ascLocation, groupName, apiVersion)



Gets an application control VM/server group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationWhitelistingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationWhitelistingsApi apiInstance = new ApplicationWhitelistingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String groupName = "groupName_example"; // String | Name of an application control VM/server group
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    try {
      AppWhitelistingGroup result = apiInstance.adaptiveApplicationControlsGet(subscriptionId, ascLocation, groupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationWhitelistingsApi#adaptiveApplicationControlsGet");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **groupName** | **String**| Name of an application control VM/server group | |
| **apiVersion** | **String**| API version for the operation | |

### Return type

[**AppWhitelistingGroup**](AppWhitelistingGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="adaptiveApplicationControlsList"></a>
# **adaptiveApplicationControlsList**
> AppWhitelistingGroups adaptiveApplicationControlsList(subscriptionId, apiVersion, includePathRecommendations, summary)



Gets a list of application control VM/server groups for the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationWhitelistingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationWhitelistingsApi apiInstance = new ApplicationWhitelistingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    Boolean includePathRecommendations = true; // Boolean | Include the policy rules
    Boolean summary = true; // Boolean | Return output in a summarized form
    try {
      AppWhitelistingGroups result = apiInstance.adaptiveApplicationControlsList(subscriptionId, apiVersion, includePathRecommendations, summary);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationWhitelistingsApi#adaptiveApplicationControlsList");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **apiVersion** | **String**| API version for the operation | |
| **includePathRecommendations** | **Boolean**| Include the policy rules | [optional] |
| **summary** | **Boolean**| Return output in a summarized form | [optional] |

### Return type

[**AppWhitelistingGroups**](AppWhitelistingGroups.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="adaptiveApplicationControlsPut"></a>
# **adaptiveApplicationControlsPut**
> AppWhitelistingGroup adaptiveApplicationControlsPut(subscriptionId, ascLocation, groupName, apiVersion, body)



Update an application control VM/server group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationWhitelistingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationWhitelistingsApi apiInstance = new ApplicationWhitelistingsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
    String ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
    String groupName = "groupName_example"; // String | Name of an application control VM/server group
    String apiVersion = "apiVersion_example"; // String | API version for the operation
    AppWhitelistingPutGroupData body = new AppWhitelistingPutGroupData(); // AppWhitelistingPutGroupData | The updated VM/server group data
    try {
      AppWhitelistingGroup result = apiInstance.adaptiveApplicationControlsPut(subscriptionId, ascLocation, groupName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationWhitelistingsApi#adaptiveApplicationControlsPut");
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
| **subscriptionId** | **String**| Azure subscription ID | |
| **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | |
| **groupName** | **String**| Name of an application control VM/server group | |
| **apiVersion** | **String**| API version for the operation | |
| **body** | [**AppWhitelistingPutGroupData**](AppWhitelistingPutGroupData.md)| The updated VM/server group data | |

### Return type

[**AppWhitelistingGroup**](AppWhitelistingGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

