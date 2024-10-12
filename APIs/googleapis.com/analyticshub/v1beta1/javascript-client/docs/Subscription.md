# AnalyticsHubApi.Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **String** | Output only. Timestamp when the subscription was created. | [optional] [readonly] 
**dataExchange** | **String** | Output only. Resource name of the source Data Exchange. e.g. projects/123/locations/US/dataExchanges/456 | [optional] [readonly] 
**lastModifyTime** | **String** | Output only. Timestamp when the subscription was last modified. | [optional] [readonly] 
**linkedDatasetMap** | [**{String: LinkedResource}**](LinkedResource.md) | Output only. Map of listing resource names to associated linked resource, e.g. projects/123/locations/US/dataExchanges/456/listings/789 -&gt; projects/123/datasets/my_dataset For listing-level subscriptions, this is a map of size 1. Only contains values if state &#x3D;&#x3D; STATE_ACTIVE. | [optional] [readonly] 
**listing** | **String** | Output only. Resource name of the source Listing. e.g. projects/123/locations/US/dataExchanges/456/listings/789 | [optional] [readonly] 
**name** | **String** | Output only. The resource name of the subscription. e.g. &#x60;projects/myproject/locations/US/subscriptions/123&#x60;. | [optional] [readonly] 
**organizationDisplayName** | **String** | Output only. Display name of the project of this subscription. | [optional] [readonly] 
**organizationId** | **String** | Output only. Organization of the project this subscription belongs to. | [optional] [readonly] 
**state** | **String** | Output only. Current state of the subscription. | [optional] [readonly] 
**subscriberContact** | **String** | Output only. Email of the subscriber. | [optional] [readonly] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"STATE_ACTIVE"`)

* `STALE` (value: `"STATE_STALE"`)

* `INACTIVE` (value: `"STATE_INACTIVE"`)




