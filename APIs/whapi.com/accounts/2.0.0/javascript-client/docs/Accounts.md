# AccountsApi.Accounts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID | [optional] 
**accountNum** | **String** | Account number | 
**additionalSystemStatuses** | **String** | Statuses of systems specific to that account - seperate from account status | [optional] 
**birthPlace** | **String** | Birthplace details (city, province country code) for customer - primaly used in italy | [optional] 
**city** | **String** | The city of the customer&#39;s address | [optional] 
**contactable** | **Boolean** | Is it okay for the bookmaker to contact the customer with marketing information | [optional] 
**country** | **String** | The country of the customer&#39;s address | [optional] 
**countryCode** | **String** | A two-character ISO 3166-1-Alpha-2 code representing the customer&#39;s country of registration | [optional] 
**county** | **String** | The county of the customer&#39;s address | [optional] 
**currencyCode** | **String** | A three-character ISO4217 currency code. This will be the currency that the customer registered in | [optional] 
**customerId** | **String** | Customer ID | [optional] 
**email** | **String** | The primary email address of the customer with that account. Must be unique. | [optional] 
**fax** | **String** | The fax number of the customer | [optional] 
**firstName** | **String** | The first name of the customer with that account | 
**flags** | [**[FlagsInner]**](FlagsInner.md) |  | [optional] 
**ipAddress** | **String** | Registered ip address of user | [optional] 
**language** | **String** | The registered language of the customer | [optional] 
**lastLogin** | **String** | The last time customer logged in - mandatory in italy - available if populated in other territories | [optional] 
**lastName** | **String** | The last name of the customer with that account | 
**mobile** | **String** | The mobile number of the customer with that account | [optional] 
**nif** | **String** | The national identifcation number of the customer (italy only - mandatory response field) | [optional] 
**office** | **String** | Office phone number of customer | [optional] 
**partnerContactable** | **Boolean** | Is it okay for the bookmaker to give the user&#39;s contact details to companies with which it has partnerships | [optional] 
**postcode** | **String** | The postCode of the customer&#39;s address | [optional] 
**secondLastName** | **String** | The second last name of the customer with that account - primarily used in Spanish territory | 
**status** | **String** | Account status | 
**street1** | **String** | Line number 1 of the customer&#39;s street address written out in full | [optional] 
**street2** | **String** | Line number 2 of the customer&#39;s street address written out in full | [optional] 
**street3** | **String** | Line number 3 of the customer&#39;s street address written out in full | [optional] 
**termsAndConditions** | **String** | name and url location of terms and conditions applicable to this account | [optional] 
**timeZone** | **String** | The primary time zone for the customer | [optional] 
**title** | **String** | The title of the name of the customer with that account | [optional] 


