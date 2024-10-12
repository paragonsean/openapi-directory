

# EventsCapacitiesEntityEventCategoriesInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comps** | **Integer** | Number of comps in the category. |  |
|**holds** | **Integer** | Number of *holds* in the category. &lt;span class&#x3D;\&quot;definition\&quot;&gt;Holds&lt;/span&gt; are seats/places that are not in sale at the date of the capacity, but will eventually be later. |  |
|**id** | **Integer** | Unique ID of the event category. |  |
|**kills** | **Integer** | Number of *kills* in the category. &lt;span class&#x3D;\&quot;definition\&quot;&gt;Kills&lt;/span&gt; are seats/places that will not be sold for technical reasons. |  |
|**sellableCapacity** | **Integer** | Number of sellable seats/places in the category. This is calculated by the formula: &#x60;total_capacity - kills - comps - holds&#x60;. |  |
|**totalCapacity** | **Integer** | Total number of seats/places in the category. |  |



