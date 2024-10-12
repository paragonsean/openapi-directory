

# LocationFilter

<p>Narrow down the list of resources returned by <code>ListLocations</code>. For example, to see all your Amazon S3 locations, create a filter using <code>\"Name\": \"LocationType\"</code>, <code>\"Operator\": \"Equals\"</code>, and <code>\"Values\": \"S3\"</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/datasync/latest/userguide/query-resources.html\">filtering resources</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**LocationFilterName**](LocationFilterName.md) |  |  |
|**values** | [**List**](List.md) |  |  |
|**operator** | [**Operator**](Operator.md) |  |  |



