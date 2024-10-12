# ConsumerInvitationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consumerInvitationsGet**](ConsumerInvitationApi.md#consumerInvitationsGet) | **GET** /providers/Microsoft.DataShare/locations/{location}/consumerInvitations/{invitationId} | Gets the invitation identified by invitationId |
| [**consumerInvitationsListInvitations**](ConsumerInvitationApi.md#consumerInvitationsListInvitations) | **GET** /providers/Microsoft.DataShare/ListInvitations | List the invitations |
| [**consumerInvitationsRejectInvitation**](ConsumerInvitationApi.md#consumerInvitationsRejectInvitation) | **POST** /providers/Microsoft.DataShare/locations/{location}/RejectInvitation | Rejects the invitation identified by invitationId |


<a id="consumerInvitationsGet"></a>
# **consumerInvitationsGet**
> ConsumerInvitation consumerInvitationsGet(location, invitationId, apiVersion)

Gets the invitation identified by invitationId

Get an invitation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsumerInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConsumerInvitationApi apiInstance = new ConsumerInvitationApi(defaultClient);
    String location = "location_example"; // String | Location of the invitation
    String invitationId = "invitationId_example"; // String | An invitation id
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      ConsumerInvitation result = apiInstance.consumerInvitationsGet(location, invitationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsumerInvitationApi#consumerInvitationsGet");
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
| **location** | **String**| Location of the invitation | |
| **invitationId** | **String**| An invitation id | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**ConsumerInvitation**](ConsumerInvitation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="consumerInvitationsListInvitations"></a>
# **consumerInvitationsListInvitations**
> ConsumerInvitationList consumerInvitationsListInvitations(apiVersion, $skipToken)

List the invitations

Lists invitations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsumerInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConsumerInvitationApi apiInstance = new ConsumerInvitationApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | The continuation token
    try {
      ConsumerInvitationList result = apiInstance.consumerInvitationsListInvitations(apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsumerInvitationApi#consumerInvitationsListInvitations");
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
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| The continuation token | [optional] |

### Return type

[**ConsumerInvitationList**](ConsumerInvitationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="consumerInvitationsRejectInvitation"></a>
# **consumerInvitationsRejectInvitation**
> ConsumerInvitation consumerInvitationsRejectInvitation(location, apiVersion, invitation)

Rejects the invitation identified by invitationId

Reject an invitation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConsumerInvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConsumerInvitationApi apiInstance = new ConsumerInvitationApi(defaultClient);
    String location = "location_example"; // String | Location of the invitation
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    ConsumerInvitation invitation = new ConsumerInvitation(); // ConsumerInvitation | An invitation payload
    try {
      ConsumerInvitation result = apiInstance.consumerInvitationsRejectInvitation(location, apiVersion, invitation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConsumerInvitationApi#consumerInvitationsRejectInvitation");
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
| **location** | **String**| Location of the invitation | |
| **apiVersion** | **String**| The api version to use. | |
| **invitation** | [**ConsumerInvitation**](ConsumerInvitation.md)| An invitation payload | |

### Return type

[**ConsumerInvitation**](ConsumerInvitation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

