

# Fileshare


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | The size of the file share in gigabyte. |  [optional] |
|**createdDate** | **String** | The timestamp when the file share was created. |  [optional] |
|**fsName** | **String** | The name of the file share. |  [optional] |
|**hostPath** | **String** | The path to the volume on the host node. |  [optional] |
|**iops** | **Double** | The number of Input/Output operations per second.  |  [optional] |
|**iopsTotal** | **Integer** | The total number of IOPS considering the size of the file share. The size of your file share in gigabyte multiplied with the number of IOPS indicates the total number of IOPS. The higher the number of IOPS the faster you can read from and write to your volumes. |  [optional] |
|**orderId** | **String** | The ID received from softlayer when the file share was ordered to be set up in softlayer. |  [optional] |
|**provider** | **String** | The provider of the file share. |  [optional] |
|**spaceGuid** | **String** | The unique ID representing a Bluemix space in which the file share was created. |  [optional] |
|**state** | **String** | The current state of the file share. When the file share is ready to be used, this attribute is set to &#x60;READY&#x60;. |  [optional] |
|**updatedDate** | **String** | The timestamp when the file share last was updated. |  [optional] |



