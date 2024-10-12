

# GoogleCloudDialogflowV2beta1IntentMessageRbmCarouselCard

Carousel Rich Business Messaging (RBM) rich card. Rich cards allow you to respond to users with more vivid content, e.g. with media and suggestions. If you want to show a single card with more control over the layout, please use RbmStandaloneCard instead.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cardContents** | [**List&lt;GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent&gt;**](GoogleCloudDialogflowV2beta1IntentMessageRbmCardContent.md) | Required. The cards in the carousel. A carousel must have at least 2 cards and at most 10. |  [optional] |
|**cardWidth** | [**CardWidthEnum**](#CardWidthEnum) | Required. The width of the cards in the carousel. |  [optional] |



## Enum: CardWidthEnum

| Name | Value |
|---- | -----|
| CARD_WIDTH_UNSPECIFIED | &quot;CARD_WIDTH_UNSPECIFIED&quot; |
| SMALL | &quot;SMALL&quot; |
| MEDIUM | &quot;MEDIUM&quot; |



