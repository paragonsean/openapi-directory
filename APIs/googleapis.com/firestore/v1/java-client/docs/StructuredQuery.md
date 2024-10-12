

# StructuredQuery

A Firestore query. The query stages are executed in the following order: 1. from 2. where 3. select 4. order_by + start_at + end_at 5. offset 6. limit

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endAt** | [**Cursor**](Cursor.md) |  |  [optional] |
|**from** | [**List&lt;CollectionSelector&gt;**](CollectionSelector.md) | The collections to query. |  [optional] |
|**limit** | **Integer** | The maximum number of results to return. Applies after all other constraints. Requires: * The value must be greater than or equal to zero if specified. |  [optional] |
|**offset** | **Integer** | The number of documents to skip before returning the first result. This applies after the constraints specified by the &#x60;WHERE&#x60;, &#x60;START AT&#x60;, &amp; &#x60;END AT&#x60; but before the &#x60;LIMIT&#x60; clause. Requires: * The value must be greater than or equal to zero if specified. |  [optional] |
|**orderBy** | [**List&lt;Order&gt;**](Order.md) | The order to apply to the query results. Firestore allows callers to provide a full ordering, a partial ordering, or no ordering at all. In all cases, Firestore guarantees a stable ordering through the following rules: * The &#x60;order_by&#x60; is required to reference all fields used with an inequality filter. * All fields that are required to be in the &#x60;order_by&#x60; but are not already present are appended in lexicographical ordering of the field name. * If an order on &#x60;__name__&#x60; is not specified, it is appended by default. Fields are appended with the same sort direction as the last order specified, or &#39;ASCENDING&#39; if no order was specified. For example: * &#x60;ORDER BY a&#x60; becomes &#x60;ORDER BY a ASC, __name__ ASC&#x60; * &#x60;ORDER BY a DESC&#x60; becomes &#x60;ORDER BY a DESC, __name__ DESC&#x60; * &#x60;WHERE a &gt; 1&#x60; becomes &#x60;WHERE a &gt; 1 ORDER BY a ASC, __name__ ASC&#x60; * &#x60;WHERE __name__ &gt; ... AND a &gt; 1&#x60; becomes &#x60;WHERE __name__ &gt; ... AND a &gt; 1 ORDER BY a ASC, __name__ ASC&#x60; |  [optional] |
|**select** | [**Projection**](Projection.md) |  |  [optional] |
|**startAt** | [**Cursor**](Cursor.md) |  |  [optional] |
|**where** | [**Filter**](Filter.md) |  |  [optional] |



