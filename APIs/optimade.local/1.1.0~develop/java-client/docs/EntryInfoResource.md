

# EntryInfoResource


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the entry. |  |
|**formats** | **List&lt;String&gt;** | List of output formats available for this type of entry. |  |
|**outputFieldsByFormat** | **Map&lt;String, List&lt;String&gt;&gt;** | Dictionary of available output fields for this entry type, where the keys are the values of the &#x60;formats&#x60; list and the values are the keys of the &#x60;properties&#x60; dictionary. |  |
|**properties** | [**Map&lt;String, EntryInfoProperty&gt;**](EntryInfoProperty.md) | A dictionary describing queryable properties for this entry type, where each key is a property name. |  |



