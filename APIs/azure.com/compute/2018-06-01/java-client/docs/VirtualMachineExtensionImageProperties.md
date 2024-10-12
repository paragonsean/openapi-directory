

# VirtualMachineExtensionImageProperties

Describes the properties of a Virtual Machine Extension Image.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computeRole** | **String** | The type of role (IaaS or PaaS) this extension supports. |  |
|**handlerSchema** | **String** | The schema defined by publisher, where extension consumers should provide settings in a matching schema. |  |
|**operatingSystem** | **String** | The operating system this extension supports. |  |
|**supportsMultipleExtensions** | **Boolean** | Whether the handler can support multiple extensions. |  [optional] |
|**vmScaleSetEnabled** | **Boolean** | Whether the extension can be used on xRP VMScaleSets. By default existing extensions are usable on scalesets, but there might be cases where a publisher wants to explicitly indicate the extension is only enabled for CRP VMs but not VMSS. |  [optional] |



