# ApigeeApi.GoogleCloudApigeeV1Quota

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **String** | Required. Time interval over which the number of request messages is calculated. | [optional] 
**limit** | **String** | Required. Upper limit allowed for the time interval and time unit specified. Requests exceeding this limit will be rejected. | [optional] 
**timeUnit** | **String** | Time unit defined for the &#x60;interval&#x60;. Valid values include &#x60;minute&#x60;, &#x60;hour&#x60;, &#x60;day&#x60;, or &#x60;month&#x60;. If &#x60;limit&#x60; and &#x60;interval&#x60; are valid, the default value is &#x60;hour&#x60;; otherwise, the default is null. | [optional] 


