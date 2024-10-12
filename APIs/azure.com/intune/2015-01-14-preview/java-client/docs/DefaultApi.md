# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**androidAddAppForMAMPolicy**](DefaultApi.md#androidAddAppForMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName}/apps/{appName} |  |
| [**androidAddGroupForMAMPolicy**](DefaultApi.md#androidAddGroupForMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName}/groups/{groupId} |  |
| [**androidCreateOrUpdateMAMPolicy**](DefaultApi.md#androidCreateOrUpdateMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName} |  |
| [**androidDeleteAppForMAMPolicy**](DefaultApi.md#androidDeleteAppForMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName}/apps/{appName} |  |
| [**androidDeleteGroupForMAMPolicy**](DefaultApi.md#androidDeleteGroupForMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName}/groups/{groupId} |  |
| [**androidDeleteMAMPolicy**](DefaultApi.md#androidDeleteMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName} |  |
| [**androidGetAppForMAMPolicy**](DefaultApi.md#androidGetAppForMAMPolicy) | **GET** /providers/Microsoft.Intune/locations/{hostName}/AndroidPolicies/{policyName}/apps |  |
| [**androidGetGroupsForMAMPolicy**](DefaultApi.md#androidGetGroupsForMAMPolicy) | **GET** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName}/groups |  |
| [**androidGetMAMPolicies**](DefaultApi.md#androidGetMAMPolicies) | **GET** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies |  |
| [**androidGetMAMPolicyByName**](DefaultApi.md#androidGetMAMPolicyByName) | **GET** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName} |  |
| [**androidPatchMAMPolicy**](DefaultApi.md#androidPatchMAMPolicy) | **PATCH** /providers/Microsoft.Intune/locations/{hostName}/androidPolicies/{policyName} |  |
| [**getApps**](DefaultApi.md#getApps) | **GET** /providers/Microsoft.Intune/locations/{hostName}/apps |  |
| [**getLocationByHostName**](DefaultApi.md#getLocationByHostName) | **GET** /providers/Microsoft.Intune/locations/hostName |  |
| [**getLocations**](DefaultApi.md#getLocations) | **GET** /providers/Microsoft.Intune/locations |  |
| [**getMAMFlaggedUserByName**](DefaultApi.md#getMAMFlaggedUserByName) | **GET** /providers/Microsoft.Intune/locations/{hostName}/flaggedUsers/{userName} |  |
| [**getMAMFlaggedUsers**](DefaultApi.md#getMAMFlaggedUsers) | **GET** /providers/Microsoft.Intune/locations/{hostName}/flaggedUsers |  |
| [**getMAMStatuses**](DefaultApi.md#getMAMStatuses) | **GET** /providers/Microsoft.Intune/locations/{hostName}/statuses/default |  |
| [**getMAMUserDeviceByDeviceName**](DefaultApi.md#getMAMUserDeviceByDeviceName) | **GET** /providers/Microsoft.Intune/locations/{hostName}/users/{userName}/devices/{deviceName} |  |
| [**getMAMUserDevices**](DefaultApi.md#getMAMUserDevices) | **GET** /providers/Microsoft.Intune/locations/{hostName}/users/{userName}/devices |  |
| [**getMAMUserFlaggedEnrolledApps**](DefaultApi.md#getMAMUserFlaggedEnrolledApps) | **GET** /providers/Microsoft.Intune/locations/{hostName}/flaggedUsers/{userName}/flaggedEnrolledApps |  |
| [**getOperationResults**](DefaultApi.md#getOperationResults) | **GET** /providers/Microsoft.Intune/locations/{hostName}/operationResults |  |
| [**iosAddAppForMAMPolicy**](DefaultApi.md#iosAddAppForMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/apps/{appName} |  |
| [**iosAddGroupForMAMPolicy**](DefaultApi.md#iosAddGroupForMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/groups/{groupId} |  |
| [**iosCreateOrUpdateMAMPolicy**](DefaultApi.md#iosCreateOrUpdateMAMPolicy) | **PUT** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName} |  |
| [**iosDeleteAppForMAMPolicy**](DefaultApi.md#iosDeleteAppForMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/apps/{appName} |  |
| [**iosDeleteGroupForMAMPolicy**](DefaultApi.md#iosDeleteGroupForMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/groups/{groupId} |  |
| [**iosDeleteMAMPolicy**](DefaultApi.md#iosDeleteMAMPolicy) | **DELETE** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName} |  |
| [**iosGetAppForMAMPolicy**](DefaultApi.md#iosGetAppForMAMPolicy) | **GET** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/apps |  |
| [**iosGetGroupsForMAMPolicy**](DefaultApi.md#iosGetGroupsForMAMPolicy) | **GET** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName}/groups |  |
| [**iosGetMAMPolicies**](DefaultApi.md#iosGetMAMPolicies) | **GET** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies |  |
| [**iosGetMAMPolicyByName**](DefaultApi.md#iosGetMAMPolicyByName) | **GET** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName} |  |
| [**iosPatchMAMPolicy**](DefaultApi.md#iosPatchMAMPolicy) | **PATCH** /providers/Microsoft.Intune/locations/{hostName}/iosPolicies/{policyName} |  |
| [**wipeMAMUserDevice**](DefaultApi.md#wipeMAMUserDevice) | **POST** /providers/Microsoft.Intune/locations/{hostName}/users/{userName}/devices/{deviceName}/wipe |  |


<a id="androidAddAppForMAMPolicy"></a>
# **androidAddAppForMAMPolicy**
> androidAddAppForMAMPolicy(hostName, policyName, appName, apiVersion, parameters)



Add app to an AndroidMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String appName = "appName_example"; // String | application unique Name
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    MAMPolicyAppIdOrGroupIdPayload parameters = new MAMPolicyAppIdOrGroupIdPayload(); // MAMPolicyAppIdOrGroupIdPayload | Parameters supplied to the Create or update app to an android policy operation.
    try {
      apiInstance.androidAddAppForMAMPolicy(hostName, policyName, appName, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#androidAddAppForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **appName** | **String**| application unique Name | |
| **apiVersion** | **String**| Service Api Version. | |
| **parameters** | [**MAMPolicyAppIdOrGroupIdPayload**](MAMPolicyAppIdOrGroupIdPayload.md)| Parameters supplied to the Create or update app to an android policy operation. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No-Content. |  -  |
| **204** | No-Content. |  -  |
| **0** | unexpected error |  -  |

<a id="androidAddGroupForMAMPolicy"></a>
# **androidAddGroupForMAMPolicy**
> androidAddGroupForMAMPolicy(hostName, policyName, groupId, apiVersion, parameters)



Add group to an AndroidMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String groupId = "groupId_example"; // String | group Id
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    MAMPolicyAppIdOrGroupIdPayload parameters = new MAMPolicyAppIdOrGroupIdPayload(); // MAMPolicyAppIdOrGroupIdPayload | Parameters supplied to the Create or update app to an android policy operation.
    try {
      apiInstance.androidAddGroupForMAMPolicy(hostName, policyName, groupId, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#androidAddGroupForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **groupId** | **String**| group Id | |
| **apiVersion** | **String**| Service Api Version. | |
| **parameters** | [**MAMPolicyAppIdOrGroupIdPayload**](MAMPolicyAppIdOrGroupIdPayload.md)| Parameters supplied to the Create or update app to an android policy operation. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No-Content. |  -  |
| **204** | No-Content. |  -  |
| **0** | unexpected error |  -  |

<a id="androidCreateOrUpdateMAMPolicy"></a>
# **androidCreateOrUpdateMAMPolicy**
> AndroidMAMPolicy androidCreateOrUpdateMAMPolicy(hostName, policyName, apiVersion, parameters)



Creates or updates AndroidMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    AndroidMAMPolicy parameters = new AndroidMAMPolicy(); // AndroidMAMPolicy | Parameters supplied to the Create or update an android policy operation.
    try {
      AndroidMAMPolicy result = apiInstance.androidCreateOrUpdateMAMPolicy(hostName, policyName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#androidCreateOrUpdateMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **apiVersion** | **String**| Service Api Version. | |
| **parameters** | [**AndroidMAMPolicy**](AndroidMAMPolicy.md)| Parameters supplied to the Create or update an android policy operation. | |

### Return type

[**AndroidMAMPolicy**](AndroidMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | android entity. |  -  |
| **0** | unexpected error |  -  |

<a id="androidDeleteAppForMAMPolicy"></a>
# **androidDeleteAppForMAMPolicy**
> androidDeleteAppForMAMPolicy(hostName, policyName, appName, apiVersion)



Delete App for Android Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String appName = "appName_example"; // String | application unique Name
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      apiInstance.androidDeleteAppForMAMPolicy(hostName, policyName, appName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#androidDeleteAppForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **appName** | **String**| application unique Name | |
| **apiVersion** | **String**| Service Api Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No-Content. |  -  |
| **204** | No-Content. |  -  |
| **0** | unexpected error |  -  |

<a id="androidDeleteGroupForMAMPolicy"></a>
# **androidDeleteGroupForMAMPolicy**
> androidDeleteGroupForMAMPolicy(hostName, policyName, groupId, apiVersion)



Delete Group for Android Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String groupId = "groupId_example"; // String | application unique Name
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      apiInstance.androidDeleteGroupForMAMPolicy(hostName, policyName, groupId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#androidDeleteGroupForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **groupId** | **String**| application unique Name | |
| **apiVersion** | **String**| Service Api Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No-Content. |  -  |
| **204** | No-Content. |  -  |
| **0** | unexpected error |  -  |

<a id="androidDeleteMAMPolicy"></a>
# **androidDeleteMAMPolicy**
> androidDeleteMAMPolicy(hostName, policyName, apiVersion)



Delete Android Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      apiInstance.androidDeleteMAMPolicy(hostName, policyName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#androidDeleteMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **apiVersion** | **String**| Service Api Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No-Content. |  -  |
| **204** | No-Content. |  -  |
| **0** | unexpected error |  -  |

<a id="androidGetAppForMAMPolicy"></a>
# **androidGetAppForMAMPolicy**
> ApplicationCollection androidGetAppForMAMPolicy(hostName, policyName, apiVersion, $filter, $top, $select)



Get apps for an AndroidMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      ApplicationCollection result = apiInstance.androidGetAppForMAMPolicy(hostName, policyName, apiVersion, $filter, $top, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#androidGetAppForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **apiVersion** | **String**| Service Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**ApplicationCollection**](ApplicationCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | applications as collection response |  -  |
| **0** | unexpected error |  -  |

<a id="androidGetGroupsForMAMPolicy"></a>
# **androidGetGroupsForMAMPolicy**
> GroupsCollection androidGetGroupsForMAMPolicy(hostName, policyName, apiVersion)



Returns groups for a given AndroidMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | policy name for the tenant
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      GroupsCollection result = apiInstance.androidGetGroupsForMAMPolicy(hostName, policyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#androidGetGroupsForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| policy name for the tenant | |
| **apiVersion** | **String**| Service Api Version. | |

### Return type

[**GroupsCollection**](GroupsCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | groups as collection response |  -  |
| **0** | unexpected error |  -  |

<a id="androidGetMAMPolicies"></a>
# **androidGetMAMPolicies**
> AndroidMAMPolicyCollection androidGetMAMPolicies(hostName, apiVersion, $filter, $top, $select)



Returns Intune Android policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      AndroidMAMPolicyCollection result = apiInstance.androidGetMAMPolicies(hostName, apiVersion, $filter, $top, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#androidGetMAMPolicies");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **apiVersion** | **String**| Service Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**AndroidMAMPolicyCollection**](AndroidMAMPolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | android Policies response |  -  |
| **0** | unexpected error |  -  |

<a id="androidGetMAMPolicyByName"></a>
# **androidGetMAMPolicyByName**
> AndroidMAMPolicy androidGetMAMPolicyByName(hostName, policyName, apiVersion, $select)



Returns AndroidMAMPolicy with given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      AndroidMAMPolicy result = apiInstance.androidGetMAMPolicyByName(hostName, policyName, apiVersion, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#androidGetMAMPolicyByName");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **apiVersion** | **String**| Service Api Version. | |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**AndroidMAMPolicy**](AndroidMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | iOSMAMPolicy entity. |  -  |
| **0** | unexpected error |  -  |

<a id="androidPatchMAMPolicy"></a>
# **androidPatchMAMPolicy**
> AndroidMAMPolicy androidPatchMAMPolicy(hostName, policyName, apiVersion, parameters)



Patch AndroidMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    AndroidMAMPolicy parameters = new AndroidMAMPolicy(); // AndroidMAMPolicy | Parameters supplied to the Create or update an android policy operation.
    try {
      AndroidMAMPolicy result = apiInstance.androidPatchMAMPolicy(hostName, policyName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#androidPatchMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **apiVersion** | **String**| Service Api Version. | |
| **parameters** | [**AndroidMAMPolicy**](AndroidMAMPolicy.md)| Parameters supplied to the Create or update an android policy operation. | |

### Return type

[**AndroidMAMPolicy**](AndroidMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | android entity. |  -  |
| **0** | unexpected error |  -  |

<a id="getApps"></a>
# **getApps**
> ApplicationCollection getApps(hostName, apiVersion, $filter, $top, $select)



Returns Intune Manageable apps.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      ApplicationCollection result = apiInstance.getApps(hostName, apiVersion, $filter, $top, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getApps");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **apiVersion** | **String**| Service Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**ApplicationCollection**](ApplicationCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | applications as collection response |  -  |
| **0** | unexpected error |  -  |

<a id="getLocationByHostName"></a>
# **getLocationByHostName**
> Location getLocationByHostName(apiVersion)



Returns location for given tenant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      Location result = apiInstance.getLocationByHostName(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLocationByHostName");
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
| **apiVersion** | **String**| Service Api Version. | |

### Return type

[**Location**](Location.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | single location response |  -  |
| **0** | unexpected error |  -  |

<a id="getLocations"></a>
# **getLocations**
> LocationCollection getLocations(apiVersion)



Returns location for user tenant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      LocationCollection result = apiInstance.getLocations(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLocations");
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
| **apiVersion** | **String**| Service Api Version. | |

### Return type

[**LocationCollection**](LocationCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | location response as a collection |  -  |
| **0** | unexpected error |  -  |

<a id="getMAMFlaggedUserByName"></a>
# **getMAMFlaggedUserByName**
> FlaggedUser getMAMFlaggedUserByName(hostName, userName, apiVersion, $select)



Returns Intune flagged user details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String userName = "userName_example"; // String | Flagged userName
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      FlaggedUser result = apiInstance.getMAMFlaggedUserByName(hostName, userName, apiVersion, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMAMFlaggedUserByName");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **userName** | **String**| Flagged userName | |
| **apiVersion** | **String**| Service Api Version. | |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**FlaggedUser**](FlaggedUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flagged user details in response |  -  |
| **0** | unexpected error |  -  |

<a id="getMAMFlaggedUsers"></a>
# **getMAMFlaggedUsers**
> FlaggedUserCollection getMAMFlaggedUsers(hostName, apiVersion, $filter, $top, $select)



Returns Intune flagged user collection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      FlaggedUserCollection result = apiInstance.getMAMFlaggedUsers(hostName, apiVersion, $filter, $top, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMAMFlaggedUsers");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **apiVersion** | **String**| Service Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**FlaggedUserCollection**](FlaggedUserCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flagged users as collection response |  -  |
| **0** | unexpected error |  -  |

<a id="getMAMStatuses"></a>
# **getMAMStatuses**
> StatusesDefault getMAMStatuses(hostName, apiVersion)



Returns Intune Tenant level statuses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      StatusesDefault result = apiInstance.getMAMStatuses(hostName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMAMStatuses");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **apiVersion** | **String**| Service Api Version. | |

### Return type

[**StatusesDefault**](StatusesDefault.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | applications as collection response |  -  |
| **0** | unexpected error |  -  |

<a id="getMAMUserDeviceByDeviceName"></a>
# **getMAMUserDeviceByDeviceName**
> Device getMAMUserDeviceByDeviceName(hostName, userName, deviceName, apiVersion, $select)



Get a unique device for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String userName = "userName_example"; // String | unique user name
    String deviceName = "deviceName_example"; // String | device name
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      Device result = apiInstance.getMAMUserDeviceByDeviceName(hostName, userName, deviceName, apiVersion, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMAMUserDeviceByDeviceName");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **userName** | **String**| unique user name | |
| **deviceName** | **String**| device name | |
| **apiVersion** | **String**| Service Api Version. | |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Device entity. |  -  |
| **0** | unexpected error |  -  |

<a id="getMAMUserDevices"></a>
# **getMAMUserDevices**
> DeviceCollection getMAMUserDevices(hostName, userName, apiVersion, $filter, $top, $select)



Get devices for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String userName = "userName_example"; // String | user unique Name
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      DeviceCollection result = apiInstance.getMAMUserDevices(hostName, userName, apiVersion, $filter, $top, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMAMUserDevices");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **userName** | **String**| user unique Name | |
| **apiVersion** | **String**| Service Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**DeviceCollection**](DeviceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | devices as collection response |  -  |
| **0** | unexpected error |  -  |

<a id="getMAMUserFlaggedEnrolledApps"></a>
# **getMAMUserFlaggedEnrolledApps**
> FlaggedEnrolledAppCollection getMAMUserFlaggedEnrolledApps(hostName, userName, apiVersion, $filter, $top, $select)



Returns Intune flagged enrolled app collection for the User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String userName = "userName_example"; // String | User name for the tenant
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      FlaggedEnrolledAppCollection result = apiInstance.getMAMUserFlaggedEnrolledApps(hostName, userName, apiVersion, $filter, $top, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMAMUserFlaggedEnrolledApps");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **userName** | **String**| User name for the tenant | |
| **apiVersion** | **String**| Service Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**FlaggedEnrolledAppCollection**](FlaggedEnrolledAppCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flagged enrolled Apps as collection response |  -  |
| **0** | unexpected error |  -  |

<a id="getOperationResults"></a>
# **getOperationResults**
> OperationResultCollection getOperationResults(hostName, apiVersion, $filter, $top, $select)



Returns operationResults.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      OperationResultCollection result = apiInstance.getOperationResults(hostName, apiVersion, $filter, $top, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getOperationResults");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **apiVersion** | **String**| Service Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**OperationResultCollection**](OperationResultCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | applications as collection response |  -  |
| **0** | unexpected error |  -  |

<a id="iosAddAppForMAMPolicy"></a>
# **iosAddAppForMAMPolicy**
> iosAddAppForMAMPolicy(hostName, policyName, appName, apiVersion, parameters)



Add app to an iOSMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String appName = "appName_example"; // String | application unique Name
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    MAMPolicyAppIdOrGroupIdPayload parameters = new MAMPolicyAppIdOrGroupIdPayload(); // MAMPolicyAppIdOrGroupIdPayload | Parameters supplied to add an app to an ios policy.
    try {
      apiInstance.iosAddAppForMAMPolicy(hostName, policyName, appName, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iosAddAppForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **appName** | **String**| application unique Name | |
| **apiVersion** | **String**| Service Api Version. | |
| **parameters** | [**MAMPolicyAppIdOrGroupIdPayload**](MAMPolicyAppIdOrGroupIdPayload.md)| Parameters supplied to add an app to an ios policy. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No-Content. |  -  |
| **204** | No-Content. |  -  |
| **0** | unexpected error |  -  |

<a id="iosAddGroupForMAMPolicy"></a>
# **iosAddGroupForMAMPolicy**
> iosAddGroupForMAMPolicy(hostName, policyName, groupId, apiVersion, parameters)



Add group to an iOSMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String groupId = "groupId_example"; // String | group Id
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    MAMPolicyAppIdOrGroupIdPayload parameters = new MAMPolicyAppIdOrGroupIdPayload(); // MAMPolicyAppIdOrGroupIdPayload | Parameters supplied to the Create or update app to an android policy operation.
    try {
      apiInstance.iosAddGroupForMAMPolicy(hostName, policyName, groupId, apiVersion, parameters);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iosAddGroupForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **groupId** | **String**| group Id | |
| **apiVersion** | **String**| Service Api Version. | |
| **parameters** | [**MAMPolicyAppIdOrGroupIdPayload**](MAMPolicyAppIdOrGroupIdPayload.md)| Parameters supplied to the Create or update app to an android policy operation. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No-Content. |  -  |
| **204** | No-Content. |  -  |
| **0** | unexpected error |  -  |

<a id="iosCreateOrUpdateMAMPolicy"></a>
# **iosCreateOrUpdateMAMPolicy**
> IOSMAMPolicy iosCreateOrUpdateMAMPolicy(hostName, policyName, apiVersion, parameters)



Creates or updates iOSMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    IOSMAMPolicy parameters = new IOSMAMPolicy(); // IOSMAMPolicy | Parameters supplied to the Create or update an android policy operation.
    try {
      IOSMAMPolicy result = apiInstance.iosCreateOrUpdateMAMPolicy(hostName, policyName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iosCreateOrUpdateMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **apiVersion** | **String**| Service Api Version. | |
| **parameters** | [**IOSMAMPolicy**](IOSMAMPolicy.md)| Parameters supplied to the Create or update an android policy operation. | |

### Return type

[**IOSMAMPolicy**](IOSMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | iOSMAMPolicy entity. |  -  |
| **0** | unexpected error |  -  |

<a id="iosDeleteAppForMAMPolicy"></a>
# **iosDeleteAppForMAMPolicy**
> iosDeleteAppForMAMPolicy(hostName, policyName, appName, apiVersion)



Delete App for Ios Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String appName = "appName_example"; // String | application unique Name
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      apiInstance.iosDeleteAppForMAMPolicy(hostName, policyName, appName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iosDeleteAppForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **appName** | **String**| application unique Name | |
| **apiVersion** | **String**| Service Api Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No-Content. |  -  |
| **204** | No-Content. |  -  |
| **0** | unexpected error |  -  |

<a id="iosDeleteGroupForMAMPolicy"></a>
# **iosDeleteGroupForMAMPolicy**
> iosDeleteGroupForMAMPolicy(hostName, policyName, groupId, apiVersion)



Delete Group for iOS Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String groupId = "groupId_example"; // String | application unique Name
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      apiInstance.iosDeleteGroupForMAMPolicy(hostName, policyName, groupId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iosDeleteGroupForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **groupId** | **String**| application unique Name | |
| **apiVersion** | **String**| Service Api Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No-Content. |  -  |
| **204** | No-Content. |  -  |
| **0** | unexpected error |  -  |

<a id="iosDeleteMAMPolicy"></a>
# **iosDeleteMAMPolicy**
> iosDeleteMAMPolicy(hostName, policyName, apiVersion)



Delete Ios Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      apiInstance.iosDeleteMAMPolicy(hostName, policyName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iosDeleteMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **apiVersion** | **String**| Service Api Version. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No-Content. |  -  |
| **204** | No-Content. |  -  |
| **0** | unexpected error |  -  |

<a id="iosGetAppForMAMPolicy"></a>
# **iosGetAppForMAMPolicy**
> ApplicationCollection iosGetAppForMAMPolicy(hostName, policyName, apiVersion, $filter, $top, $select)



Get apps for an iOSMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      ApplicationCollection result = apiInstance.iosGetAppForMAMPolicy(hostName, policyName, apiVersion, $filter, $top, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iosGetAppForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **apiVersion** | **String**| Service Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**ApplicationCollection**](ApplicationCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | applications as collection response |  -  |
| **0** | unexpected error |  -  |

<a id="iosGetGroupsForMAMPolicy"></a>
# **iosGetGroupsForMAMPolicy**
> GroupsCollection iosGetGroupsForMAMPolicy(hostName, policyName, apiVersion)



Returns groups for a given iOSMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | policy name for the tenant
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      GroupsCollection result = apiInstance.iosGetGroupsForMAMPolicy(hostName, policyName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iosGetGroupsForMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| policy name for the tenant | |
| **apiVersion** | **String**| Service Api Version. | |

### Return type

[**GroupsCollection**](GroupsCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | groups as collection response |  -  |
| **0** | unexpected error |  -  |

<a id="iosGetMAMPolicies"></a>
# **iosGetMAMPolicies**
> IOSMAMPolicyCollection iosGetMAMPolicies(hostName, apiVersion, $filter, $top, $select)



Returns Intune iOSPolicies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    Integer $top = 56; // Integer | 
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      IOSMAMPolicyCollection result = apiInstance.iosGetMAMPolicies(hostName, apiVersion, $filter, $top, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iosGetMAMPolicies");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **apiVersion** | **String**| Service Api Version. | |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |
| **$top** | **Integer**|  | [optional] |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**IOSMAMPolicyCollection**](IOSMAMPolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | applications as collection response |  -  |
| **0** | unexpected error |  -  |

<a id="iosGetMAMPolicyByName"></a>
# **iosGetMAMPolicyByName**
> IOSMAMPolicy iosGetMAMPolicyByName(hostName, policyName, apiVersion, $select)



Returns Intune iOS policies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    String $select = "$select_example"; // String | select specific fields in entity.
    try {
      IOSMAMPolicy result = apiInstance.iosGetMAMPolicyByName(hostName, policyName, apiVersion, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iosGetMAMPolicyByName");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **apiVersion** | **String**| Service Api Version. | |
| **$select** | **String**| select specific fields in entity. | [optional] |

### Return type

[**IOSMAMPolicy**](IOSMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | iOSMAMPolicy entity. |  -  |
| **0** | unexpected error |  -  |

<a id="iosPatchMAMPolicy"></a>
# **iosPatchMAMPolicy**
> IOSMAMPolicy iosPatchMAMPolicy(hostName, policyName, apiVersion, parameters)



 patch an iOSMAMPolicy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String policyName = "policyName_example"; // String | Unique name for the policy
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    IOSMAMPolicy parameters = new IOSMAMPolicy(); // IOSMAMPolicy | Parameters supplied to the Create or update an android policy operation.
    try {
      IOSMAMPolicy result = apiInstance.iosPatchMAMPolicy(hostName, policyName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#iosPatchMAMPolicy");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **policyName** | **String**| Unique name for the policy | |
| **apiVersion** | **String**| Service Api Version. | |
| **parameters** | [**IOSMAMPolicy**](IOSMAMPolicy.md)| Parameters supplied to the Create or update an android policy operation. | |

### Return type

[**IOSMAMPolicy**](IOSMAMPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | iOSMAMPolicy entity. |  -  |
| **0** | unexpected error |  -  |

<a id="wipeMAMUserDevice"></a>
# **wipeMAMUserDevice**
> WipeDeviceOperationResult wipeMAMUserDevice(hostName, userName, deviceName, apiVersion)



Wipe a device for a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hostName = "hostName_example"; // String | Location hostName for the tenant
    String userName = "userName_example"; // String | unique user name
    String deviceName = "deviceName_example"; // String | device name
    String apiVersion = "apiVersion_example"; // String | Service Api Version.
    try {
      WipeDeviceOperationResult result = apiInstance.wipeMAMUserDevice(hostName, userName, deviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#wipeMAMUserDevice");
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
| **hostName** | **String**| Location hostName for the tenant | |
| **userName** | **String**| unique user name | |
| **deviceName** | **String**| device name | |
| **apiVersion** | **String**| Service Api Version. | |

### Return type

[**WipeDeviceOperationResult**](WipeDeviceOperationResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Wipe operation result. |  -  |
| **0** | unexpected error |  -  |

