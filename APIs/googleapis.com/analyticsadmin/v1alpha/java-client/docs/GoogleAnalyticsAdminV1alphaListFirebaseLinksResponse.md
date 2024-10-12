

# GoogleAnalyticsAdminV1alphaListFirebaseLinksResponse

Response message for ListFirebaseLinks RPC

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**firebaseLinks** | [**List&lt;GoogleAnalyticsAdminV1alphaFirebaseLink&gt;**](GoogleAnalyticsAdminV1alphaFirebaseLink.md) | List of FirebaseLinks. This will have at most one value. |  [optional] |
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. Currently, Google Analytics supports only one FirebaseLink per property, so this will never be populated. |  [optional] |



