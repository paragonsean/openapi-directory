

# Organization


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**address** | **String** | The organization street address. |  [optional] |
|**address2** | **String** | The organization street address. |  [optional] |
|**city** | **String** | The organization city. |  [optional] |
|**country** | **String** | The organization country ISO Alpha-2 code. |  |
|**createdTime** | **OffsetDateTime** | The organization created time. |  [optional] [readonly] |
|**emails** | [**List&lt;ContactEmailsInner&gt;**](ContactEmailsInner.md) | The list of emails. |  [optional] |
|**id** | **String** | The organization identifier string. |  [optional] [readonly] |
|**invoiceTimeZone** | **String** | Invoice will use this time zone to display time otherwise UTC will be used. Example \&quot;America/New_York\&quot;. |  [optional] |
|**isPrimary** | **Boolean** | True, if Organization is primary (available to set as true only, other organizations will become as isPrimary&#x3D;false). |  [optional] |
|**name** | **String** | The organization name. |  |
|**phoneNumbers** | [**List&lt;ContactPhoneNumbersInner&gt;**](ContactPhoneNumbersInner.md) | The list of phone numbers. |  [optional] |
|**postalCode** | **String** | The organization postal code. |  [optional] |
|**questionnaire** | [**OrganizationQuestionnaire**](OrganizationQuestionnaire.md) |  |  [optional] |
|**region** | **String** | The organization region (state). |  [optional] |
|**taxDescriptor** | **String** | The organization&#39;s tax label. This will be displayed on the invoice. |  [optional] |
|**updatedTime** | **OffsetDateTime** | The organization updated time. |  [optional] [readonly] |



