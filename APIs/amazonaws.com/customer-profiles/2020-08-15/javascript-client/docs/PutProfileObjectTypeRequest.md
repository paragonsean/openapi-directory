# AmazonConnectCustomerProfiles.PutProfileObjectTypeRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | Description of the profile object type. | 
**templateId** | **String** | A unique identifier for the object template. For some attributes in the request, the service will use the default value from the object template when TemplateId is present. If these attributes are present in the request, the service may return a &lt;code&gt;BadRequestException&lt;/code&gt;. These attributes include: AllowProfileCreation, SourceLastUpdatedTimestampFormat, Fields, and Keys. For example, if AllowProfileCreation is set to true when TemplateId is set, the service may return a &lt;code&gt;BadRequestException&lt;/code&gt;. | [optional] 
**expirationDays** | **Number** | The number of days until the data in the object expires. | [optional] 
**encryptionKey** | **String** | The customer-provided key to encrypt the profile object that will be created in this profile object type. | [optional] 
**allowProfileCreation** | **Boolean** | Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is &lt;code&gt;FALSE&lt;/code&gt;. If the AllowProfileCreation flag is set to &lt;code&gt;FALSE&lt;/code&gt;, then the service tries to fetch a standard profile and associate this object with the profile. If it is set to &lt;code&gt;TRUE&lt;/code&gt;, and if no match is found, then the service creates a new standard profile. | [optional] 
**sourceLastUpdatedTimestampFormat** | **String** | The format of your &lt;code&gt;sourceLastUpdatedTimestamp&lt;/code&gt; that was previously set up.  | [optional] 
**fields** | [**{String: ObjectTypeField}**](ObjectTypeField.md) | A map of the name and ObjectType field. | [optional] 
**keys** | **{String: Array}** | A list of unique keys that can be used to map data to the profile. | [optional] 
**tags** | **{String: String}** | The tags used to organize, track, or control access for this resource. | [optional] 


