# DialogflowApi.GoogleCloudDialogflowCxV3beta1TestConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow** | **String** | Flow name to start the test case with. Format: &#x60;projects//locations//agents//flows/&#x60;. Only one of &#x60;flow&#x60; and &#x60;page&#x60; should be set to indicate the starting point of the test case. If both are set, &#x60;page&#x60; takes precedence over &#x60;flow&#x60;. If neither is set, the test case will start with start page on the default start flow. | [optional] 
**page** | **String** | The page to start the test case with. Format: &#x60;projects//locations//agents//flows//pages/&#x60;. Only one of &#x60;flow&#x60; and &#x60;page&#x60; should be set to indicate the starting point of the test case. If both are set, &#x60;page&#x60; takes precedence over &#x60;flow&#x60;. If neither is set, the test case will start with start page on the default start flow. | [optional] 
**trackingParameters** | **[String]** | Session parameters to be compared when calculating differences. | [optional] 


