# AmazonConnectCustomerProfiles.PutIntegrationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **String** | The URI of the S3 bucket or any other type of data source. | [optional] 
**objectTypeName** | **String** | The name of the profile object type. | [optional] 
**tags** | **{String: String}** | The tags used to organize, track, or control access for this resource. | [optional] 
**flowDefinition** | [**PutIntegrationRequestFlowDefinition**](PutIntegrationRequestFlowDefinition.md) |  | [optional] 
**objectTypeNames** | **{String: String}** | A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an &lt;code&gt;ObjectTypeName&lt;/code&gt; (template) used to ingest the event. It supports the following event types: &lt;code&gt;SegmentIdentify&lt;/code&gt;, &lt;code&gt;ShopifyCreateCustomers&lt;/code&gt;, &lt;code&gt;ShopifyUpdateCustomers&lt;/code&gt;, &lt;code&gt;ShopifyCreateDraftOrders&lt;/code&gt;, &lt;code&gt;ShopifyUpdateDraftOrders&lt;/code&gt;, &lt;code&gt;ShopifyCreateOrders&lt;/code&gt;, and &lt;code&gt;ShopifyUpdatedOrders&lt;/code&gt;. | [optional] 


