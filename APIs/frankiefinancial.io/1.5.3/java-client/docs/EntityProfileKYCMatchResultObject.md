

# EntityProfileKYCMatchResultObject

Summary of all KYC matches

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchCount** | **Integer** | Number of matches for this set of match types. In other words the sum of the matchCounts in the matchTypes map. Note that for match sets that include government ID (gov_id) this will not neccessaily be the count of matched sources.  |  [optional] |
|**matchCountRequired** | **Integer** | Number of distinct matches (sources and/or matched government ID documents) required for this set of match types.  |  [optional] |
|**matchTypes** | [**Map&lt;String, EntityProfileKYCMatchResultObjectMatchTypesValue&gt;**](EntityProfileKYCMatchResultObjectMatchTypesValue.md) | The match types that this overall count and result refer to. Currently one or more of: - name - address - dob - gender - gov_id - other_id  These will be keys in a map whose values hold the values for the individual match types. The resultant structure would look like the following. Here dob has zero matches and is not verfied but it was check, so other than the checked flag the value object is simply empty. A completely empty object would imply that match type was not checked.      \&quot;matchTypes\&quot;: {       \&quot;address\&quot;: {         \&quot;matchCount\&quot;: 1,         \&quot;matchSources\&quot;: [ \&quot;au-elec-roll\&quot; ],         \&quot;checked\&quot;: true,         \&quot;verified\&quot;: true       },       \&quot;dob\&quot;: {         \&quot;checked\&quot;: true       }     }  So for a one_plus KYC check there will be two EntityProfileKYCMatchResultObject records. One for &#39;name&#39; and one for &#39;address, dob&#39; (like the sample above).  |  [optional] |
|**verified** | **Boolean** | True if there are enough matches to meet the requirement |  [optional] |



