# CrossbrowsertestingComScreenshotComparisonsApi.DefaultApi

All URIs are relative to *https://crossbrowsertesting.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet**](DefaultApi.md#screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet) | **GET** /screenshots/{target_screenshot_test_id}/{target_version_id}/comparison/{base_result_id} | Compare Full Screenshot Test
[**screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet**](DefaultApi.md#screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet) | **GET** /screenshots/{target_screenshot_test_id}/{target_version_id}/comparison/parallel/{base_version_id} | Compare Screenshot Test Versions
[**screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet**](DefaultApi.md#screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet) | **GET** /screenshots/{target_screenshot_test_id}/{target_version_id}/{target_result_id}/comparison/{base_result_id} | Compare Single Screenshot



## screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet

> FullComparisonTest screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet(targetScreenshotTestId, targetVersionId, baseResultId, opts)

Compare Full Screenshot Test

Get comparison results for all browsers in target screenshot test against a base screenshot result. The base result can be from the same test or from another test run at an earlier time. This is a one-to-many comparison.

### Example

```javascript
import CrossbrowsertestingComScreenshotComparisonsApi from 'crossbrowsertesting_com_screenshot_comparisons_api';
let defaultClient = CrossbrowsertestingComScreenshotComparisonsApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CrossbrowsertestingComScreenshotComparisonsApi.DefaultApi();
let targetScreenshotTestId = 56; // Number | test id of the target Screenshot Test
let targetVersionId = 56; // Number | version id of the target Screenshot Test
let baseResultId = 56; // Number | result id of the base Screenshot Test
let opts = {
  'format': "'json'", // String | The format of the returned data. Possible values are \"json\" or \"jsonp\".
  'callback': "callback_example", // String | Name of callback method for JSONP requests.
  'tolerance': 30 // Number | Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences.
};
apiInstance.screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet(targetScreenshotTestId, targetVersionId, baseResultId, opts, (error, data, response) => {
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
 **targetScreenshotTestId** | **Number**| test id of the target Screenshot Test | 
 **targetVersionId** | **Number**| version id of the target Screenshot Test | 
 **baseResultId** | **Number**| result id of the base Screenshot Test | 
 **format** | **String**| The format of the returned data. Possible values are \&quot;json\&quot; or \&quot;jsonp\&quot;. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| Name of callback method for JSONP requests. | [optional] 
 **tolerance** | **Number**| Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences. | [optional] [default to 30]

### Return type

[**FullComparisonTest**](FullComparisonTest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet

> [SingleComparisonTest] screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet(targetScreenshotTestId, targetVersionId, baseVersionId, opts)

Compare Screenshot Test Versions

Get comparison results for all browsers in target screenshot test against the same browser in the base screenshot test. This is a good method for regression testing. For example, you&#39;ve run a screenshot test against a set of browsers that is \&quot;good\&quot;. Then, after some changes, you run a new screenshot test against the same set of browsers. This method will compare each of the same browsers against each other. For example, IE9 will be compared to IE9 from an earlier test. This is a many-to-many comparison where the OS/Browser/Resolution must match between the two test versions in order for the comparison to return results. The two versions can be from the same screenshot_test_id or not.

### Example

```javascript
import CrossbrowsertestingComScreenshotComparisonsApi from 'crossbrowsertesting_com_screenshot_comparisons_api';
let defaultClient = CrossbrowsertestingComScreenshotComparisonsApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CrossbrowsertestingComScreenshotComparisonsApi.DefaultApi();
let targetScreenshotTestId = 56; // Number | test id of the target Screenshot Test
let targetVersionId = 56; // Number | version id of the target Screenshot Test
let baseVersionId = 56; // Number | version id of the base Screenshot Test
let opts = {
  'format': "'json'", // String | The format of the returned data. Possible values are \"json\" or \"jsonp\".
  'callback': "callback_example", // String | Name of callback method for JSONP requests.
  'tolerance': 30 // Number | Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences.
};
apiInstance.screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet(targetScreenshotTestId, targetVersionId, baseVersionId, opts, (error, data, response) => {
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
 **targetScreenshotTestId** | **Number**| test id of the target Screenshot Test | 
 **targetVersionId** | **Number**| version id of the target Screenshot Test | 
 **baseVersionId** | **Number**| version id of the base Screenshot Test | 
 **format** | **String**| The format of the returned data. Possible values are \&quot;json\&quot; or \&quot;jsonp\&quot;. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| Name of callback method for JSONP requests. | [optional] 
 **tolerance** | **Number**| Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences. | [optional] [default to 30]

### Return type

[**[SingleComparisonTest]**](SingleComparisonTest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet

> SingleComparisonTest screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet(targetScreenshotTestId, targetVersionId, targetResultId, baseResultId, opts)

Compare Single Screenshot

Get comparison results for a single target screenshot result against a base screenshot result. This is a one-to-one comparison.

### Example

```javascript
import CrossbrowsertestingComScreenshotComparisonsApi from 'crossbrowsertesting_com_screenshot_comparisons_api';
let defaultClient = CrossbrowsertestingComScreenshotComparisonsApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CrossbrowsertestingComScreenshotComparisonsApi.DefaultApi();
let targetScreenshotTestId = 56; // Number | test id of the target Screenshot Test
let targetVersionId = 56; // Number | version id of the target Screenshot Test
let targetResultId = 56; // Number | result id of the target Screenshot Test
let baseResultId = 56; // Number | result id of the base Screenshot Test
let opts = {
  'format': "'json'", // String | The format of the returned data. Possible values are \"json\" or \"jsonp\".
  'callback': "callback_example", // String | Name of callback method for JSONP requests.
  'tolerance': 30 // Number | Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences.
};
apiInstance.screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet(targetScreenshotTestId, targetVersionId, targetResultId, baseResultId, opts, (error, data, response) => {
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
 **targetScreenshotTestId** | **Number**| test id of the target Screenshot Test | 
 **targetVersionId** | **Number**| version id of the target Screenshot Test | 
 **targetResultId** | **Number**| result id of the target Screenshot Test | 
 **baseResultId** | **Number**| result id of the base Screenshot Test | 
 **format** | **String**| The format of the returned data. Possible values are \&quot;json\&quot; or \&quot;jsonp\&quot;. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| Name of callback method for JSONP requests. | [optional] 
 **tolerance** | **Number**| Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences. | [optional] [default to 30]

### Return type

[**SingleComparisonTest**](SingleComparisonTest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

