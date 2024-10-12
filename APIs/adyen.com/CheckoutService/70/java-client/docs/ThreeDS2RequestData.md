

# ThreeDS2RequestData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acctInfo** | [**AcctInfo**](AcctInfo.md) | Additional information about the Cardholder’s account provided by the 3DS Requestor. |  [optional] |
|**acctType** | [**AcctTypeEnum**](#AcctTypeEnum) | Indicates the type of account. For example, for a multi-account card product. Length: 2 characters. Allowed values: * **01** — Not applicable * **02** — Credit * **03** — Debit |  [optional] |
|**acquirerBIN** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The acquiring BIN enrolled for 3D Secure 2. This string should match the value that you will use in the authorisation. Use 123456 on the Test platform. |  [optional] |
|**acquirerMerchantID** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The merchantId that is enrolled for 3D Secure 2 by the merchant&#39;s acquirer. This string should match the value that you will use in the authorisation. Use 123456 on the Test platform. |  [optional] |
|**addrMatch** | [**AddrMatchEnum**](#AddrMatchEnum) | Indicates whether the Cardholder Shipping Address and Cardholder Billing Address are the same. Allowed values: * **Y** — Shipping Address matches Billing Address. * **N** — Shipping Address does not match Billing Address. |  [optional] |
|**authenticationOnly** | **Boolean** | If set to true, you will only perform the [3D Secure 2 authentication](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only), and not the payment authorisation. |  [optional] |
|**challengeIndicator** | [**ChallengeIndicatorEnum**](#ChallengeIndicatorEnum) | Possibility to specify a preference for receiving a challenge from the issuer. Allowed values: * &#x60;noPreference&#x60; * &#x60;requestNoChallenge&#x60; * &#x60;requestChallenge&#x60; * &#x60;requestChallengeAsMandate&#x60;  |  [optional] |
|**deviceChannel** | **String** | The environment of the shopper. Allowed values: * &#x60;app&#x60; * &#x60;browser&#x60; |  |
|**deviceRenderOptions** | [**DeviceRenderOptions**](DeviceRenderOptions.md) | Display options for the 3D Secure 2 SDK. Optional and only for &#x60;deviceChannel&#x60; **app**. |  [optional] |
|**homePhone** | [**Phone**](Phone.md) | The home phone number provided by the Cardholder. |  [optional] |
|**mcc** | **String** | Required for merchants that have been enrolled for 3D Secure 2 by another party than Adyen, mostly [authentication-only integrations](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The &#x60;mcc&#x60; is a four-digit code with which the previously given &#x60;acquirerMerchantID&#x60; is registered at the scheme. |  [optional] |
|**merchantName** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only). The merchant name that the issuer presents to the shopper if they get a challenge. We recommend to use the same value that you will use in the authorization. Maximum length is 40 characters. &gt; Optional for a [full 3D Secure 2 integration](https://docs.adyen.com/online-payments/3d-secure/native-3ds2/api-integration). Use this field if you are enrolled for 3D Secure 2 with us and want to override the merchant name already configured on your account. |  [optional] |
|**messageVersion** | **String** | The &#x60;messageVersion&#x60; value indicating the 3D Secure 2 protocol version. |  [optional] |
|**mobilePhone** | [**Phone**](Phone.md) | The mobile phone number provided by the Cardholder. |  [optional] |
|**notificationURL** | **String** | URL to where the issuer should send the &#x60;CRes&#x60;. Required if you are not using components for &#x60;channel&#x60; **Web** or if you are using classic integration &#x60;deviceChannel&#x60; **browser**. |  [optional] |
|**payTokenInd** | **Boolean** | Value **true** indicates that the transaction was de-tokenised prior to being received by the ACS. |  [optional] |
|**paymentAuthenticationUseCase** | **String** | Indicates the type of payment for which an authentication is requested (message extension) |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | The platform of the shopper. Allowed values: * &#x60;iOS&#x60; * &#x60;android&#x60; * &#x60;browser&#x60; |  [optional] |
|**purchaseInstalData** | **String** | Indicates the maximum number of authorisations permitted for instalment payments. Length: 1–3 characters. |  [optional] |
|**recurringExpiry** | **String** | Date after which no further authorisations shall be performed. Format: YYYYMMDD |  [optional] |
|**recurringFrequency** | **String** | Indicates the minimum number of days between authorisations. Maximum length: 4 characters. |  [optional] |
|**sdkAppID** | **String** | The &#x60;sdkAppID&#x60; value as received from the 3D Secure 2 SDK. Required for &#x60;deviceChannel&#x60; set to **app**. |  [optional] |
|**sdkEncData** | **String** | The &#x60;sdkEncData&#x60; value as received from the 3D Secure 2 SDK. Required for &#x60;deviceChannel&#x60; set to **app**. |  [optional] |
|**sdkEphemPubKey** | [**SDKEphemPubKey**](SDKEphemPubKey.md) | The &#x60;sdkEphemPubKey&#x60; value as received from the 3D Secure 2 SDK. Required for &#x60;deviceChannel&#x60; set to **app**. |  [optional] |
|**sdkMaxTimeout** | **Integer** | The maximum amount of time in minutes for the 3D Secure 2 authentication process. Optional and only for &#x60;deviceChannel&#x60; set to **app**. Defaults to **60** minutes. |  [optional] |
|**sdkReferenceNumber** | **String** | The &#x60;sdkReferenceNumber&#x60; value as received from the 3D Secure 2 SDK. Only for &#x60;deviceChannel&#x60; set to **app**. |  [optional] |
|**sdkTransID** | **String** | The &#x60;sdkTransID&#x60; value as received from the 3D Secure 2 SDK. Only for &#x60;deviceChannel&#x60; set to **app**. |  [optional] |
|**sdkVersion** | **String** | Version of the 3D Secure 2 mobile SDK.  Only for &#x60;deviceChannel&#x60; set to **app**. |  [optional] |
|**threeDSCompInd** | **String** | Completion indicator for the device fingerprinting. |  [optional] |
|**threeDSRequestorAuthenticationInd** | **String** | Indicates the type of Authentication request. |  [optional] |
|**threeDSRequestorAuthenticationInfo** | [**ThreeDSRequestorAuthenticationInfo**](ThreeDSRequestorAuthenticationInfo.md) | Information about how the 3DS Requestor authenticated the cardholder before or during the transaction |  [optional] |
|**threeDSRequestorChallengeInd** | [**ThreeDSRequestorChallengeIndEnum**](#ThreeDSRequestorChallengeIndEnum) | Indicates whether a challenge is requested for this transaction. Possible values: * **01** — No preference * **02** — No challenge requested * **03** — Challenge requested (3DS Requestor preference) * **04** — Challenge requested (Mandate) * **05** — No challenge (transactional risk analysis is already performed) * **06** — Data Only |  [optional] |
|**threeDSRequestorID** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor identifier assigned by the Directory Server when you enrol for 3D Secure 2. |  [optional] |
|**threeDSRequestorName** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor name assigned by the Directory Server when you enrol for 3D Secure 2. |  [optional] |
|**threeDSRequestorPriorAuthenticationInfo** | [**ThreeDSRequestorPriorAuthenticationInfo**](ThreeDSRequestorPriorAuthenticationInfo.md) | Information about how the 3DS Requestor authenticated the cardholder as part of a previous 3DS transaction. |  [optional] |
|**threeDSRequestorURL** | **String** | URL of the (customer service) website that will be shown to the shopper in case of technical errors during the 3D Secure 2 process. |  [optional] |
|**transType** | [**TransTypeEnum**](#TransTypeEnum) | Identifies the type of transaction being authenticated. Length: 2 characters. Allowed values: * **01** — Goods/Service Purchase * **03** — Check Acceptance * **10** — Account Funding * **11** — Quasi-Cash Transaction * **28** — Prepaid Activation and Load |  [optional] |
|**transactionType** | [**TransactionTypeEnum**](#TransactionTypeEnum) | Identify the type of the transaction being authenticated. |  [optional] |
|**whiteListStatus** | **String** | The &#x60;whiteListStatus&#x60; value returned from a previous 3D Secure 2 transaction, only applicable for 3D Secure 2 protocol version 2.2.0. |  [optional] |
|**workPhone** | [**Phone**](Phone.md) | The work phone number provided by the Cardholder. |  [optional] |



## Enum: AcctTypeEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |
| _03 | &quot;03&quot; |



## Enum: AddrMatchEnum

| Name | Value |
|---- | -----|
| Y | &quot;Y&quot; |
| N | &quot;N&quot; |



## Enum: ChallengeIndicatorEnum

| Name | Value |
|---- | -----|
| NO_PREFERENCE | &quot;noPreference&quot; |
| REQUEST_NO_CHALLENGE | &quot;requestNoChallenge&quot; |
| REQUEST_CHALLENGE | &quot;requestChallenge&quot; |
| REQUEST_CHALLENGE_AS_MANDATE | &quot;requestChallengeAsMandate&quot; |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| I_OS | &quot;iOS&quot; |
| ANDROID | &quot;android&quot; |
| BROWSER | &quot;browser&quot; |



## Enum: ThreeDSRequestorChallengeIndEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |
| _03 | &quot;03&quot; |
| _04 | &quot;04&quot; |
| _05 | &quot;05&quot; |
| _06 | &quot;06&quot; |



## Enum: TransTypeEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _03 | &quot;03&quot; |
| _10 | &quot;10&quot; |
| _11 | &quot;11&quot; |
| _28 | &quot;28&quot; |



## Enum: TransactionTypeEnum

| Name | Value |
|---- | -----|
| GOODS_OR_SERVICE_PURCHASE | &quot;goodsOrServicePurchase&quot; |
| CHECK_ACCEPTANCE | &quot;checkAcceptance&quot; |
| ACCOUNT_FUNDING | &quot;accountFunding&quot; |
| QUASI_CASH_TRANSACTION | &quot;quasiCashTransaction&quot; |
| PREPAID_ACTIVATION_AND_LOAD | &quot;prepaidActivationAndLoad&quot; |



