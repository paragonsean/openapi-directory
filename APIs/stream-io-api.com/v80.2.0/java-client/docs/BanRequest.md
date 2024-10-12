

# BanRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bannedBy** | **UserObjectRequest** |  |  [optional] |
|**bannedById** | **String** | User ID who issued a ban |  [optional] |
|**id** | **String** | Channel ID to ban user in |  [optional] |
|**ipBan** | **Boolean** | Whether to perform IP ban or not |  [optional] |
|**reason** | **String** | Ban reason |  [optional] |
|**shadow** | **Boolean** | Whether to perform shadow ban or not |  [optional] |
|**targetUserId** | **String** | ID of user to ban |  |
|**timeout** | **Integer** | Timeout of ban in minutes. User will be unbanned after this period of time |  [optional] |
|**type** | **String** | Channel type to ban user in |  [optional] |
|**user** | **UserObjectRequest** |  |  [optional] |
|**userId** | **String** |  |  [optional] |



