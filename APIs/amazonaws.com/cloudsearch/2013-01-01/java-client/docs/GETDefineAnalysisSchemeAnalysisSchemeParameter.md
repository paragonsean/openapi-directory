

# GETDefineAnalysisSchemeAnalysisSchemeParameter

Configuration information for an analysis scheme. Each analysis scheme has a unique name and specifies the language of the text to be processed. The following options can be configured for an analysis scheme: <code>Synonyms</code>, <code>Stopwords</code>, <code>StemmingDictionary</code>, <code>JapaneseTokenizationDictionary</code> and <code>AlgorithmicStemming</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysisSchemeName** | **String** | Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). |  |
|**analysisSchemeLanguage** | **AnalysisSchemeLanguage** |  |  |
|**analysisOptions** | [**AnalysisOptions**](AnalysisOptions.md) |  |  [optional] |



