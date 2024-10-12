

# AspectValueDistribution

This type contains information about one value of a specified aspect. This value serves as a product refinement.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**localizedAspectValue** | **String** | The localized value of the category aspect identified by &lt;b&gt;refinement.aspectDistributions.localizedAspectName&lt;/b&gt;. |  [optional] |
|**matchCount** | **Integer** | The number of times the value of &lt;b&gt;localizedAspectValue&lt;/b&gt; has been used for eBay product listings. By comparing this quantity to the &lt;b&gt;matchCount&lt;/b&gt; for other values of the same aspect, you can present a histogram of the values to sellers, who can use that information to select which aspect value is most appropriate for their product. You can then include the user-selected value in the the &lt;b&gt;search&lt;/b&gt; call&#39;s &lt;b&gt;aspect_filter&lt;/b&gt; parameter to refine your search. |  [optional] |
|**refinementHref** | **String** | A HATEOAS reference that further refines the search with this particular &lt;b&gt;localizedAspectValue&lt;/b&gt;. |  [optional] |



