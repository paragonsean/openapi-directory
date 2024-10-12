# ConfigCatPublicManagementApi.FeatureFlagSettingValuesUsingSDKKeyApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSettingValueBySdkkey**](FeatureFlagSettingValuesUsingSDKKeyApi.md#getSettingValueBySdkkey) | **GET** /v1/settings/{settingKeyOrId}/value | Get value
[**replaceSettingValueBySdkkey**](FeatureFlagSettingValuesUsingSDKKeyApi.md#replaceSettingValueBySdkkey) | **PUT** /v1/settings/{settingKeyOrId}/value | Replace value
[**updateSettingValueBySdkkey**](FeatureFlagSettingValuesUsingSDKKeyApi.md#updateSettingValueBySdkkey) | **PATCH** /v1/settings/{settingKeyOrId}/value | Update value



## getSettingValueBySdkkey

> SettingValueModelHaljson getSettingValueBySdkkey(settingKeyOrId, opts)

Get value

This endpoint returns the value of a Feature Flag or Setting  in a specified Environment identified by the &lt;a target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; href&#x3D;\&quot;https://app.configcat.com/sdkkey\&quot;&gt;SDK key&lt;/a&gt; passed in the &#x60;X-CONFIGCAT-SDKKEY&#x60; header.  The most important attributes in the response are the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60;. The &#x60;value&#x60; represents what the clients will get when the evaluation requests of our SDKs  are not matching to any of the defined Targeting or Percentage Rules, or when there are no additional rules to evaluate.  The &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are representing the current  Targeting and Percentage Rules configuration of the actual Feature Flag or Setting  in an **ordered** collection, which means the order of the returned rules is matching to the evaluation order. You can read more about these rules [here](https://configcat.com/docs/advanced/targeting/).

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagSettingValuesUsingSDKKeyApi();
let settingKeyOrId = "settingKeyOrId_example"; // String | The key or id of the Setting.
let opts = {
  'X_CONFIGCAT_SDKKEY': "X_CONFIGCAT_SDKKEY_example" // String | The ConfigCat SDK Key. (https://app.configcat.com/sdkkey)
};
apiInstance.getSettingValueBySdkkey(settingKeyOrId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settingKeyOrId** | **String**| The key or id of the Setting. | 
 **X_CONFIGCAT_SDKKEY** | **String**| The ConfigCat SDK Key. (https://app.configcat.com/sdkkey) | [optional] 

### Return type

[**SettingValueModelHaljson**](SettingValueModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## replaceSettingValueBySdkkey

> SettingValueModelHaljson replaceSettingValueBySdkkey(settingKeyOrId, updateSettingValueModel, opts)

Replace value

This endpoint replaces the value of a Feature Flag or Setting  in a specified Environment identified by the &lt;a target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; href&#x3D;\&quot;https://app.configcat.com/sdkkey\&quot;&gt;SDK key&lt;/a&gt; passed in the &#x60;X-CONFIGCAT-SDKKEY&#x60; header.  Only the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are modifiable by this endpoint.  **Important:** As this endpoint is doing a complete replace, it&#39;s important to set every other attribute that you don&#39;t  want to change to its original state. Not listing one means that it will reset.  For example: We have the following resource. &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: false } &#x60;&#x60;&#x60; If we send a replace request body as below: &#x60;&#x60;&#x60; {  \&quot;value\&quot;: true } &#x60;&#x60;&#x60; Then besides that the default served value is set to &#x60;true&#x60;, all the Percentage Rules are deleted.  So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: true } &#x60;&#x60;&#x60;

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagSettingValuesUsingSDKKeyApi();
let settingKeyOrId = "settingKeyOrId_example"; // String | The key or id of the Setting.
let updateSettingValueModel = {"rolloutPercentageItems":[{"percentage":30,"value":true},{"percentage":70,"value":false}],"value":true}; // UpdateSettingValueModel | 
let opts = {
  'reason': "reason_example", // String | The reason note for the Audit Log if the Product's \"Config changes require a reason\" preference is turned on.
  'X_CONFIGCAT_SDKKEY': "X_CONFIGCAT_SDKKEY_example" // String | The ConfigCat SDK Key. (https://app.configcat.com/sdkkey)
};
apiInstance.replaceSettingValueBySdkkey(settingKeyOrId, updateSettingValueModel, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settingKeyOrId** | **String**| The key or id of the Setting. | 
 **updateSettingValueModel** | [**UpdateSettingValueModel**](UpdateSettingValueModel.md)|  | 
 **reason** | **String**| The reason note for the Audit Log if the Product&#39;s \&quot;Config changes require a reason\&quot; preference is turned on. | [optional] 
 **X_CONFIGCAT_SDKKEY** | **String**| The ConfigCat SDK Key. (https://app.configcat.com/sdkkey) | [optional] 

### Return type

[**SettingValueModelHaljson**](SettingValueModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## updateSettingValueBySdkkey

> SettingValueModelHaljson updateSettingValueBySdkkey(settingKeyOrId, jsonPatch, opts)

Update value

This endpoint updates the value of a Feature Flag or Setting  with a collection of [JSON Patch](http://jsonpatch.com) operations in a specified Environment identified by the &lt;a target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; href&#x3D;\&quot;https://app.configcat.com/sdkkey\&quot;&gt;SDK key&lt;/a&gt; passed in the &#x60;X-CONFIGCAT-SDKKEY&#x60; header.  Only the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are modifiable by this endpoint.  The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don&#39;t want to change. It supports collection reordering, so it also  can be used for reordering the targeting rules of a Feature Flag or Setting.  For example: We have the following resource. &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: false } &#x60;&#x60;&#x60; If we send an update request body as below: &#x60;&#x60;&#x60; [  {   \&quot;op\&quot;: \&quot;replace\&quot;,   \&quot;path\&quot;: \&quot;/value\&quot;,   \&quot;value\&quot;: true  } ] &#x60;&#x60;&#x60; Only the default served value is going to be set to &#x60;true&#x60; and all the Percentage Rules are remaining unchanged. So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: true } &#x60;&#x60;&#x60;

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagSettingValuesUsingSDKKeyApi();
let settingKeyOrId = "settingKeyOrId_example"; // String | The key or id of the Setting.
let jsonPatch = [{"op":"add","path":"/rolloutPercentageItems/-","value":{"percentage":30,"value":true}},{"op":"add","path":"/rolloutPercentageItems/-","value":{"percentage":70,"value":false}}]; // JsonPatch | 
let opts = {
  'reason': "reason_example", // String | The reason note for the Audit Log if the Product's \"Config changes require a reason\" preference is turned on.
  'X_CONFIGCAT_SDKKEY': "X_CONFIGCAT_SDKKEY_example" // String | The ConfigCat SDK Key. (https://app.configcat.com/sdkkey)
};
apiInstance.updateSettingValueBySdkkey(settingKeyOrId, jsonPatch, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settingKeyOrId** | **String**| The key or id of the Setting. | 
 **jsonPatch** | [**JsonPatch**](JsonPatch.md)|  | 
 **reason** | **String**| The reason note for the Audit Log if the Product&#39;s \&quot;Config changes require a reason\&quot; preference is turned on. | [optional] 
 **X_CONFIGCAT_SDKKEY** | **String**| The ConfigCat SDK Key. (https://app.configcat.com/sdkkey) | [optional] 

### Return type

[**SettingValueModelHaljson**](SettingValueModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json

