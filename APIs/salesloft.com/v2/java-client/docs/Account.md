

# Account


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountTier** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**archivedAt** | **OffsetDateTime** | Datetime of when the Account was archived, if archived |  [optional] |
|**city** | **String** | City |  [optional] |
|**companyStage** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**companyType** | **String** | Type of the Account&#39;s company |  [optional] |
|**conversationalName** | **String** | Conversational name of the Account |  [optional] |
|**country** | **String** | Country |  [optional] |
|**counts** | [**EmbeddedAccountCounts**](EmbeddedAccountCounts.md) |  |  [optional] |
|**createdAt** | **OffsetDateTime** | Datetime of when the Account was created |  [optional] |
|**creator** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**crmId** | **String** | CRM ID |  [optional] |
|**crmObjectType** | **String** | CRM object type |  [optional] |
|**crmUrl** | **String** | CRM url |  [optional] |
|**customFields** | **Object** | Custom fields are defined by the user&#39;s team. Only fields with values are presented in the API. |  [optional] |
|**description** | **String** | Description |  [optional] |
|**doNotContact** | **Boolean** | Whether this company has opted out of communications. Do not contact someone at this company when this is set to true |  [optional] |
|**domain** | **String** | Website domain, not a fully qualified URI |  [optional] |
|**founded** | **String** | Date or year of founding |  [optional] |
|**id** | **Integer** | ID of Account |  [optional] |
|**industry** | **String** | Industry |  [optional] |
|**lastContactedAt** | **OffsetDateTime** | Datetime this Account was last contacted |  [optional] |
|**lastContactedBy** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**lastContactedPerson** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**lastContactedType** | **String** | The type of the last touch to this Account. Can be call, email, other |  [optional] |
|**linkedinUrl** | **String** | Full LinkedIn url |  [optional] |
|**locale** | **String** | Time locale |  [optional] |
|**name** | **String** | Account Full Name |  [optional] |
|**owner** | [**EmbeddedResource**](EmbeddedResource.md) |  |  [optional] |
|**ownerCrmId** | **String** | Mapped owner field from the CRM |  [optional] |
|**phone** | **String** | Phone number without formatting |  [optional] |
|**postalCode** | **String** | Postal code |  [optional] |
|**revenueRange** | **String** | Estimated revenue range |  [optional] |
|**size** | **String** | Estimated number of people in employment |  [optional] |
|**state** | **String** | State |  [optional] |
|**street** | **String** | Street name and number |  [optional] |
|**tags** | **List&lt;String&gt;** | All tags applied to this Account |  [optional] |
|**twitterHandle** | **String** | Twitter handle, with @ |  [optional] |
|**updatedAt** | **OffsetDateTime** | Datetime of when the Account was last updated |  [optional] |
|**userRelationships** | **Object** | Filters by accounts matching all given user relationship fields, _is_null or _unmapped can be passed to filter accounts with null or unmapped user relationship values |  [optional] |
|**website** | **String** | Website |  [optional] |



