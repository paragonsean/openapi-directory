

# AdminDimension

A custom dimension is additional numeric metadata that you want to affect Vectara's scoring.  For example, these could be \"number of stars\" ratings, or other business metrics like a product's margins that you want to use to boost where a result is in the list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description for the custom dimension. |  [optional] |
|**indexingDefault** | **Double** | The default value to give to documents for this custom dimension. |  [optional] |
|**name** | **String** | The name of the custom dimension.  The maximum length of the name is 8 characters. |  [optional] |
|**servingDefault** | **Double** | The default weight to give this dimension when running queries. A value of 0.0, for example, gives it no weight at all. |  [optional] |



