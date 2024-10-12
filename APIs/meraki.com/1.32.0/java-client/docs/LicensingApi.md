# LicensingApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrganizationLicensingCotermLicenses**](LicensingApi.md#getOrganizationLicensingCotermLicenses) | **GET** /organizations/{organizationId}/licensing/coterm/licenses | List the licenses in a coterm organization |
| [**moveOrganizationLicensingCotermLicenses**](LicensingApi.md#moveOrganizationLicensingCotermLicenses) | **POST** /organizations/{organizationId}/licensing/coterm/licenses/move | Moves a license to a different organization (coterm only) |


<a id="getOrganizationLicensingCotermLicenses"></a>
# **getOrganizationLicensingCotermLicenses**
> List&lt;GetOrganizationLicensingCotermLicenses200ResponseInner&gt; getOrganizationLicensingCotermLicenses(organizationId, perPage, startingAfter, endingBefore, invalidated, expired)

List the licenses in a coterm organization

List the licenses in a coterm organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensingApi apiInstance = new LicensingApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    Boolean invalidated = true; // Boolean | Filter for licenses that are invalidated
    Boolean expired = true; // Boolean | Filter for licenses that are expired
    try {
      List<GetOrganizationLicensingCotermLicenses200ResponseInner> result = apiInstance.getOrganizationLicensingCotermLicenses(organizationId, perPage, startingAfter, endingBefore, invalidated, expired);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensingApi#getOrganizationLicensingCotermLicenses");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **invalidated** | **Boolean**| Filter for licenses that are invalidated | [optional] |
| **expired** | **Boolean**| Filter for licenses that are expired | [optional] |

### Return type

[**List&lt;GetOrganizationLicensingCotermLicenses200ResponseInner&gt;**](GetOrganizationLicensingCotermLicenses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="moveOrganizationLicensingCotermLicenses"></a>
# **moveOrganizationLicensingCotermLicenses**
> MoveOrganizationLicensingCotermLicenses200Response moveOrganizationLicensingCotermLicenses(organizationId, moveOrganizationLicensingCotermLicensesRequest)

Moves a license to a different organization (coterm only)

Moves a license to a different organization (coterm only)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LicensingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LicensingApi apiInstance = new LicensingApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    MoveOrganizationLicensingCotermLicensesRequest moveOrganizationLicensingCotermLicensesRequest = new MoveOrganizationLicensingCotermLicensesRequest(); // MoveOrganizationLicensingCotermLicensesRequest | 
    try {
      MoveOrganizationLicensingCotermLicenses200Response result = apiInstance.moveOrganizationLicensingCotermLicenses(organizationId, moveOrganizationLicensingCotermLicensesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LicensingApi#moveOrganizationLicensingCotermLicenses");
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
| **organizationId** | **String**|  | |
| **moveOrganizationLicensingCotermLicensesRequest** | [**MoveOrganizationLicensingCotermLicensesRequest**](MoveOrganizationLicensingCotermLicensesRequest.md)|  | |

### Return type

[**MoveOrganizationLicensingCotermLicenses200Response**](MoveOrganizationLicensingCotermLicenses200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

