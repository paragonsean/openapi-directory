# BatchApi.InstancePolicyOrTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installGpuDrivers** | **Boolean** | Set this field true if users want Batch to help fetch drivers from a third party location and install them for GPUs specified in policy.accelerators or instance_template on their behalf. Default is false. For Container-Optimized Image cases, Batch will install the accelerator driver following milestones of https://cloud.google.com/container-optimized-os/docs/release-notes. For non Container-Optimized Image cases, following https://github.com/GoogleCloudPlatform/compute-gpu-installation/blob/main/linux/install_gpu_driver.py. | [optional] 
**instanceTemplate** | **String** | Name of an instance template used to create VMs. Named the field as &#39;instance_template&#39; instead of &#39;template&#39; to avoid c++ keyword conflict. | [optional] 
**policy** | [**InstancePolicy**](InstancePolicy.md) |  | [optional] 


