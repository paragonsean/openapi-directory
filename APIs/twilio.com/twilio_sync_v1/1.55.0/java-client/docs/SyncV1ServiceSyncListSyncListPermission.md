

# SyncV1ServiceSyncListSyncListPermission


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Sync List Permission resource. |  [optional] |
|**identity** | **String** | The application-defined string that uniquely identifies the resource&#39;s User within the Service to an FPA token. |  [optional] |
|**listSid** | **String** | The SID of the Sync List to which the Permission applies. |  [optional] |
|**manage** | **Boolean** | Whether the identity can delete the Sync List. |  [optional] |
|**read** | **Boolean** | Whether the identity can read the Sync List and its Items. |  [optional] |
|**serviceSid** | **String** | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with. |  [optional] |
|**url** | **URI** | The absolute URL of the Sync List Permission resource. |  [optional] |
|**write** | **Boolean** | Whether the identity can create, update, and delete Items in the Sync List. |  [optional] |



