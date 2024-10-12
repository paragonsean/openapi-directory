# CollaboratorInvitationsApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**collaboratorInvitationsGet**](CollaboratorInvitationsApi.md#collaboratorInvitationsGet) | **GET** /collaborator_invitations | List your collaborator invitations |
| [**collaboratorInvitationsIdDelete**](CollaboratorInvitationsApi.md#collaboratorInvitationsIdDelete) | **DELETE** /collaborator_invitations/{id} | Delete collaborator invitation |
| [**collaboratorInvitationsIdGet**](CollaboratorInvitationsApi.md#collaboratorInvitationsIdGet) | **GET** /collaborator_invitations/{id} | Show collaborator invitation |
| [**collaboratorInvitationsIdPatch**](CollaboratorInvitationsApi.md#collaboratorInvitationsIdPatch) | **PATCH** /collaborator_invitations/{id} | Accept collaborator invitation. |
| [**collaboratorInvitationsPost**](CollaboratorInvitationsApi.md#collaboratorInvitationsPost) | **POST** /collaborator_invitations | Invite user to collaborate on map |


<a id="collaboratorInvitationsGet"></a>
# **collaboratorInvitationsGet**
> List&lt;CollaboratorInvitation&gt; collaboratorInvitationsGet()

List your collaborator invitations

List your collaborator invitations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollaboratorInvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CollaboratorInvitationsApi apiInstance = new CollaboratorInvitationsApi(defaultClient);
    try {
      List<CollaboratorInvitation> result = apiInstance.collaboratorInvitationsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollaboratorInvitationsApi#collaboratorInvitationsGet");
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

[**List&lt;CollaboratorInvitation&gt;**](CollaboratorInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of collaborator invitations. |  -  |

<a id="collaboratorInvitationsIdDelete"></a>
# **collaboratorInvitationsIdDelete**
> CollaboratorInvitation collaboratorInvitationsIdDelete(id)

Delete collaborator invitation

Delete collaborator invitation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollaboratorInvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CollaboratorInvitationsApi apiInstance = new CollaboratorInvitationsApi(defaultClient);
    Integer id = 56; // Integer | Collaborator invitation id
    try {
      CollaboratorInvitation result = apiInstance.collaboratorInvitationsIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollaboratorInvitationsApi#collaboratorInvitationsIdDelete");
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
| **id** | **Integer**| Collaborator invitation id | |

### Return type

[**CollaboratorInvitation**](CollaboratorInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains deleted collaborator invitation. |  -  |

<a id="collaboratorInvitationsIdGet"></a>
# **collaboratorInvitationsIdGet**
> CollaboratorInvitation collaboratorInvitationsIdGet(id)

Show collaborator invitation

Show collaborator invitation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollaboratorInvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CollaboratorInvitationsApi apiInstance = new CollaboratorInvitationsApi(defaultClient);
    Integer id = 56; // Integer | Collaborator invitation id
    try {
      CollaboratorInvitation result = apiInstance.collaboratorInvitationsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollaboratorInvitationsApi#collaboratorInvitationsIdGet");
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
| **id** | **Integer**| Collaborator invitation id | |

### Return type

[**CollaboratorInvitation**](CollaboratorInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains collaborator invitation data. |  -  |

<a id="collaboratorInvitationsIdPatch"></a>
# **collaboratorInvitationsIdPatch**
> CollaboratorInvitation collaboratorInvitationsIdPatch(id)

Accept collaborator invitation.

Accept collaborator invitation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollaboratorInvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CollaboratorInvitationsApi apiInstance = new CollaboratorInvitationsApi(defaultClient);
    Integer id = 56; // Integer | Collaborator invitation id
    try {
      CollaboratorInvitation result = apiInstance.collaboratorInvitationsIdPatch(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollaboratorInvitationsApi#collaboratorInvitationsIdPatch");
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
| **id** | **Integer**| Collaborator invitation id | |

### Return type

[**CollaboratorInvitation**](CollaboratorInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains collaborator invitation data. |  -  |

<a id="collaboratorInvitationsPost"></a>
# **collaboratorInvitationsPost**
> CollaboratorInvitation collaboratorInvitationsPost(body)

Invite user to collaborate on map

Invite user to collaborate on map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollaboratorInvitationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CollaboratorInvitationsApi apiInstance = new CollaboratorInvitationsApi(defaultClient);
    CollaboratorInvitationCreate body = new CollaboratorInvitationCreate(); // CollaboratorInvitationCreate | Supply map_id and either a comma separated list of user_ids or emails. Optionally you can provide a 'is_admin' parameter with 'true' or 'false' to give the invited users admin privileges.
    try {
      CollaboratorInvitation result = apiInstance.collaboratorInvitationsPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollaboratorInvitationsApi#collaboratorInvitationsPost");
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
| **body** | [**CollaboratorInvitationCreate**](CollaboratorInvitationCreate.md)| Supply map_id and either a comma separated list of user_ids or emails. Optionally you can provide a &#39;is_admin&#39; parameter with &#39;true&#39; or &#39;false&#39; to give the invited users admin privileges. | [optional] |

### Return type

[**CollaboratorInvitation**](CollaboratorInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains collaborator invitation data. |  -  |

