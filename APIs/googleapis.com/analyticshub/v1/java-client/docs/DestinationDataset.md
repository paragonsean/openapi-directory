

# DestinationDataset

Defines the destination bigquery dataset.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**datasetReference** | [**DestinationDatasetReference**](DestinationDatasetReference.md) |  |  [optional] |
|**description** | **String** | Optional. A user-friendly description of the dataset. |  [optional] |
|**friendlyName** | **String** | Optional. A descriptive name for the dataset. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. The labels associated with this dataset. You can use these to organize and group your datasets. You can set this property when inserting or updating a dataset. See https://cloud.google.com/resource-manager/docs/creating-managing-labels for more information. |  [optional] |
|**location** | **String** | Required. The geographic location where the dataset should reside. See https://cloud.google.com/bigquery/docs/locations for supported locations. |  [optional] |



