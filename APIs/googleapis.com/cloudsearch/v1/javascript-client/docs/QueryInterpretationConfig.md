# CloudSearchApi.QueryInterpretationConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forceDisableSupplementalResults** | **Boolean** | Set this flag to disable supplemental results retrieval, setting a flag here will not retrieve supplemental results for queries associated with a given search application. If this flag is set to True, it will take precedence over the option set at Query level. For the default value of False, query level flag will set the correct interpretation for supplemental results. | [optional] 
**forceVerbatimMode** | **Boolean** | Enable this flag to turn off all internal optimizations like natural language (NL) interpretation of queries, supplemental results retrieval, and usage of synonyms including custom ones. If this flag is set to True, it will take precedence over the option set at Query level. For the default value of False, query level flag will set the correct interpretation for verbatim mode. | [optional] 


