

# ProfileCreationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**languageCode** | **String** | The code of the preferred language for the profile. Must be a valid ISO language code e.g. \&quot;en-US\&quot; and must match the code of one of the languages specified in the app config. See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes  |  [optional] |
|**name** | **String** | The unique name of the profile. |  |
|**pinEnabled** | **Boolean** | Whether an account pin is required to enter the profile.  If no account pin is defined this has no impact.  |  [optional] |
|**purchaseEnabled** | **Boolean** | Whether the profile can make purchases with the account payment options. |  [optional] |
|**segments** | **List&lt;String&gt;** | The segments a profile should be placed under |  [optional] |



