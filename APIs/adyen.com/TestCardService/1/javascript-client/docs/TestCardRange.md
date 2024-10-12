# AdyenTestCardsApi.TestCardRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**AvsAddress**](AvsAddress.md) | Contains the billing address of the card holder. The address details need to be AVS-compliant, which means that you need to provide at least street address. | [optional] 
**cardHolderName** | **String** | The name of the card holder, as it appears on the card, for the test card range. | 
**cvc** | **String** | The test card range security code.  Example: 123 | [optional] 
**expiryMonth** | **String** | Expiry month for the test card range.  Allowed values: * JANUARY * FEBRUARY * MARCH * APRIL * MAY * JUNE * JULY * AUGUST * SEPTEMBER * OCTOBER * NOVEMBER * DECEMBER | 
**expiryYear** | **Number** | Expiry year for the test card range.  Example: 2020 | 
**rangeEnd** | **String** | The last test card number in the test card range (inclusive):  * Min 6, max 19 digits * BIN compliant Example: 5432 1234 1234 4321 | 
**rangeStart** | **String** | The first test card number in the test card range (inclusive):  * Min 6, max 19 digits * BIN compliant Example: 5432 1234 1234 1234 | 
**threeDDirectoryServerResponse** | **String** | 3D Secure server response. It notifies whether the specified card holder is enrolled in a 3D Secure service. Possible values:  * Y (Authentication available) * N (Card holder not enrolled/not participating) * U (Unable to authenticate) | [optional] 
**threeDPassword** | **String** | The password used for 3D Secure authentication. | [optional] 
**threeDUsername** | **String** | The username used for 3D Secure authentication. | [optional] 



## Enum: ExpiryMonthEnum


* `APRIL` (value: `"APRIL"`)

* `AUGUST` (value: `"AUGUST"`)

* `DECEMBER` (value: `"DECEMBER"`)

* `FEBRUARY` (value: `"FEBRUARY"`)

* `JANUARY` (value: `"JANUARY"`)

* `JULY` (value: `"JULY"`)

* `JUNE` (value: `"JUNE"`)

* `MARCH` (value: `"MARCH"`)

* `MAY` (value: `"MAY"`)

* `NOVEMBER` (value: `"NOVEMBER"`)

* `OCTOBER` (value: `"OCTOBER"`)

* `SEPTEMBER` (value: `"SEPTEMBER"`)





## Enum: ThreeDDirectoryServerResponseEnum


* `N` (value: `"N"`)

* `U` (value: `"U"`)

* `Y` (value: `"Y"`)




