# RubrikRestApi.VmwareVmMountSummaryV1

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachingDiskCount** | **Number** | An integer value that identifies how many disks are attached. | [optional] 
**createDatastoreOnlyMount** | **Boolean** | This boolean value determines whether or not the mount is created as a datastore only. When &#39;true,&#39; the mount is created with datastore and not the associated virtual machine. When &#39;false,&#39; the mount is created with both the datastore and the associated virtual machine. | [optional] 
**datastoreName** | **String** | The name of the datastore that contains the mounted VMDK. | [optional] 
**datastoreReady** | **Boolean** | A boolean value that specifies whether the datastore is ready. When &#39;true,&#39; the datastore is ready. When &#39;false,&#39; the datastore is not ready. | [optional] 
**hasAttachingDisk** | **Boolean** | A Boolean value that determines whether this job is an attaching disk mount job. When &#39;true,&#39; this is an attaching disk mount job. When &#39;false,&#39; this is not an attaching disk mount job. | [optional] 
**hostId** | **String** |  | [optional] 
**id** | **String** |  | 
**isReady** | **Boolean** |  | 
**mountRequestId** | **String** |  | [optional] 
**mountTimestamp** | **Date** | Gives the timestamp at which the mount was created. | [optional] 
**mountedVmId** | **String** |  | [optional] 
**snapshotDate** | **Date** |  | 
**unmountRequestId** | **String** |  | [optional] 
**vmId** | **String** |  | 


