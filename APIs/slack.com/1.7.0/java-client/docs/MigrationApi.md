# MigrationApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**migrationExchange**](MigrationApi.md#migrationExchange) | **GET** /migration.exchange |  |


<a id="migrationExchange"></a>
# **migrationExchange**
> MigrationExchangeSuccessSchema migrationExchange(token, users, teamId, toOld)



For Enterprise Grid workspaces, map local user IDs to global user IDs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MigrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    MigrationApi apiInstance = new MigrationApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `tokens.basic`
    String users = "users_example"; // String | A comma-separated list of user ids, up to 400 per request
    String teamId = "teamId_example"; // String | Specify team_id starts with `T` in case of Org Token
    Boolean toOld = true; // Boolean | Specify `true` to convert `W` global user IDs to workspace-specific `U` IDs. Defaults to `false`.
    try {
      MigrationExchangeSuccessSchema result = apiInstance.migrationExchange(token, users, teamId, toOld);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MigrationApi#migrationExchange");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;tokens.basic&#x60; | |
| **users** | **String**| A comma-separated list of user ids, up to 400 per request | |
| **teamId** | **String**| Specify team_id starts with &#x60;T&#x60; in case of Org Token | [optional] |
| **toOld** | **Boolean**| Specify &#x60;true&#x60; to convert &#x60;W&#x60; global user IDs to workspace-specific &#x60;U&#x60; IDs. Defaults to &#x60;false&#x60;. | [optional] |

### Return type

[**MigrationExchangeSuccessSchema**](MigrationExchangeSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response when mappings exist for the specified user IDs |  -  |
| **0** | Typical error response when there are no mappings to provide |  -  |

