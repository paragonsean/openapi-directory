# OptimadeApi.EntryInfoResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the entry. | 
**formats** | **[String]** | List of output formats available for this type of entry. | 
**outputFieldsByFormat** | **{String: [String]}** | Dictionary of available output fields for this entry type, where the keys are the values of the &#x60;formats&#x60; list and the values are the keys of the &#x60;properties&#x60; dictionary. | 
**properties** | [**{String: EntryInfoProperty}**](EntryInfoProperty.md) | A dictionary describing queryable properties for this entry type, where each key is a property name. | 


