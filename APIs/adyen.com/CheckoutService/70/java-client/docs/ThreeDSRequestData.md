

# ThreeDSRequestData


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**challengeWindowSize** | [**ChallengeWindowSizeEnum**](#ChallengeWindowSizeEnum) | Dimensions of the 3DS2 challenge window to be displayed to the cardholder.  Possible values:  * **01** - size of 250x400  * **02** - size of 390x400 * **03** - size of 500x600 * **04** - size of 600x400 * **05** - Fullscreen |  [optional] |
|**dataOnly** | [**DataOnlyEnum**](#DataOnlyEnum) | Flag for data only flow. |  [optional] |
|**nativeThreeDS** | [**NativeThreeDSEnum**](#NativeThreeDSEnum) | Indicates if [native 3D Secure authentication](https://docs.adyen.com/online-payments/3d-secure/native-3ds2) should be used when available.  Possible values: * **preferred**: Use native 3D Secure authentication when available. |  [optional] |
|**threeDSVersion** | [**ThreeDSVersionEnum**](#ThreeDSVersionEnum) | The version of 3D Secure to use.  Possible values:  * **2.1.0** * **2.2.0** |  [optional] |



## Enum: ChallengeWindowSizeEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |
| _03 | &quot;03&quot; |
| _04 | &quot;04&quot; |
| _05 | &quot;05&quot; |



## Enum: DataOnlyEnum

| Name | Value |
|---- | -----|
| FALSE | &quot;false&quot; |
| TRUE | &quot;true&quot; |



## Enum: NativeThreeDSEnum

| Name | Value |
|---- | -----|
| PREFERRED | &quot;preferred&quot; |



## Enum: ThreeDSVersionEnum

| Name | Value |
|---- | -----|
| _1_0 | &quot;2.1.0&quot; |
| _2_0 | &quot;2.2.0&quot; |



