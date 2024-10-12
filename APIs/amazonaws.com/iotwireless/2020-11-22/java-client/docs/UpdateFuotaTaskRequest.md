

# UpdateFuotaTaskRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of a FUOTA task. |  [optional] |
|**description** | **String** | The description of the new resource. |  [optional] |
|**loRaWAN** | [**CreateFuotaTaskRequestLoRaWAN**](CreateFuotaTaskRequestLoRaWAN.md) |  |  [optional] |
|**firmwareUpdateImage** | **String** | The S3 URI points to a firmware update image that is to be used with a FUOTA task. |  [optional] |
|**firmwareUpdateRole** | **String** | The firmware update role that is to be used with a FUOTA task. |  [optional] |
|**redundancyPercent** | **Integer** | The percentage of the added fragments that are redundant. For example, if the size of the firmware image file is 100 bytes and the fragment size is 10 bytes, with &lt;code&gt;RedundancyPercent&lt;/code&gt; set to 50(%), the final number of encoded fragments is (100 / 10) + (100 / 10 * 50%) &#x3D; 15. |  [optional] |
|**fragmentSizeBytes** | **Integer** | The size of each fragment in bytes. This parameter is supported only for FUOTA tasks with multicast groups. |  [optional] |
|**fragmentIntervalMS** | **Integer** | &lt;p&gt;The interval for sending fragments in milliseconds, rounded to the nearest second.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This interval only determines the timing for when the Cloud sends down the fragments to yor device. There can be a delay for when your device will receive these fragments. This delay depends on the device&#39;s class and the communication delay with the cloud.&lt;/p&gt; &lt;/note&gt; |  [optional] |



