# TwilioSync.SyncV1ServiceSyncMapSyncMapItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Map Item resource. | [optional] 
**createdBy** | **String** | The identity of the Map Item&#39;s creator. If the Map Item is created from the client SDK, the value matches the Access Token&#39;s &#x60;identity&#x60; field. If the Map Item was created from the REST API, the value is &#x60;system&#x60;. | [optional] 
**data** | **Object** | An arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**dateExpires** | **Date** | The date and time in GMT when the Map Item expires and will be deleted, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. If the Map Item does not expire, this value is &#x60;null&#x60;.  The Map Item might not be deleted immediately after it expires. | [optional] 
**dateUpdated** | **Date** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**key** | **String** | The unique, user-defined key for the Map Item. | [optional] 
**mapSid** | **String** | The SID of the Sync Map that contains the Map Item. | [optional] 
**revision** | **String** | The current revision of the Map Item, represented as a string. | [optional] 
**serviceSid** | **String** | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with. | [optional] 
**url** | **String** | The absolute URL of the Map Item resource. | [optional] 


