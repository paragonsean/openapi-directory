

# Visa

Fields specific to the `visa` network

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**electronicCommerceIndicator** | [**ElectronicCommerceIndicatorEnum**](#ElectronicCommerceIndicatorEnum) | For electronic commerce transactions, this identifies the level of security used in obtaining the customer&#39;s payment credential. For mail or telephone order transactions, identifies the type of mail or telephone order. |  |
|**pointOfServiceEntryMode** | [**PointOfServiceEntryModeEnum**](#PointOfServiceEntryModeEnum) | The method used to enter the cardholder&#39;s primary account number and card expiration date |  |



## Enum: ElectronicCommerceIndicatorEnum

| Name | Value |
|---- | -----|
| MAIL_PHONE_ORDER | &quot;mail_phone_order&quot; |
| RECURRING | &quot;recurring&quot; |
| INSTALLMENT | &quot;installment&quot; |
| UNKNOWN_MAIL_PHONE_ORDER | &quot;unknown_mail_phone_order&quot; |
| SECURE_ELECTRONIC_COMMERCE | &quot;secure_electronic_commerce&quot; |
| NON_AUTHENTICATED_SECURITY_TRANSACTION_AT_3DS_CAPABLE_MERCHANT | &quot;non_authenticated_security_transaction_at_3ds_capable_merchant&quot; |
| NON_AUTHENTICATED_SECURITY_TRANSACTION | &quot;non_authenticated_security_transaction&quot; |
| NON_SECURE_TRANSACTION | &quot;non_secure_transaction&quot; |



## Enum: PointOfServiceEntryModeEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;manual&quot; |
| MAGNETIC_STRIPE_NO_CVV | &quot;magnetic_stripe_no_cvv&quot; |
| OPTICAL_CODE | &quot;optical_code&quot; |
| INTEGRATED_CIRCUIT_CARD | &quot;integrated_circuit_card&quot; |
| CONTACTLESS | &quot;contactless&quot; |
| CREDENTIAL_ON_FILE | &quot;credential_on_file&quot; |
| MAGNETIC_STRIPE | &quot;magnetic_stripe&quot; |
| CONTACTLESS_MAGNETIC_STRIPE | &quot;contactless_magnetic_stripe&quot; |
| INTEGRATED_CIRCUIT_CARD_NO_CVV | &quot;integrated_circuit_card_no_cvv&quot; |



