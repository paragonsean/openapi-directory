

# ImageSizeRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**crop** | [**CropEnum**](#CropEnum) | Crop mode |  [optional] |
|**height** | **Integer** | Target image height |  [optional] |
|**resize** | [**ResizeEnum**](#ResizeEnum) | Resize method |  [optional] |
|**width** | **Integer** | Target image width |  [optional] |



## Enum: CropEnum

| Name | Value |
|---- | -----|
| TOP | &quot;top&quot; |
| BOTTOM | &quot;bottom&quot; |
| LEFT | &quot;left&quot; |
| RIGHT | &quot;right&quot; |
| CENTER | &quot;center&quot; |



## Enum: ResizeEnum

| Name | Value |
|---- | -----|
| CLIP | &quot;clip&quot; |
| CROP | &quot;crop&quot; |
| SCALE | &quot;scale&quot; |
| FILL | &quot;fill&quot; |



