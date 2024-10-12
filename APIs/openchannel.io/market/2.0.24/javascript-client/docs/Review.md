# OpenChannelMarketApi.Review

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | The Id of the App that owns this review | 
**customData** | **String** | A custom JSON object that you can create and attach to this record | 
**description** | **String** | The review&#39;s description. Limited to 2000 characters. | 
**headline** | **String** | The review&#39;s headline. Limited to 50 characters. | 
**rating** | **Number** | The rating given within this review. The rating is represented as an integer between 100 and 500 (1 - 5 stars) | 
**reportDate** | **Number** | The date (in millis) this Review was posted | 
**reviewId** | **String** | The id for this review. | 
**status** | [**Status**](Status.md) |  | 
**type** | **String** | The type for this review | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**userAccount** | [**UserAccount**](UserAccount.md) |  | [optional] 
**userAccountId** | **String** | The id of the user account that posted this review | [optional] 
**userId** | **String** | The id of the User that posted this review | 


