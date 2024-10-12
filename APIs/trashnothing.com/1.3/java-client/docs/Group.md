

# Group

Groups are run by volunteer moderators and provide a way to group activity in a specific location. Because each group is usually run by different people, there can be variations in rules from group to group (eg. who is allowed to join, what is allowed to be posted, how often reposts are allowed). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | [**GroupCountry**](GroupCountry.md) |  |  [optional] |
|**groupId** | **String** |  |  [optional] |
|**hasQuestions** | **Boolean** | When true, anyone requesting membership to this group will be required to answer a new membership questionnaire. |  [optional] |
|**homepage** | **String** | A URL to the group homepage. |  [optional] |
|**identifier** | **String** | A unique identifier for the group that is used in URLs. |  [optional] |
|**latitude** | **BigDecimal** |  |  [optional] |
|**longitude** | **BigDecimal** |  |  [optional] |
|**memberCount** | **Integer** | The number of members who belong to the group. |  [optional] |
|**membership** | [**GroupMembership**](GroupMembership.md) |  |  [optional] |
|**name** | **String** | The name of the group (not guaranteed to be unique). |  [optional] |
|**openArchives** | **Boolean** | When true, the group posts are viewable by anyone.  When false, the group posts can only be viewed by members of the group. |  [optional] |
|**openMembership** | **Boolean** | When true, the group allows anyone to join.  When false, the group moderators review and approve applicants. |  [optional] |
|**region** | [**GroupRegion**](GroupRegion.md) |  |  [optional] |
|**timezone** | **String** | The timezone that the group is in (eg. America/New_York). |  [optional] |



