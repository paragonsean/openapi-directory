# TwilioSync.SyncV1ServiceDocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Document resource. | [optional] 
**createdBy** | **String** | The identity of the Sync Document&#39;s creator. If the Sync Document is created from the client SDK, the value matches the Access Token&#39;s &#x60;identity&#x60; field. If the Sync Document was created from the REST API, the value is &#x60;system&#x60;. | [optional] 
**data** | **Object** | An arbitrary, schema-less object that the Sync Document stores. Can be up to 16 KiB in length. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateExpires** | **Date** | The date and time in GMT when the Sync Document expires and will be deleted, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. If the Sync Document does not expire, this value is &#x60;null&#x60;. The Document resource might not be deleted immediately after it expires. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**links** | **Object** | The URLs of resources related to the Sync Document. | [optional] 
**revision** | **String** | The current revision of the Sync Document, represented as a string. The &#x60;revision&#x60; property is used with conditional updates to ensure data consistency. | [optional] 
**serviceSid** | **String** | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the Document resource. | [optional] 
**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource and can be up to 320 characters long. | [optional] 
**url** | **String** | The absolute URL of the Document resource. | [optional] 


