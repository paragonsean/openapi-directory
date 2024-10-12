

# PatientAuthConfirmResponseAuth

depending on the purpose of auth, as specified in /auth/init, the response may include the following    1. LINK - only returns **accessToken**   2. KYC - only returns **patient**   3. KYC_AND_LINK - returns both **accessToken** and **patient** 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessToken** | **String** | access token for initialization of subsequent action. |  [optional] |
|**patient** | [**PatientDemographicResponse**](PatientDemographicResponse.md) |  |  [optional] |
|**validity** | [**AccessTokenValidity**](AccessTokenValidity.md) |  |  [optional] |



