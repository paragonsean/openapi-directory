

# GoogleCloudDiscoveryengineV1betaUserInfo

Information of an end user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**userAgent** | **String** | User agent as included in the HTTP header. The field must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. This should not be set when using the client side event reporting with GTM or JavaScript tag in UserEventService.CollectUserEvent or if UserEvent.direct_user_request is set. |  [optional] |
|**userId** | **String** | Highly recommended for logged-in users. Unique identifier for logged-in user, such as a user name. Don&#39;t set for anonymous users. Always use a hashed value for this ID. Don&#39;t set the field to the same fixed ID for different users. This mixes the event history of those users together, which results in degraded model quality. The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an &#x60;INVALID_ARGUMENT&#x60; error is returned. |  [optional] |



