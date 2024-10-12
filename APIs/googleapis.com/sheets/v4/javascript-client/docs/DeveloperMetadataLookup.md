# GoogleSheetsApi.DeveloperMetadataLookup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locationMatchingStrategy** | **String** | Determines how this lookup matches the location. If this field is specified as EXACT, only developer metadata associated on the exact location specified is matched. If this field is specified to INTERSECTING, developer metadata associated on intersecting locations is also matched. If left unspecified, this field assumes a default value of INTERSECTING. If this field is specified, a metadataLocation must also be specified. | [optional] 
**locationType** | **String** | Limits the selected developer metadata to those entries which are associated with locations of the specified type. For example, when this field is specified as ROW this lookup only considers developer metadata associated on rows. If the field is left unspecified, all location types are considered. This field cannot be specified as SPREADSHEET when the locationMatchingStrategy is specified as INTERSECTING or when the metadataLocation is specified as a non-spreadsheet location: spreadsheet metadata cannot intersect any other developer metadata location. This field also must be left unspecified when the locationMatchingStrategy is specified as EXACT. | [optional] 
**metadataId** | **Number** | Limits the selected developer metadata to that which has a matching DeveloperMetadata.metadata_id. | [optional] 
**metadataKey** | **String** | Limits the selected developer metadata to that which has a matching DeveloperMetadata.metadata_key. | [optional] 
**metadataLocation** | [**DeveloperMetadataLocation**](DeveloperMetadataLocation.md) |  | [optional] 
**metadataValue** | **String** | Limits the selected developer metadata to that which has a matching DeveloperMetadata.metadata_value. | [optional] 
**visibility** | **String** | Limits the selected developer metadata to that which has a matching DeveloperMetadata.visibility. If left unspecified, all developer metadata visibile to the requesting project is considered. | [optional] 



## Enum: LocationMatchingStrategyEnum


* `DEVELOPER_METADATA_LOCATION_MATCHING_STRATEGY_UNSPECIFIED` (value: `"DEVELOPER_METADATA_LOCATION_MATCHING_STRATEGY_UNSPECIFIED"`)

* `EXACT_LOCATION` (value: `"EXACT_LOCATION"`)

* `INTERSECTING_LOCATION` (value: `"INTERSECTING_LOCATION"`)





## Enum: LocationTypeEnum


* `DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED` (value: `"DEVELOPER_METADATA_LOCATION_TYPE_UNSPECIFIED"`)

* `ROW` (value: `"ROW"`)

* `COLUMN` (value: `"COLUMN"`)

* `SHEET` (value: `"SHEET"`)

* `SPREADSHEET` (value: `"SPREADSHEET"`)





## Enum: VisibilityEnum


* `DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED` (value: `"DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED"`)

* `DOCUMENT` (value: `"DOCUMENT"`)

* `PROJECT` (value: `"PROJECT"`)




