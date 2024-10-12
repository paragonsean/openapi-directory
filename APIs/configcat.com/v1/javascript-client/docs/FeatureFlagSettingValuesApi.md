# ConfigCatPublicManagementApi.FeatureFlagSettingValuesApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSettingValue**](FeatureFlagSettingValuesApi.md#getSettingValue) | **GET** /v1/environments/{environmentId}/settings/{settingId}/value | Get value
[**getSettingValues**](FeatureFlagSettingValuesApi.md#getSettingValues) | **GET** /v1/configs/{configId}/environments/{environmentId}/values | Get values
[**postSettingValues**](FeatureFlagSettingValuesApi.md#postSettingValues) | **POST** /v1/configs/{configId}/environments/{environmentId}/values | Post values
[**replaceSettingValue**](FeatureFlagSettingValuesApi.md#replaceSettingValue) | **PUT** /v1/environments/{environmentId}/settings/{settingId}/value | Replace value
[**updateSettingValue**](FeatureFlagSettingValuesApi.md#updateSettingValue) | **PATCH** /v1/environments/{environmentId}/settings/{settingId}/value | Update value



## getSettingValue

> SettingValueModelHaljson getSettingValue(environmentId, settingId)

Get value

This endpoint returns the value of a Feature Flag or Setting  in a specified Environment identified by the &#x60;environmentId&#x60; parameter.  The most important attributes in the response are the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60;. The &#x60;value&#x60; represents what the clients will get when the evaluation requests of our SDKs  are not matching to any of the defined Targeting or Percentage Rules, or when there are no additional rules to evaluate.  The &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are representing the current  Targeting and Percentage Rules configuration of the actual Feature Flag or Setting  in an **ordered** collection, which means the order of the returned rules is matching to the evaluation order. You can read more about these rules [here](https://configcat.com/docs/advanced/targeting/).

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagSettingValuesApi();
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
let settingId = 56; // Number | The id of the Setting.
apiInstance.getSettingValue(environmentId, settingId, (error, data, response) => {
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
 **environmentId** | **String**| The identifier of the Environment. | 
 **settingId** | **Number**| The id of the Setting. | 

### Return type

[**SettingValueModelHaljson**](SettingValueModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getSettingValues

> ConfigSettingValuesModel getSettingValues(configId, environmentId)

Get values

This endpoint returns the value of a specified Config&#39;s Feature Flags or Settings identified by the &#x60;configId&#x60; parameter in a specified Environment identified by the &#x60;environmentId&#x60; parameter.  The most important attributes in the response are the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60;. The &#x60;value&#x60; represents what the clients will get when the evaluation requests of our SDKs  are not matching to any of the defined Targeting or Percentage Rules, or when there are no additional rules to evaluate.  The &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are representing the current  Targeting and Percentage Rules configuration of the actual Feature Flag or Setting  in an **ordered** collection, which means the order of the returned rules is matching to the evaluation order. You can read more about these rules [here](https://configcat.com/docs/advanced/targeting/).

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagSettingValuesApi();
let configId = "configId_example"; // String | The identifier of the Config.
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
apiInstance.getSettingValues(configId, environmentId, (error, data, response) => {
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
 **configId** | **String**| The identifier of the Config. | 
 **environmentId** | **String**| The identifier of the Environment. | 

### Return type

[**ConfigSettingValuesModel**](ConfigSettingValuesModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## postSettingValues

> ConfigSettingValuesModel postSettingValues(configId, environmentId, updateSettingValuesWithIdModel, opts)

Post values

This endpoint replaces the values of a specified Config&#39;s Feature Flags or Settings identified by the &#x60;configId&#x60; parameter in a specified Environment identified by the &#x60;environmentId&#x60; parameter.  Only the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are modifiable by this endpoint.  **Important:** As this endpoint is doing a complete replace, it&#39;s important to set every other attribute that you don&#39;t  want to change in its original state. Not listing one means that it will reset.  For example: We have the following resource. &#x60;&#x60;&#x60; {     \&quot;settingValues\&quot;: [   {    \&quot;rolloutPercentageItems\&quot;: [     {      \&quot;percentage\&quot;: 30,      \&quot;value\&quot;: true     },     {      \&quot;percentage\&quot;: 70,      \&quot;value\&quot;: false     }    ],    \&quot;rolloutRules\&quot;: [],    \&quot;value\&quot;: false,    \&quot;settingId\&quot;: 1   }  ] } &#x60;&#x60;&#x60; If we send a replace request body as below: &#x60;&#x60;&#x60; {   \&quot;settingValues\&quot;: [   {    \&quot;value\&quot;: true,    \&quot;settingId\&quot;: 1   }  ] } &#x60;&#x60;&#x60; Then besides that the default value is set to &#x60;true&#x60;, all the Percentage Rules are deleted.  So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;settingValues\&quot;: [   {    \&quot;rolloutPercentageItems\&quot;: [],    \&quot;rolloutRules\&quot;: [],    \&quot;value\&quot;: true,    \&quot;setting\&quot;:     {     \&quot;settingId\&quot;: 1    }   }  ] } &#x60;&#x60;&#x60;  The &#x60;rolloutRules&#x60; property describes two types of rules:  - **Targeting rules**: When you want to add or update a targenting rule, the &#x60;comparator&#x60;, &#x60;comparisonAttribute&#x60;, and &#x60;comparisonValue&#x60; members are required. - **Segment rules**: When you want to add add or update a segment rule, the &#x60;segmentId&#x60; which identifies the desired segment and the &#x60;segmentComparator&#x60; members are required.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagSettingValuesApi();
let configId = "configId_example"; // String | The identifier of the Config.
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
let updateSettingValuesWithIdModel = new ConfigCatPublicManagementApi.UpdateSettingValuesWithIdModel(); // UpdateSettingValuesWithIdModel | 
let opts = {
  'reason': "reason_example" // String | The reason note for the Audit Log if the Product's \"Config changes require a reason\" preference is turned on.
};
apiInstance.postSettingValues(configId, environmentId, updateSettingValuesWithIdModel, opts, (error, data, response) => {
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
 **configId** | **String**| The identifier of the Config. | 
 **environmentId** | **String**| The identifier of the Environment. | 
 **updateSettingValuesWithIdModel** | [**UpdateSettingValuesWithIdModel**](UpdateSettingValuesWithIdModel.md)|  | 
 **reason** | **String**| The reason note for the Audit Log if the Product&#39;s \&quot;Config changes require a reason\&quot; preference is turned on. | [optional] 

### Return type

[**ConfigSettingValuesModel**](ConfigSettingValuesModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## replaceSettingValue

> SettingValueModelHaljson replaceSettingValue(environmentId, settingId, updateSettingValueModel, opts)

Replace value

This endpoint replaces the whole value of a Feature Flag or Setting in a specified Environment.  Only the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are modifiable by this endpoint.  **Important:** As this endpoint is doing a complete replace, it&#39;s important to set every other attribute that you don&#39;t  want to change in its original state. Not listing one means that it will reset.  For example: We have the following resource. &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: false } &#x60;&#x60;&#x60; If we send a replace request body as below: &#x60;&#x60;&#x60; {  \&quot;value\&quot;: true } &#x60;&#x60;&#x60; Then besides that the default value is set to &#x60;true&#x60;, all the Percentage Rules are deleted.  So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: true } &#x60;&#x60;&#x60;  The &#x60;rolloutRules&#x60; property describes two types of rules:  - **Targeting rules**: When you want to add or update a targenting rule, the &#x60;comparator&#x60;, &#x60;comparisonAttribute&#x60;, and &#x60;comparisonValue&#x60; members are required. - **Segment rules**: When you want to add add or update a segment rule, the &#x60;segmentId&#x60; which identifies the desired segment and the &#x60;segmentComparator&#x60; members are required.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagSettingValuesApi();
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
let settingId = 56; // Number | The id of the Setting.
let updateSettingValueModel = {"rolloutPercentageItems":[{"percentage":30,"value":true},{"percentage":70,"value":false}],"value":true}; // UpdateSettingValueModel | 
let opts = {
  'reason': "reason_example" // String | The reason note for the Audit Log if the Product's \"Config changes require a reason\" preference is turned on.
};
apiInstance.replaceSettingValue(environmentId, settingId, updateSettingValueModel, opts, (error, data, response) => {
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
 **environmentId** | **String**| The identifier of the Environment. | 
 **settingId** | **Number**| The id of the Setting. | 
 **updateSettingValueModel** | [**UpdateSettingValueModel**](UpdateSettingValueModel.md)|  | 
 **reason** | **String**| The reason note for the Audit Log if the Product&#39;s \&quot;Config changes require a reason\&quot; preference is turned on. | [optional] 

### Return type

[**SettingValueModelHaljson**](SettingValueModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## updateSettingValue

> SettingValueModelHaljson updateSettingValue(environmentId, settingId, jsonPatch, opts)

Update value

This endpoint updates the value of a Feature Flag or Setting  with a collection of [JSON Patch](http://jsonpatch.com) operations in a specified Environment.  Only the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are modifiable by this endpoint.  The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don&#39;t want to change. It supports collection reordering, so it also  can be used for reordering the targeting rules of a Feature Flag or Setting.  For example: We have the following resource. &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: false } &#x60;&#x60;&#x60; If we send an update request body as below: &#x60;&#x60;&#x60; [  {   \&quot;op\&quot;: \&quot;replace\&quot;,   \&quot;path\&quot;: \&quot;/value\&quot;,   \&quot;value\&quot;: true  } ] &#x60;&#x60;&#x60; Only the default value is going to be set to &#x60;true&#x60; and all the Percentage Rules are remaining unchanged. So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: true } &#x60;&#x60;&#x60;  The &#x60;rolloutRules&#x60; property describes two types of rules:  - **Targeting rules**: When you want to add or update a targenting rule, the &#x60;comparator&#x60;, &#x60;comparisonAttribute&#x60;, and &#x60;comparisonValue&#x60; members are required. - **Segment rules**: When you want to add add or update a segment rule, the &#x60;segmentId&#x60; which identifies the desired segment and the &#x60;segmentComparator&#x60; members are required.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.FeatureFlagSettingValuesApi();
let environmentId = "environmentId_example"; // String | The identifier of the Environment.
let settingId = 56; // Number | The id of the Setting.
let jsonPatch = [{"op":"add","path":"/rolloutPercentageItems/-","value":{"percentage":30,"value":true}},{"op":"add","path":"/rolloutPercentageItems/-","value":{"percentage":70,"value":false}}]; // JsonPatch | 
let opts = {
  'reason': "reason_example" // String | The reason note for the Audit Log if the Product's \"Config changes require a reason\" preference is turned on.
};
apiInstance.updateSettingValue(environmentId, settingId, jsonPatch, opts, (error, data, response) => {
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
 **environmentId** | **String**| The identifier of the Environment. | 
 **settingId** | **Number**| The id of the Setting. | 
 **jsonPatch** | [**JsonPatch**](JsonPatch.md)|  | 
 **reason** | **String**| The reason note for the Audit Log if the Product&#39;s \&quot;Config changes require a reason\&quot; preference is turned on. | [optional] 

### Return type

[**SettingValueModelHaljson**](SettingValueModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json

