# CloudSpeechToTextApi.SpeechAdaptation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abnfGrammar** | [**ABNFGrammar**](ABNFGrammar.md) |  | [optional] 
**customClasses** | [**[CustomClass]**](CustomClass.md) | A collection of custom classes. To specify the classes inline, leave the class&#39; &#x60;name&#x60; blank and fill in the rest of its fields, giving it a unique &#x60;custom_class_id&#x60;. Refer to the inline defined class in phrase hints by its &#x60;custom_class_id&#x60;. | [optional] 
**phraseSetReferences** | **[String]** | A collection of phrase set resource names to use. | [optional] 
**phraseSets** | [**[PhraseSet]**](PhraseSet.md) | A collection of phrase sets. To specify the hints inline, leave the phrase set&#39;s &#x60;name&#x60; blank and fill in the rest of its fields. Any phrase set can use any custom class. | [optional] 


