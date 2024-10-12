# AmazonLexModelBuildingV2.CreateBotAliasRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**botAliasName** | **String** | The alias to create. The name must be unique for the bot. | 
**description** | **String** | A description of the alias. Use this description to help identify the alias. | [optional] 
**botVersion** | **String** | The version of the bot that this alias points to. You can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateBotAlias.html\&quot;&gt;UpdateBotAlias&lt;/a&gt; operation to change the bot version associated with the alias. | [optional] 
**botAliasLocaleSettings** | [**{String: BotAliasLocaleSettings}**](BotAliasLocaleSettings.md) | Maps configuration information to a specific locale. You can use this parameter to specify a specific Lambda function to run different functions in different locales. | [optional] 
**conversationLogSettings** | [**CreateBotAliasRequestConversationLogSettings**](CreateBotAliasRequestConversationLogSettings.md) |  | [optional] 
**sentimentAnalysisSettings** | [**CreateBotAliasRequestSentimentAnalysisSettings**](CreateBotAliasRequestSentimentAnalysisSettings.md) |  | [optional] 
**tags** | **{String: String}** | A list of tags to add to the bot alias. You can only add tags when you create an alias, you can&#39;t use the &lt;code&gt;UpdateBotAlias&lt;/code&gt; operation to update the tags on a bot alias. To update tags, use the &lt;code&gt;TagResource&lt;/code&gt; operation. | [optional] 


