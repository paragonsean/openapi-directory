# AmazonFsx.VolumeOpenZFSConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parentVolumeId** | **String** |  | [optional] 
**volumePath** | **String** |  | [optional] 
**storageCapacityReservationGiB** | **Number** |  | [optional] 
**storageCapacityQuotaGiB** | **Number** |  | [optional] 
**recordSizeKiB** | **Number** |  | [optional] 
**dataCompressionType** | [**OpenZFSDataCompressionType**](OpenZFSDataCompressionType.md) |  | [optional] 
**copyTagsToSnapshots** | **Boolean** |  | [optional] 
**originSnapshot** | [**OpenZFSVolumeConfigurationOriginSnapshot**](OpenZFSVolumeConfigurationOriginSnapshot.md) |  | [optional] 
**readOnly** | **Boolean** |  | [optional] 
**nfsExports** | **Array** |  | [optional] 
**userAndGroupQuotas** | **Array** |  | [optional] 
**restoreToSnapshot** | **String** |  | [optional] 
**deleteIntermediateSnaphots** | **Boolean** |  | [optional] 
**deleteClonedVolumes** | **Boolean** |  | [optional] 


