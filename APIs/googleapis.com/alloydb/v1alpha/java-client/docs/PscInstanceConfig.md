

# PscInstanceConfig

PscInstanceConfig contains PSC related configuration at an instance level.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedConsumerNetworks** | **List&lt;String&gt;** | Optional. List of consumer networks that are allowed to create PSC endpoints to service-attachments to this instance. |  [optional] |
|**allowedConsumerProjects** | **List&lt;String&gt;** | Optional. List of consumer projects that are allowed to create PSC endpoints to service-attachments to this instance. |  [optional] |
|**outgoingServiceAttachmentLinks** | **List&lt;String&gt;** | Optional. List of service attachments that this instance has created endpoints to connect with. Currently, only a single outgoing service attachment is supported per instance. |  [optional] |
|**pscEnabled** | **Boolean** | Optional. Whether PSC connectivity is enabled for this instance. This is populated by referencing the value from the parent cluster. |  [optional] |
|**pscInterfaceConfigs** | [**List&lt;PscInterfaceConfig&gt;**](PscInterfaceConfig.md) | Optional. Configurations for setting up PSC interfaces attached to the instance which are used for outbound connectivity. Only primary instances can have PSC interface attached. All the VMs created for the primary instance will share the same configurations. Currently we only support 0 or 1 PSC interface. |  [optional] |
|**serviceAttachmentLink** | **String** | Output only. The service attachment created when Private Service Connect (PSC) is enabled for the instance. The name of the resource will be in the format of &#x60;projects//regions//serviceAttachments/&#x60; |  [optional] [readonly] |



