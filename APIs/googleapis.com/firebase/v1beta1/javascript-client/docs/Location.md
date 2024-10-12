# FirebaseManagementApi.Location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **[String]** | Products and services that are available in the GCP resource location. | [optional] 
**locationId** | **String** | The ID of the GCP resource location. It will be one of the available [GCP resource locations](https://firebase.google.com/docs/projects/locations#types). | [optional] 
**type** | **String** | Indicates whether the GCP resource location is a [regional or multi-regional location](https://firebase.google.com/docs/projects/locations#types) for data replication. | [optional] 



## Enum: [FeaturesEnum]


* `LOCATION_FEATURE_UNSPECIFIED` (value: `"LOCATION_FEATURE_UNSPECIFIED"`)

* `FIRESTORE` (value: `"FIRESTORE"`)

* `DEFAULT_STORAGE` (value: `"DEFAULT_STORAGE"`)

* `FUNCTIONS` (value: `"FUNCTIONS"`)





## Enum: TypeEnum


* `LOCATION_TYPE_UNSPECIFIED` (value: `"LOCATION_TYPE_UNSPECIFIED"`)

* `REGIONAL` (value: `"REGIONAL"`)

* `MULTI_REGIONAL` (value: `"MULTI_REGIONAL"`)




