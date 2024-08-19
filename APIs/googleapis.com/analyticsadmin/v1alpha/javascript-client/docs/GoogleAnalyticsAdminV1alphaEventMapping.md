# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaEventMapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventName** | **String** | Required. Name of the GA4 event. It must always be set. The max allowed display name length is 40 UTF-16 code units. | [optional] 
**maxEventCount** | **String** | The maximum number of times the event occurred. If not set, maximum event count won&#39;t be checked. | [optional] 
**maxEventValue** | **Number** | The maximum revenue generated due to the event. Revenue currency will be defined at the property level. If not set, maximum event value won&#39;t be checked. | [optional] 
**minEventCount** | **String** | At least one of the following four min/max values must be set. The values set will be ANDed together to qualify an event. The minimum number of times the event occurred. If not set, minimum event count won&#39;t be checked. | [optional] 
**minEventValue** | **Number** | The minimum revenue generated due to the event. Revenue currency will be defined at the property level. If not set, minimum event value won&#39;t be checked. | [optional] 


