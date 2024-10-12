

# PublishDevicesRequest

The publising information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountServiceConnectionId** | **String** | The service_connection_id of the stored Apple credentials instead of username, password. |  [optional] |
|**devices** | **List&lt;String&gt;** | Array of device UDID&#39;s to be published to the Apple Developer account. |  [optional] |
|**password** | **String** | The password for the Apple Developer account to publish the devices to. |  [optional] |
|**publishAllDevices** | **Boolean** | When set to true, all unprovisioned devices will be published to the Apple Developer account.  When false, only the provided devices will be published to the Apple Developer account. |  [optional] |
|**username** | **String** | The username for the Apple Developer account to publish the devices to. |  [optional] |



