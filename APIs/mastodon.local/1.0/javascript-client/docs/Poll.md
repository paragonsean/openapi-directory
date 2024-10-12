# MastodonApiSpecificationHttpsGithubComMastodonMastodon.Poll

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emojis** | [**[Emoji]**](Emoji.md) | Custom emoji to be used for rendering poll options. | [optional] 
**expired** | **Boolean** | Is the poll currently expired? | [optional] 
**expiresAt** | **Date** | When the poll ends. ISO 8601 Datetime, or null if the poll does not end. | [optional] 
**id** | **String** | The ID of the poll in the database. Cast from an integer, but not guaranteed to be a number. | [optional] 
**multiple** | **Boolean** | Does the poll allow multiple-choice answers? | [optional] 
**options** | **[Object]** | Possible answers for the poll. | [optional] 
**ownVotes** | **[Number]** | When called with a user token, which options has the authorized user chosen? Contains an array of index values for &#x60;options&#x60;. Array of Number, or null if no current user | [optional] 
**voted** | **Boolean** | When called with a user token, has the authorized user voted? Boolean, or null if no current user | [optional] 
**votersCount** | **Number** | How many unique accounts have voted on a multiple-choice poll. Number, or null if &#x60;multiple&#x60; is false. | [optional] 
**votesCount** | **Number** | How many votes have been received. | [optional] 


