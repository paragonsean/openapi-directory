# StoryCollaboratorsApi

All URIs are relative to */story*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storyIdCollaboratorsGet**](StoryCollaboratorsApi.md#storyIdCollaboratorsGet) | **GET** /{id}/collaborators | Story Collaborators: List |
| [**storyIdCollaboratorsInactivePost**](StoryCollaboratorsApi.md#storyIdCollaboratorsInactivePost) | **POST** /{id}/collaborators/inactive | Story Collaborators: Edit Inactive User Permission |
| [**storyIdCollaboratorsPost**](StoryCollaboratorsApi.md#storyIdCollaboratorsPost) | **POST** /{id}/collaborators | Story Collaborators: Add New User |
| [**storyIdCollaboratorsUseridDelete**](StoryCollaboratorsApi.md#storyIdCollaboratorsUseridDelete) | **DELETE** /{id}/collaborators/{story_collaborator_userid} | Story Collaborators: Remove User |
| [**storyIdCollaboratorsUseridGet**](StoryCollaboratorsApi.md#storyIdCollaboratorsUseridGet) | **GET** /{id}/collaborators/{story_collaborator_userid} | Story Collaborators: Access Permissions |
| [**storyIdCollaboratorsUseridPut**](StoryCollaboratorsApi.md#storyIdCollaboratorsUseridPut) | **PUT** /{id}/collaborators/{story_collaborator_userid} | Story Collaborators: Edit Access Rights |


<a id="storyIdCollaboratorsGet"></a>
# **storyIdCollaboratorsGet**
> List&lt;StoryCollaborator&gt; storyIdCollaboratorsGet(id)

Story Collaborators: List

Gets a list users that can read or edit this story

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryCollaboratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryCollaboratorsApi apiInstance = new StoryCollaboratorsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    try {
      List<StoryCollaborator> result = apiInstance.storyIdCollaboratorsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryCollaboratorsApi#storyIdCollaboratorsGet");
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
| **id** | **UUID**| the id from the story object | |

### Return type

[**List&lt;StoryCollaborator&gt;**](StoryCollaborator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of collaborators on the story |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdCollaboratorsInactivePost"></a>
# **storyIdCollaboratorsInactivePost**
> StoryCollaborator storyIdCollaboratorsInactivePost(id, modifyInactiveCollaborator)

Story Collaborators: Edit Inactive User Permission

Edit story permissions for inactive users.  Requires admin rights.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryCollaboratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryCollaboratorsApi apiInstance = new StoryCollaboratorsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    ModifyInactiveCollaborator modifyInactiveCollaborator = new ModifyInactiveCollaborator(); // ModifyInactiveCollaborator | Collaborator user id and permission type
    try {
      StoryCollaborator result = apiInstance.storyIdCollaboratorsInactivePost(id, modifyInactiveCollaborator);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryCollaboratorsApi#storyIdCollaboratorsInactivePost");
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
| **id** | **UUID**| the id from the story object | |
| **modifyInactiveCollaborator** | [**ModifyInactiveCollaborator**](ModifyInactiveCollaborator.md)| Collaborator user id and permission type | |

### Return type

[**StoryCollaborator**](StoryCollaborator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collaborator data |  -  |
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdCollaboratorsPost"></a>
# **storyIdCollaboratorsPost**
> StoryCollaborator storyIdCollaboratorsPost(id, addNewCollaboratorRequest)

Story Collaborators: Add New User

Add a colloborator to this story

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryCollaboratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryCollaboratorsApi apiInstance = new StoryCollaboratorsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    AddNewCollaboratorRequest addNewCollaboratorRequest = new AddNewCollaboratorRequest(); // AddNewCollaboratorRequest | Collaborator user id and permission type
    try {
      StoryCollaborator result = apiInstance.storyIdCollaboratorsPost(id, addNewCollaboratorRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryCollaboratorsApi#storyIdCollaboratorsPost");
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
| **id** | **UUID**| the id from the story object | |
| **addNewCollaboratorRequest** | [**AddNewCollaboratorRequest**](AddNewCollaboratorRequest.md)| Collaborator user id and permission type | |

### Return type

[**StoryCollaborator**](StoryCollaborator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collaborator data |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdCollaboratorsUseridDelete"></a>
# **storyIdCollaboratorsUseridDelete**
> storyIdCollaboratorsUseridDelete(id, storyCollaboratorUserid)

Story Collaborators: Remove User

Remove a collaborator from this story

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryCollaboratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryCollaboratorsApi apiInstance = new StoryCollaboratorsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    UUID storyCollaboratorUserid = UUID.randomUUID(); // UUID | The presalytics userid (NOT the Id of the story_collaborator object)
    try {
      apiInstance.storyIdCollaboratorsUseridDelete(id, storyCollaboratorUserid);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryCollaboratorsApi#storyIdCollaboratorsUseridDelete");
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
| **id** | **UUID**| the id from the story object | |
| **storyCollaboratorUserid** | **UUID**| The presalytics userid (NOT the Id of the story_collaborator object) | |

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
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdCollaboratorsUseridGet"></a>
# **storyIdCollaboratorsUseridGet**
> StoryCollaborator storyIdCollaboratorsUseridGet(id, storyCollaboratorUserid)

Story Collaborators: Access Permissions

Data to help you understand the access rights of a particular collaborator on this story

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryCollaboratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryCollaboratorsApi apiInstance = new StoryCollaboratorsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    UUID storyCollaboratorUserid = UUID.randomUUID(); // UUID | The presalytics userid (NOT the Id of the story_collaborator object)
    try {
      StoryCollaborator result = apiInstance.storyIdCollaboratorsUseridGet(id, storyCollaboratorUserid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryCollaboratorsApi#storyIdCollaboratorsUseridGet");
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
| **id** | **UUID**| the id from the story object | |
| **storyCollaboratorUserid** | **UUID**| The presalytics userid (NOT the Id of the story_collaborator object) | |

### Return type

[**StoryCollaborator**](StoryCollaborator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collaborator data |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="storyIdCollaboratorsUseridPut"></a>
# **storyIdCollaboratorsUseridPut**
> StoryCollaborator storyIdCollaboratorsUseridPut(id, storyCollaboratorUserid, storyCollaborator)

Story Collaborators: Edit Access Rights

Modify a user&#39;s access right to this story (e.g., grant edit permissions)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoryCollaboratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    StoryCollaboratorsApi apiInstance = new StoryCollaboratorsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    UUID storyCollaboratorUserid = UUID.randomUUID(); // UUID | The presalytics userid (NOT the Id of the story_collaborator object)
    StoryCollaborator storyCollaborator = new StoryCollaborator(); // StoryCollaborator | Collaborator user id (presalytics userid) and permission type
    try {
      StoryCollaborator result = apiInstance.storyIdCollaboratorsUseridPut(id, storyCollaboratorUserid, storyCollaborator);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoryCollaboratorsApi#storyIdCollaboratorsUseridPut");
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
| **id** | **UUID**| the id from the story object | |
| **storyCollaboratorUserid** | **UUID**| The presalytics userid (NOT the Id of the story_collaborator object) | |
| **storyCollaborator** | [**StoryCollaborator**](StoryCollaborator.md)| Collaborator user id (presalytics userid) and permission type | |

### Return type

[**StoryCollaborator**](StoryCollaborator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collaborator data |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

