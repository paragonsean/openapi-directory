

# Iteration

Iteration model to be sent over JSON

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**classificationType** | [**ClassificationTypeEnum**](#ClassificationTypeEnum) | Gets the classification type of the project |  [optional] [readonly] |
|**created** | **OffsetDateTime** | Gets the time this iteration was completed |  [optional] [readonly] |
|**domainId** | **UUID** | Get or sets a guid of the domain the iteration has been trained on |  [optional] [readonly] |
|**exportable** | **Boolean** | Whether the iteration can be exported to another format for download |  [optional] [readonly] |
|**id** | **UUID** | Gets the id of the iteration |  [optional] [readonly] |
|**isDefault** | **Boolean** | Gets or sets a value indicating whether the iteration is the default iteration for the project |  [optional] |
|**lastModified** | **OffsetDateTime** | Gets the time this iteration was last modified |  [optional] [readonly] |
|**name** | **String** | Gets or sets the name of the iteration |  [optional] |
|**projectId** | **UUID** | Gets the project id of the iteration |  [optional] [readonly] |
|**status** | **String** | Gets the current iteration status |  [optional] [readonly] |
|**trainedAt** | **OffsetDateTime** | Gets the time this iteration was last modified |  [optional] [readonly] |



## Enum: ClassificationTypeEnum

| Name | Value |
|---- | -----|
| MULTICLASS | &quot;Multiclass&quot; |
| MULTILABEL | &quot;Multilabel&quot; |



