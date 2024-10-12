# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1betaSearchRequestFacetSpecFacetKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caseInsensitive** | **Boolean** | True to make facet keys case insensitive when getting faceting values with prefixes or contains; false otherwise. | [optional] 
**contains** | **[String]** | Only get facet values that contains the given strings. For example, suppose \&quot;category\&quot; has three values \&quot;Action &gt; 2022\&quot;, \&quot;Action &gt; 2021\&quot; and \&quot;Sci-Fi &gt; 2022\&quot;. If set \&quot;contains\&quot; to \&quot;2022\&quot;, the \&quot;category\&quot; facet only contains \&quot;Action &gt; 2022\&quot; and \&quot;Sci-Fi &gt; 2022\&quot;. Only supported on textual fields. Maximum is 10. | [optional] 
**intervals** | [**[GoogleCloudDiscoveryengineV1betaInterval]**](GoogleCloudDiscoveryengineV1betaInterval.md) | Set only if values should be bucketed into intervals. Must be set for facets with numerical values. Must not be set for facet with text values. Maximum number of intervals is 30. | [optional] 
**key** | **String** | Required. Supported textual and numerical facet keys in Document object, over which the facet values are computed. Facet key is case-sensitive. | [optional] 
**orderBy** | **String** | The order in which documents are returned. Allowed values are: * \&quot;count desc\&quot;, which means order by SearchResponse.Facet.values.count descending. * \&quot;value desc\&quot;, which means order by SearchResponse.Facet.values.value descending. Only applies to textual facets. If not set, textual values are sorted in [natural order](https://en.wikipedia.org/wiki/Natural_sort_order); numerical intervals are sorted in the order given by FacetSpec.FacetKey.intervals. | [optional] 
**prefixes** | **[String]** | Only get facet values that start with the given string prefix. For example, suppose \&quot;category\&quot; has three values \&quot;Action &gt; 2022\&quot;, \&quot;Action &gt; 2021\&quot; and \&quot;Sci-Fi &gt; 2022\&quot;. If set \&quot;prefixes\&quot; to \&quot;Action\&quot;, the \&quot;category\&quot; facet only contains \&quot;Action &gt; 2022\&quot; and \&quot;Action &gt; 2021\&quot;. Only supported on textual fields. Maximum is 10. | [optional] 
**restrictedValues** | **[String]** | Only get facet for the given restricted values. Only supported on textual fields. For example, suppose \&quot;category\&quot; has three values \&quot;Action &gt; 2022\&quot;, \&quot;Action &gt; 2021\&quot; and \&quot;Sci-Fi &gt; 2022\&quot;. If set \&quot;restricted_values\&quot; to \&quot;Action &gt; 2022\&quot;, the \&quot;category\&quot; facet only contains \&quot;Action &gt; 2022\&quot;. Only supported on textual fields. Maximum is 10. | [optional] 


