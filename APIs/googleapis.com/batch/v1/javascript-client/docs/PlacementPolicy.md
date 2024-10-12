# BatchApi.PlacementPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collocation** | **String** | UNSPECIFIED vs. COLLOCATED (default UNSPECIFIED). Use COLLOCATED when you want VMs to be located close to each other for low network latency between the VMs. No placement policy will be generated when collocation is UNSPECIFIED. | [optional] 
**maxDistance** | **String** | When specified, causes the job to fail if more than max_distance logical switches are required between VMs. Batch uses the most compact possible placement of VMs even when max_distance is not specified. An explicit max_distance makes that level of compactness a strict requirement. Not yet implemented | [optional] 


