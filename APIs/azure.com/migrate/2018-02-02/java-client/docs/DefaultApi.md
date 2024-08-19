# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**assessedMachinesGet**](DefaultApi.md#assessedMachinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName}/assessedMachines/{assessedMachineName} | Get an assessed machine. |
| [**assessedMachinesListByAssessment**](DefaultApi.md#assessedMachinesListByAssessment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName}/assessedMachines | Get assessed machines for assessment. |
| [**assessmentOptionsGet**](DefaultApi.md#assessmentOptionsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Migrate/locations/{locationName}/assessmentOptions | Get the assessment options. |
| [**assessmentsCreate**](DefaultApi.md#assessmentsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Create or Update assessment. |
| [**assessmentsDelete**](DefaultApi.md#assessmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Deletes an assessment from the project. |
| [**assessmentsGet**](DefaultApi.md#assessmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName} | Get an assessment. |
| [**assessmentsGetReportDownloadUrl**](DefaultApi.md#assessmentsGetReportDownloadUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments/{assessmentName}/downloadUrl | Get download URL for the assessment report. |
| [**assessmentsListByGroup**](DefaultApi.md#assessmentsListByGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName}/assessments | Get all assessments created for the specified group. |
| [**assessmentsListByProject**](DefaultApi.md#assessmentsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/assessments | Get all assessments created in the project. |
| [**groupsCreate**](DefaultApi.md#groupsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName} | Create a new group with specified settings. If group with the name provided already exists, then the existing group is updated. |
| [**groupsDelete**](DefaultApi.md#groupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName} | Delete the group |
| [**groupsGet**](DefaultApi.md#groupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups/{groupName} | Get a specific group. |
| [**groupsListByProject**](DefaultApi.md#groupsListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/groups | Get all groups |
| [**locationCheckNameAvailability**](DefaultApi.md#locationCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Migrate/locations/{locationName}/checkNameAvailability |  |
| [**machinesGet**](DefaultApi.md#machinesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/machines/{machineName} | Get a specific machine. |
| [**machinesListByProject**](DefaultApi.md#machinesListByProject) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/machines | Get all machines in the project |
| [**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.Migrate/operations | Get list of operations supported in the API. |
| [**projectsCreate**](DefaultApi.md#projectsCreate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName} | Create or update project. |
| [**projectsDelete**](DefaultApi.md#projectsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName} | Delete the project |
| [**projectsGet**](DefaultApi.md#projectsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName} | Get the specified project. |
| [**projectsGetKeys**](DefaultApi.md#projectsGetKeys) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName}/keys | Get shared keys for the project. |
| [**projectsListByResourceGroup**](DefaultApi.md#projectsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects | Get all projects. |
| [**projectsListBySubscription**](DefaultApi.md#projectsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Migrate/projects | Get all projects. |
| [**projectsUpdate**](DefaultApi.md#projectsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Migrate/projects/{projectName} | Update project. |


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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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

<a id="assessmentOptionsGet"></a>
# **assessmentOptionsGet**
> AssessmentOptionsResultList assessmentOptionsGet(subscriptionId, locationName, apiVersion, acceptLanguage)

Get the assessment options.

Get the available options for the properties of an assessment.

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
    String locationName = "locationName_example"; // String | Azure region in which the project is created.
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      AssessmentOptionsResultList result = apiInstance.assessmentOptionsGet(subscriptionId, locationName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#assessmentOptionsGet");
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
| **locationName** | **String**| Azure region in which the project is created. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
| **200** | OK. Returns assessment options. |  -  |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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

Create a new group with specified settings. If group with the name provided already exists, then the existing group is updated.

Create a new group by sending a json object of type &#39;group&#39; as given in Models section as part of the Request Body. The group name in a project is unique. Labels can be applied on a group as part of creation.  If a group with the groupName specified in the URL already exists, then this call acts as an update.  This operation is Idempotent. 

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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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

<a id="locationCheckNameAvailability"></a>
# **locationCheckNameAvailability**
> CheckNameAvailabilityResult locationCheckNameAvailability(locationName, apiVersion, subscriptionId, parameters)



Checks whether the project name is available in the specified region.

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
    String locationName = "locationName_example"; // String | The desired region for the name check.
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription Id in which project was created.
    CheckNameAvailabilityParameters parameters = new CheckNameAvailabilityParameters(); // CheckNameAvailabilityParameters | Properties needed to check the availability of a name.
    try {
      CheckNameAvailabilityResult result = apiInstance.locationCheckNameAvailability(locationName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#locationCheckNameAvailability");
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
| **locationName** | **String**| The desired region for the name check. | |
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
| **subscriptionId** | **String**| Azure Subscription Id in which project was created. | |
| **parameters** | [**CheckNameAvailabilityParameters**](CheckNameAvailabilityParameters.md)| Properties needed to check the availability of a name. | |

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Returns details about whether a project name is available. |  -  |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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

<a id="projectsGetKeys"></a>
# **projectsGetKeys**
> ProjectKey projectsGetKeys(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage)

Get shared keys for the project.

Gets the Log Analytics Workspace ID and Primary Key for the specified project.

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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      ProjectKey result = apiInstance.projectsGetKeys(subscriptionId, resourceGroupName, projectName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectsGetKeys");
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
| **acceptLanguage** | **String**| Standard request header. Used by service to respond to client in appropriate language. | [optional] |

### Return type

[**ProjectKey**](ProjectKey.md)

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

<a id="projectsListByResourceGroup"></a>
# **projectsListByResourceGroup**
> ProjectResultList projectsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, acceptLanguage)

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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
    String acceptLanguage = "acceptLanguage_example"; // String | Standard request header. Used by service to respond to client in appropriate language.
    try {
      ProjectResultList result = apiInstance.projectsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#projectsListByResourceGroup");
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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
    String apiVersion = "2018-02-02"; // String | Standard request header. Used by service to identify API version used by client.
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
| **apiVersion** | **String**| Standard request header. Used by service to identify API version used by client. | [enum: 2018-02-02] |
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

