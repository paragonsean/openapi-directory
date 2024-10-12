# Pims.EventsCapacitiesEntityEventCategoriesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comps** | **Number** | Number of comps in the category. | 
**holds** | **Number** | Number of *holds* in the category. &lt;span class&#x3D;\&quot;definition\&quot;&gt;Holds&lt;/span&gt; are seats/places that are not in sale at the date of the capacity, but will eventually be later. | 
**id** | **Number** | Unique ID of the event category. | 
**kills** | **Number** | Number of *kills* in the category. &lt;span class&#x3D;\&quot;definition\&quot;&gt;Kills&lt;/span&gt; are seats/places that will not be sold for technical reasons. | 
**sellableCapacity** | **Number** | Number of sellable seats/places in the category. This is calculated by the formula: &#x60;total_capacity - kills - comps - holds&#x60;. | 
**totalCapacity** | **Number** | Total number of seats/places in the category. | 


