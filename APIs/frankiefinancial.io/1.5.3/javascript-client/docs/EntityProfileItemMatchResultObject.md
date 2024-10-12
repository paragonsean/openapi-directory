# FrankieFinancialApi.EntityProfileItemMatchResultObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checked** | **Boolean** | True if an attempt was made to verify | [optional] 
**matchCount** | **Number** | The number of distinct sources that matched this address or document | [optional] 
**matchSources** | **[String]** | List of sources that matched. The matchCount will be the number of entries in this list.  | [optional] 
**matchType** | **String** | The match type that this count and result refer to. For document matches this will be \&quot;gov_id\&quot; or \&quot;other_id\&quot;. For addresses ir will be \&quot;curr_addr\&quot; or \&quot;prev_addr\&quot; depending on the status of the address at the time of the check.  | [optional] 
**verified** | **Boolean** | True if there is at least one match | [optional] 


