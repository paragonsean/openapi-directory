# ProjectsApi

All URIs are relative to *http://learnifier.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extprojectGet**](ProjectsApi.md#extprojectGet) | **GET** /extproject | Gets Organization Unit by external id |
| [**orgunitsOrgidProjectsGet**](ProjectsApi.md#orgunitsOrgidProjectsGet) | **GET** /orgunits/{orgid}/projects | Organization Unit Projects |
| [**orgunitsOrgidProjectsPost**](ProjectsApi.md#orgunitsOrgidProjectsPost) | **POST** /orgunits/{orgid}/projects | Create project |
| [**orgunitsOrgidProjectsProjectidDelete**](ProjectsApi.md#orgunitsOrgidProjectsProjectidDelete) | **DELETE** /orgunits/{orgid}/projects/{projectid} | Deletes the project |
| [**orgunitsOrgidProjectsProjectidGet**](ProjectsApi.md#orgunitsOrgidProjectsProjectidGet) | **GET** /orgunits/{orgid}/projects/{projectid} | Project information |
| [**orgunitsOrgidProjectsProjectidParticipantsGet**](ProjectsApi.md#orgunitsOrgidProjectsProjectidParticipantsGet) | **GET** /orgunits/{orgid}/projects/{projectid}/participants | Project participants |
| [**orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost**](ProjectsApi.md#orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost) | **POST** /orgunits/{orgid}/projects/{projectid}/participants/${participantId}/activate | Activate participant |
| [**orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete**](ProjectsApi.md#orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete) | **DELETE** /orgunits/{orgid}/projects/{projectid}/participants/${participantId} | Deletes a participant |
| [**orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost**](ProjectsApi.md#orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost) | **POST** /orgunits/{orgid}/projects/{projectid}/participants/${participantId}/loginlink | Participant login link |
| [**orgunitsOrgidProjectsProjectidParticipantsPost**](ProjectsApi.md#orgunitsOrgidProjectsProjectidParticipantsPost) | **POST** /orgunits/{orgid}/projects/{projectid}/participants | Add participant |
| [**orgunitsOrgidProjectsProjectidPatch**](ProjectsApi.md#orgunitsOrgidProjectsProjectidPatch) | **PATCH** /orgunits/{orgid}/projects/{projectid} | Update project information |
| [**orgunitsOrgidProjectsProjectidTeammembersGet**](ProjectsApi.md#orgunitsOrgidProjectsProjectidTeammembersGet) | **GET** /orgunits/{orgid}/projects/{projectid}/teammembers | Project team members |


<a id="extprojectGet"></a>
# **extprojectGet**
> Project extprojectGet(extid)

Gets Organization Unit by external id

Gets an Organization Unit by external id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String extid = "extid_example"; // String | The external id of the organization unit
    try {
      Project result = apiInstance.extprojectGet(extid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#extprojectGet");
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
| **extid** | **String**| The external id of the organization unit | |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching project |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidProjectsGet"></a>
# **orgunitsOrgidProjectsGet**
> List&lt;Project&gt; orgunitsOrgidProjectsGet(orgid)

Organization Unit Projects

Returns the available projects for the organization unit 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    BigDecimal orgid = new BigDecimal(78); // BigDecimal | Id of the organization unit
    try {
      List<Project> result = apiInstance.orgunitsOrgidProjectsGet(orgid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#orgunitsOrgidProjectsGet");
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
| **orgid** | **BigDecimal**| Id of the organization unit | |

### Return type

[**List&lt;Project&gt;**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list with projects |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidProjectsPost"></a>
# **orgunitsOrgidProjectsPost**
> Project orgunitsOrgidProjectsPost(orgid, body)

Create project

Creates a new project 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer orgid = 56; // Integer | Id of the organization unit
    AddProject body = new AddProject(); // AddProject | 
    try {
      Project result = apiInstance.orgunitsOrgidProjectsPost(orgid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#orgunitsOrgidProjectsPost");
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
| **orgid** | **Integer**| Id of the organization unit | |
| **body** | [**AddProject**](AddProject.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The project was succesfully created created. |  * location - Location to the added participant <br>  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidProjectsProjectidDelete"></a>
# **orgunitsOrgidProjectsProjectidDelete**
> orgunitsOrgidProjectsProjectidDelete(orgid, projectid)

Deletes the project

Deletes the project. The project can only be deleted if the project do not contain any participants. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer orgid = 56; // Integer | Id of the organization unit
    Integer projectid = 56; // Integer | Id of the project
    try {
      apiInstance.orgunitsOrgidProjectsProjectidDelete(orgid, projectid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#orgunitsOrgidProjectsProjectidDelete");
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
| **orgid** | **Integer**| Id of the organization unit | |
| **projectid** | **Integer**| Id of the project | |

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
| **204** | The project was deleted |  -  |
| **404** | The project could not be found |  -  |
| **406** | The project could not be delted due to constraints |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidProjectsProjectidGet"></a>
# **orgunitsOrgidProjectsProjectidGet**
> Project orgunitsOrgidProjectsProjectidGet(orgid, projectid)

Project information

Returns project information 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer orgid = 56; // Integer | Id of the organization unit
    Integer projectid = 56; // Integer | Id of the project
    try {
      Project result = apiInstance.orgunitsOrgidProjectsProjectidGet(orgid, projectid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#orgunitsOrgidProjectsProjectidGet");
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
| **orgid** | **Integer**| Id of the organization unit | |
| **projectid** | **Integer**| Id of the project | |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project information |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidProjectsProjectidParticipantsGet"></a>
# **orgunitsOrgidProjectsProjectidParticipantsGet**
> List&lt;Participation&gt; orgunitsOrgidProjectsProjectidParticipantsGet(orgid, projectid)

Project participants

Returns project participants 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer orgid = 56; // Integer | Id of the organization unit
    Integer projectid = 56; // Integer | Id of the project
    try {
      List<Participation> result = apiInstance.orgunitsOrgidProjectsProjectidParticipantsGet(orgid, projectid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#orgunitsOrgidProjectsProjectidParticipantsGet");
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
| **orgid** | **Integer**| Id of the organization unit | |
| **projectid** | **Integer**| Id of the project | |

### Return type

[**List&lt;Participation&gt;**](Participation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project information |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost"></a>
# **orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost**
> orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost(orgid, projectid, participantId)

Activate participant

Activates a participant so that it can be used 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer orgid = 56; // Integer | Id of the organization unit
    Integer projectid = 56; // Integer | Id of the project
    Integer participantId = 56; // Integer | Id of the participant
    try {
      apiInstance.orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost(orgid, projectid, participantId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost");
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
| **orgid** | **Integer**| Id of the organization unit | |
| **projectid** | **Integer**| Id of the project | |
| **participantId** | **Integer**| Id of the participant | |

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
| **201** | Participant is activated |  -  |
| **406** | The participant could not be activated |  -  |
| **422** | The participant could not be activated due to invalid project state |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete"></a>
# **orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete**
> orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete(orgid, projectid, participantId)

Deletes a participant

Deletes a participant. The user itself will still remain but any state related to the project will be deleted. It might not be possible due to constraints from the products in the project to delete the participant. However this can only be determined at the time of the delete. If a delete fails the participant will have their inError flag set. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer orgid = 56; // Integer | Id of the organization unit
    Integer projectid = 56; // Integer | Id of the project
    Integer participantId = 56; // Integer | Participant id
    try {
      apiInstance.orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete(orgid, projectid, participantId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete");
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
| **orgid** | **Integer**| Id of the organization unit | |
| **projectid** | **Integer**| Id of the project | |
| **participantId** | **Integer**| Participant id | |

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
| **204** | Participant is deleted |  -  |
| **409** | The delete failed due to internal constraints |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost"></a>
# **orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost**
> LoginLink orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost(orgid, projectid, participantId)

Participant login link

Returns a single sign on link for the participant. The link is only usable once and should be used directly. The link expires after a few minutes.  This operation requires the *login link* permission. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer orgid = 56; // Integer | Id of the organization unit
    Integer projectid = 56; // Integer | Id of the project
    Integer participantId = 56; // Integer | Id of the participant
    try {
      LoginLink result = apiInstance.orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost(orgid, projectid, participantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost");
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
| **orgid** | **Integer**| Id of the organization unit | |
| **projectid** | **Integer**| Id of the project | |
| **participantId** | **Integer**| Id of the participant | |

### Return type

[**LoginLink**](LoginLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A generated one time use login link |  -  |
| **422** | The participant is not in a state where a loginlink is possible to get |  -  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidProjectsProjectidParticipantsPost"></a>
# **orgunitsOrgidProjectsProjectidParticipantsPost**
> orgunitsOrgidProjectsProjectidParticipantsPost(orgid, projectid, body)

Add participant

Add a user to the project. Participant information is created for the user. In the body object, only one of either email or userid must be specified. The participant needs to be activated before it the user can access it. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer orgid = 56; // Integer | Id of the organization unit
    Integer projectid = 56; // Integer | Id of the project
    AddParticipant body = new AddParticipant(); // AddParticipant | 
    try {
      apiInstance.orgunitsOrgidProjectsProjectidParticipantsPost(orgid, projectid, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#orgunitsOrgidProjectsProjectidParticipantsPost");
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
| **orgid** | **Integer**| Id of the organization unit | |
| **projectid** | **Integer**| Id of the project | |
| **body** | [**AddParticipant**](AddParticipant.md)|  | |

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
| **201** | Participant was created |  * location - Location to the added participant <br>  |
| **409** | Participant with the same email already existed. Location header contains the url to the already existing participant. |  * location - Location to the added participant <br>  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidProjectsProjectidPatch"></a>
# **orgunitsOrgidProjectsProjectidPatch**
> Project orgunitsOrgidProjectsProjectidPatch(orgid, projectid, body)

Update project information

Updates information about a project. Values are only updated if the fields are specified in the input 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer orgid = 56; // Integer | Id of the organization unit
    Integer projectid = 56; // Integer | Id of the project
    UpdateProject body = new UpdateProject(); // UpdateProject | 
    try {
      Project result = apiInstance.orgunitsOrgidProjectsProjectidPatch(orgid, projectid, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#orgunitsOrgidProjectsProjectidPatch");
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
| **orgid** | **Integer**| Id of the organization unit | |
| **projectid** | **Integer**| Id of the project | |
| **body** | [**UpdateProject**](UpdateProject.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project was succesfully updated |  * location - Location to the added participant <br>  |
| **0** | Unexpected error |  -  |

<a id="orgunitsOrgidProjectsProjectidTeammembersGet"></a>
# **orgunitsOrgidProjectsProjectidTeammembersGet**
> List&lt;ProjectTeamMember&gt; orgunitsOrgidProjectsProjectidTeammembersGet(orgid, projectid)

Project team members

Returns the project team members. A team member is a .... 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer orgid = 56; // Integer | Id of the organization unit
    Integer projectid = 56; // Integer | Id of the project
    try {
      List<ProjectTeamMember> result = apiInstance.orgunitsOrgidProjectsProjectidTeammembersGet(orgid, projectid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#orgunitsOrgidProjectsProjectidTeammembersGet");
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
| **orgid** | **Integer**| Id of the organization unit | |
| **projectid** | **Integer**| Id of the project | |

### Return type

[**List&lt;ProjectTeamMember&gt;**](ProjectTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project information |  -  |
| **0** | Unexpected error |  -  |

