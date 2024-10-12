

# HrisCompany


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addresses** | [**List&lt;Address&gt;**](Address.md) |  |  [optional] |
|**companyNumber** | **String** | An Company Number, Company ID or Company Code, is a unique number that has been assigned to each company. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**createdBy** | **String** | The user who created the object. |  [optional] [readonly] |
|**currency** | **Currency** |  |  [optional] |
|**customMappings** | **Object** | When custom mappings are configured on the resource, the result is included here. |  [optional] |
|**debtorId** | **String** |  |  [optional] |
|**deleted** | **Boolean** |  |  [optional] [readonly] |
|**displayName** | **String** |  |  [optional] |
|**emails** | [**List&lt;Email&gt;**](Email.md) |  |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**legalName** | **String** |  |  |
|**phoneNumbers** | [**List&lt;PhoneNumber&gt;**](PhoneNumber.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**subdomain** | **String** |  |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |
|**updatedBy** | **String** | The user who last updated the object. |  [optional] [readonly] |
|**websites** | [**List&lt;Website&gt;**](Website.md) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| TRIAL | &quot;trial&quot; |
| OTHER | &quot;other&quot; |



