# DataBoxManagementClient.DataBoxDiskJobDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copyProgress** | [**[DataBoxDiskCopyProgress]**](DataBoxDiskCopyProgress.md) | Copy progress per disk. | [optional] [readonly] 
**disksAndSizeDetails** | **{String: Number}** | Contains the map of disk serial number to the disk size being used for the job. Is returned only after the disks are shipped to the customer. | [optional] [readonly] 
**passkey** | **String** | User entered passkey for DataBox Disk job. | [optional] 
**preferredDisks** | **{String: Number}** | User preference on what size disks are needed for the job. The map is from the disk size in TB to the count. Eg. {2,5} means 5 disks of 2 TB size. Key is string but will be checked against an int. | [optional] 


