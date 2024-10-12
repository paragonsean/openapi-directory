

# EntityProfileKYCMatchResultObjectMatchTypesValue


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checked** | **Boolean** | True if an attempt was made to verify |  [optional] |
|**matchCount** | **Integer** | Number of distinct matches for this match type. Note that for government ID (gov_id) this is the count of matched documents, not sources.  |  [optional] |
|**matchSources** | **List&lt;String&gt;** | List of sources that matched. Note that the matchCount is not always a count of the matchSources. Particularly for gov_id, the count is the number of distinct documents matched, not the number of sources.  |  [optional] |
|**verified** | **Boolean** | True if there is at least one match |  [optional] |



