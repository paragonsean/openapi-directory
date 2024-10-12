# BackupSchedulesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**backupSchedulesCreateOrUpdate**](BackupSchedulesApi.md#backupSchedulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupPolicies/{backupPolicyName}/schedules/{backupScheduleName} |  |
| [**backupSchedulesDelete**](BackupSchedulesApi.md#backupSchedulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupPolicies/{backupPolicyName}/schedules/{backupScheduleName} |  |
| [**backupSchedulesGet**](BackupSchedulesApi.md#backupSchedulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupPolicies/{backupPolicyName}/schedules/{backupScheduleName} |  |
| [**backupSchedulesListByBackupPolicy**](BackupSchedulesApi.md#backupSchedulesListByBackupPolicy) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/devices/{deviceName}/backupPolicies/{backupPolicyName}/schedules |  |


<a id="backupSchedulesCreateOrUpdate"></a>
# **backupSchedulesCreateOrUpdate**
> BackupSchedule backupSchedulesCreateOrUpdate(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters)



Creates or updates the backup schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupSchedulesApi apiInstance = new BackupSchedulesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name
    String backupPolicyName = "backupPolicyName_example"; // String | The backup policy name.
    String backupScheduleName = "backupScheduleName_example"; // String | The backup schedule name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    BackupSchedule parameters = new BackupSchedule(); // BackupSchedule | The backup schedule.
    try {
      BackupSchedule result = apiInstance.backupSchedulesCreateOrUpdate(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupSchedulesApi#backupSchedulesCreateOrUpdate");
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
| **deviceName** | **String**| The device name | |
| **backupPolicyName** | **String**| The backup policy name. | |
| **backupScheduleName** | **String**| The backup schedule name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |
| **parameters** | [**BackupSchedule**](BackupSchedule.md)| The backup schedule. | |

### Return type

[**BackupSchedule**](BackupSchedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully created or updated the backup schedule. |  -  |
| **202** | Accepted the request to create or update the backup schedule. |  -  |

<a id="backupSchedulesDelete"></a>
# **backupSchedulesDelete**
> backupSchedulesDelete(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the backup schedule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupSchedulesApi apiInstance = new BackupSchedulesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name
    String backupPolicyName = "backupPolicyName_example"; // String | The backup policy name.
    String backupScheduleName = "backupScheduleName_example"; // String | The name the backup schedule.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      apiInstance.backupSchedulesDelete(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupSchedulesApi#backupSchedulesDelete");
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
| **deviceName** | **String**| The device name | |
| **backupPolicyName** | **String**| The backup policy name. | |
| **backupScheduleName** | **String**| The name the backup schedule. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted the request to delete the backup schedule. |  -  |
| **204** | Successfully deleted the backup schedule. |  -  |

<a id="backupSchedulesGet"></a>
# **backupSchedulesGet**
> BackupSchedule backupSchedulesGet(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion)



Gets the properties of the specified backup schedule name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupSchedulesApi apiInstance = new BackupSchedulesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name
    String backupPolicyName = "backupPolicyName_example"; // String | The backup policy name.
    String backupScheduleName = "backupScheduleName_example"; // String | The name of the backup schedule to be fetched
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      BackupSchedule result = apiInstance.backupSchedulesGet(deviceName, backupPolicyName, backupScheduleName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupSchedulesApi#backupSchedulesGet");
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
| **deviceName** | **String**| The device name | |
| **backupPolicyName** | **String**| The backup policy name. | |
| **backupScheduleName** | **String**| The name of the backup schedule to be fetched | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**BackupSchedule**](BackupSchedule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The backup schedule. |  -  |

<a id="backupSchedulesListByBackupPolicy"></a>
# **backupSchedulesListByBackupPolicy**
> BackupScheduleList backupSchedulesListByBackupPolicy(deviceName, backupPolicyName, subscriptionId, resourceGroupName, managerName, apiVersion)



Gets all the backup schedules in a backup policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BackupSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BackupSchedulesApi apiInstance = new BackupSchedulesApi(defaultClient);
    String deviceName = "deviceName_example"; // String | The device name
    String backupPolicyName = "backupPolicyName_example"; // String | The backup policy name.
    String subscriptionId = "subscriptionId_example"; // String | The subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name
    String managerName = "managerName_example"; // String | The manager name
    String apiVersion = "apiVersion_example"; // String | The api version
    try {
      BackupScheduleList result = apiInstance.backupSchedulesListByBackupPolicy(deviceName, backupPolicyName, subscriptionId, resourceGroupName, managerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BackupSchedulesApi#backupSchedulesListByBackupPolicy");
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
| **deviceName** | **String**| The device name | |
| **backupPolicyName** | **String**| The backup policy name. | |
| **subscriptionId** | **String**| The subscription id | |
| **resourceGroupName** | **String**| The resource group name | |
| **managerName** | **String**| The manager name | |
| **apiVersion** | **String**| The api version | |

### Return type

[**BackupScheduleList**](BackupScheduleList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The collection of backup schedules. |  -  |

