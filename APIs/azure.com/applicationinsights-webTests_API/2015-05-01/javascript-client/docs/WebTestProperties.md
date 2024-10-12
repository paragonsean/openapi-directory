# ApplicationInsightsManagementClient.WebTestProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**WebTestPropertiesConfiguration**](WebTestPropertiesConfiguration.md) |  | [optional] 
**description** | **String** | Purpose/user defined descriptive test for this WebTest. | [optional] 
**enabled** | **Boolean** | Is the test actively being monitored. | [optional] 
**frequency** | **Number** | Interval in seconds between test runs for this WebTest. Default value is 300. | [optional] [default to 300]
**kind** | **String** | The kind of web test this is, valid choices are ping and multistep. | [default to &#39;ping&#39;]
**locations** | [**[WebTestGeolocation]**](WebTestGeolocation.md) | A list of where to physically run the tests from to give global coverage for accessibility of your application. | 
**name** | **String** | User defined name if this WebTest. | 
**retryEnabled** | **Boolean** | Allow for retries should this WebTest fail. | [optional] 
**syntheticMonitorId** | **String** | Unique ID of this WebTest. This is typically the same value as the Name field. | 
**timeout** | **Number** | Seconds until this WebTest will timeout and fail. Default value is 30. | [optional] [default to 30]
**provisioningState** | **String** | Current state of this component, whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed. | [optional] [readonly] 



## Enum: KindEnum


* `ping` (value: `"ping"`)

* `multistep` (value: `"multistep"`)




