

# Accelerator

Carries information about an accelerator that can be attached to a VM.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **String** | How many accelerators of this type to attach. |  [optional] |
|**type** | **String** | The accelerator type string (for example, \&quot;nvidia-tesla-k80\&quot;). Only NVIDIA GPU accelerators are currently supported. If an NVIDIA GPU is attached, the required runtime libraries will be made available to all containers under &#x60;/usr/local/nvidia&#x60;. The driver version to install must be specified using the NVIDIA driver version parameter on the virtual machine specification. Note that attaching a GPU increases the worker VM startup time by a few minutes. |  [optional] |



