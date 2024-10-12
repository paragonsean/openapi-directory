

# WipeDeviceRequest

Request message for wiping all data on the device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customer** | **String** | Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you&#39;re using this API for your own organization, use &#x60;customers/my_customer&#x60; If you&#39;re using this API to manage another organization, use &#x60;customers/{customer_id}&#x60;, where customer_id is the customer to whom the device belongs. |  [optional] |
|**removeResetLock** | **Boolean** | Optional. Specifies if a user is able to factory reset a device after a Device Wipe. On iOS, this is called \&quot;Activation Lock\&quot;, while on Android, this is known as \&quot;Factory Reset Protection\&quot;. If true, this protection will be removed from the device, so that a user can successfully factory reset. If false, the setting is untouched on the device. |  [optional] |



