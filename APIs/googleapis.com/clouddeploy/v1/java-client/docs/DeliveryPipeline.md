

# DeliveryPipeline

A `DeliveryPipeline` resource in the Cloud Deploy API. A `DeliveryPipeline` defines a pipeline through which a Skaffold configuration can progress.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. |  [optional] |
|**condition** | [**PipelineCondition**](PipelineCondition.md) |  |  [optional] |
|**createTime** | **String** | Output only. Time at which the pipeline was created. |  [optional] [readonly] |
|**description** | **String** | Description of the &#x60;DeliveryPipeline&#x60;. Max length is 255 characters. |  [optional] |
|**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;&#x3D; 128 bytes. |  [optional] |
|**name** | **String** | Optional. Name of the &#x60;DeliveryPipeline&#x60;. Format is &#x60;projects/{project}/locations/{location}/deliveryPipelines/a-z{0,62}&#x60;. |  [optional] |
|**serialPipeline** | [**SerialPipeline**](SerialPipeline.md) |  |  [optional] |
|**suspended** | **Boolean** | When suspended, no new releases or rollouts can be created, but in-progress ones will complete. |  [optional] |
|**uid** | **String** | Output only. Unique identifier of the &#x60;DeliveryPipeline&#x60;. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Most recent time at which the pipeline was updated. |  [optional] [readonly] |



