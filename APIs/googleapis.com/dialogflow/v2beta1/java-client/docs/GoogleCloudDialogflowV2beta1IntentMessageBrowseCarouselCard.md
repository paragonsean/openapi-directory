

# GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCard

Browse Carousel Card for Actions on Google. https://developers.google.com/actions/assistant/responses#browsing_carousel

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageDisplayOptions** | [**ImageDisplayOptionsEnum**](#ImageDisplayOptionsEnum) | Optional. Settings for displaying the image. Applies to every image in items. |  [optional] |
|**items** | [**List&lt;GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItem&gt;**](GoogleCloudDialogflowV2beta1IntentMessageBrowseCarouselCardBrowseCarouselCardItem.md) | Required. List of items in the Browse Carousel Card. Minimum of two items, maximum of ten. |  [optional] |



## Enum: ImageDisplayOptionsEnum

| Name | Value |
|---- | -----|
| IMAGE_DISPLAY_OPTIONS_UNSPECIFIED | &quot;IMAGE_DISPLAY_OPTIONS_UNSPECIFIED&quot; |
| GRAY | &quot;GRAY&quot; |
| WHITE | &quot;WHITE&quot; |
| CROPPED | &quot;CROPPED&quot; |
| BLURRED_BACKGROUND | &quot;BLURRED_BACKGROUND&quot; |



