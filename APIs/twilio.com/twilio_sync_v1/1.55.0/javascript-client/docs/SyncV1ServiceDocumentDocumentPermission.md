# TwilioSync.SyncV1ServiceDocumentDocumentPermission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Document Permission resource. | [optional] 
**documentSid** | **String** | The SID of the Sync Document to which the Document Permission applies. | [optional] 
**identity** | **String** | The application-defined string that uniquely identifies the resource&#39;s User within the Service to an FPA token. | [optional] 
**manage** | **Boolean** | Whether the identity can delete the Sync Document. | [optional] 
**read** | **Boolean** | Whether the identity can read the Sync Document. | [optional] 
**serviceSid** | **String** | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with. | [optional] 
**url** | **String** | The absolute URL of the Sync Document Permission resource. | [optional] 
**write** | **Boolean** | Whether the identity can update the Sync Document. | [optional] 


