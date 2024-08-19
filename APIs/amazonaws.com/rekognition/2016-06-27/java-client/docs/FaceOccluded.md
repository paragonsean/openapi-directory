

# FaceOccluded

<p> <code>FaceOccluded</code> should return \"true\" with a high confidence score if a detected face’s eyes, nose, and mouth are partially captured or if they are covered by masks, dark sunglasses, cell phones, hands, or other objects. <code>FaceOccluded</code> should return \"false\" with a high confidence score if common occurrences that do not impact face verification are detected, such as eye glasses, lightly tinted sunglasses, strands of hair, and others. </p> <p>You can use <code>FaceOccluded</code> to determine if an obstruction on a face negatively impacts using the image for face matching.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**value** | [**Boolean**](Boolean.md) |  |  [optional] |
|**confidence** | [**Float**](Float.md) |  |  [optional] |



