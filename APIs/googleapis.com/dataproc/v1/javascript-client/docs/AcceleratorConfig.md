# CloudDataprocApi.AcceleratorConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceleratorCount** | **Number** | The number of the accelerator cards of this type exposed to this instance. | [optional] 
**acceleratorTypeUri** | **String** | Full URL, partial URI, or short name of the accelerator type resource to expose to this instance. See Compute Engine AcceleratorTypes (https://cloud.google.com/compute/docs/reference/v1/acceleratorTypes).Examples: https://www.googleapis.com/compute/v1/projects/[project_id]/zones/[zone]/acceleratorTypes/nvidia-tesla-k80 projects/[project_id]/zones/[zone]/acceleratorTypes/nvidia-tesla-k80 nvidia-tesla-k80Auto Zone Exception: If you are using the Dataproc Auto Zone Placement (https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone#using_auto_zone_placement) feature, you must use the short name of the accelerator type resource, for example, nvidia-tesla-k80. | [optional] 


