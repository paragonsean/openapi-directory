

# ConsentsResponse201

Body of the JSON response for a successful consent request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | **LinksConsents** |  |  |
|**challengeData** | [**ChallengeData**](ChallengeData.md) |  |  [optional] |
|**chosenScaMethod** | [**AuthenticationObject**](AuthenticationObject.md) |  |  [optional] |
|**consentId** | **String** | ID of the corresponding consent object as returned by an account information consent request.  |  |
|**consentStatus** | **ConsentStatus** |  |  |
|**psuMessage** | **String** | Text to be displayed to the PSU. |  [optional] |
|**scaMethods** | [**List&lt;AuthenticationObject&gt;**](AuthenticationObject.md) | This data element might be contained, if SCA is required and if the PSU has a choice between different authentication methods.  Depending on the risk management of the ASPSP this choice might be offered before or after the PSU has been identified with the first relevant factor, or if an access token is transported.  If this data element is contained, then there is also a hyperlink of type &#39;startAuthorisationWithAuthenticationMethodSelection&#39; contained in the response body.  These methods shall be presented towards the PSU for selection by the TPP.  |  [optional] |



