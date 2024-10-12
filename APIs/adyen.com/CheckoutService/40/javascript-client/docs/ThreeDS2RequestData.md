# AdyenCheckoutApi.ThreeDS2RequestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationOnly** | **Boolean** | If set to true, you will only perform the [3D Secure 2 authentication](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only), and not the payment authorisation. | [optional] [default to false]
**challengeIndicator** | **String** | Possibility to specify a preference for receiving a challenge from the issuer. Allowed values: * &#x60;noPreference&#x60; * &#x60;requestNoChallenge&#x60; * &#x60;requestChallenge&#x60; * &#x60;requestChallengeAsMandate&#x60;  | [optional] 
**deviceChannel** | **String** | The environment of the shopper. Allowed values: * &#x60;app&#x60; * &#x60;browser&#x60; | 
**deviceRenderOptions** | [**DeviceRenderOptions**](DeviceRenderOptions.md) | Display options for the 3D Secure 2 SDK. Optional and only for &#x60;deviceChannel&#x60; **app**. | [optional] 
**messageVersion** | **String** | The &#x60;messageVersion&#x60; value indicating the 3D Secure 2 protocol version. | [optional] 
**notificationURL** | **String** | URL to where the issuer should send the &#x60;CRes&#x60;. Required if you are not using components for &#x60;channel&#x60; **Web** or if you are using classic integration &#x60;deviceChannel&#x60; **browser**. | [optional] 
**platform** | **String** | The platform of the shopper. Allowed values: * &#x60;iOS&#x60; * &#x60;android&#x60; * &#x60;browser&#x60; | [optional] 
**sdkAppID** | **String** | The &#x60;sdkAppID&#x60; value as received from the 3D Secure 2 SDK. Required for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**sdkEncData** | **String** | The &#x60;sdkEncData&#x60; value as received from the 3D Secure 2 SDK. Required for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**sdkEphemPubKey** | [**SDKEphemPubKey**](SDKEphemPubKey.md) | The &#x60;sdkEphemPubKey&#x60; value as received from the 3D Secure 2 SDK. Required for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**sdkMaxTimeout** | **Number** | The maximum amount of time in minutes for the 3D Secure 2 authentication process. Optional and only for &#x60;deviceChannel&#x60; set to **app**. Defaults to **60** minutes. | [optional] [default to 60]
**sdkReferenceNumber** | **String** | The &#x60;sdkReferenceNumber&#x60; value as received from the 3D Secure 2 SDK. Only for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**sdkTransID** | **String** | The &#x60;sdkTransID&#x60; value as received from the 3D Secure 2 SDK. Only for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**sdkVersion** | **String** | Version of the 3D Secure 2 mobile SDK.  Only for &#x60;deviceChannel&#x60; set to **app**. | [optional] 
**threeDSCompInd** | **String** | Completion indicator for the device fingerprinting. | [optional] 
**threeDSRequestorID** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor identifier assigned by the Directory Server when you enrol for 3D Secure 2. | [optional] 
**threeDSRequestorName** | **String** | Required for [authentication-only integration](https://docs.adyen.com/online-payments/3d-secure/other-3ds-flows/authentication-only) for Visa. Unique 3D Secure requestor name assigned by the Directory Server when you enrol for 3D Secure 2. | [optional] 
**threeDSRequestorURL** | **String** | URL of the (customer service) website that will be shown to the shopper in case of technical errors during the 3D Secure 2 process. | [optional] 



## Enum: ChallengeIndicatorEnum


* `noPreference` (value: `"noPreference"`)

* `requestNoChallenge` (value: `"requestNoChallenge"`)

* `requestChallenge` (value: `"requestChallenge"`)

* `requestChallengeAsMandate` (value: `"requestChallengeAsMandate"`)





## Enum: PlatformEnum


* `iOS` (value: `"iOS"`)

* `android` (value: `"android"`)

* `browser` (value: `"browser"`)




