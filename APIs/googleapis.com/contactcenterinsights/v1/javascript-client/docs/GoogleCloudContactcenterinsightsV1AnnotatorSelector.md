# ContactCenterAiInsightsApi.GoogleCloudContactcenterinsightsV1AnnotatorSelector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issueModels** | **[String]** | The issue model to run. If not provided, the most recently deployed topic model will be used. The provided issue model will only be used for inference if the issue model is deployed and if run_issue_model_annotator is set to true. If more than one issue model is provided, only the first provided issue model will be used for inference. | [optional] 
**phraseMatchers** | **[String]** | The list of phrase matchers to run. If not provided, all active phrase matchers will be used. If inactive phrase matchers are provided, they will not be used. Phrase matchers will be run only if run_phrase_matcher_annotator is set to true. Format: projects/{project}/locations/{location}/phraseMatchers/{phrase_matcher} | [optional] 
**runEntityAnnotator** | **Boolean** | Whether to run the entity annotator. | [optional] 
**runIntentAnnotator** | **Boolean** | Whether to run the intent annotator. | [optional] 
**runInterruptionAnnotator** | **Boolean** | Whether to run the interruption annotator. | [optional] 
**runIssueModelAnnotator** | **Boolean** | Whether to run the issue model annotator. A model should have already been deployed for this to take effect. | [optional] 
**runPhraseMatcherAnnotator** | **Boolean** | Whether to run the active phrase matcher annotator(s). | [optional] 
**runSentimentAnnotator** | **Boolean** | Whether to run the sentiment annotator. | [optional] 
**runSilenceAnnotator** | **Boolean** | Whether to run the silence annotator. | [optional] 
**runSummarizationAnnotator** | **Boolean** | Whether to run the summarization annotator. | [optional] 
**summarizationConfig** | [**GoogleCloudContactcenterinsightsV1AnnotatorSelectorSummarizationConfig**](GoogleCloudContactcenterinsightsV1AnnotatorSelectorSummarizationConfig.md) |  | [optional] 


