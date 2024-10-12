# HetrasBookingApiVersion0.CustomerResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{String: LinkObject}**](LinkObject.md) | Collection of links to related resources | [optional] 
**customerId** | **String** | The id of a customer profile. The id is build out of the Supplier Code a dash and the profile id              shown in the hetras UI. An example id on the API for a profile with id 12345 on the level of supplier ABC               would be ABC-12345 | [optional] 
**email** | **String** | The primary email address of the guest | [optional] 
**firstName** | **String** | First name of the guest | [optional] 
**gender** | **String** | Gender | [optional] 
**lastName** | **String** | Last name of the guest | [optional] 
**mailingAddress** | [**MailingAddress**](MailingAddress.md) |  | [optional] 
**nationality** | **String** | The nationality of the guest in ISO 3166-1 alpha-2 format              (see: http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm) | [optional] 
**phone** | **String** | The primary phone number of the guest | [optional] 
**primary** | **Boolean** | Defines if the guest is the primary guest of the reservation | [optional] 
**subscribedConsents** | **[String]** | Gets or sets the list of consents subscribed by customer | [optional] 
**title** | **String** | Title of the guest. Needs to be taken from the available titles defined in the codes | [optional] 



## Enum: GenderEnum


* `Unspecified` (value: `"Unspecified"`)

* `Male` (value: `"Male"`)

* `Female` (value: `"Female"`)




