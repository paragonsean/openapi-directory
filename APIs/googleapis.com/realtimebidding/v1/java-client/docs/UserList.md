

# UserList

Represents an Authorized Buyers user list. Authorized Buyers can create/update/list user lists. Once a user list is created in the system, Authorized Buyers can add users to the user list using the bulk uploader API. Alternatively, users can be added by hosting a tag on the advertiser's page.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description for the user list. |  [optional] |
|**displayName** | **String** | Required. Display name of the user list. This must be unique across all user lists for a given account. |  [optional] |
|**membershipDurationDays** | **String** | Required. The number of days a user&#39;s cookie stays on the user list. The field must be between 0 and 540 inclusive. |  [optional] |
|**name** | **String** | Output only. Name of the user list that must follow the pattern &#x60;buyers/{buyer}/userLists/{user_list}&#x60;, where &#x60;{buyer}&#x60; represents the account ID of the buyer who owns the user list. For a bidder accessing user lists on behalf of a child seat buyer, &#x60;{buyer}&#x60; represents the account ID of the child seat buyer. &#x60;{user_list}&#x60; is an int64 identifier assigned by Google to uniquely identify a user list. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. The status of the user list. A new user list starts out as open. |  [optional] [readonly] |
|**urlRestriction** | [**UrlRestriction**](UrlRestriction.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| OPEN | &quot;OPEN&quot; |
| CLOSED | &quot;CLOSED&quot; |



