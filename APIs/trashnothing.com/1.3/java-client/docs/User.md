

# User


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aboutMe** | **String** | A short bio a user has written about themselves to help other members get to know them better. May be null if the user has not written anything about themselves.  |  [optional] |
|**country** | **String** | A 2 letter country code for the country that has been automatically detected for the user (see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 ). May be null if no country has been set.  |  [optional] |
|**feedback** | [**UserFeedback**](UserFeedback.md) |  |  [optional] |
|**firstname** | **String** | The first name of the user (may be null). |  [optional] |
|**lastname** | **String** | The last name of the user (may be null). |  [optional] |
|**memberSince** | **String** | The date and time when the user first became publicly active on a group (the date may be older than when the user signed up). |  [optional] |
|**profileImage** | **String** | A URL to a profile image for the user.  Profile images sizes vary based on the source (Google, Facebook, Gravatar, etc) and some can be as small as 64px by 64px.  Will be null for api key requests and requests where the oauth user doesn&#39;t belong to any of the same groups as this user.  |  [optional] |
|**replyTime** | **Integer** | An estimate of how many seconds it takes this user to reply to messages. May be null when there is not enough data to calculate an estimate.  |  [optional] |
|**userId** | **String** |  |  [optional] |
|**username** | **String** | A username that can be displayed for the user (the username is NOT guaranteed to be unique). Will be null for api key requests and requests where the oauth user doesn&#39;t belong to any of the same groups as this user.  |  [optional] |



