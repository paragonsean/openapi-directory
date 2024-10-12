

# GroupsV2GroupQuery

NOTE: GroupQuery, as of Destiny 2, has essentially two totally different and incompatible \"modes\".  If you are querying for a group, you can pass any of the properties below.  If you are querying for a Clan, you MUST NOT pass any of the following properties (they must be null or undefined in your request, not just empty string/default values):  - groupMemberCountFilter - localeFilter - tagText  If you pass these, you will get a useless InvalidParameters error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationDate** | **Integer** |  |  [optional] |
|**currentPage** | **Integer** |  |  [optional] |
|**groupMemberCountFilter** | [**GroupMemberCountFilterEnum**](#GroupMemberCountFilterEnum) |  |  [optional] |
|**groupType** | **Integer** |  |  [optional] |
|**itemsPerPage** | **Integer** |  |  [optional] |
|**localeFilter** | **String** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**requestContinuationToken** | **String** |  |  [optional] |
|**sortBy** | **Integer** |  |  [optional] |
|**tagText** | **String** |  |  [optional] |



## Enum: GroupMemberCountFilterEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



