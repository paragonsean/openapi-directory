

# StartMigrationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**v1BotName** | **String** | The name of the Amazon Lex V1 bot that you are migrating to Amazon Lex V2. |  |
|**v1BotVersion** | **String** | The version of the bot to migrate to Amazon Lex V2. You can migrate the &lt;code&gt;$LATEST&lt;/code&gt; version as well as any numbered version. |  |
|**v2BotName** | **String** | &lt;p&gt;The name of the Amazon Lex V2 bot that you are migrating the Amazon Lex V1 bot to. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the Amazon Lex V2 bot doesn&#39;t exist, you must use the &lt;code&gt;CREATE_NEW&lt;/code&gt; migration strategy.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the Amazon Lex V2 bot exists, you must use the &lt;code&gt;UPDATE_EXISTING&lt;/code&gt; migration strategy to change the contents of the Amazon Lex V2 bot.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |
|**v2BotRole** | **String** | The IAM role that Amazon Lex uses to run the Amazon Lex V2 bot. |  |
|**migrationStrategy** | [**MigrationStrategyEnum**](#MigrationStrategyEnum) | &lt;p&gt;The strategy used to conduct the migration.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CREATE_NEW&lt;/code&gt; - Creates a new Amazon Lex V2 bot and migrates the Amazon Lex V1 bot to the new bot.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UPDATE_EXISTING&lt;/code&gt; - Overwrites the existing Amazon Lex V2 bot metadata and the locale being migrated. It doesn&#39;t change any other locales in the Amazon Lex V2 bot. If the locale doesn&#39;t exist, a new locale is created in the Amazon Lex V2 bot.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |  |



## Enum: MigrationStrategyEnum

| Name | Value |
|---- | -----|
| CREATE_NEW | &quot;CREATE_NEW&quot; |
| UPDATE_EXISTING | &quot;UPDATE_EXISTING&quot; |



