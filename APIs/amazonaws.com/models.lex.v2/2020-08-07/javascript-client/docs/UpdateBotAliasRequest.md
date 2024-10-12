# AmazonLexModelBuildingV2.UpdateBotAliasRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**botAliasName** | **String** | The new name to assign to the bot alias. | 
**description** | **String** | The new description to assign to the bot alias. | [optional] 
**botVersion** | **String** | The new bot version to assign to the bot alias. | [optional] 
**botAliasLocaleSettings** | [**{String: BotAliasLocaleSettings}**](BotAliasLocaleSettings.md) | The new Lambda functions to use in each locale for the bot alias. | [optional] 
**conversationLogSettings** | [**CreateBotAliasRequestConversationLogSettings**](CreateBotAliasRequestConversationLogSettings.md) |  | [optional] 
**sentimentAnalysisSettings** | [**CreateBotAliasRequestSentimentAnalysisSettings**](CreateBotAliasRequestSentimentAnalysisSettings.md) |  | [optional] 


