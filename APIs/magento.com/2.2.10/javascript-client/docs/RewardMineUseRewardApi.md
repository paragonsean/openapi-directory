# MagentoB2B.RewardMineUseRewardApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rewardRewardManagementV1SetPost**](RewardMineUseRewardApi.md#rewardRewardManagementV1SetPost) | **POST** /V1/reward/mine/use-reward | reward/mine/use-reward



## rewardRewardManagementV1SetPost

> Boolean rewardRewardManagementV1SetPost()

reward/mine/use-reward

Set reward points to quote

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.RewardMineUseRewardApi();
apiInstance.rewardRewardManagementV1SetPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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

