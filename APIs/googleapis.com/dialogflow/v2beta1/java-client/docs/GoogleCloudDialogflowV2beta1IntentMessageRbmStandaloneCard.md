

# GoogleCloudDialogflowV2beta1IntentMessageRbmStandaloneCard

Standalone Rich Business Messaging (RBM) rich card. Rich cards allow you to respond to users with more vivid content, e.g. with media and suggestions. You can group multiple rich cards into one using RbmCarouselCard but carousel cards will give you less control over the card layout.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardContent** | [**GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent**](GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent.md) |  |  [optional] |
|**cardOrientation** | [**CardOrientationEnum**](#CardOrientationEnum) | Required. Orientation of the card. |  [optional] |
|**thumbnailImageAlignment** | [**ThumbnailImageAlignmentEnum**](#ThumbnailImageAlignmentEnum) | Required if orientation is horizontal. Image preview alignment for standalone cards with horizontal layout. |  [optional] |



## Enum: CardOrientationEnum

| Name | Value |
|---- | -----|
| CARD_ORIENTATION_UNSPECIFIED | &quot;CARD_ORIENTATION_UNSPECIFIED&quot; |
| HORIZONTAL | &quot;HORIZONTAL&quot; |
| VERTICAL | &quot;VERTICAL&quot; |



## Enum: ThumbnailImageAlignmentEnum

| Name | Value |
|---- | -----|
| THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED | &quot;THUMBNAIL_IMAGE_ALIGNMENT_UNSPECIFIED&quot; |
| LEFT | &quot;LEFT&quot; |
| RIGHT | &quot;RIGHT&quot; |



