# FrankieFinancialApi.DeviceCheckDetailsObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityType** | **String** | The type of activity we&#39;re checking. Choices are:   - SIGNUP: Used when an entity is signing up to your service  - LOGIN: Used when an already registered entity is logging in to your service  - PAYMENT: Used when you wish to check that all is well for a payment  - CONFIRMATION: User has confirmed an action and you wish to double check they&#39;re still legitimate    You can also supply vendor specific activityTypes if you know them. To do this, make the first character an underscore _.   So for example, to use BioCatch&#39;s LOGIN_3 type, you can send \&quot;_LOGIN_3\&quot; as a value. Note, if you do this, there is no error checking on the Frankie side, and thus if you supply an incorrect value, the call will fail.  | [optional] 
**additionalData** | [**[KeyValuePairObject]**](KeyValuePairObject.md) | Collection of additional data points you wish to add to the activity check. These are defined in conjunction with the Customer and the device checking service being used.  Standard values are supplied upon request:  | kvpKey | kvpType | kvpValue | | ------- | -------- | -------- | | detectedIp | general.string | The IP address you detect the transaction coming from | | accountId.src | id.external | Your account identifier. Can be a SHA hash or similar | | accountId.dst | id.external | Target/payee account identifier. Can be a SHA hash or similar | | entityId | id.external | Use this to override the Frankie entityID that would be used to identify | | amount | general.float | Amount involved in the transaction  | | platform  | general.string | One of APP, WEB, MOBILE_WEB. Assumes APP if not supplied | |   |   |   Like the activityType, you can also specify vendor specific additional data parameters by adding a leading underscore \&quot;_\&quot; to the kvpKey. You can set the kvpType to one of the available types, or just use general.string (recommended)  | [optional] 
**checkSessionKey** | **String** | the unique session based ID that will be checked against the service. | [optional] 
**checkType** | **String** | Describes the type of check service we need to verify with. Choices are:    - DEVICE: Services that will be checking device characteristics   - BIOMETRIC: Services that will be checking biomentric characteristics  | [optional] 



## Enum: ActivityTypeEnum


* `SIGNUP` (value: `"SIGNUP"`)

* `LOGIN` (value: `"LOGIN"`)

* `PAYMENT` (value: `"PAYMENT"`)

* `CONFIRMATION` (value: `"CONFIRMATION"`)

* `_&lt;Vendor Specific List&gt;` (value: `"_<Vendor Specific List>"`)





## Enum: CheckTypeEnum


* `DEVICE` (value: `"DEVICE"`)

* `BIOMETRIC` (value: `"BIOMETRIC"`)




