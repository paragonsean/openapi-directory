

# QueryInterpretationOptions

Options to interpret user query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableNlInterpretation** | **Boolean** | Flag to disable natural language (NL) interpretation of queries. Default is false, Set to true to disable natural language interpretation. NL interpretation only applies to predefined datasources. |  [optional] |
|**disableSupplementalResults** | **Boolean** | Use this flag to disable supplemental results for a query. Supplemental results setting chosen at SearchApplication level will take precedence if set to True. |  [optional] |
|**enableVerbatimMode** | **Boolean** | Enable this flag to turn off all internal optimizations like natural language (NL) interpretation of queries, supplemental result retrieval, and usage of synonyms including custom ones. Nl interpretation will be disabled if either one of the two flags is true. |  [optional] |



