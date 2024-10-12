

# ApiResponseSuccess


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cost** | **BigDecimal** | Cost of the operation (mbIn + mbOut) * $.001 |  [optional] |
|**mbIn** | **BigDecimal** | The amount of megabytes of bandwidth used to process the pdf |  [optional] |
|**mbOut** | **BigDecimal** | The amount of megabytes of bandwidth generated from the resulting pdf |  [optional] |
|**pdf** | **String** | A url to the PDF that will exist only for 24 hours |  [optional] |
|**success** | **Boolean** | Will be true if the operation suceeded |  [optional] |



