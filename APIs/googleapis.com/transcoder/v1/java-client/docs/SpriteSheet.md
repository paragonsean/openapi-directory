

# SpriteSheet

Sprite sheet configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnCount** | **Integer** | The maximum number of sprites per row in a sprite sheet. The default is 0, which indicates no maximum limit. |  [optional] |
|**endTimeOffset** | **String** | End time in seconds, relative to the output file timeline. When &#x60;end_time_offset&#x60; is not specified, the sprites are generated until the end of the output file. |  [optional] |
|**filePrefix** | **String** | Required. File name prefix for the generated sprite sheets. Each sprite sheet has an incremental 10-digit zero-padded suffix starting from 0 before the extension, such as &#x60;sprite_sheet0000000123.jpeg&#x60;. |  [optional] |
|**format** | **String** | Format type. The default is &#x60;jpeg&#x60;. Supported formats: - &#x60;jpeg&#x60; |  [optional] |
|**interval** | **String** | Starting from &#x60;0s&#x60;, create sprites at regular intervals. Specify the interval value in seconds. |  [optional] |
|**quality** | **Integer** | The quality of the generated sprite sheet. Enter a value between 1 and 100, where 1 is the lowest quality and 100 is the highest quality. The default is 100. A high quality value corresponds to a low image data compression ratio. |  [optional] |
|**rowCount** | **Integer** | The maximum number of rows per sprite sheet. When the sprite sheet is full, a new sprite sheet is created. The default is 0, which indicates no maximum limit. |  [optional] |
|**spriteHeightPixels** | **Integer** | Required. The height of sprite in pixels. Must be an even integer. To preserve the source aspect ratio, set the SpriteSheet.sprite_height_pixels field or the SpriteSheet.sprite_width_pixels field, but not both (the API will automatically calculate the missing field). For portrait videos that contain horizontal ASR and rotation metadata, provide the height, in pixels, per the horizontal ASR. The API calculates the width per the horizontal ASR. The API detects any rotation metadata and swaps the requested height and width for the output. |  [optional] |
|**spriteWidthPixels** | **Integer** | Required. The width of sprite in pixels. Must be an even integer. To preserve the source aspect ratio, set the SpriteSheet.sprite_width_pixels field or the SpriteSheet.sprite_height_pixels field, but not both (the API will automatically calculate the missing field). For portrait videos that contain horizontal ASR and rotation metadata, provide the width, in pixels, per the horizontal ASR. The API calculates the height per the horizontal ASR. The API detects any rotation metadata and swaps the requested height and width for the output. |  [optional] |
|**startTimeOffset** | **String** | Start time in seconds, relative to the output file timeline. Determines the first sprite to pick. The default is &#x60;0s&#x60;. |  [optional] |
|**totalCount** | **Integer** | Total number of sprites. Create the specified number of sprites distributed evenly across the timeline of the output media. The default is 100. |  [optional] |



