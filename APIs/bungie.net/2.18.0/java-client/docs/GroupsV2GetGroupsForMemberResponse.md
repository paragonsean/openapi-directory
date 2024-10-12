

# GroupsV2GetGroupsForMemberResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**areAllMembershipsInactive** | **Map&lt;String, Boolean&gt;** | A convenience property that indicates if every membership this user has that is a part of this group are part of an account that is considered inactive - for example, overridden accounts in Cross Save.   The key is the Group ID for the group being checked, and the value is true if the users&#39; memberships for that group are all inactive. |  [optional] |
|**hasMore** | **Boolean** |  |  [optional] |
|**query** | [**QueriesPagedQuery**](QueriesPagedQuery.md) |  |  [optional] |
|**replacementContinuationToken** | **String** |  |  [optional] |
|**results** | [**List&lt;GroupsV2GroupMembership&gt;**](GroupsV2GroupMembership.md) |  |  [optional] |
|**totalResults** | **Integer** |  |  [optional] |
|**useTotalResults** | **Boolean** | If useTotalResults is true, then totalResults represents an accurate count.  If False, it does not, and may be estimated/only the size of the current page.  Either way, you should probably always only trust hasMore.  This is a long-held historical throwback to when we used to do paging with known total results. Those queries toasted our database, and we were left to hastily alter our endpoints and create backward- compatible shims, of which useTotalResults is one. |  [optional] |



