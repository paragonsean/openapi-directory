# AdyenCheckoutApi.ThreeDSRequestData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challengeWindowSize** | **String** | Dimensions of the 3DS2 challenge window to be displayed to the cardholder.  Possible values:  * **01** - size of 250x400  * **02** - size of 390x400 * **03** - size of 500x600 * **04** - size of 600x400 * **05** - Fullscreen | [optional] 
**dataOnly** | **String** | Flag for data only flow. | [optional] 
**nativeThreeDS** | **String** | Indicates if [native 3D Secure authentication](https://docs.adyen.com/online-payments/3d-secure/native-3ds2) should be used when available.  Possible values: * **preferred**: Use native 3D Secure authentication when available. | [optional] 
**threeDSVersion** | **String** | The version of 3D Secure to use.  Possible values:  * **2.1.0** * **2.2.0** | [optional] 



## Enum: ChallengeWindowSizeEnum


* `01` (value: `"01"`)

* `02` (value: `"02"`)

* `03` (value: `"03"`)

* `04` (value: `"04"`)

* `05` (value: `"05"`)





## Enum: DataOnlyEnum


* `false` (value: `"false"`)

* `true` (value: `"true"`)





## Enum: NativeThreeDSEnum


* `preferred` (value: `"preferred"`)





## Enum: ThreeDSVersionEnum


* `1.0` (value: `"2.1.0"`)

* `2.0` (value: `"2.2.0"`)




