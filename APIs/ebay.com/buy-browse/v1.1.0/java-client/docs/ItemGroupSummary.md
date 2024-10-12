

# ItemGroupSummary

The type that defines the fields for the details of each item in an item group. An item group is  an item that has various aspect differences, such as color, size, storage capacity, etc. When an item group is created, one of the item variations, such as the red shirt size L, is chosen as the \"parent\". All the other items in the group are the children, such as the blue shirt size L, red shirt size M, etc. <br /><br /><span class=\"tablenote\"><b> Note: </b> This container is returned only if the <b> item_id</b> in the request is an item group (parent ID of an item with variations).</span>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**itemGroupAdditionalImages** | [**List&lt;Image&gt;**](Image.md) | An array of containers with the URLs for images that are in addition to the primary image of the item group. The primary image is returned in the itemGroupImage field. |  [optional] |
|**itemGroupHref** | **String** | The HATEOAS reference of the parent page of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc. |  [optional] |
|**itemGroupId** | **String** | The unique identifier for the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc. |  [optional] |
|**itemGroupImage** | [**Image**](Image.md) |  |  [optional] |
|**itemGroupTitle** | **String** | The title of the item that appears on the item group page. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc. |  [optional] |
|**itemGroupType** | **String** | An enumeration value that indicates the type of the item group. An item group is an item that has various aspect differences, such as color, size, storage capacity, etc. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/buy/browse/types/gct:ItemGroupTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; |  [optional] |



