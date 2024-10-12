

# DistributionGroupWithUsersResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aadGroups** | [**List&lt;DistributionGroupWithUsersResponseAadGroupsInner&gt;**](DistributionGroupWithUsersResponseAadGroupsInner.md) | The distribution group aad groups |  [optional] |
|**id** | **UUID** | The unique ID of the distribution group |  |
|**isPublic** | **Boolean** | Whether the distribution group is public |  [optional] |
|**name** | **String** | The name of the distribution group used in URLs |  |
|**notifiedUserCount** | **BigDecimal** | The count of non-pending users in the distribution group who will be notified by new releases |  |
|**totalGroupsCount** | **BigDecimal** | The count of aad groups in the distribution group |  [optional] |
|**totalUserCount** | **BigDecimal** | The count of users in the distribution group |  |
|**users** | [**List&lt;DistributionGroupsListUsers200ResponseInner&gt;**](DistributionGroupsListUsers200ResponseInner.md) | The distribution group users |  |



