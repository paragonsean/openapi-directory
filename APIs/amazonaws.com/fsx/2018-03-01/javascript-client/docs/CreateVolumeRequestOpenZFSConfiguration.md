# AmazonFsx.CreateVolumeRequestOpenZFSConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parentVolumeId** | **String** |  | 
**storageCapacityReservationGiB** | **Number** |  | [optional] 
**storageCapacityQuotaGiB** | **Number** |  | [optional] 
**recordSizeKiB** | **Number** |  | [optional] 
**dataCompressionType** | [**OpenZFSDataCompressionType**](OpenZFSDataCompressionType.md) |  | [optional] 
**copyTagsToSnapshots** | **Boolean** |  | [optional] 
**originSnapshot** | [**CreateOpenZFSVolumeConfigurationOriginSnapshot**](CreateOpenZFSVolumeConfigurationOriginSnapshot.md) |  | [optional] 
**readOnly** | **Boolean** |  | [optional] 
**nfsExports** | **Array** |  | [optional] 
**userAndGroupQuotas** | **Array** |  | [optional] 


