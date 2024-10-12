

# ImageProcessingSettings

Represents image preprocessing settings used by image augmentation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**augmentationMethods** | **Map&lt;String, Boolean&gt;** | Gets or sets enabled image transforms. The key corresponds to the transform name. If value is set to true, then correspondent transform is enabled. Otherwise this transform will not be used.  Augmentation will be uniformly distributed among enabled transforms. |  [optional] |



