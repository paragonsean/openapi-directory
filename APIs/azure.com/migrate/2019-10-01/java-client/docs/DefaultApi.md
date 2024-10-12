# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assessedMachinesGet**](DefaultApi.md#assessedMachinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName}/assessedMachines/{assessedMachineName} | Get an assessed machine. |
| [**assessedMachinesListByAssessment**](DefaultApi.md#assessedMachinesListByAssessment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName}/assessedMachines | Get assessed machines for assessment. |
| [**assessmentsCreate**](DefaultApi.md#assessmentsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Create or Update assessment. |
| [**assessmentsDelete**](DefaultApi.md#assessmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Deletes an assessment from the project. |
| [**assessmentsGet**](DefaultApi.md#assessmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Get an assessment. |
| [**assessmentsGetReportDownloadUrl**](DefaultApi.md#assessmentsGetReportDownloadUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments/{assessmentName}/downloadUrl | Get download URL for the assessment report. |
| [**assessmentsListByGroup**](DefaultApi.md#assessmentsListByGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/assessments | Get all assessments created for the specified group. |
| [**assessmentsListByProject**](DefaultApi.md#assessmentsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/assessments | Get all assessments created in the project. |
| [**groupsCreate**](DefaultApi.md#groupsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName} | Create a new group with specified settings. |
| [**groupsDelete**](DefaultApi.md#groupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName} | Delete the group |
| [**groupsGet**](DefaultApi.md#groupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName} | Get a specific group. |
| [**groupsListByProject**](DefaultApi.md#groupsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups | Get all groups |
| [**groupsUpdateMachines**](DefaultApi.md#groupsUpdateMachines) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/groups/{groupName}/updateMachines | Update machines in group. |
| [**hyperVCollectorsCreate**](DefaultApi.md#hyperVCollectorsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/hypervcollectors/{hyperVCollectorName} | Create or Update Hyper-V collector. |
| [**hyperVCollectorsDelete**](DefaultApi.md#hyperVCollectorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/hypervcollectors/{hyperVCollectorName} | Deletes Hyper-V collector from the project. |
| [**hyperVCollectorsGet**](DefaultApi.md#hyperVCollectorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/hypervcollectors/{hyperVCollectorName} | Get a Hyper-V collector. |
| [**hyperVCollectorsListByProject**](DefaultApi.md#hyperVCollectorsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/hypervcollectors | Get a list of Hyper-V collector. |
| [**machinesGet**](DefaultApi.md#machinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/machines/{machineName} | Get a specific machine. |
| [**machinesListByProject**](DefaultApi.md#machinesListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/machines | Get all machines in the project |
| [**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.Migrate/operations | Get list of operations supported in the API. |
| [**projectAssessmentOptions**](DefaultApi.md#projectAssessmentOptions) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/assessmentOptions/{assessmentOptionsName} | Get all available options for the properties of an assessment on a project. |
| [**projectAssessmentOptionsList**](DefaultApi.md#projectAssessmentOptionsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/assessmentOptions | Gets list of all available options for the properties of an assessment on a project. |
| [**projectsCreate**](DefaultApi.md#projectsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName} | Create or update project. |
| [**projectsDelete**](DefaultApi.md#projectsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName} | Delete the project |
| [**projectsGet**](DefaultApi.md#projectsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName} | Get the specified project. |
| [**projectsList**](DefaultApi.md#projectsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects | Get all projects. |
| [**projectsListBySubscription**](DefaultApi.md#projectsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Migrate/assessmentProjects | Get all projects. |
| [**projectsUpdate**](DefaultApi.md#projectsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName} | Update project. |
| [**vMwareCollectorsCreate**](DefaultApi.md#vMwareCollectorsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/vmwarecollectors/{vmWareCollectorName} | Create or Update VMware collector. |
| [**vMwareCollectorsDelete**](DefaultApi.md#vMwareCollectorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/vmwarecollectors/{vmWareCollectorName} | Deletes VMware collector from the project. |
| [**vMwareCollectorsGet**](DefaultApi.md#vMwareCollectorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/vmwarecollectors/{vmWareCollectorName} | Get a VMware collector. |
| [**vMwareCollectorsListByProject**](DefaultApi.md#vMwareCollectorsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}/vmwarecollectors | Get a list of VMware collector. |


<a id="assessedMachinesGet"></a>
# **assessedMachinesGet**
> AssessedMachine assessedMachinesGet(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, assessedMachineName, apiVersion, acceptLanguage)

Get an assessed machine.

Get an assessed machine with its size &amp; cost estimate that was evaluated in the specified assessment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String groupName = "groupName_example"; // String | Unique name of a group within a project.
    String assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
    String assessedMachineName = "assessedMachineName_example"; // String | Unique name of an assessed machine evaluated as part of an assessment.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      AssessedMachine result = apiInstance.assessedMachinesGet(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, assessedMachineName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assessedMachinesGet");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **groupName** | **String**| Unique name of a group within a project. | |
| **assessmentName** | **String**| Unique name of an assessment within a project. | |
| **assessedMachineName** | **String**| Unique name of an assessed machine evaluated as part of an assessment. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**AssessedMachine**](AssessedMachine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns a specific assessed machine. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessedMachinesListByAssessment"></a>
# **assessedMachinesListByAssessment**
> AssessedMachineResultList assessedMachinesListByAssessment(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, acceptLanguage)

Get assessed machines for assessment.

Get list of machines that assessed as part of the specified assessment. Returns a json array of objects of type &#39;assessedMachine&#39; as specified in the Models section.  Whenever an assessment is created or updated, it goes under computation. During this phase, the &#39;status&#39; field of Assessment object reports &#39;Computing&#39;. During the period when the assessment is under computation, the list of assessed machines is empty and no assessed machines are returned by this call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String groupName = "groupName_example"; // String | Unique name of a group within a project.
    String assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      AssessedMachineResultList result = apiInstance.assessedMachinesListByAssessment(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assessedMachinesListByAssessment");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **groupName** | **String**| Unique name of a group within a project. | |
| **assessmentName** | **String**| Unique name of an assessment within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**AssessedMachineResultList**](AssessedMachineResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of machines with their assessment data in the assessment. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessmentsCreate"></a>
# **assessmentsCreate**
> Assessment assessmentsCreate(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, acceptLanguage, assessment)

Create or Update assessment.

Create a new assessment with the given name and the specified settings. Since name of an assessment in a project is a unique identifier, if an assessment with the name provided already exists, then the existing assessment is updated.  Any PUT operation, resulting in either create or update on an assessment, will cause the assessment to go in a \&quot;InProgress\&quot; state. This will be indicated by the field &#39;computationState&#39; on the Assessment object. During this time no other PUT operation will be allowed on that assessment object, nor will a Delete operation. Once the computation for the assessment is complete, the field &#39;computationState&#39; will be updated to &#39;Ready&#39;, and then other PUT or DELETE operations can happen on the assessment.  When assessment is under computation, any PUT will lead to a 400 - Bad Request error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String groupName = "groupName_example"; // String | Unique name of a group within a project.
    String assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    Assessment assessment = new Assessment(); // Assessment | New or Updated Assessment object.
    try {
      Assessment result = apiInstance.assessmentsCreate(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, acceptLanguage, assessment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assessmentsCreate");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **groupName** | **String**| Unique name of a group within a project. | |
| **assessmentName** | **String**| Unique name of an assessment within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |
| **assessment** | [**Assessment**](Assessment.md)| New or Updated Assessment object. | [optional] |

### Return type

[**Assessment**](Assessment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Existing assessment updated. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **201** | Created. New assessment was created. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessmentsDelete"></a>
# **assessmentsDelete**
> assessmentsDelete(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, acceptLanguage)

Deletes an assessment from the project.

Delete an assessment from the project. The machines remain in the assessment. Deleting a non-existent assessment results in a no-operation.  When an assessment is under computation, as indicated by the &#39;computationState&#39; field, it cannot be deleted. Any such attempt will return a 400 - Bad Request. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String groupName = "groupName_example"; // String | Unique name of a group within a project.
    String assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      apiInstance.assessmentsDelete(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, acceptLanguage);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assessmentsDelete");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **groupName** | **String**| Unique name of a group within a project. | |
| **assessmentName** | **String**| Unique name of an assessment within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Deleted the assessment. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **204** | No content. No assessment with specified name was found. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessmentsGet"></a>
# **assessmentsGet**
> Assessment assessmentsGet(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, acceptLanguage)

Get an assessment.

Get an existing assessment with the specified name. Returns a json object of type &#39;assessment&#39; as specified in Models section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String groupName = "groupName_example"; // String | Unique name of a group within a project.
    String assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      Assessment result = apiInstance.assessmentsGet(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assessmentsGet");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **groupName** | **String**| Unique name of a group within a project. | |
| **assessmentName** | **String**| Unique name of an assessment within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**Assessment**](Assessment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns Assessment object. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessmentsGetReportDownloadUrl"></a>
# **assessmentsGetReportDownloadUrl**
> DownloadUrl assessmentsGetReportDownloadUrl(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, acceptLanguage)

Get download URL for the assessment report.

Get the URL for downloading the assessment in a report format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String groupName = "groupName_example"; // String | Unique name of a group within a project.
    String assessmentName = "assessmentName_example"; // String | Unique name of an assessment within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      DownloadUrl result = apiInstance.assessmentsGetReportDownloadUrl(subscriptionId, resourceGroupName, projectName, groupName, assessmentName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assessmentsGetReportDownloadUrl");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **groupName** | **String**| Unique name of a group within a project. | |
| **assessmentName** | **String**| Unique name of an assessment within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**DownloadUrl**](DownloadUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessmentsListByGroup"></a>
# **assessmentsListByGroup**
> AssessmentResultList assessmentsListByGroup(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, acceptLanguage)

Get all assessments created for the specified group.

Get all assessments created for the specified group.  Returns a json array of objects of type &#39;assessment&#39; as specified in Models section. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String groupName = "groupName_example"; // String | Unique name of a group within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      AssessmentResultList result = apiInstance.assessmentsListByGroup(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assessmentsListByGroup");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **groupName** | **String**| Unique name of a group within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**AssessmentResultList**](AssessmentResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of Assessment objects. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="assessmentsListByProject"></a>
# **assessmentsListByProject**
> AssessmentResultList assessmentsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage)

Get all assessments created in the project.

Get all assessments created in the project.  Returns a json array of objects of type &#39;assessment&#39; as specified in Models section. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      AssessmentResultList result = apiInstance.assessmentsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assessmentsListByProject");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**AssessmentResultList**](AssessmentResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of Assessment objects. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsCreate"></a>
# **groupsCreate**
> Group groupsCreate(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, acceptLanguage, group)

Create a new group with specified settings.

Create a new group by sending a json object of type &#39;group&#39; as given in Models section as part of the Request Body. The group name in a project is unique.  This operation is Idempotent. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String groupName = "groupName_example"; // String | Unique name of a group within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    Group group = new Group(); // Group | New or Updated Group object.
    try {
      Group result = apiInstance.groupsCreate(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, acceptLanguage, group);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#groupsCreate");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **groupName** | **String**| Unique name of a group within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |
| **group** | [**Group**](Group.md)| New or Updated Group object. | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Existing group updated. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **201** | Created. New group was created. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsDelete"></a>
# **groupsDelete**
> groupsDelete(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, acceptLanguage)

Delete the group

Delete the group from the project. The machines remain in the project. Deleting a non-existent group results in a no-operation.  A group is an aggregation mechanism for machines in a project. Therefore, deleting group does not delete machines in it. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String groupName = "groupName_example"; // String | Unique name of a group within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      apiInstance.groupsDelete(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, acceptLanguage);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#groupsDelete");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **groupName** | **String**| Unique name of a group within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Deleted the group. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **204** | No content. No group with specified name was found. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsGet"></a>
# **groupsGet**
> Group groupsGet(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, acceptLanguage)

Get a specific group.

Get information related to a specific group in the project. Returns a json object of type &#39;group&#39; as specified in the models section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String groupName = "groupName_example"; // String | Unique name of a group within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      Group result = apiInstance.groupsGet(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#groupsGet");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **groupName** | **String**| Unique name of a group within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns the group with the specified name. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsListByProject"></a>
# **groupsListByProject**
> GroupResultList groupsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage)

Get all groups

Get all groups created in the project. Returns a json array of objects of type &#39;group&#39; as specified in the Models section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      GroupResultList result = apiInstance.groupsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#groupsListByProject");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**GroupResultList**](GroupResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of groups. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="groupsUpdateMachines"></a>
# **groupsUpdateMachines**
> Group groupsUpdateMachines(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, acceptLanguage, groupUpdateProperties)

Update machines in group.

Update machines in group by adding or removing machines.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String groupName = "groupName_example"; // String | Unique name of a group within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    UpdateGroupBody groupUpdateProperties = new UpdateGroupBody(); // UpdateGroupBody | Machines list to be added or removed from group.
    try {
      Group result = apiInstance.groupsUpdateMachines(subscriptionId, resourceGroupName, projectName, groupName, apiVersion, acceptLanguage, groupUpdateProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#groupsUpdateMachines");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **groupName** | **String**| Unique name of a group within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |
| **groupUpdateProperties** | [**UpdateGroupBody**](UpdateGroupBody.md)| Machines list to be added or removed from group. | [optional] |

### Return type

[**Group**](Group.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Existing group updated. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hyperVCollectorsCreate"></a>
# **hyperVCollectorsCreate**
> HyperVCollector hyperVCollectorsCreate(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, acceptLanguage, collectorBody)

Create or Update Hyper-V collector.

Create or Update Hyper-V collector

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String hyperVCollectorName = "hyperVCollectorName_example"; // String | Unique name of a Hyper-V collector within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    HyperVCollector collectorBody = new HyperVCollector(); // HyperVCollector | New or Updated Hyper-V collector.
    try {
      HyperVCollector result = apiInstance.hyperVCollectorsCreate(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, acceptLanguage, collectorBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hyperVCollectorsCreate");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **hyperVCollectorName** | **String**| Unique name of a Hyper-V collector within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |
| **collectorBody** | [**HyperVCollector**](HyperVCollector.md)| New or Updated Hyper-V collector. | [optional] |

### Return type

[**HyperVCollector**](HyperVCollector.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Existing Hyper-V collector. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **201** | Created. New Hyper-V collector was created. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hyperVCollectorsDelete"></a>
# **hyperVCollectorsDelete**
> hyperVCollectorsDelete(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, acceptLanguage)

Deletes Hyper-V collector from the project.

Delete a Hyper-V collector from the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String hyperVCollectorName = "hyperVCollectorName_example"; // String | Unique name of a Hyper-V collector within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      apiInstance.hyperVCollectorsDelete(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, acceptLanguage);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hyperVCollectorsDelete");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **hyperVCollectorName** | **String**| Unique name of a Hyper-V collector within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Deleted the Hyper-V collector. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **204** | No content. No Hyper-V collector with specified name was found. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hyperVCollectorsGet"></a>
# **hyperVCollectorsGet**
> HyperVCollector hyperVCollectorsGet(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, acceptLanguage)

Get a Hyper-V collector.

Get a Hyper-V collector.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String hyperVCollectorName = "hyperVCollectorName_example"; // String | Unique name of a Hyper-V collector within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      HyperVCollector result = apiInstance.hyperVCollectorsGet(subscriptionId, resourceGroupName, projectName, hyperVCollectorName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hyperVCollectorsGet");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **hyperVCollectorName** | **String**| Unique name of a Hyper-V collector within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**HyperVCollector**](HyperVCollector.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns the specific Hyper-V collector. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="hyperVCollectorsListByProject"></a>
# **hyperVCollectorsListByProject**
> HyperVCollectorList hyperVCollectorsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage)

Get a list of Hyper-V collector.

Get a list of Hyper-V collector.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      HyperVCollectorList result = apiInstance.hyperVCollectorsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#hyperVCollectorsListByProject");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**HyperVCollectorList**](HyperVCollectorList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of Hyper-V collectors. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="machinesGet"></a>
# **machinesGet**
> Machine machinesGet(subscriptionId, resourceGroupName, projectName, machineName, apiVersion, acceptLanguage)

Get a specific machine.

Get the machine with the specified name. Returns a json object of type &#39;machine&#39; defined in Models section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String machineName = "machineName_example"; // String | Unique name of a machine in private datacenter.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      Machine result = apiInstance.machinesGet(subscriptionId, resourceGroupName, projectName, machineName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#machinesGet");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **machineName** | **String**| Unique name of a machine in private datacenter. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**Machine**](Machine.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns the machine with the specified name. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="machinesListByProject"></a>
# **machinesListByProject**
> MachineResultList machinesListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage)

Get all machines in the project

Get data of all the machines available in the project. Returns a json array of objects of type &#39;machine&#39; defined in Models section.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      MachineResultList result = apiInstance.machinesListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#machinesListByProject");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**MachineResultList**](MachineResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of all machine objects. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="operationsList"></a>
# **operationsList**
> OperationResultList operationsList()

Get list of operations supported in the API.

Get a list of REST API supported by Microsoft.Migrate provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      OperationResultList result = apiInstance.operationsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#operationsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OperationResultList**](OperationResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of operations. |  -  |

<a id="projectAssessmentOptions"></a>
# **projectAssessmentOptions**
> AssessmentOptions projectAssessmentOptions(subscriptionId, resourceGroupName, projectName, assessmentOptionsName, apiVersion, acceptLanguage)

Get all available options for the properties of an assessment on a project.

Get all available options for the properties of an assessment on a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String assessmentOptionsName = "assessmentOptionsName_example"; // String | Name of the assessment options. The only name accepted in default.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      AssessmentOptions result = apiInstance.projectAssessmentOptions(subscriptionId, resourceGroupName, projectName, assessmentOptionsName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectAssessmentOptions");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **assessmentOptionsName** | **String**| Name of the assessment options. The only name accepted in default. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**AssessmentOptions**](AssessmentOptions.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="projectAssessmentOptionsList"></a>
# **projectAssessmentOptionsList**
> AssessmentOptionsResultList projectAssessmentOptionsList(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage)

Gets list of all available options for the properties of an assessment on a project.

Gets list of all available options for the properties of an assessment on a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      AssessmentOptionsResultList result = apiInstance.projectAssessmentOptionsList(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectAssessmentOptionsList");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**AssessmentOptionsResultList**](AssessmentOptionsResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="projectsCreate"></a>
# **projectsCreate**
> Project projectsCreate(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage, project)

Create or update project.

Create a project with specified name. If a project already exists, update it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    Project project = new Project(); // Project | New or Updated project object.
    try {
      Project result = apiInstance.projectsCreate(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage, project);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectsCreate");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |
| **project** | [**Project**](Project.md)| New or Updated project object. | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Existing project updated. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **201** | Created. New project was created. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="projectsDelete"></a>
# **projectsDelete**
> projectsDelete(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage)

Delete the project

Delete the project. Deleting non-existent project is a no-operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      apiInstance.projectsDelete(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectsDelete");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Deleted the group. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **204** | No content. No project with specified name was found. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="projectsGet"></a>
# **projectsGet**
> Project projectsGet(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage)

Get the specified project.

Get the project with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      Project result = apiInstance.projectsGet(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectsGet");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="projectsList"></a>
# **projectsList**
> ProjectResultList projectsList(subscriptionId, resourceGroupName, apiVersion, acceptLanguage)

Get all projects.

Get all the projects in the resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      ProjectResultList result = apiInstance.projectsList(subscriptionId, resourceGroupName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectsList");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**ProjectResultList**](ProjectResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="projectsListBySubscription"></a>
# **projectsListBySubscription**
> ProjectResultList projectsListBySubscription(subscriptionId, apiVersion, acceptLanguage)

Get all projects.

Get all the projects in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      ProjectResultList result = apiInstance.projectsListBySubscription(subscriptionId, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectsListBySubscription");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**ProjectResultList**](ProjectResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="projectsUpdate"></a>
# **projectsUpdate**
> Project projectsUpdate(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage, project)

Update project.

Update a project with specified name. Supports partial updates, for example only tags can be provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    Project project = new Project(); // Project | Updated project object.
    try {
      Project result = apiInstance.projectsUpdate(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage, project);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectsUpdate");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |
| **project** | [**Project**](Project.md)| Updated project object. | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Existing project updated. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="vMwareCollectorsCreate"></a>
# **vMwareCollectorsCreate**
> VMwareCollector vMwareCollectorsCreate(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, acceptLanguage, collectorBody)

Create or Update VMware collector.

Create or Update VMware collector

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String vmWareCollectorName = "vmWareCollectorName_example"; // String | Unique name of a VMware collector within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    VMwareCollector collectorBody = new VMwareCollector(); // VMwareCollector | New or Updated VMware collector.
    try {
      VMwareCollector result = apiInstance.vMwareCollectorsCreate(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, acceptLanguage, collectorBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vMwareCollectorsCreate");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **vmWareCollectorName** | **String**| Unique name of a VMware collector within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |
| **collectorBody** | [**VMwareCollector**](VMwareCollector.md)| New or Updated VMware collector. | [optional] |

### Return type

[**VMwareCollector**](VMwareCollector.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Existing VMware collector. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **201** | Created. New VMware collector was created. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="vMwareCollectorsDelete"></a>
# **vMwareCollectorsDelete**
> vMwareCollectorsDelete(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, acceptLanguage)

Deletes VMware collector from the project.

Delete a VMware collector from the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String vmWareCollectorName = "vmWareCollectorName_example"; // String | Unique name of a VMware collector within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      apiInstance.vMwareCollectorsDelete(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, acceptLanguage);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vMwareCollectorsDelete");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **vmWareCollectorName** | **String**| Unique name of a VMware collector within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Deleted the VMware collector. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **204** | No content. No VMware collector with specified name was found. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="vMwareCollectorsGet"></a>
# **vMwareCollectorsGet**
> VMwareCollector vMwareCollectorsGet(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, acceptLanguage)

Get a VMware collector.

Get a VMware collector.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String vmWareCollectorName = "vmWareCollectorName_example"; // String | Unique name of a VMware collector within a project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      VMwareCollector result = apiInstance.vMwareCollectorsGet(subscriptionId, resourceGroupName, projectName, vmWareCollectorName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vMwareCollectorsGet");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **vmWareCollectorName** | **String**| Unique name of a VMware collector within a project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**VMwareCollector**](VMwareCollector.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns the specific VMware collector. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="vMwareCollectorsListByProject"></a>
# **vMwareCollectorsListByProject**
> VMwareCollectorList vMwareCollectorsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage)

Get a list of VMware collector.

Get a list of VMware collector.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Azure Resource Group that project is part of.
    String projectName = "projectName_example"; // String | Name of the Azure Migrate project.
    String apiVersion = "2019-10-01"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      VMwareCollectorList result = apiInstance.vMwareCollectorsListByProject(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#vMwareCollectorsListByProject");
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
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **resourceGroupName** | **String**| Name of the Azure Resource Group that project is part of. | |
| **projectName** | **String**| Name of the Azure Migrate project. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2019-10-01] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**VMwareCollectorList**](VMwareCollectorList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns list of VMware collectors. |  * x-ms-request-id - Service generated Request ID. <br>  |
| **0** | Error response describing why the operation failed. |  -  |

