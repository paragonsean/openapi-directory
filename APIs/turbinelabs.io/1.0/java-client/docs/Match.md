

# Match

Represents a mapping of request attributes to constraints on a cluster using different matching schemes.  Certain combinations of `kind` and `behavior` are not allowed   | kind | behavior |   | ---- | -------- |   | query | regex |   | query | range |   | cookie | range | 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**behavior** | **String** | Defines how a request attribute should be matched. If not specified, defaults to &#x60;exact&#x60;. Valid values are   * exact   * regex   * range   * prefix   * suffix  |  [optional] |
|**from** | [**Metadatum**](Metadatum.md) | The request attribute key and value to match. &#x60;key&#x60; must always be defined while &#x60;value&#x60; can be unspecified (only if behavior is set to &#x60;exact&#x60;) to indicate that all values should be matched. If to.value is also unspecified, the matched value of the request will be used as a constraint on the destination cluster.  \\# Behavior   * &#x60;regex&#x60; if To.Value is unspecified, &#x60;value&#x60; must contain one and   only one subgroup. Otherwise, &#x60;value&#x60; must not be empty.   * &#x60;range&#x60; &#x60;value&#x60; must be specified and must be of the format   &#x60;[start_integer, end_integer)&#x60;. Start and end must be valid integer   values and &#x60;end_integer&#x60; must be greater than &#x60;start_integer&#x60;.   * &#x60;prefix&#x60;/&#x60;suffix&#x60; &#x60;value&#x60; must be specified  \\# Kind   * &#x60;cookie&#x60; does not support &#x60;range&#x60; behavior   * &#x60;query&#x60; does not support &#x60;regex&#x60; behavior  |  [optional] |
|**kind** | **String** | Defines the attribute by which a request should be matched on. Valid values are   * cookie   * header   * query (for query parameter)  |  [optional] |
|**to** | [**Metadatum**](Metadatum.md) | The constraints on a cluster that a matched request should map to. If to.key is specified and to.value is not, the matched from.value will be used as a metadata constraint on instances in the destination cluster, keyed by to.key. If using &#x60;regex&#x60; behavior with multiple subgroups in from.value, variables &#x60;$1&#x60; through &#x60;$n&#x60;, where n is the number of subgroups in the matching regex, can be used to interpolate captured matches in to.value.  |  [optional] |



