

# ResourcePermission

<p>Resource permission for a dataset. When you create a dataset, all the other members of the same user group inherit access to the dataset. You can only create a dataset if your user group has application permission for Create Datasets.</p> <p>The following is a list of valid dataset permissions that you can apply: </p> <ul> <li> <p> <code>ViewDatasetDetails</code> </p> </li> <li> <p> <code>ReadDatasetDetails</code> </p> </li> <li> <p> <code>AddDatasetData</code> </p> </li> <li> <p> <code>CreateDataView</code> </p> </li> <li> <p> <code>EditDatasetMetadata</code> </p> </li> <li> <p> <code>DeleteDataset</code> </p> </li> </ul> <p>For more information on the dataset permissions, see <a href=\"https://docs.aws.amazon.com/finspace/latest/userguide/managing-user-permissions.html#supported-dataset-permissions\">Supported Dataset Permissions</a> in the FinSpace User Guide.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**permission** | [**String**](String.md) |  |  [optional] |



