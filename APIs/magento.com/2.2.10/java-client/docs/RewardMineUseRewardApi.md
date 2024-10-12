# RewardMineUseRewardApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rewardRewardManagementV1SetPost**](RewardMineUseRewardApi.md#rewardRewardManagementV1SetPost) | **POST** /V1/reward/mine/use-reward | reward/mine/use-reward |


<a id="rewardRewardManagementV1SetPost"></a>
# **rewardRewardManagementV1SetPost**
> Boolean rewardRewardManagementV1SetPost()

reward/mine/use-reward

Set reward points to quote

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RewardMineUseRewardApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    RewardMineUseRewardApi apiInstance = new RewardMineUseRewardApi(defaultClient);
    try {
      Boolean result = apiInstance.rewardRewardManagementV1SetPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RewardMineUseRewardApi#rewardRewardManagementV1SetPost");
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

