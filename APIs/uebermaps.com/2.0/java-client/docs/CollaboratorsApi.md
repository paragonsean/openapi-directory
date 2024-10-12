# CollaboratorsApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mapsIdCollaboratorsGet**](CollaboratorsApi.md#mapsIdCollaboratorsGet) | **GET** /maps/{id}/collaborators/ | List collaborators of a map |
| [**mapsIdCollaboratorsUserIdDelete**](CollaboratorsApi.md#mapsIdCollaboratorsUserIdDelete) | **DELETE** /maps/{id}/collaborators/{user_id} | Delete collaboration |
| [**mapsIdCollaboratorsUserIdPatch**](CollaboratorsApi.md#mapsIdCollaboratorsUserIdPatch) | **PATCH** /maps/{id}/collaborators/{user_id} | Update collaborator |


<a id="mapsIdCollaboratorsGet"></a>
# **mapsIdCollaboratorsGet**
> List&lt;Collaborator&gt; mapsIdCollaboratorsGet(id)

List collaborators of a map

List collaborators of a map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollaboratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CollaboratorsApi apiInstance = new CollaboratorsApi(defaultClient);
    Integer id = 56; // Integer | Map id
    try {
      List<Collaborator> result = apiInstance.mapsIdCollaboratorsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollaboratorsApi#mapsIdCollaboratorsGet");
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
| **id** | **Integer**| Map id | |

### Return type

[**List&lt;Collaborator&gt;**](Collaborator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of collaborators. |  -  |

<a id="mapsIdCollaboratorsUserIdDelete"></a>
# **mapsIdCollaboratorsUserIdDelete**
> Collaborator mapsIdCollaboratorsUserIdDelete(id, userId)

Delete collaboration

Delete collaboration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollaboratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CollaboratorsApi apiInstance = new CollaboratorsApi(defaultClient);
    Integer id = 56; // Integer | map id
    Integer userId = 56; // Integer | user id
    try {
      Collaborator result = apiInstance.mapsIdCollaboratorsUserIdDelete(id, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollaboratorsApi#mapsIdCollaboratorsUserIdDelete");
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
| **id** | **Integer**| map id | |
| **userId** | **Integer**| user id | |

### Return type

[**Collaborator**](Collaborator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains deleted collaborator. |  -  |

<a id="mapsIdCollaboratorsUserIdPatch"></a>
# **mapsIdCollaboratorsUserIdPatch**
> Collaborator mapsIdCollaboratorsUserIdPatch(id, userId, collaborator)

Update collaborator

Update collaborator. Wrap collaborator parameters in [collaborator]

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CollaboratorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    CollaboratorsApi apiInstance = new CollaboratorsApi(defaultClient);
    Integer id = 56; // Integer | map id
    Integer userId = 56; // Integer | user id
    CollaboratorEditable collaborator = new CollaboratorEditable(); // CollaboratorEditable | collaborator attributes
    try {
      Collaborator result = apiInstance.mapsIdCollaboratorsUserIdPatch(id, userId, collaborator);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CollaboratorsApi#mapsIdCollaboratorsUserIdPatch");
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
| **id** | **Integer**| map id | |
| **userId** | **Integer**| user id | |
| **collaborator** | [**CollaboratorEditable**](CollaboratorEditable.md)| collaborator attributes | [optional] |

### Return type

[**Collaborator**](Collaborator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains collaborator data |  -  |

