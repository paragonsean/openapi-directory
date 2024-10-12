# ApigeeApi.GoogleCloudApigeeV1Developer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessType** | **String** | Access type. | [optional] 
**appFamily** | **String** | Developer app family. | [optional] 
**apps** | **[String]** | List of apps associated with the developer. | [optional] 
**attributes** | [**[GoogleCloudApigeeV1Attribute]**](GoogleCloudApigeeV1Attribute.md) | Optional. Developer attributes (name/value pairs). The custom attribute limit is 18. | [optional] 
**companies** | **[String]** | List of companies associated with the developer. | [optional] 
**createdAt** | **String** | Output only. Time at which the developer was created in milliseconds since epoch. | [optional] [readonly] 
**developerId** | **String** | ID of the developer. **Note**: IDs are generated internally by Apigee and are not guaranteed to stay the same over time. | [optional] 
**email** | **String** | Required. Email address of the developer. This value is used to uniquely identify the developer in Apigee hybrid. Note that the email address has to be in lowercase only. | [optional] 
**firstName** | **String** | Required. First name of the developer. | [optional] 
**lastModifiedAt** | **String** | Output only. Time at which the developer was last modified in milliseconds since epoch. | [optional] [readonly] 
**lastName** | **String** | Required. Last name of the developer. | [optional] 
**organizationName** | **String** | Output only. Name of the Apigee organization in which the developer resides. | [optional] [readonly] 
**status** | **String** | Output only. Status of the developer. Valid values are &#x60;active&#x60; and &#x60;inactive&#x60;. | [optional] [readonly] 
**userName** | **String** | Required. User name of the developer. Not used by Apigee hybrid. | [optional] 


