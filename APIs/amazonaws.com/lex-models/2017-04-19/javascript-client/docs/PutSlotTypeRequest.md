# AmazonLexModelBuildingService.PutSlotTypeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A description of the slot type. | [optional] 
**enumerationValues** | [**[EnumerationValue]**](EnumerationValue.md) | &lt;p&gt;A list of &lt;code&gt;EnumerationValue&lt;/code&gt; objects that defines the values that the slot type can take. Each value can have a list of &lt;code&gt;synonyms&lt;/code&gt;, which are additional values that help train the machine learning model about the values that it resolves for a slot. &lt;/p&gt; &lt;p&gt;A regular expression slot type doesn&#39;t require enumeration values. All other slot types require a list of enumeration values.&lt;/p&gt; &lt;p&gt;When Amazon Lex resolves a slot value, it generates a resolution list that contains up to five possible values for the slot. If you are using a Lambda function, this resolution list is passed to the function. If you are not using a Lambda function you can choose to return the value that the user entered or the first value in the resolution list as the slot value. The &lt;code&gt;valueSelectionStrategy&lt;/code&gt; field indicates the option to use. &lt;/p&gt; | [optional] 
**checksum** | **String** | &lt;p&gt;Identifies a specific revision of the &lt;code&gt;$LATEST&lt;/code&gt; version.&lt;/p&gt; &lt;p&gt;When you create a new slot type, leave the &lt;code&gt;checksum&lt;/code&gt; field blank. If you specify a checksum you get a &lt;code&gt;BadRequestException&lt;/code&gt; exception.&lt;/p&gt; &lt;p&gt;When you want to update a slot type, set the &lt;code&gt;checksum&lt;/code&gt; field to the checksum of the most recent revision of the &lt;code&gt;$LATEST&lt;/code&gt; version. If you don&#39;t specify the &lt;code&gt; checksum&lt;/code&gt; field, or if the checksum does not match the &lt;code&gt;$LATEST&lt;/code&gt; version, you get a &lt;code&gt;PreconditionFailedException&lt;/code&gt; exception.&lt;/p&gt; | [optional] 
**valueSelectionStrategy** | **String** | &lt;p&gt;Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ORIGINAL_VALUE&lt;/code&gt; - Returns the value entered by the user, if the user value is similar to the slot value.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TOP_RESOLUTION&lt;/code&gt; - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you don&#39;t specify the &lt;code&gt;valueSelectionStrategy&lt;/code&gt;, the default is &lt;code&gt;ORIGINAL_VALUE&lt;/code&gt;.&lt;/p&gt; | [optional] 
**createVersion** | **Boolean** | When set to &lt;code&gt;true&lt;/code&gt; a new numbered version of the slot type is created. This is the same as calling the &lt;code&gt;CreateSlotTypeVersion&lt;/code&gt; operation. If you do not specify &lt;code&gt;createVersion&lt;/code&gt;, the default is &lt;code&gt;false&lt;/code&gt;. | [optional] 
**parentSlotTypeSignature** | **String** | &lt;p&gt;The built-in slot type used as the parent of the slot type. When you define a parent slot type, the new slot type has all of the same configuration as the parent.&lt;/p&gt; &lt;p&gt;Only &lt;code&gt;AMAZON.AlphaNumeric&lt;/code&gt; is supported.&lt;/p&gt; | [optional] 
**slotTypeConfigurations** | [**[SlotTypeConfiguration]**](SlotTypeConfiguration.md) | Configuration information that extends the parent built-in slot type. The configuration is added to the settings for the parent slot type. | [optional] 



## Enum: ValueSelectionStrategyEnum


* `ORIGINAL_VALUE` (value: `"ORIGINAL_VALUE"`)

* `TOP_RESOLUTION` (value: `"TOP_RESOLUTION"`)




