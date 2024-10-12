# CloudLifeSciencesApi.PersistentDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sizeGb** | **Number** | The size, in GB, of the disk to attach. If the size is not specified, a default is chosen to ensure reasonable I/O performance. If the disk type is specified as &#x60;local-ssd&#x60;, multiple local drives are automatically combined to provide the requested size. Note, however, that each physical SSD is 375GB in size, and no more than 8 drives can be attached to a single instance. | [optional] 
**sourceImage** | **String** | An image to put on the disk before attaching it to the VM. | [optional] 
**type** | **String** | The Compute Engine disk type. If unspecified, &#x60;pd-standard&#x60; is used. | [optional] 


