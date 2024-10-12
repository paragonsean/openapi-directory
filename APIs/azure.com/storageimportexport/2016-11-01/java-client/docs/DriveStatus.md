

# DriveStatus

Provides information about the drive's status

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bitLockerKey** | **String** | The BitLocker key used to encrypt the drive. |  [optional] |
|**bytesSucceeded** | **Long** | Bytes successfully transferred for the drive. |  [optional] |
|**copyStatus** | **String** | Detailed status about the data transfer process. This field is not returned in the response until the drive is in the Transferring state. |  [optional] |
|**driveHeaderHash** | **String** | The drive header hash value. |  [optional] |
|**driveId** | **String** | The drive&#39;s hardware serial number, without spaces. |  [optional] |
|**errorLogUri** | **String** | A URI that points to the blob containing the error log for the data transfer operation. |  [optional] |
|**manifestFile** | **String** | The relative path of the manifest file on the drive.  |  [optional] |
|**manifestHash** | **String** | The Base16-encoded MD5 hash of the manifest file on the drive. |  [optional] |
|**manifestUri** | **String** | A URI that points to the blob containing the drive manifest file.  |  [optional] |
|**percentComplete** | **Integer** | Percentage completed for the drive.  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The drive&#39;s current state.  |  [optional] |
|**verboseLogUri** | **String** | A URI that points to the blob containing the verbose log for the data transfer operation.  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| SPECIFIED | &quot;Specified&quot; |
| RECEIVED | &quot;Received&quot; |
| NEVER_RECEIVED | &quot;NeverReceived&quot; |
| TRANSFERRING | &quot;Transferring&quot; |
| COMPLETED | &quot;Completed&quot; |
| COMPLETED_MORE_INFO | &quot;CompletedMoreInfo&quot; |
| SHIPPED_BACK | &quot;ShippedBack&quot; |



