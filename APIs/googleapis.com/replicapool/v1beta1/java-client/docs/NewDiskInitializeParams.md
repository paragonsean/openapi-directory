

# NewDiskInitializeParams

Initialization parameters for creating a new disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskSizeGb** | **String** | The size of the created disk in gigabytes. |  [optional] |
|**diskType** | **String** | Name of the disk type resource describing which disk type to use to create the disk. For example &#39;pd-ssd&#39; or &#39;pd-standard&#39;. Default is &#39;pd-standard&#39; |  [optional] |
|**sourceImage** | **String** | The name or fully-qualified URL of a source image to use to create this disk. If you provide a name of the source image, Replica Pool will look for an image with that name in your project. If you are specifying an image provided by Compute Engine, you will need to provide the full URL with the correct project, such as: http://www.googleapis.com/compute/v1/projects/debian-cloud/ global/images/debian-wheezy-7-vYYYYMMDD |  [optional] |



