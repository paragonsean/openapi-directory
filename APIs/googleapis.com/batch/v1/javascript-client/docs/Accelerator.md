# BatchApi.Accelerator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **String** | The number of accelerators of this type. | [optional] 
**driverVersion** | **String** | Optional. The NVIDIA GPU driver version that should be installed for this type. You can define the specific driver version such as \&quot;470.103.01\&quot;, following the driver version requirements in https://cloud.google.com/compute/docs/gpus/install-drivers-gpu#minimum-driver. Batch will install the specific accelerator driver if qualified. | [optional] 
**installGpuDrivers** | **Boolean** | Deprecated: please use instances[0].install_gpu_drivers instead. | [optional] 
**type** | **String** | The accelerator type. For example, \&quot;nvidia-tesla-t4\&quot;. See &#x60;gcloud compute accelerator-types list&#x60;. | [optional] 


