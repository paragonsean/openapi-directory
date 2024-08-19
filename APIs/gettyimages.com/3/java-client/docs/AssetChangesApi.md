# AssetChangesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v3AssetChangesChangeSetsChangeSetIdDelete**](AssetChangesApi.md#v3AssetChangesChangeSetsChangeSetIdDelete) | **DELETE** /v3/asset-changes/change-sets/{change-set-id} | Confirm asset change notifications. |
| [**v3AssetChangesChangeSetsPut**](AssetChangesApi.md#v3AssetChangesChangeSetsPut) | **PUT** /v3/asset-changes/change-sets | Get asset change notifications. |
| [**v3AssetChangesChannelsGet**](AssetChangesApi.md#v3AssetChangesChannelsGet) | **GET** /v3/asset-changes/channels | Get a list of asset change notification channels. |


<a id="v3AssetChangesChangeSetsChangeSetIdDelete"></a>
# **v3AssetChangesChangeSetsChangeSetIdDelete**
> v3AssetChangesChangeSetsChangeSetIdDelete(changeSetId)

Confirm asset change notifications.

# Delete Asset Changes  Confirm asset changes acknowledges receipt of asset changes (from the PUT asset-changes endpoint).  ##  Quickstart  You&#39;ll need an API key and an access token to use this resource.  Use the change_set_id from the PUT asset-changes/change-sets endpoint to confirm receipt of notifications. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetChangesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Api-Key
    ApiKeyAuth Api-Key = (ApiKeyAuth) defaultClient.getAuthentication("Api-Key");
    Api-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Api-Key.setApiKeyPrefix("Token");

    AssetChangesApi apiInstance = new AssetChangesApi(defaultClient);
    Long changeSetId = 56L; // Long | Specify the change-set-id associated with a transaction resource whose receipt you want to confirm.
    try {
      apiInstance.v3AssetChangesChangeSetsChangeSetIdDelete(changeSetId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetChangesApi#v3AssetChangesChangeSetsChangeSetIdDelete");
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
| **changeSetId** | **Long**| Specify the change-set-id associated with a transaction resource whose receipt you want to confirm. | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | InvalidChangeSetId |  -  |
| **403** | Your access token does not authorize access to this resource |  -  |
| **404** | Transaction was not found |  -  |

<a id="v3AssetChangesChangeSetsPut"></a>
# **v3AssetChangesChangeSetsPut**
> AssetChanges v3AssetChangesChangeSetsPut(channelId, batchSize)

Get asset change notifications.

# Asset Changes  Get notifications about new, updated or deleted assets for a specific channel.  ##  Quickstart  You&#39;ll need an API key and an access token to use this resource.   Maximum batch size is 2200.  Change-sets must be confirmed before a new batch of notifications can be retrieved from this endpoint. Use the DELETE asset-changes/change-sets/{change-set-id} endpoint to confirm reciept of these notifications.  Values returned for asset_type include Image, Film, and null. Values returned for asset_lifecycle include New, Update, and Delete.  Delete notifications may be provided for asset ids that have not previously been received as New or Update notifications. Delete notifications may return null for the asset_type.  If there are no notifications in the channel an empty response body will be returned.  Notifications older than 60 days will be removed from partner channels. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetChangesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Api-Key
    ApiKeyAuth Api-Key = (ApiKeyAuth) defaultClient.getAuthentication("Api-Key");
    Api-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Api-Key.setApiKeyPrefix("Token");

    AssetChangesApi apiInstance = new AssetChangesApi(defaultClient);
    Integer channelId = 56; // Integer | Specifies the id of the channel for the asset data. Valid channel ids can be found in the results of the Get Partner Channel query.
    Integer batchSize = 56; // Integer | Specifies the number of assets to return. The default is 2200; maximum is 2200.
    try {
      AssetChanges result = apiInstance.v3AssetChangesChangeSetsPut(channelId, batchSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetChangesApi#v3AssetChangesChangeSetsPut");
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
| **channelId** | **Integer**| Specifies the id of the channel for the asset data. Valid channel ids can be found in the results of the Get Partner Channel query. | [optional] |
| **batchSize** | **Integer**| Specifies the number of assets to return. The default is 2200; maximum is 2200. | [optional] |

### Return type

[**AssetChanges**](AssetChanges.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - Channel contains unconfirmed asset change notifications |  -  |
| **201** | Created |  -  |
| **400** | InvalidChannelIdException |  -  |
| **403** | Your access token does not authorize access to this resource |  -  |
| **404** | The channel you specified does not exist |  -  |

<a id="v3AssetChangesChannelsGet"></a>
# **v3AssetChangesChannelsGet**
> List&lt;Channel&gt; v3AssetChangesChannelsGet()

Get a list of asset change notification channels.

# Get Partner Channels  Retrieves the channel data for the partner. This data can be used to populate the channel_id parameter in the Put Asset Changes query.  ##  Quickstart  You&#39;ll need an API key and an access token to use this resource.  Partners who have a channel that has been removed should contact their sales representative to be set up again.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetChangesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure API key authorization: Api-Key
    ApiKeyAuth Api-Key = (ApiKeyAuth) defaultClient.getAuthentication("Api-Key");
    Api-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Api-Key.setApiKeyPrefix("Token");

    AssetChangesApi apiInstance = new AssetChangesApi(defaultClient);
    try {
      List<Channel> result = apiInstance.v3AssetChangesChannelsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetChangesApi#v3AssetChangesChannelsGet");
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

[**List&lt;Channel&gt;**](Channel.md)

### Authorization

[OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [OAuth2](../README.md#OAuth2), [Api-Key](../README.md#Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | UnauthorizedToAccessResource |  -  |
| **404** | ChannelsNotFound |  -  |

