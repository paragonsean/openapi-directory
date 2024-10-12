

# SyncV1ServiceSyncMapSyncMapPermission


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Sync Map Permission resource. |  [optional] |
|**identity** | **String** | The application-defined string that uniquely identifies the resource&#39;s User within the Service to an FPA token. |  [optional] |
|**manage** | **Boolean** | Whether the identity can delete the Sync Map. |  [optional] |
|**mapSid** | **String** | The SID of the Sync Map to which the Permission applies. |  [optional] |
|**read** | **Boolean** | Whether the identity can read the Sync Map and its Items. |  [optional] |
|**serviceSid** | **String** | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with. |  [optional] |
|**url** | **URI** | The absolute URL of the Sync Map Permission resource. |  [optional] |
|**write** | **Boolean** | Whether the identity can create, update, and delete Items in the Sync Map. |  [optional] |



