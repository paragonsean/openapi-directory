

# EntityIDVDetailsObject

Contains all the details we need to create/update an entity and generate an IDV token 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicantId** | **String** | The applicantId previously supplied when creating a token for the first time for an entity. Only required if re-submitting for a fresh token on a previously created applicant.  |  [optional] |
|**applicationId** | **String** | If this is for a native application SDK, then we need the applicationId as reported by the SDK. This will then be tied to the token so it cannot be used in another application or handset.  You must send either an applicationID or a referrer (see below)  |  [optional] |
|**entity** | [**EntityObject**](EntityObject.md) |  |  |
|**referrer** | **String** | If this is for a web SDK, then you need to supply the referrer domain so that the token can be validated by the IDV service  You must send either a referrer or an applicationID (see above)  |  [optional] |



