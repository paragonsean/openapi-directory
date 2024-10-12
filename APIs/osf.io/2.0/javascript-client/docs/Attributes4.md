# OsfApiv2Documentation.Attributes4

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The category of the Draft Registration. | [optional] 
**currentUserPermissions** | **[String]** | The current users permission level for the Draft Registration. | [optional] [readonly] 
**datetimeInitiated** | **Date** | The time at which the draft registration was first initiated, as an iso8601 formatted timestamp. | [optional] [readonly] 
**datetimeUpdated** | **Date** | The time at which the draft registration was last updated, as an iso8601 formatted timestamp. | [optional] [readonly] 
**description** | **String** | The description of the Draft Registration. | [optional] 
**hasProject** | **Boolean** | This indicates whether a Draft Registration was branched from a project. | [optional] [readonly] 
**nodeLicense** | [**NodeLicense**](NodeLicense.md) |  | [optional] 
**registrationMetadata** | **Object** | This is a legacy format for &#x60;registration_responses&#x60;. | [optional] 
**registrationResponses** | **Object** | A dictionary of question IDs and responses from the registration schema. | [optional] 
**tags** | **[String]** | The searchable tags of the Draft Registration. | [optional] 
**title** | **String** | The title of the Draft Registration. | [optional] 


