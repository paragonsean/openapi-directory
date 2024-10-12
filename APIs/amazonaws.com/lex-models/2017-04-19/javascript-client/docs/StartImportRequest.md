# AmazonLexModelBuildingService.StartImportRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **String** | A zip archive in binary format. The archive should contain one file, a JSON file containing the resource to import. The resource should match the type specified in the &lt;code&gt;resourceType&lt;/code&gt; field. | 
**resourceType** | **String** | &lt;p&gt;Specifies the type of resource to export. Each resource also exports any resources that it depends on. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A bot exports dependent intents.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An intent exports dependent slot types.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**mergeStrategy** | **String** | &lt;p&gt;Specifies the action that the &lt;code&gt;StartImport&lt;/code&gt; operation should take when there is an existing resource with the same name.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;FAIL_ON_CONFLICT - The import operation is stopped on the first conflict between a resource in the import file and an existing resource. The name of the resource causing the conflict is in the &lt;code&gt;failureReason&lt;/code&gt; field of the response to the &lt;code&gt;GetImport&lt;/code&gt; operation.&lt;/p&gt; &lt;p&gt;OVERWRITE_LATEST - The import operation proceeds even if there is a conflict with an existing resource. The $LASTEST version of the existing resource is overwritten with the data from the import file.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | 
**tags** | [**[Tag]**](Tag.md) | A list of tags to add to the imported bot. You can only add tags when you import a bot, you can&#39;t add tags to an intent or slot type. | [optional] 



## Enum: ResourceTypeEnum


* `BOT` (value: `"BOT"`)

* `INTENT` (value: `"INTENT"`)

* `SLOT_TYPE` (value: `"SLOT_TYPE"`)





## Enum: MergeStrategyEnum


* `OVERWRITE_LATEST` (value: `"OVERWRITE_LATEST"`)

* `FAIL_ON_CONFLICT` (value: `"FAIL_ON_CONFLICT"`)




