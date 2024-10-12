

# Paragraph

A StructuralElement representing a paragraph. A paragraph is a range of content that's terminated with a newline character.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bullet** | [**Bullet**](Bullet.md) |  |  [optional] |
|**elements** | [**List&lt;ParagraphElement&gt;**](ParagraphElement.md) | The content of the paragraph, broken down into its component parts. |  [optional] |
|**paragraphStyle** | [**ParagraphStyle**](ParagraphStyle.md) |  |  [optional] |
|**positionedObjectIds** | **List&lt;String&gt;** | The IDs of the positioned objects tethered to this paragraph. |  [optional] |
|**suggestedBulletChanges** | [**Map&lt;String, SuggestedBullet&gt;**](SuggestedBullet.md) | The suggested changes to this paragraph&#39;s bullet. |  [optional] |
|**suggestedParagraphStyleChanges** | [**Map&lt;String, SuggestedParagraphStyle&gt;**](SuggestedParagraphStyle.md) | The suggested paragraph style changes to this paragraph, keyed by suggestion ID. |  [optional] |
|**suggestedPositionedObjectIds** | [**Map&lt;String, ObjectReferences&gt;**](ObjectReferences.md) | The IDs of the positioned objects suggested to be attached to this paragraph, keyed by suggestion ID. |  [optional] |



