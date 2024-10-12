

# Group

<p>A resource group that contains Amazon Web Services resources. You can assign resources to the group by associating either of the following elements with the group:</p> <ul> <li> <p> <a>ResourceQuery</a> - Use a resource query to specify a set of tag keys and values. All resources in the same Amazon Web Services Region and Amazon Web Services account that have those keys with the same values are included in the group. You can add a resource query when you create the group, or later by using the <a>PutGroupConfiguration</a> operation.</p> </li> <li> <p> <a>GroupConfiguration</a> - Use a service configuration to associate the group with an Amazon Web Services service. The configuration specifies which resource types can be included in the group.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupArn** | [**String**](String.md) |  |  |
|**name** | [**String**](String.md) |  |  |
|**description** | [**String**](String.md) |  |  [optional] |



