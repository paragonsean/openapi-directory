

# ThreeDSRequestorAuthenticationInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**threeDSReqAuthData** | **String** | Data that documents and supports a specific authentication process. Maximum length: 2048 bytes. |  [optional] |
|**threeDSReqAuthMethod** | [**ThreeDSReqAuthMethodEnum**](#ThreeDSReqAuthMethodEnum) | Mechanism used by the Cardholder to authenticate to the 3DS Requestor. Allowed values: * **01** — No 3DS Requestor authentication occurred (for example, cardholder “logged in” as guest). * **02** — Login to the cardholder account at the 3DS Requestor system using 3DS Requestor’s own credentials. * **03** — Login to the cardholder account at the 3DS Requestor system using federated ID. * **04** — Login to the cardholder account at the 3DS Requestor system using issuer credentials. * **05** — Login to the cardholder account at the 3DS Requestor system using third-party authentication. * **06** — Login to the cardholder account at the 3DS Requestor system using FIDO Authenticator. |  [optional] |
|**threeDSReqAuthTimestamp** | **String** | Date and time in UTC of the cardholder authentication. Format: YYYYMMDDHHMM |  [optional] |



## Enum: ThreeDSReqAuthMethodEnum

| Name | Value |
|---- | -----|
| _01 | &quot;01&quot; |
| _02 | &quot;02&quot; |
| _03 | &quot;03&quot; |
| _04 | &quot;04&quot; |
| _05 | &quot;05&quot; |
| _06 | &quot;06&quot; |



