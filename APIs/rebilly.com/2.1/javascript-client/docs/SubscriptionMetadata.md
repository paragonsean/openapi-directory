# RebillyRestApi.SubscriptionMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**[SubscriptionMetadataEmbeddedInner]**](SubscriptionMetadataEmbeddedInner.md) | Any embedded objects available that are requested by the &#x60;expand&#x60; querystring parameter. | [optional] [readonly] 
**links** | [**[SubscriptionMetadataLinksInner]**](SubscriptionMetadataLinksInner.md) | The links related to resource. | [optional] [readonly] 
**createdTime** | **Date** | Order created time. | [optional] [readonly] 
**customFields** | **Object** | Custom Fields list as a map &#x60;{\&quot;custom field name\&quot;: \&quot;custom field value\&quot;, ...}&#x60;. The format must follow the saved format (see Custom Fields section for the formats).  | [optional] 
**revision** | **Number** | The number of times the order data has been modified. The revision is useful when analyzing webhook data to determine if the change takes precedence over the current representation.  | [optional] [readonly] 
**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) | Risk metadata. If null, the value would coalesce to the risk metadata captured when creating the payment token. | [optional] 
**updatedTime** | **Date** | Order updated time. | [optional] [readonly] 


