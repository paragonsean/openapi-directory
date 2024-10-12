

# GroupMembership

Provides information about the current users' active or pending membership to this group (if any).  Will be null if there is no active or pending membership to this group. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **OffsetDateTime** | The UTC date and time when the membership was last updated.  |  [optional] |
|**questionnaire** | [**GroupMembershipQuestionnaire**](GroupMembershipQuestionnaire.md) |  |  [optional] |
|**status** | **String** | One of: subscribed, pending, pending-questions  |  [optional] |



