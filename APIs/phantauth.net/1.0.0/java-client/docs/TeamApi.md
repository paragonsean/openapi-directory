# TeamApi

All URIs are relative to *https://phantauth.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**teamTeamnameGet**](TeamApi.md#teamTeamnameGet) | **GET** /team/{teamname} | Get a Team |


<a id="teamTeamnameGet"></a>
# **teamTeamnameGet**
> TeamTeamnameGet200Response teamTeamnameGet(teamname)

Get a Team

Use this endpoint to generate a random group of users. The team is generated in a deterministic way, on the basis of the team name given as the path parameter. In the case of identical team names, the endpoint will generate the same team object. The properties of the generated team object are randomly generated on the basis of the team name. In lack of a team name, all calls generate a different team object to the randomly generated team name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://phantauth.net");

    TeamApi apiInstance = new TeamApi(defaultClient);
    String teamname = "teamname_example"; // String |  The identifier or email address of the team; it is integrated in the `sub` property and is the basis of the other generated properties. 
    try {
      TeamTeamnameGet200Response result = apiInstance.teamTeamnameGet(teamname);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamApi#teamTeamnameGet");
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
| **teamname** | **String**|  The identifier or email address of the team; it is integrated in the &#x60;sub&#x60; property and is the basis of the other generated properties.  | |

### Return type

[**TeamTeamnameGet200Response**](TeamTeamnameGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

