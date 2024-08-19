# ProfilesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**profilesCheckTrafficManagerRelativeDnsNameAvailability**](ProfilesApi.md#profilesCheckTrafficManagerRelativeDnsNameAvailability) | **POST** /providers/Microsoft.Network/checkTrafficManagerNameAvailability |  |
| [**profilesCreateOrUpdate**](ProfilesApi.md#profilesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName} |  |
| [**profilesDelete**](ProfilesApi.md#profilesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName} |  |
| [**profilesGet**](ProfilesApi.md#profilesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName} |  |
| [**profilesListAll**](ProfilesApi.md#profilesListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/trafficmanagerprofiles |  |
| [**profilesListAllInResourceGroup**](ProfilesApi.md#profilesListAllInResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles |  |
| [**profilesUpdate**](ProfilesApi.md#profilesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName} |  |


<a id="profilesCheckTrafficManagerRelativeDnsNameAvailability"></a>
# **profilesCheckTrafficManagerRelativeDnsNameAvailability**
> TrafficManagerNameAvailability profilesCheckTrafficManagerRelativeDnsNameAvailability(apiVersion, parameters)



Checks the availability of a Traffic Manager Relative DNS name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    CheckTrafficManagerRelativeDnsNameAvailabilityParameters parameters = new CheckTrafficManagerRelativeDnsNameAvailabilityParameters(); // CheckTrafficManagerRelativeDnsNameAvailabilityParameters | The Traffic Manager name parameters supplied to the CheckTrafficManagerNameAvailability operation.
    try {
      TrafficManagerNameAvailability result = apiInstance.profilesCheckTrafficManagerRelativeDnsNameAvailability(apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesCheckTrafficManagerRelativeDnsNameAvailability");
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
| **parameters** | [**CheckTrafficManagerRelativeDnsNameAvailabilityParameters**](CheckTrafficManagerRelativeDnsNameAvailabilityParameters.md)| The Traffic Manager name parameters supplied to the CheckTrafficManagerNameAvailability operation. | |

### Return type

[**TrafficManagerNameAvailability**](TrafficManagerNameAvailability.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Traffic Manager Name Availability. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="profilesCreateOrUpdate"></a>
# **profilesCreateOrUpdate**
> Profile profilesCreateOrUpdate(resourceGroupName, profileName, apiVersion, subscriptionId, parameters)



Create or update a Traffic Manager profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager profile.
    String profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Profile parameters = new Profile(); // Profile | The Traffic Manager profile parameters supplied to the CreateOrUpdate operation.
    try {
      Profile result = apiInstance.profilesCreateOrUpdate(resourceGroupName, profileName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager profile. | |
| **profileName** | **String**| The name of the Traffic Manager profile. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**Profile**](Profile.md)| The Traffic Manager profile parameters supplied to the CreateOrUpdate operation. | |

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The created or updated Traffic Manager profile. |  -  |
| **201** | The created or updated Traffic Manager profile. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="profilesDelete"></a>
# **profilesDelete**
> DeleteOperationResult profilesDelete(resourceGroupName, profileName, apiVersion, subscriptionId)



Deletes a Traffic Manager profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager profile to be deleted.
    String profileName = "profileName_example"; // String | The name of the Traffic Manager profile to be deleted.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      DeleteOperationResult result = apiInstance.profilesDelete(resourceGroupName, profileName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesDelete");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager profile to be deleted. | |
| **profileName** | **String**| The name of the Traffic Manager profile to be deleted. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**DeleteOperationResult**](DeleteOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Traffic Manager Profile was deleted successfully. |  -  |
| **204** | The profile does not exist. It could have been deleted on a previous request. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="profilesGet"></a>
# **profilesGet**
> Profile profilesGet(resourceGroupName, profileName, apiVersion, subscriptionId)



Gets a Traffic Manager profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager profile.
    String profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      Profile result = apiInstance.profilesGet(resourceGroupName, profileName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesGet");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager profile. | |
| **profileName** | **String**| The name of the Traffic Manager profile. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Traffic Manager profile. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="profilesListAll"></a>
# **profilesListAll**
> ProfileListResult profilesListAll(apiVersion, subscriptionId)



Lists all Traffic Manager profiles within a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ProfileListResult result = apiInstance.profilesListAll(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesListAll");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ProfileListResult**](ProfileListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of Traffic Manager profiles. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="profilesListAllInResourceGroup"></a>
# **profilesListAllInResourceGroup**
> ProfileListResult profilesListAllInResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists all Traffic Manager profiles within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager profiles to be listed.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ProfileListResult result = apiInstance.profilesListAllInResourceGroup(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesListAllInResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager profiles to be listed. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ProfileListResult**](ProfileListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of Traffic Manager profiles. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="profilesUpdate"></a>
# **profilesUpdate**
> Profile profilesUpdate(resourceGroupName, profileName, apiVersion, subscriptionId, parameters)



Update a Traffic Manager profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ProfilesApi apiInstance = new ProfilesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager profile.
    String profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Profile parameters = new Profile(); // Profile | The Traffic Manager profile parameters supplied to the Update operation.
    try {
      Profile result = apiInstance.profilesUpdate(resourceGroupName, profileName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfilesApi#profilesUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager profile. | |
| **profileName** | **String**| The name of the Traffic Manager profile. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**Profile**](Profile.md)| The Traffic Manager profile parameters supplied to the Update operation. | |

### Return type

[**Profile**](Profile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated Traffic Manager profile. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

