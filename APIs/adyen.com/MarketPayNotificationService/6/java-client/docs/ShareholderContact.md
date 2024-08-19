

# ShareholderContact


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**ViasAddress**](ViasAddress.md) | The address of the person. |  [optional] |
|**email** | **String** | The e-mail address of the person. |  [optional] |
|**fullPhoneNumber** | **String** | The phone number of the person provided as a single string.  It will be handled as a landline phone. Examples: \&quot;0031 6 11 22 33 44\&quot;, \&quot;+316/1122-3344\&quot;, \&quot;(0031) 611223344\&quot; |  [optional] |
|**jobTitle** | **String** | Job title of the person. Required when the &#x60;shareholderType&#x60; is **Controller**.  Example values: **Chief Executive Officer**, **Chief Financial Officer**, **Chief Operating Officer**, **President**, **Vice President**, **Executive President**, **Managing Member**, **Partner**, **Treasurer**, **Director**, or **Other**. |  [optional] |
|**name** | [**ViasName**](ViasName.md) | The name of the person. |  [optional] |
|**personalData** | [**ViasPersonalData**](ViasPersonalData.md) | Contains information about the person. |  [optional] |
|**phoneNumber** | [**ViasPhoneNumber**](ViasPhoneNumber.md) | The phone number of the person. |  [optional] |
|**shareholderCode** | **String** | The unique identifier (UUID) of the shareholder entry. &gt;**If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Shareholder will be created with a procedurally-generated UUID.**  &gt;**If, during an Account Holder create request, a UUID is provided, the creation of Account Holder will fail with a validation Error..**  &gt;**If, during an Account Holder update request, a UUID that is not correlated with an existing Shareholder is provided, the update of the Shareholder will fail.**  &gt;**If, during an Account Holder update request, a UUID that is correlated with an existing Shareholder is provided, the existing Shareholder will be updated.**  |  [optional] |
|**shareholderReference** | **String** | Your reference for the shareholder entry. |  [optional] |
|**shareholderType** | [**ShareholderTypeEnum**](#ShareholderTypeEnum) | Specifies how the person is associated with the account holder.   Possible values:   * **Owner**: Individuals who directly or indirectly own 25% or more of a company.  * **Controller**: Individuals who are members of senior management staff responsible for managing a company or organization. |  [optional] |
|**webAddress** | **String** | The URL of the person&#39;s website. |  [optional] |



## Enum: ShareholderTypeEnum

| Name | Value |
|---- | -----|
| CONTROLLER | &quot;Controller&quot; |
| OWNER | &quot;Owner&quot; |
| SIGNATORY | &quot;Signatory&quot; |



