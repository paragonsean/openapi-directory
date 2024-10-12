

# Dataset


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**available** | **Boolean** |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Date and time that the dataset was created. |  [optional] |
|**id** | **Long** |  |  |
|**labelSummary** | [**LabelSummary**](LabelSummary.md) |  |  [optional] |
|**language** | **String** | Dataset language. |  [optional] |
|**name** | **String** |  |  |
|**numOfDuplicates** | **Integer** | Number of duplicate images. This number includes duplicates in the .zip file from which the dataset was created plus the number of duplicate images from subsequent PUT calls to add images to the dataset. |  [optional] |
|**_object** | **String** | Object returned; in this case, dataset. |  [optional] |
|**statusMsg** | **String** |  |  [optional] |
|**totalExamples** | **Integer** | Total number of examples in the dataset. |  [optional] |
|**totalLabels** | **Integer** | Total number of labels in the dataset. |  [optional] |
|**type** | **String** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] |



