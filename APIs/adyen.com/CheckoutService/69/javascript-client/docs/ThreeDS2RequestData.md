# AdyenCheckoutApi.ThreeDS2RequestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acctInfo** | [**AcctInfo**](AcctInfo.md) | Additional information about the Cardholder’s account provided by the 3DS Requestor. | [optional] 
**acctType** | **String** | Indicates the type of account. For example, for a multi-account card product. Length: 2 characters. Allowed values: * **01** — Not applicable * **02** — Credit * **03** — Debit | [optional] 
**acquirerBIN** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The acquiring BIN enrolled for 3D Secure 2. This string should match the value that you will use in the authorisation. Use 123456 on the Test platform. | [optional] 
**acquirerMerchantID** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The merchantId that is enrolled for 3D Secure 2 by the merchant&#39;s acquirer. This string should match the value that you will use in the authorisation. Use 123456 on the Test platform. | [optional] 
**addrMatch** | **String** | Indicates whether the Cardholder Shipping Address and Cardholder Billing Address are the same. Allowed values: * **Y** — Shipping Address matches Billing Address. * **N** — Shipping Address does not match Billing Address. | [optional] 
**authenticationOnly** | **Boolean** | If set to true, you will only perform the [3D Secure 2 authentication](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only), and not the payment authorisation. | [optional] [default to false]
**challengeIndicator** | **String** | Possibility to specify a preference for receiving a challenge from the issuer. Allowed values: * &#x60;noPreference&#x60; * &#x60;requestNoChallenge&#x60; * &#x60;requestChallenge&#x60; * &#x60;requestChallengeAsMandate&#x60;  | [optional] 
**deviceChannel** | **String** | The environment of the shopper. Allowed values: * &#x60;app&#x60; * &#x60;browser&#x60; | 
**deviceRenderOptions** | [**DeviceRenderOptions**](DeviceRenderOptions.md) | Display options for the 3D Secure 2 SDK. Optional and only for &#x60;deviceChannel&#x60; **app**. | [optional] 
**homePhone** | [**Phone**](Phone.md) | The home phone number provided by the Cardholder. | [optional] 
**mcc** | **String** | Required for merchants that have been enrolled for 3D Secure 2 by another party than Adyen, mostly [authentication-only integrations](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The &#x60;mcc&#x60; is a four-digit code with which the previously given &#x60;acquirerMerchantID&#x60; is registered at the scheme. | [optional] 
**merchantName** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The merchant name that the issuer presents to the shopper if they get a challenge. We recommend to use the same value that you will use in the authorization. Maximum length is 40 characters. &gt; Optional for a [full 3D Secure 2 integration](https://docs.adyen.com/online-payments/3d-secure/native-3ds2/api-integration). Use this field if you are enrolled for 3D Secure 2 with us and want to override the merchant name already configured on your account. | [optional] 
**messageVersion** | **String** | The &#x60;messageVersion&#x60; value indicating the 3D Secure 2 protocol version. | [optional] 
**mobilePhone** | [**Phone**](Phone.md) | The mobile phone number provided by the Cardholder. | [optional] 
**notificationURL** | **String** | URL to where the issuer should send the &#x60;CRes&#x60;. Required if you are not using components for &#x60;channel&#x60; **Web** or if you are using classic integration &#x60;deviceChannel&#x60; **browser**. | [optional] 
**payTokenInd** | **Boolean** | Value **true** indicates that the transaction was de-tokenised prior to being received by the ACS. | [optional] 
**paymentAuthenticationUseCase** | **String** | Indicates the type of payment for which an authentication is requested (message extension) | [optional] 
**platform** | **String** | The platform of the shopper. Allowed values: * &#x60;iOS&#x60; * &#x60;android&#x60; * &#x60;browser&#x60; | [optional] 
**purchaseInstalData** | **String** | Indicates the maximum number of authorisations permitted for instalment payments. Length: 1–3 characters. | [optional] 
**recurringExpiry** | **String** | Date after which no further authorisations shall be performed. Format: YYYYMMDD | [optional] 
**recurringFrequency** | **String** | Indicates the minimum number of days between authorisations. Maximum length: 4 characters. | [optional] 
**sdkAppID** | **String** | The &#x60;sdkAppID&#x60; value as received from the 3D Secure 2 SDK. Required for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**sdkEncData** | **String** | The &#x60;sdkEncData&#x60; value as received from the 3D Secure 2 SDK. Required for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**sdkEphemPubKey** | [**SDKEphemPubKey**](SDKEphemPubKey.md) | The &#x60;sdkEphemPubKey&#x60; value as received from the 3D Secure 2 SDK. Required for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**sdkMaxTimeout** | **Number** | The maximum amount of time in minutes for the 3D Secure 2 authentication process. Optional and only for &#x60;deviceChannel&#x60; set to **app**. Defaults to **60** minutes. | [optional] [default to 60]
**sdkReferenceNumber** | **String** | The &#x60;sdkReferenceNumber&#x60; value as received from the 3D Secure 2 SDK. Only for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**sdkTransID** | **String** | The &#x60;sdkTransID&#x60; value as received from the 3D Secure 2 SDK. Only for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**sdkVersion** | **String** | Version of the 3D Secure 2 mobile SDK.  Only for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**threeDSCompInd** | **String** | Completion indicator for the device fingerprinting. | [optional] 
**threeDSRequestorAuthenticationInd** | **String** | Indicates the type of Authentication request. | [optional] 
**threeDSRequestorAuthenticationInfo** | [**ThreeDSRequestorAuthenticationInfo**](ThreeDSRequestorAuthenticationInfo.md) | Information about how the 3DS Requestor authenticated the cardholder before or during the transaction | [optional] 
**threeDSRequestorChallengeInd** | **String** | Indicates whether a challenge is requested for this transaction. Possible values: * **01** — No preference * **02** — No challenge requested * **03** — Challenge requested (3DS Requestor preference) * **04** — Challenge requested (Mandate) * **05** — No challenge (transactional risk analysis is already performed) * **06** — Data Only | [optional] 
**threeDSRequestorID** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor identifier assigned by the Directory Server when you enrol for 3D Secure 2. | [optional] 
**threeDSRequestorName** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor name assigned by the Directory Server when you enrol for 3D Secure 2. | [optional] 
**threeDSRequestorPriorAuthenticationInfo** | [**ThreeDSRequestorPriorAuthenticationInfo**](ThreeDSRequestorPriorAuthenticationInfo.md) | Information about how the 3DS Requestor authenticated the cardholder as part of a previous 3DS transaction. | [optional] 
**threeDSRequestorURL** | **String** | URL of the (customer service) website that will be shown to the shopper in case of technical errors during the 3D Secure 2 process. | [optional] 
**transType** | **String** | Identifies the type of transaction being authenticated. Length: 2 characters. Allowed values: * **01** — Goods/Service Purchase * **03** — Check Acceptance * **10** — Account Funding * **11** — Quasi-Cash Transaction * **28** — Prepaid Activation and Load | [optional] 
**transactionType** | **String** | Identify the type of the transaction being authenticated. | [optional] 
**whiteListStatus** | **String** | The &#x60;whiteListStatus&#x60; value returned from a previous 3D Secure 2 transaction, only applicable for 3D Secure 2 protocol version 2.2.0. | [optional] 
**workPhone** | [**Phone**](Phone.md) | The work phone number provided by the Cardholder. | [optional] 



## Enum: AcctTypeEnum


* `01` (value: `"01"`)

* `02` (value: `"02"`)

* `03` (value: `"03"`)





## Enum: AddrMatchEnum


* `Y` (value: `"Y"`)

* `N` (value: `"N"`)





## Enum: ChallengeIndicatorEnum


* `noPreference` (value: `"noPreference"`)

* `requestNoChallenge` (value: `"requestNoChallenge"`)

* `requestChallenge` (value: `"requestChallenge"`)

* `requestChallengeAsMandate` (value: `"requestChallengeAsMandate"`)





## Enum: PlatformEnum


* `iOS` (value: `"iOS"`)

* `android` (value: `"android"`)

* `browser` (value: `"browser"`)





## Enum: ThreeDSRequestorChallengeIndEnum


* `01` (value: `"01"`)

* `02` (value: `"02"`)

* `03` (value: `"03"`)

* `04` (value: `"04"`)

* `05` (value: `"05"`)

* `06` (value: `"06"`)





## Enum: TransTypeEnum


* `01` (value: `"01"`)

* `03` (value: `"03"`)

* `10` (value: `"10"`)

* `11` (value: `"11"`)

* `28` (value: `"28"`)





## Enum: TransactionTypeEnum


* `goodsOrServicePurchase` (value: `"goodsOrServicePurchase"`)

* `checkAcceptance` (value: `"checkAcceptance"`)

* `accountFunding` (value: `"accountFunding"`)

* `quasiCashTransaction` (value: `"quasiCashTransaction"`)

* `prepaidActivationAndLoad` (value: `"prepaidActivationAndLoad"`)




