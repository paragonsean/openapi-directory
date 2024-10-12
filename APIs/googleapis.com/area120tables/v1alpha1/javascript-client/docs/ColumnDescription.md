# Area120TablesApi.ColumnDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataType** | **String** | Data type of the column Supported types are auto_id, boolean, boolean_list, creator, create_timestamp, date, dropdown, location, integer, integer_list, number, number_list, person, person_list, tags, check_list, text, text_list, update_timestamp, updater, relationship, file_attachment_list. These types directly map to the column types supported on Tables website. | [optional] 
**dateDetails** | [**DateDetails**](DateDetails.md) |  | [optional] 
**id** | **String** | Internal id for a column. | [optional] 
**labels** | [**[LabeledItem]**](LabeledItem.md) | Optional. Range of labeled values for the column. Some columns like tags and drop-downs limit the values to a set of possible values. We return the range of values in such cases to help clients implement better user data validation. | [optional] 
**lookupDetails** | [**LookupDetails**](LookupDetails.md) |  | [optional] 
**multipleValuesDisallowed** | **Boolean** | Optional. Indicates whether or not multiple values are allowed for array types where such a restriction is possible. | [optional] 
**name** | **String** | column name | [optional] 
**readonly** | **Boolean** | Optional. Indicates that values for the column cannot be set by the user. | [optional] 
**relationshipDetails** | [**RelationshipDetails**](RelationshipDetails.md) |  | [optional] 


