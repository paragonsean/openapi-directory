# AmazonChime.DefaultApi

All URIs are relative to *http://service.chime.aws.amazon.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associatePhoneNumberWithUser**](DefaultApi.md#associatePhoneNumberWithUser) | **POST** /accounts/{accountId}/users/{userId}#operation&#x3D;associate-phone-number | 
[**associatePhoneNumbersWithVoiceConnector**](DefaultApi.md#associatePhoneNumbersWithVoiceConnector) | **POST** /voice-connectors/{voiceConnectorId}#operation&#x3D;associate-phone-numbers | 
[**associatePhoneNumbersWithVoiceConnectorGroup**](DefaultApi.md#associatePhoneNumbersWithVoiceConnectorGroup) | **POST** /voice-connector-groups/{voiceConnectorGroupId}#operation&#x3D;associate-phone-numbers | 
[**associateSigninDelegateGroupsWithAccount**](DefaultApi.md#associateSigninDelegateGroupsWithAccount) | **POST** /accounts/{accountId}#operation&#x3D;associate-signin-delegate-groups | 
[**batchCreateAttendee**](DefaultApi.md#batchCreateAttendee) | **POST** /meetings/{meetingId}/attendees#operation&#x3D;batch-create | 
[**batchCreateChannelMembership**](DefaultApi.md#batchCreateChannelMembership) | **POST** /channels/{channelArn}/memberships#operation&#x3D;batch-create | 
[**batchCreateRoomMembership**](DefaultApi.md#batchCreateRoomMembership) | **POST** /accounts/{accountId}/rooms/{roomId}/memberships#operation&#x3D;batch-create | 
[**batchDeletePhoneNumber**](DefaultApi.md#batchDeletePhoneNumber) | **POST** /phone-numbers#operation&#x3D;batch-delete | 
[**batchSuspendUser**](DefaultApi.md#batchSuspendUser) | **POST** /accounts/{accountId}/users#operation&#x3D;suspend | 
[**batchUnsuspendUser**](DefaultApi.md#batchUnsuspendUser) | **POST** /accounts/{accountId}/users#operation&#x3D;unsuspend | 
[**batchUpdatePhoneNumber**](DefaultApi.md#batchUpdatePhoneNumber) | **POST** /phone-numbers#operation&#x3D;batch-update | 
[**batchUpdateUser**](DefaultApi.md#batchUpdateUser) | **POST** /accounts/{accountId}/users | 
[**createAccount**](DefaultApi.md#createAccount) | **POST** /accounts | 
[**createAppInstance**](DefaultApi.md#createAppInstance) | **POST** /app-instances | 
[**createAppInstanceAdmin**](DefaultApi.md#createAppInstanceAdmin) | **POST** /app-instances/{appInstanceArn}/admins | 
[**createAppInstanceUser**](DefaultApi.md#createAppInstanceUser) | **POST** /app-instance-users | 
[**createAttendee**](DefaultApi.md#createAttendee) | **POST** /meetings/{meetingId}/attendees | 
[**createBot**](DefaultApi.md#createBot) | **POST** /accounts/{accountId}/bots | 
[**createChannel**](DefaultApi.md#createChannel) | **POST** /channels | 
[**createChannelBan**](DefaultApi.md#createChannelBan) | **POST** /channels/{channelArn}/bans | 
[**createChannelMembership**](DefaultApi.md#createChannelMembership) | **POST** /channels/{channelArn}/memberships | 
[**createChannelModerator**](DefaultApi.md#createChannelModerator) | **POST** /channels/{channelArn}/moderators | 
[**createMediaCapturePipeline**](DefaultApi.md#createMediaCapturePipeline) | **POST** /media-capture-pipelines | 
[**createMeeting**](DefaultApi.md#createMeeting) | **POST** /meetings | 
[**createMeetingDialOut**](DefaultApi.md#createMeetingDialOut) | **POST** /meetings/{meetingId}/dial-outs | 
[**createMeetingWithAttendees**](DefaultApi.md#createMeetingWithAttendees) | **POST** /meetings#operation&#x3D;create-attendees | 
[**createPhoneNumberOrder**](DefaultApi.md#createPhoneNumberOrder) | **POST** /phone-number-orders | 
[**createProxySession**](DefaultApi.md#createProxySession) | **POST** /voice-connectors/{voiceConnectorId}/proxy-sessions | 
[**createRoom**](DefaultApi.md#createRoom) | **POST** /accounts/{accountId}/rooms | 
[**createRoomMembership**](DefaultApi.md#createRoomMembership) | **POST** /accounts/{accountId}/rooms/{roomId}/memberships | 
[**createSipMediaApplication**](DefaultApi.md#createSipMediaApplication) | **POST** /sip-media-applications | 
[**createSipMediaApplicationCall**](DefaultApi.md#createSipMediaApplicationCall) | **POST** /sip-media-applications/{sipMediaApplicationId}/calls | 
[**createSipRule**](DefaultApi.md#createSipRule) | **POST** /sip-rules | 
[**createUser**](DefaultApi.md#createUser) | **POST** /accounts/{accountId}/users#operation&#x3D;create | 
[**createVoiceConnector**](DefaultApi.md#createVoiceConnector) | **POST** /voice-connectors | 
[**createVoiceConnectorGroup**](DefaultApi.md#createVoiceConnectorGroup) | **POST** /voice-connector-groups | 
[**deleteAccount**](DefaultApi.md#deleteAccount) | **DELETE** /accounts/{accountId} | 
[**deleteAppInstance**](DefaultApi.md#deleteAppInstance) | **DELETE** /app-instances/{appInstanceArn} | 
[**deleteAppInstanceAdmin**](DefaultApi.md#deleteAppInstanceAdmin) | **DELETE** /app-instances/{appInstanceArn}/admins/{appInstanceAdminArn} | 
[**deleteAppInstanceStreamingConfigurations**](DefaultApi.md#deleteAppInstanceStreamingConfigurations) | **DELETE** /app-instances/{appInstanceArn}/streaming-configurations | 
[**deleteAppInstanceUser**](DefaultApi.md#deleteAppInstanceUser) | **DELETE** /app-instance-users/{appInstanceUserArn} | 
[**deleteAttendee**](DefaultApi.md#deleteAttendee) | **DELETE** /meetings/{meetingId}/attendees/{attendeeId} | 
[**deleteChannel**](DefaultApi.md#deleteChannel) | **DELETE** /channels/{channelArn} | 
[**deleteChannelBan**](DefaultApi.md#deleteChannelBan) | **DELETE** /channels/{channelArn}/bans/{memberArn} | 
[**deleteChannelMembership**](DefaultApi.md#deleteChannelMembership) | **DELETE** /channels/{channelArn}/memberships/{memberArn} | 
[**deleteChannelMessage**](DefaultApi.md#deleteChannelMessage) | **DELETE** /channels/{channelArn}/messages/{messageId} | 
[**deleteChannelModerator**](DefaultApi.md#deleteChannelModerator) | **DELETE** /channels/{channelArn}/moderators/{channelModeratorArn} | 
[**deleteEventsConfiguration**](DefaultApi.md#deleteEventsConfiguration) | **DELETE** /accounts/{accountId}/bots/{botId}/events-configuration | 
[**deleteMediaCapturePipeline**](DefaultApi.md#deleteMediaCapturePipeline) | **DELETE** /media-capture-pipelines/{mediaPipelineId} | 
[**deleteMeeting**](DefaultApi.md#deleteMeeting) | **DELETE** /meetings/{meetingId} | 
[**deletePhoneNumber**](DefaultApi.md#deletePhoneNumber) | **DELETE** /phone-numbers/{phoneNumberId} | 
[**deleteProxySession**](DefaultApi.md#deleteProxySession) | **DELETE** /voice-connectors/{voiceConnectorId}/proxy-sessions/{proxySessionId} | 
[**deleteRoom**](DefaultApi.md#deleteRoom) | **DELETE** /accounts/{accountId}/rooms/{roomId} | 
[**deleteRoomMembership**](DefaultApi.md#deleteRoomMembership) | **DELETE** /accounts/{accountId}/rooms/{roomId}/memberships/{memberId} | 
[**deleteSipMediaApplication**](DefaultApi.md#deleteSipMediaApplication) | **DELETE** /sip-media-applications/{sipMediaApplicationId} | 
[**deleteSipRule**](DefaultApi.md#deleteSipRule) | **DELETE** /sip-rules/{sipRuleId} | 
[**deleteVoiceConnector**](DefaultApi.md#deleteVoiceConnector) | **DELETE** /voice-connectors/{voiceConnectorId} | 
[**deleteVoiceConnectorEmergencyCallingConfiguration**](DefaultApi.md#deleteVoiceConnectorEmergencyCallingConfiguration) | **DELETE** /voice-connectors/{voiceConnectorId}/emergency-calling-configuration | 
[**deleteVoiceConnectorGroup**](DefaultApi.md#deleteVoiceConnectorGroup) | **DELETE** /voice-connector-groups/{voiceConnectorGroupId} | 
[**deleteVoiceConnectorOrigination**](DefaultApi.md#deleteVoiceConnectorOrigination) | **DELETE** /voice-connectors/{voiceConnectorId}/origination | 
[**deleteVoiceConnectorProxy**](DefaultApi.md#deleteVoiceConnectorProxy) | **DELETE** /voice-connectors/{voiceConnectorId}/programmable-numbers/proxy | 
[**deleteVoiceConnectorStreamingConfiguration**](DefaultApi.md#deleteVoiceConnectorStreamingConfiguration) | **DELETE** /voice-connectors/{voiceConnectorId}/streaming-configuration | 
[**deleteVoiceConnectorTermination**](DefaultApi.md#deleteVoiceConnectorTermination) | **DELETE** /voice-connectors/{voiceConnectorId}/termination | 
[**deleteVoiceConnectorTerminationCredentials**](DefaultApi.md#deleteVoiceConnectorTerminationCredentials) | **POST** /voice-connectors/{voiceConnectorId}/termination/credentials#operation&#x3D;delete | 
[**describeAppInstance**](DefaultApi.md#describeAppInstance) | **GET** /app-instances/{appInstanceArn} | 
[**describeAppInstanceAdmin**](DefaultApi.md#describeAppInstanceAdmin) | **GET** /app-instances/{appInstanceArn}/admins/{appInstanceAdminArn} | 
[**describeAppInstanceUser**](DefaultApi.md#describeAppInstanceUser) | **GET** /app-instance-users/{appInstanceUserArn} | 
[**describeChannel**](DefaultApi.md#describeChannel) | **GET** /channels/{channelArn} | 
[**describeChannelBan**](DefaultApi.md#describeChannelBan) | **GET** /channels/{channelArn}/bans/{memberArn} | 
[**describeChannelMembership**](DefaultApi.md#describeChannelMembership) | **GET** /channels/{channelArn}/memberships/{memberArn} | 
[**describeChannelMembershipForAppInstanceUser**](DefaultApi.md#describeChannelMembershipForAppInstanceUser) | **GET** /channels/{channelArn}#scope&#x3D;app-instance-user-membership&amp;app-instance-user-arn | 
[**describeChannelModeratedByAppInstanceUser**](DefaultApi.md#describeChannelModeratedByAppInstanceUser) | **GET** /channels/{channelArn}#scope&#x3D;app-instance-user-moderated-channel&amp;app-instance-user-arn | 
[**describeChannelModerator**](DefaultApi.md#describeChannelModerator) | **GET** /channels/{channelArn}/moderators/{channelModeratorArn} | 
[**disassociatePhoneNumberFromUser**](DefaultApi.md#disassociatePhoneNumberFromUser) | **POST** /accounts/{accountId}/users/{userId}#operation&#x3D;disassociate-phone-number | 
[**disassociatePhoneNumbersFromVoiceConnector**](DefaultApi.md#disassociatePhoneNumbersFromVoiceConnector) | **POST** /voice-connectors/{voiceConnectorId}#operation&#x3D;disassociate-phone-numbers | 
[**disassociatePhoneNumbersFromVoiceConnectorGroup**](DefaultApi.md#disassociatePhoneNumbersFromVoiceConnectorGroup) | **POST** /voice-connector-groups/{voiceConnectorGroupId}#operation&#x3D;disassociate-phone-numbers | 
[**disassociateSigninDelegateGroupsFromAccount**](DefaultApi.md#disassociateSigninDelegateGroupsFromAccount) | **POST** /accounts/{accountId}#operation&#x3D;disassociate-signin-delegate-groups | 
[**getAccount**](DefaultApi.md#getAccount) | **GET** /accounts/{accountId} | 
[**getAccountSettings**](DefaultApi.md#getAccountSettings) | **GET** /accounts/{accountId}/settings | 
[**getAppInstanceRetentionSettings**](DefaultApi.md#getAppInstanceRetentionSettings) | **GET** /app-instances/{appInstanceArn}/retention-settings | 
[**getAppInstanceStreamingConfigurations**](DefaultApi.md#getAppInstanceStreamingConfigurations) | **GET** /app-instances/{appInstanceArn}/streaming-configurations | 
[**getAttendee**](DefaultApi.md#getAttendee) | **GET** /meetings/{meetingId}/attendees/{attendeeId} | 
[**getBot**](DefaultApi.md#getBot) | **GET** /accounts/{accountId}/bots/{botId} | 
[**getChannelMessage**](DefaultApi.md#getChannelMessage) | **GET** /channels/{channelArn}/messages/{messageId} | 
[**getEventsConfiguration**](DefaultApi.md#getEventsConfiguration) | **GET** /accounts/{accountId}/bots/{botId}/events-configuration | 
[**getGlobalSettings**](DefaultApi.md#getGlobalSettings) | **GET** /settings | 
[**getMediaCapturePipeline**](DefaultApi.md#getMediaCapturePipeline) | **GET** /media-capture-pipelines/{mediaPipelineId} | 
[**getMeeting**](DefaultApi.md#getMeeting) | **GET** /meetings/{meetingId} | 
[**getMessagingSessionEndpoint**](DefaultApi.md#getMessagingSessionEndpoint) | **GET** /endpoints/messaging-session | 
[**getPhoneNumber**](DefaultApi.md#getPhoneNumber) | **GET** /phone-numbers/{phoneNumberId} | 
[**getPhoneNumberOrder**](DefaultApi.md#getPhoneNumberOrder) | **GET** /phone-number-orders/{phoneNumberOrderId} | 
[**getPhoneNumberSettings**](DefaultApi.md#getPhoneNumberSettings) | **GET** /settings/phone-number | 
[**getProxySession**](DefaultApi.md#getProxySession) | **GET** /voice-connectors/{voiceConnectorId}/proxy-sessions/{proxySessionId} | 
[**getRetentionSettings**](DefaultApi.md#getRetentionSettings) | **GET** /accounts/{accountId}/retention-settings | 
[**getRoom**](DefaultApi.md#getRoom) | **GET** /accounts/{accountId}/rooms/{roomId} | 
[**getSipMediaApplication**](DefaultApi.md#getSipMediaApplication) | **GET** /sip-media-applications/{sipMediaApplicationId} | 
[**getSipMediaApplicationLoggingConfiguration**](DefaultApi.md#getSipMediaApplicationLoggingConfiguration) | **GET** /sip-media-applications/{sipMediaApplicationId}/logging-configuration | 
[**getSipRule**](DefaultApi.md#getSipRule) | **GET** /sip-rules/{sipRuleId} | 
[**getUser**](DefaultApi.md#getUser) | **GET** /accounts/{accountId}/users/{userId} | 
[**getUserSettings**](DefaultApi.md#getUserSettings) | **GET** /accounts/{accountId}/users/{userId}/settings | 
[**getVoiceConnector**](DefaultApi.md#getVoiceConnector) | **GET** /voice-connectors/{voiceConnectorId} | 
[**getVoiceConnectorEmergencyCallingConfiguration**](DefaultApi.md#getVoiceConnectorEmergencyCallingConfiguration) | **GET** /voice-connectors/{voiceConnectorId}/emergency-calling-configuration | 
[**getVoiceConnectorGroup**](DefaultApi.md#getVoiceConnectorGroup) | **GET** /voice-connector-groups/{voiceConnectorGroupId} | 
[**getVoiceConnectorLoggingConfiguration**](DefaultApi.md#getVoiceConnectorLoggingConfiguration) | **GET** /voice-connectors/{voiceConnectorId}/logging-configuration | 
[**getVoiceConnectorOrigination**](DefaultApi.md#getVoiceConnectorOrigination) | **GET** /voice-connectors/{voiceConnectorId}/origination | 
[**getVoiceConnectorProxy**](DefaultApi.md#getVoiceConnectorProxy) | **GET** /voice-connectors/{voiceConnectorId}/programmable-numbers/proxy | 
[**getVoiceConnectorStreamingConfiguration**](DefaultApi.md#getVoiceConnectorStreamingConfiguration) | **GET** /voice-connectors/{voiceConnectorId}/streaming-configuration | 
[**getVoiceConnectorTermination**](DefaultApi.md#getVoiceConnectorTermination) | **GET** /voice-connectors/{voiceConnectorId}/termination | 
[**getVoiceConnectorTerminationHealth**](DefaultApi.md#getVoiceConnectorTerminationHealth) | **GET** /voice-connectors/{voiceConnectorId}/termination/health | 
[**inviteUsers**](DefaultApi.md#inviteUsers) | **POST** /accounts/{accountId}/users#operation&#x3D;add | 
[**listAccounts**](DefaultApi.md#listAccounts) | **GET** /accounts | 
[**listAppInstanceAdmins**](DefaultApi.md#listAppInstanceAdmins) | **GET** /app-instances/{appInstanceArn}/admins | 
[**listAppInstanceUsers**](DefaultApi.md#listAppInstanceUsers) | **GET** /app-instance-users#app-instance-arn | 
[**listAppInstances**](DefaultApi.md#listAppInstances) | **GET** /app-instances | 
[**listAttendeeTags**](DefaultApi.md#listAttendeeTags) | **GET** /meetings/{meetingId}/attendees/{attendeeId}/tags | 
[**listAttendees**](DefaultApi.md#listAttendees) | **GET** /meetings/{meetingId}/attendees | 
[**listBots**](DefaultApi.md#listBots) | **GET** /accounts/{accountId}/bots | 
[**listChannelBans**](DefaultApi.md#listChannelBans) | **GET** /channels/{channelArn}/bans | 
[**listChannelMemberships**](DefaultApi.md#listChannelMemberships) | **GET** /channels/{channelArn}/memberships | 
[**listChannelMembershipsForAppInstanceUser**](DefaultApi.md#listChannelMembershipsForAppInstanceUser) | **GET** /channels#scope&#x3D;app-instance-user-memberships | 
[**listChannelMessages**](DefaultApi.md#listChannelMessages) | **GET** /channels/{channelArn}/messages | 
[**listChannelModerators**](DefaultApi.md#listChannelModerators) | **GET** /channels/{channelArn}/moderators | 
[**listChannels**](DefaultApi.md#listChannels) | **GET** /channels#app-instance-arn | 
[**listChannelsModeratedByAppInstanceUser**](DefaultApi.md#listChannelsModeratedByAppInstanceUser) | **GET** /channels#scope&#x3D;app-instance-user-moderated-channels | 
[**listMediaCapturePipelines**](DefaultApi.md#listMediaCapturePipelines) | **GET** /media-capture-pipelines | 
[**listMeetingTags**](DefaultApi.md#listMeetingTags) | **GET** /meetings/{meetingId}/tags | 
[**listMeetings**](DefaultApi.md#listMeetings) | **GET** /meetings | 
[**listPhoneNumberOrders**](DefaultApi.md#listPhoneNumberOrders) | **GET** /phone-number-orders | 
[**listPhoneNumbers**](DefaultApi.md#listPhoneNumbers) | **GET** /phone-numbers | 
[**listProxySessions**](DefaultApi.md#listProxySessions) | **GET** /voice-connectors/{voiceConnectorId}/proxy-sessions | 
[**listRoomMemberships**](DefaultApi.md#listRoomMemberships) | **GET** /accounts/{accountId}/rooms/{roomId}/memberships | 
[**listRooms**](DefaultApi.md#listRooms) | **GET** /accounts/{accountId}/rooms | 
[**listSipMediaApplications**](DefaultApi.md#listSipMediaApplications) | **GET** /sip-media-applications | 
[**listSipRules**](DefaultApi.md#listSipRules) | **GET** /sip-rules | 
[**listSupportedPhoneNumberCountries**](DefaultApi.md#listSupportedPhoneNumberCountries) | **GET** /phone-number-countries#product-type | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags#arn | 
[**listUsers**](DefaultApi.md#listUsers) | **GET** /accounts/{accountId}/users | 
[**listVoiceConnectorGroups**](DefaultApi.md#listVoiceConnectorGroups) | **GET** /voice-connector-groups | 
[**listVoiceConnectorTerminationCredentials**](DefaultApi.md#listVoiceConnectorTerminationCredentials) | **GET** /voice-connectors/{voiceConnectorId}/termination/credentials | 
[**listVoiceConnectors**](DefaultApi.md#listVoiceConnectors) | **GET** /voice-connectors | 
[**logoutUser**](DefaultApi.md#logoutUser) | **POST** /accounts/{accountId}/users/{userId}#operation&#x3D;logout | 
[**putAppInstanceRetentionSettings**](DefaultApi.md#putAppInstanceRetentionSettings) | **PUT** /app-instances/{appInstanceArn}/retention-settings | 
[**putAppInstanceStreamingConfigurations**](DefaultApi.md#putAppInstanceStreamingConfigurations) | **PUT** /app-instances/{appInstanceArn}/streaming-configurations | 
[**putEventsConfiguration**](DefaultApi.md#putEventsConfiguration) | **PUT** /accounts/{accountId}/bots/{botId}/events-configuration | 
[**putRetentionSettings**](DefaultApi.md#putRetentionSettings) | **PUT** /accounts/{accountId}/retention-settings | 
[**putSipMediaApplicationLoggingConfiguration**](DefaultApi.md#putSipMediaApplicationLoggingConfiguration) | **PUT** /sip-media-applications/{sipMediaApplicationId}/logging-configuration | 
[**putVoiceConnectorEmergencyCallingConfiguration**](DefaultApi.md#putVoiceConnectorEmergencyCallingConfiguration) | **PUT** /voice-connectors/{voiceConnectorId}/emergency-calling-configuration | 
[**putVoiceConnectorLoggingConfiguration**](DefaultApi.md#putVoiceConnectorLoggingConfiguration) | **PUT** /voice-connectors/{voiceConnectorId}/logging-configuration | 
[**putVoiceConnectorOrigination**](DefaultApi.md#putVoiceConnectorOrigination) | **PUT** /voice-connectors/{voiceConnectorId}/origination | 
[**putVoiceConnectorProxy**](DefaultApi.md#putVoiceConnectorProxy) | **PUT** /voice-connectors/{voiceConnectorId}/programmable-numbers/proxy | 
[**putVoiceConnectorStreamingConfiguration**](DefaultApi.md#putVoiceConnectorStreamingConfiguration) | **PUT** /voice-connectors/{voiceConnectorId}/streaming-configuration | 
[**putVoiceConnectorTermination**](DefaultApi.md#putVoiceConnectorTermination) | **PUT** /voice-connectors/{voiceConnectorId}/termination | 
[**putVoiceConnectorTerminationCredentials**](DefaultApi.md#putVoiceConnectorTerminationCredentials) | **POST** /voice-connectors/{voiceConnectorId}/termination/credentials#operation&#x3D;put | 
[**redactChannelMessage**](DefaultApi.md#redactChannelMessage) | **POST** /channels/{channelArn}/messages/{messageId}#operation&#x3D;redact | 
[**redactConversationMessage**](DefaultApi.md#redactConversationMessage) | **POST** /accounts/{accountId}/conversations/{conversationId}/messages/{messageId}#operation&#x3D;redact | 
[**redactRoomMessage**](DefaultApi.md#redactRoomMessage) | **POST** /accounts/{accountId}/rooms/{roomId}/messages/{messageId}#operation&#x3D;redact | 
[**regenerateSecurityToken**](DefaultApi.md#regenerateSecurityToken) | **POST** /accounts/{accountId}/bots/{botId}#operation&#x3D;regenerate-security-token | 
[**resetPersonalPIN**](DefaultApi.md#resetPersonalPIN) | **POST** /accounts/{accountId}/users/{userId}#operation&#x3D;reset-personal-pin | 
[**restorePhoneNumber**](DefaultApi.md#restorePhoneNumber) | **POST** /phone-numbers/{phoneNumberId}#operation&#x3D;restore | 
[**searchAvailablePhoneNumbers**](DefaultApi.md#searchAvailablePhoneNumbers) | **GET** /search#type&#x3D;phone-numbers | 
[**sendChannelMessage**](DefaultApi.md#sendChannelMessage) | **POST** /channels/{channelArn}/messages | 
[**startMeetingTranscription**](DefaultApi.md#startMeetingTranscription) | **POST** /meetings/{meetingId}/transcription#operation&#x3D;start | 
[**stopMeetingTranscription**](DefaultApi.md#stopMeetingTranscription) | **POST** /meetings/{meetingId}/transcription#operation&#x3D;stop | 
[**tagAttendee**](DefaultApi.md#tagAttendee) | **POST** /meetings/{meetingId}/attendees/{attendeeId}/tags#operation&#x3D;add | 
[**tagMeeting**](DefaultApi.md#tagMeeting) | **POST** /meetings/{meetingId}/tags#operation&#x3D;add | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags#operation&#x3D;tag-resource | 
[**untagAttendee**](DefaultApi.md#untagAttendee) | **POST** /meetings/{meetingId}/attendees/{attendeeId}/tags#operation&#x3D;delete | 
[**untagMeeting**](DefaultApi.md#untagMeeting) | **POST** /meetings/{meetingId}/tags#operation&#x3D;delete | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /tags#operation&#x3D;untag-resource | 
[**updateAccount**](DefaultApi.md#updateAccount) | **POST** /accounts/{accountId} | 
[**updateAccountSettings**](DefaultApi.md#updateAccountSettings) | **PUT** /accounts/{accountId}/settings | 
[**updateAppInstance**](DefaultApi.md#updateAppInstance) | **PUT** /app-instances/{appInstanceArn} | 
[**updateAppInstanceUser**](DefaultApi.md#updateAppInstanceUser) | **PUT** /app-instance-users/{appInstanceUserArn} | 
[**updateBot**](DefaultApi.md#updateBot) | **POST** /accounts/{accountId}/bots/{botId} | 
[**updateChannel**](DefaultApi.md#updateChannel) | **PUT** /channels/{channelArn} | 
[**updateChannelMessage**](DefaultApi.md#updateChannelMessage) | **PUT** /channels/{channelArn}/messages/{messageId} | 
[**updateChannelReadMarker**](DefaultApi.md#updateChannelReadMarker) | **PUT** /channels/{channelArn}/readMarker | 
[**updateGlobalSettings**](DefaultApi.md#updateGlobalSettings) | **PUT** /settings | 
[**updatePhoneNumber**](DefaultApi.md#updatePhoneNumber) | **POST** /phone-numbers/{phoneNumberId} | 
[**updatePhoneNumberSettings**](DefaultApi.md#updatePhoneNumberSettings) | **PUT** /settings/phone-number | 
[**updateProxySession**](DefaultApi.md#updateProxySession) | **POST** /voice-connectors/{voiceConnectorId}/proxy-sessions/{proxySessionId} | 
[**updateRoom**](DefaultApi.md#updateRoom) | **POST** /accounts/{accountId}/rooms/{roomId} | 
[**updateRoomMembership**](DefaultApi.md#updateRoomMembership) | **POST** /accounts/{accountId}/rooms/{roomId}/memberships/{memberId} | 
[**updateSipMediaApplication**](DefaultApi.md#updateSipMediaApplication) | **PUT** /sip-media-applications/{sipMediaApplicationId} | 
[**updateSipMediaApplicationCall**](DefaultApi.md#updateSipMediaApplicationCall) | **POST** /sip-media-applications/{sipMediaApplicationId}/calls/{transactionId} | 
[**updateSipRule**](DefaultApi.md#updateSipRule) | **PUT** /sip-rules/{sipRuleId} | 
[**updateUser**](DefaultApi.md#updateUser) | **POST** /accounts/{accountId}/users/{userId} | 
[**updateUserSettings**](DefaultApi.md#updateUserSettings) | **PUT** /accounts/{accountId}/users/{userId}/settings | 
[**updateVoiceConnector**](DefaultApi.md#updateVoiceConnector) | **PUT** /voice-connectors/{voiceConnectorId} | 
[**updateVoiceConnectorGroup**](DefaultApi.md#updateVoiceConnectorGroup) | **PUT** /voice-connector-groups/{voiceConnectorGroupId} | 
[**validateE911Address**](DefaultApi.md#validateE911Address) | **POST** /emergency-calling/address | 



## associatePhoneNumberWithUser

> Object associatePhoneNumberWithUser(accountId, userId, operation, associatePhoneNumberWithUserRequest, opts)



Associates a phone number with the specified Amazon Chime user.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let userId = "userId_example"; // String | The user ID.
let operation = "operation_example"; // String | 
let associatePhoneNumberWithUserRequest = new AmazonChime.AssociatePhoneNumberWithUserRequest(); // AssociatePhoneNumberWithUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associatePhoneNumberWithUser(accountId, userId, operation, associatePhoneNumberWithUserRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **userId** | **String**| The user ID. | 
 **operation** | **String**|  | 
 **associatePhoneNumberWithUserRequest** | [**AssociatePhoneNumberWithUserRequest**](AssociatePhoneNumberWithUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associatePhoneNumbersWithVoiceConnector

> AssociatePhoneNumbersWithVoiceConnectorResponse associatePhoneNumbersWithVoiceConnector(voiceConnectorId, operation, associatePhoneNumbersWithVoiceConnectorRequest, opts)



&lt;p&gt;Associates phone numbers with the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnector.html\&quot;&gt;AssociatePhoneNumbersWithVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let operation = "operation_example"; // String | 
let associatePhoneNumbersWithVoiceConnectorRequest = new AmazonChime.AssociatePhoneNumbersWithVoiceConnectorRequest(); // AssociatePhoneNumbersWithVoiceConnectorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associatePhoneNumbersWithVoiceConnector(voiceConnectorId, operation, associatePhoneNumbersWithVoiceConnectorRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **operation** | **String**|  | 
 **associatePhoneNumbersWithVoiceConnectorRequest** | [**AssociatePhoneNumbersWithVoiceConnectorRequest**](AssociatePhoneNumbersWithVoiceConnectorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociatePhoneNumbersWithVoiceConnectorResponse**](AssociatePhoneNumbersWithVoiceConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associatePhoneNumbersWithVoiceConnectorGroup

> AssociatePhoneNumbersWithVoiceConnectorGroupResponse associatePhoneNumbersWithVoiceConnectorGroup(voiceConnectorGroupId, operation, associatePhoneNumbersWithVoiceConnectorGroupRequest, opts)



&lt;p&gt;Associates phone numbers with the specified Amazon Chime Voice Connector group.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnectorGroup.html\&quot;&gt;AssociatePhoneNumbersWithVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorGroupId = "voiceConnectorGroupId_example"; // String | The Amazon Chime Voice Connector group ID.
let operation = "operation_example"; // String | 
let associatePhoneNumbersWithVoiceConnectorGroupRequest = new AmazonChime.AssociatePhoneNumbersWithVoiceConnectorGroupRequest(); // AssociatePhoneNumbersWithVoiceConnectorGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associatePhoneNumbersWithVoiceConnectorGroup(voiceConnectorGroupId, operation, associatePhoneNumbersWithVoiceConnectorGroupRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorGroupId** | **String**| The Amazon Chime Voice Connector group ID. | 
 **operation** | **String**|  | 
 **associatePhoneNumbersWithVoiceConnectorGroupRequest** | [**AssociatePhoneNumbersWithVoiceConnectorGroupRequest**](AssociatePhoneNumbersWithVoiceConnectorGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociatePhoneNumbersWithVoiceConnectorGroupResponse**](AssociatePhoneNumbersWithVoiceConnectorGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## associateSigninDelegateGroupsWithAccount

> Object associateSigninDelegateGroupsWithAccount(accountId, operation, associateSigninDelegateGroupsWithAccountRequest, opts)



Associates the specified sign-in delegate groups with the specified Amazon Chime account.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let operation = "operation_example"; // String | 
let associateSigninDelegateGroupsWithAccountRequest = new AmazonChime.AssociateSigninDelegateGroupsWithAccountRequest(); // AssociateSigninDelegateGroupsWithAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateSigninDelegateGroupsWithAccount(accountId, operation, associateSigninDelegateGroupsWithAccountRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **operation** | **String**|  | 
 **associateSigninDelegateGroupsWithAccountRequest** | [**AssociateSigninDelegateGroupsWithAccountRequest**](AssociateSigninDelegateGroupsWithAccountRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchCreateAttendee

> BatchCreateAttendeeResponse batchCreateAttendee(meetingId, operation, batchCreateAttendeeRequest, opts)



&lt;p&gt;Creates up to 100 new attendees for an active Amazon Chime SDK meeting.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_BatchCreateAttendee.html\&quot;&gt;BatchCreateAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let operation = "operation_example"; // String | 
let batchCreateAttendeeRequest = new AmazonChime.BatchCreateAttendeeRequest(); // BatchCreateAttendeeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchCreateAttendee(meetingId, operation, batchCreateAttendeeRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **operation** | **String**|  | 
 **batchCreateAttendeeRequest** | [**BatchCreateAttendeeRequest**](BatchCreateAttendeeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchCreateAttendeeResponse**](BatchCreateAttendeeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchCreateChannelMembership

> BatchCreateChannelMembershipResponse batchCreateChannelMembership(channelArn, operation, batchCreateChannelMembershipRequest, opts)



&lt;p&gt;Adds a specified number of users to a channel.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchCreateChannelMembership.html\&quot;&gt;BatchCreateChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel to which you're adding users.
let operation = "operation_example"; // String | 
let batchCreateChannelMembershipRequest = new AmazonChime.BatchCreateChannelMembershipRequest(); // BatchCreateChannelMembershipRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.batchCreateChannelMembership(channelArn, operation, batchCreateChannelMembershipRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel to which you&#39;re adding users. | 
 **operation** | **String**|  | 
 **batchCreateChannelMembershipRequest** | [**BatchCreateChannelMembershipRequest**](BatchCreateChannelMembershipRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**BatchCreateChannelMembershipResponse**](BatchCreateChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchCreateRoomMembership

> BatchCreateRoomMembershipResponse batchCreateRoomMembership(accountId, roomId, operation, batchCreateRoomMembershipRequest, opts)



Adds up to 50 members to a chat room in an Amazon Chime Enterprise account. Members can be users or bots. The member role designates whether the member is a chat room administrator or a general chat room member.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let roomId = "roomId_example"; // String | The room ID.
let operation = "operation_example"; // String | 
let batchCreateRoomMembershipRequest = new AmazonChime.BatchCreateRoomMembershipRequest(); // BatchCreateRoomMembershipRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchCreateRoomMembership(accountId, roomId, operation, batchCreateRoomMembershipRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **roomId** | **String**| The room ID. | 
 **operation** | **String**|  | 
 **batchCreateRoomMembershipRequest** | [**BatchCreateRoomMembershipRequest**](BatchCreateRoomMembershipRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchCreateRoomMembershipResponse**](BatchCreateRoomMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDeletePhoneNumber

> BatchDeletePhoneNumberResponse batchDeletePhoneNumber(operation, batchDeletePhoneNumberRequest, opts)



&lt;p&gt; Moves phone numbers into the &lt;b&gt;Deletion queue&lt;/b&gt;. Phone numbers must be disassociated from any users or Amazon Chime Voice Connectors before they can be deleted. &lt;/p&gt; &lt;p&gt; Phone numbers remain in the &lt;b&gt;Deletion queue&lt;/b&gt; for 7 days before they are deleted permanently. &lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let operation = "operation_example"; // String | 
let batchDeletePhoneNumberRequest = new AmazonChime.BatchDeletePhoneNumberRequest(); // BatchDeletePhoneNumberRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDeletePhoneNumber(operation, batchDeletePhoneNumberRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **String**|  | 
 **batchDeletePhoneNumberRequest** | [**BatchDeletePhoneNumberRequest**](BatchDeletePhoneNumberRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDeletePhoneNumberResponse**](BatchDeletePhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchSuspendUser

> BatchSuspendUserResponse batchSuspendUser(accountId, operation, batchSuspendUserRequest, opts)



&lt;p&gt;Suspends up to 50 users from a &lt;code&gt;Team&lt;/code&gt; or &lt;code&gt;EnterpriseLWA&lt;/code&gt; Amazon Chime account. For more information about different account types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\&quot;&gt;Managing Your Amazon Chime Accounts&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Users suspended from a &lt;code&gt;Team&lt;/code&gt; account are disassociated from the account,but they can continue to use Amazon Chime as free users. To remove the suspension from suspended &lt;code&gt;Team&lt;/code&gt; account users, invite them to the &lt;code&gt;Team&lt;/code&gt; account again. You can use the &lt;a&gt;InviteUsers&lt;/a&gt; action to do so.&lt;/p&gt; &lt;p&gt;Users suspended from an &lt;code&gt;EnterpriseLWA&lt;/code&gt; account are immediately signed out of Amazon Chime and can no longer sign in. To remove the suspension from suspended &lt;code&gt;EnterpriseLWA&lt;/code&gt; account users, use the &lt;a&gt;BatchUnsuspendUser&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt; To sign out users without suspending them, use the &lt;a&gt;LogoutUser&lt;/a&gt; action.&lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let operation = "operation_example"; // String | 
let batchSuspendUserRequest = new AmazonChime.BatchSuspendUserRequest(); // BatchSuspendUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchSuspendUser(accountId, operation, batchSuspendUserRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **operation** | **String**|  | 
 **batchSuspendUserRequest** | [**BatchSuspendUserRequest**](BatchSuspendUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchSuspendUserResponse**](BatchSuspendUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchUnsuspendUser

> BatchUnsuspendUserResponse batchUnsuspendUser(accountId, operation, batchUnsuspendUserRequest, opts)



&lt;p&gt;Removes the suspension from up to 50 previously suspended users for the specified Amazon Chime &lt;code&gt;EnterpriseLWA&lt;/code&gt; account. Only users on &lt;code&gt;EnterpriseLWA&lt;/code&gt; accounts can be unsuspended using this action. For more information about different account types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\&quot;&gt; Managing Your Amazon Chime Accounts &lt;/a&gt; in the account types, in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;Previously suspended users who are unsuspended using this action are returned to &lt;code&gt;Registered&lt;/code&gt; status. Users who are not previously suspended are ignored.&lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let operation = "operation_example"; // String | 
let batchUnsuspendUserRequest = new AmazonChime.BatchUnsuspendUserRequest(); // BatchUnsuspendUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchUnsuspendUser(accountId, operation, batchUnsuspendUserRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **operation** | **String**|  | 
 **batchUnsuspendUserRequest** | [**BatchUnsuspendUserRequest**](BatchUnsuspendUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchUnsuspendUserResponse**](BatchUnsuspendUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchUpdatePhoneNumber

> BatchUpdatePhoneNumberResponse batchUpdatePhoneNumber(operation, batchUpdatePhoneNumberRequest, opts)



&lt;p&gt;Updates phone number product types or calling names. You can update one attribute at a time for each &lt;code&gt;UpdatePhoneNumberRequestItem&lt;/code&gt;. For example, you can update the product type or the calling name.&lt;/p&gt; &lt;p&gt;For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.&lt;/p&gt; &lt;p&gt;Updates to outbound calling names can take up to 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.&lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let operation = "operation_example"; // String | 
let batchUpdatePhoneNumberRequest = new AmazonChime.BatchUpdatePhoneNumberRequest(); // BatchUpdatePhoneNumberRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchUpdatePhoneNumber(operation, batchUpdatePhoneNumberRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **String**|  | 
 **batchUpdatePhoneNumberRequest** | [**BatchUpdatePhoneNumberRequest**](BatchUpdatePhoneNumberRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchUpdatePhoneNumberResponse**](BatchUpdatePhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchUpdateUser

> BatchUpdateUserResponse batchUpdateUser(accountId, batchUpdateUserRequest, opts)



Updates user details within the &lt;a&gt;UpdateUserRequestItem&lt;/a&gt; object for up to 20 users for the specified Amazon Chime account. Currently, only &lt;code&gt;LicenseType&lt;/code&gt; updates are supported for this action.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let batchUpdateUserRequest = new AmazonChime.BatchUpdateUserRequest(); // BatchUpdateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchUpdateUser(accountId, batchUpdateUserRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **batchUpdateUserRequest** | [**BatchUpdateUserRequest**](BatchUpdateUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchUpdateUserResponse**](BatchUpdateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAccount

> CreateAccountResponse createAccount(createAccountRequest, opts)



Creates an Amazon Chime account under the administrator&#39;s AWS account. Only &lt;code&gt;Team&lt;/code&gt; account types are currently supported for this action. For more information about different account types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\&quot;&gt;Managing Your Amazon Chime Accounts&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let createAccountRequest = new AmazonChime.CreateAccountRequest(); // CreateAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAccount(createAccountRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createAccountRequest** | [**CreateAccountRequest**](CreateAccountRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAccountResponse**](CreateAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAppInstance

> CreateAppInstanceResponse createAppInstance(createAppInstanceRequest, opts)



&lt;p&gt;Creates an Amazon Chime SDK messaging &lt;code&gt;AppInstance&lt;/code&gt; under an AWS account. Only SDK messaging customers use this API. &lt;code&gt;CreateAppInstance&lt;/code&gt; supports idempotency behavior as described in the AWS API Standard.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_CreateAppInstance.html\&quot;&gt;CreateAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let createAppInstanceRequest = new AmazonChime.CreateAppInstanceRequest(); // CreateAppInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAppInstance(createAppInstanceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createAppInstanceRequest** | [**CreateAppInstanceRequest**](CreateAppInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAppInstanceResponse**](CreateAppInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAppInstanceAdmin

> CreateAppInstanceAdminResponse createAppInstanceAdmin(appInstanceArn, createAppInstanceAdminRequest, opts)



&lt;p&gt;Promotes an &lt;code&gt;AppInstanceUser&lt;/code&gt; to an &lt;code&gt;AppInstanceAdmin&lt;/code&gt;. The promoted user can perform the following actions. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_CreateAppInstanceAdmin.html\&quot;&gt;CreateAppInstanceAdmin&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ChannelModerator&lt;/code&gt; actions across all channels in the &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteChannelMessage&lt;/code&gt; actions.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Only an &lt;code&gt;AppInstanceUser&lt;/code&gt; can be promoted to an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; role.&lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let createAppInstanceAdminRequest = new AmazonChime.CreateAppInstanceAdminRequest(); // CreateAppInstanceAdminRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAppInstanceAdmin(appInstanceArn, createAppInstanceAdminRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **createAppInstanceAdminRequest** | [**CreateAppInstanceAdminRequest**](CreateAppInstanceAdminRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAppInstanceAdminResponse**](CreateAppInstanceAdminResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAppInstanceUser

> CreateAppInstanceUserResponse createAppInstanceUser(createAppInstanceUserRequest, opts)



&lt;p&gt;Creates a user under an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;. The request consists of a unique &lt;code&gt;appInstanceUserId&lt;/code&gt; and &lt;code&gt;Name&lt;/code&gt; for that user.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_CreateAppInstanceUser.html\&quot;&gt;CreateAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let createAppInstanceUserRequest = new AmazonChime.CreateAppInstanceUserRequest(); // CreateAppInstanceUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAppInstanceUser(createAppInstanceUserRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createAppInstanceUserRequest** | [**CreateAppInstanceUserRequest**](CreateAppInstanceUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAppInstanceUserResponse**](CreateAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAttendee

> CreateAttendeeResponse createAttendee(meetingId, createAttendeeRequest, opts)



&lt;p&gt; Creates a new attendee for an active Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendee.html\&quot;&gt;CreateAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let createAttendeeRequest = new AmazonChime.CreateAttendeeRequest(); // CreateAttendeeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAttendee(meetingId, createAttendeeRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **createAttendeeRequest** | [**CreateAttendeeRequest**](CreateAttendeeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAttendeeResponse**](CreateAttendeeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createBot

> CreateBotResponse createBot(accountId, createBotRequest, opts)



Creates a bot for an Amazon Chime Enterprise account.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let createBotRequest = new AmazonChime.CreateBotRequest(); // CreateBotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createBot(accountId, createBotRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **createBotRequest** | [**CreateBotRequest**](CreateBotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateBotResponse**](CreateBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannel

> CreateChannelResponse createChannel(createChannelRequest, opts)



&lt;p&gt;Creates a channel to which you can add users and send messages.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html\&quot;&gt;CreateChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let createChannelRequest = new AmazonChime.CreateChannelRequest(); // CreateChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.createChannel(createChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createChannelRequest** | [**CreateChannelRequest**](CreateChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**CreateChannelResponse**](CreateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannelBan

> CreateChannelBanResponse createChannelBan(channelArn, createChannelBanRequest, opts)



&lt;p&gt;Permanently bans a member from a channel. Moderators can&#39;t add banned members to a channel. To undo a ban, you first have to &lt;code&gt;DeleteChannelBan&lt;/code&gt;, and then &lt;code&gt;CreateChannelMembership&lt;/code&gt;. Bans are cleaned up when you delete users or channels.&lt;/p&gt; &lt;p&gt;If you ban a user who is already part of a channel, that user is automatically kicked from the channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelBan.html\&quot;&gt;CreateChannelBan&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the ban request.
let createChannelBanRequest = new AmazonChime.CreateChannelBanRequest(); // CreateChannelBanRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.createChannelBan(channelArn, createChannelBanRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the ban request. | 
 **createChannelBanRequest** | [**CreateChannelBanRequest**](CreateChannelBanRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**CreateChannelBanResponse**](CreateChannelBanResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannelMembership

> CreateChannelMembershipResponse createChannelMembership(channelArn, createChannelMembershipRequest, opts)



&lt;p&gt;Adds a user to a channel. The &lt;code&gt;InvitedBy&lt;/code&gt; response field is derived from the request header. A channel member can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Send messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Receive messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Edit their own messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Leave the channel&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Privacy settings impact this action as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Public Channels: You do not need to be a member to list messages, but you must be a member to send messages.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Private Channels: You must be a member to list or send messages.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelMembership.html\&quot;&gt;CreateChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel to which you're adding users.
let createChannelMembershipRequest = new AmazonChime.CreateChannelMembershipRequest(); // CreateChannelMembershipRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.createChannelMembership(channelArn, createChannelMembershipRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel to which you&#39;re adding users. | 
 **createChannelMembershipRequest** | [**CreateChannelMembershipRequest**](CreateChannelMembershipRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**CreateChannelMembershipResponse**](CreateChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createChannelModerator

> CreateChannelModeratorResponse createChannelModerator(channelArn, createChannelModeratorRequest, opts)



&lt;p&gt;Creates a new &lt;code&gt;ChannelModerator&lt;/code&gt;. A channel moderator can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Add and remove other members of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove other moderators of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove user bans for the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Redact messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelModerator.html\&quot;&gt;CreateChannelModerator&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let createChannelModeratorRequest = new AmazonChime.CreateChannelModeratorRequest(); // CreateChannelModeratorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.createChannelModerator(channelArn, createChannelModeratorRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **createChannelModeratorRequest** | [**CreateChannelModeratorRequest**](CreateChannelModeratorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**CreateChannelModeratorResponse**](CreateChannelModeratorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMediaCapturePipeline

> CreateMediaCapturePipelineResponse createMediaCapturePipeline(createMediaCapturePipelineRequest, opts)



&lt;p&gt;Creates a media capture pipeline.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline\&quot;&gt;CreateMediaCapturePipeline&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let createMediaCapturePipelineRequest = new AmazonChime.CreateMediaCapturePipelineRequest(); // CreateMediaCapturePipelineRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMediaCapturePipeline(createMediaCapturePipelineRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createMediaCapturePipelineRequest** | [**CreateMediaCapturePipelineRequest**](CreateMediaCapturePipelineRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMediaCapturePipelineResponse**](CreateMediaCapturePipelineResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMeeting

> CreateMeetingResponse createMeeting(createMeetingRequest, opts)



&lt;p&gt;Creates a new Amazon Chime SDK meeting in the specified media Region with no initial attendees. For more information about specifying media Regions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/chime-sdk-meetings-regions.html\&quot;&gt;Amazon Chime SDK Media Regions&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html\&quot;&gt;CreateMeeting&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let createMeetingRequest = new AmazonChime.CreateMeetingRequest(); // CreateMeetingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMeeting(createMeetingRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createMeetingRequest** | [**CreateMeetingRequest**](CreateMeetingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMeetingResponse**](CreateMeetingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMeetingDialOut

> CreateMeetingDialOutResponse createMeetingDialOut(meetingId, createMeetingDialOutRequest, opts)



&lt;p&gt;Uses the join token and call metadata in a meeting request (From number, To number, and so forth) to initiate an outbound call to a public switched telephone network (PSTN) and join them into a Chime meeting. Also ensures that the From number belongs to the customer.&lt;/p&gt; &lt;p&gt;To play welcome audio or implement an interactive voice response (IVR), use the &lt;code&gt;CreateSipMediaApplicationCall&lt;/code&gt; action with the corresponding SIP media application ID.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is not available in a dedicated namespace.&lt;/b&gt; &lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let createMeetingDialOutRequest = new AmazonChime.CreateMeetingDialOutRequest(); // CreateMeetingDialOutRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMeetingDialOut(meetingId, createMeetingDialOutRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **createMeetingDialOutRequest** | [**CreateMeetingDialOutRequest**](CreateMeetingDialOutRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMeetingDialOutResponse**](CreateMeetingDialOutResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMeetingWithAttendees

> CreateMeetingWithAttendeesResponse createMeetingWithAttendees(operation, createMeetingWithAttendeesRequest, opts)



&lt;p&gt; Creates a new Amazon Chime SDK meeting in the specified media Region, with attendees. For more information about specifying media Regions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/chime-sdk-meetings-regions.html\&quot;&gt;Amazon Chime SDK Media Regions&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeetingWithAttendees.html\&quot;&gt;CreateMeetingWithAttendees&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let operation = "operation_example"; // String | 
let createMeetingWithAttendeesRequest = new AmazonChime.CreateMeetingWithAttendeesRequest(); // CreateMeetingWithAttendeesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMeetingWithAttendees(operation, createMeetingWithAttendeesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **String**|  | 
 **createMeetingWithAttendeesRequest** | [**CreateMeetingWithAttendeesRequest**](CreateMeetingWithAttendeesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMeetingWithAttendeesResponse**](CreateMeetingWithAttendeesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPhoneNumberOrder

> CreatePhoneNumberOrderResponse createPhoneNumberOrder(createPhoneNumberOrderRequest, opts)



Creates an order for phone numbers to be provisioned. For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let createPhoneNumberOrderRequest = new AmazonChime.CreatePhoneNumberOrderRequest(); // CreatePhoneNumberOrderRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPhoneNumberOrder(createPhoneNumberOrderRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createPhoneNumberOrderRequest** | [**CreatePhoneNumberOrderRequest**](CreatePhoneNumberOrderRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePhoneNumberOrderResponse**](CreatePhoneNumberOrderResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createProxySession

> CreateProxySessionResponse createProxySession(voiceConnectorId, createProxySessionRequest, opts)



&lt;p&gt;Creates a proxy session on the specified Amazon Chime Voice Connector for the specified participant phone numbers.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateProxySession.html\&quot;&gt;CreateProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
let createProxySessionRequest = new AmazonChime.CreateProxySessionRequest(); // CreateProxySessionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createProxySession(voiceConnectorId, createProxySessionRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | 
 **createProxySessionRequest** | [**CreateProxySessionRequest**](CreateProxySessionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateProxySessionResponse**](CreateProxySessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRoom

> CreateRoomResponse createRoom(accountId, createRoomRequest, opts)



Creates a chat room for the specified Amazon Chime Enterprise account.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let createRoomRequest = new AmazonChime.CreateRoomRequest(); // CreateRoomRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRoom(accountId, createRoomRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **createRoomRequest** | [**CreateRoomRequest**](CreateRoomRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRoomResponse**](CreateRoomResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRoomMembership

> CreateRoomMembershipResponse createRoomMembership(accountId, roomId, createRoomMembershipRequest, opts)



Adds a member to a chat room in an Amazon Chime Enterprise account. A member can be either a user or a bot. The member role designates whether the member is a chat room administrator or a general chat room member.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let roomId = "roomId_example"; // String | The room ID.
let createRoomMembershipRequest = new AmazonChime.CreateRoomMembershipRequest(); // CreateRoomMembershipRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRoomMembership(accountId, roomId, createRoomMembershipRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **roomId** | **String**| The room ID. | 
 **createRoomMembershipRequest** | [**CreateRoomMembershipRequest**](CreateRoomMembershipRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRoomMembershipResponse**](CreateRoomMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSipMediaApplication

> CreateSipMediaApplicationResponse createSipMediaApplication(createSipMediaApplicationRequest, opts)



&lt;p&gt;Creates a SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplication.html\&quot;&gt;CreateSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let createSipMediaApplicationRequest = new AmazonChime.CreateSipMediaApplicationRequest(); // CreateSipMediaApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSipMediaApplication(createSipMediaApplicationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createSipMediaApplicationRequest** | [**CreateSipMediaApplicationRequest**](CreateSipMediaApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSipMediaApplicationResponse**](CreateSipMediaApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSipMediaApplicationCall

> CreateSipMediaApplicationCallResponse createSipMediaApplicationCall(sipMediaApplicationId, createSipMediaApplicationCallRequest, opts)



&lt;p&gt;Creates an outbound call to a phone number from the phone number specified in the request, and it invokes the endpoint of the specified &lt;code&gt;sipMediaApplicationId&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplicationCall.html\&quot;&gt;CreateSipMediaApplicationCall&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The ID of the SIP media application.
let createSipMediaApplicationCallRequest = new AmazonChime.CreateSipMediaApplicationCallRequest(); // CreateSipMediaApplicationCallRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSipMediaApplicationCall(sipMediaApplicationId, createSipMediaApplicationCallRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sipMediaApplicationId** | **String**| The ID of the SIP media application. | 
 **createSipMediaApplicationCallRequest** | [**CreateSipMediaApplicationCallRequest**](CreateSipMediaApplicationCallRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSipMediaApplicationCallResponse**](CreateSipMediaApplicationCallResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSipRule

> CreateSipRuleResponse createSipRule(createSipRuleRequest, opts)



&lt;p&gt;Creates a SIP rule which can be used to run a SIP media application as a target for a specific trigger type.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipRule.html\&quot;&gt;CreateSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let createSipRuleRequest = new AmazonChime.CreateSipRuleRequest(); // CreateSipRuleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSipRule(createSipRuleRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createSipRuleRequest** | [**CreateSipRuleRequest**](CreateSipRuleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSipRuleResponse**](CreateSipRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createUser

> CreateUserResponse createUser(accountId, operation, createUserRequest, opts)



Creates a user under the specified Amazon Chime account.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let operation = "operation_example"; // String | 
let createUserRequest = new AmazonChime.CreateUserRequest(); // CreateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createUser(accountId, operation, createUserRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **operation** | **String**|  | 
 **createUserRequest** | [**CreateUserRequest**](CreateUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVoiceConnector

> CreateVoiceConnectorResponse createVoiceConnector(createVoiceConnectorRequest, opts)



&lt;p&gt;Creates an Amazon Chime Voice Connector under the administrator&#39;s AWS account. You can choose to create an Amazon Chime Voice Connector in a specific AWS Region.&lt;/p&gt; &lt;p&gt;Enabling &lt;a&gt;CreateVoiceConnectorRequest$RequireEncryption&lt;/a&gt; configures your Amazon Chime Voice Connector to use TLS transport for SIP signaling and Secure RTP (SRTP) for media. Inbound calls use TLS transport, and unencrypted outbound calls are blocked. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnector.html\&quot;&gt;CreateVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let createVoiceConnectorRequest = new AmazonChime.CreateVoiceConnectorRequest(); // CreateVoiceConnectorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVoiceConnector(createVoiceConnectorRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createVoiceConnectorRequest** | [**CreateVoiceConnectorRequest**](CreateVoiceConnectorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVoiceConnectorResponse**](CreateVoiceConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVoiceConnectorGroup

> CreateVoiceConnectorGroupResponse createVoiceConnectorGroup(createVoiceConnectorGroupRequest, opts)



&lt;p&gt;Creates an Amazon Chime Voice Connector group under the administrator&#39;s AWS account. You can associate Amazon Chime Voice Connectors with the Amazon Chime Voice Connector group by including &lt;code&gt;VoiceConnectorItems&lt;/code&gt; in the request.&lt;/p&gt; &lt;p&gt;You can include Amazon Chime Voice Connectors from different AWS Regions in your group. This creates a fault tolerant mechanism for fallback in case of availability events.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnectorGroup.html\&quot;&gt;CreateVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let createVoiceConnectorGroupRequest = new AmazonChime.CreateVoiceConnectorGroupRequest(); // CreateVoiceConnectorGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVoiceConnectorGroup(createVoiceConnectorGroupRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createVoiceConnectorGroupRequest** | [**CreateVoiceConnectorGroupRequest**](CreateVoiceConnectorGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVoiceConnectorGroupResponse**](CreateVoiceConnectorGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAccount

> Object deleteAccount(accountId, opts)



&lt;p&gt;Deletes the specified Amazon Chime account. You must suspend all users before deleting &lt;code&gt;Team&lt;/code&gt; account. You can use the &lt;a&gt;BatchSuspendUser&lt;/a&gt; action to dodo.&lt;/p&gt; &lt;p&gt;For &lt;code&gt;EnterpriseLWA&lt;/code&gt; and &lt;code&gt;EnterpriseAD&lt;/code&gt; accounts, you must release the claimed domains for your Amazon Chime account before deletion. As soon as you release the domain, all users under that account are suspended.&lt;/p&gt; &lt;p&gt;Deleted accounts appear in your &lt;code&gt;Disabled&lt;/code&gt; accounts list for 90 days. To restore deleted account from your &lt;code&gt;Disabled&lt;/code&gt; accounts list, you must contact AWS Support.&lt;/p&gt; &lt;p&gt;After 90 days, deleted accounts are permanently removed from your &lt;code&gt;Disabled&lt;/code&gt; accounts list.&lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAccount(accountId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteAppInstance

> deleteAppInstance(appInstanceArn, opts)



&lt;p&gt;Deletes an &lt;code&gt;AppInstance&lt;/code&gt; and all associated data asynchronously.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstance.html\&quot;&gt;DeleteAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAppInstance(appInstanceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteAppInstanceAdmin

> deleteAppInstanceAdmin(appInstanceAdminArn, appInstanceArn, opts)



&lt;p&gt;Demotes an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; to an &lt;code&gt;AppInstanceUser&lt;/code&gt;. This action does not delete the user.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceAdmin.html\&quot;&gt;DeleteAppInstanceAdmin&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceAdminArn = "appInstanceAdminArn_example"; // String | The ARN of the <code>AppInstance</code>'s administrator.
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAppInstanceAdmin(appInstanceAdminArn, appInstanceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceAdminArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;&#39;s administrator. | 
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteAppInstanceStreamingConfigurations

> deleteAppInstanceStreamingConfigurations(appInstanceArn, opts)



&lt;p&gt;Deletes the streaming configurations of an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceStreamingConfigurations.html\&quot;&gt;DeleteAppInstanceStreamingConfigurations&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the streaming configurations being deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAppInstanceStreamingConfigurations(appInstanceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the streaming configurations being deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteAppInstanceUser

> deleteAppInstanceUser(appInstanceUserArn, opts)



&lt;p&gt;Deletes an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceUser.html\&quot;&gt;DeleteAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the user request being deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAppInstanceUser(appInstanceUserArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceUserArn** | **String**| The ARN of the user request being deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteAttendee

> deleteAttendee(meetingId, attendeeId, opts)



&lt;p&gt;Deletes an attendee from the specified Amazon Chime SDK meeting and deletes their &lt;code&gt;JoinToken&lt;/code&gt;. Attendees are automatically deleted when a Amazon Chime SDK meeting is deleted. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteAttendee.html\&quot;&gt;DeleteAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let attendeeId = "attendeeId_example"; // String | The Amazon Chime SDK attendee ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAttendee(meetingId, attendeeId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **attendeeId** | **String**| The Amazon Chime SDK attendee ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannel

> deleteChannel(channelArn, opts)



&lt;p&gt;Immediately makes a channel and its memberships inaccessible and marks them for deletion. This is an irreversible process.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannel.html\&quot;&gt;DeleteChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel being deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.deleteChannel(channelArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel being deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannelBan

> deleteChannelBan(channelArn, memberArn, opts)



&lt;p&gt;Removes a user from a channel&#39;s ban list.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelBan.html\&quot;&gt;DeleteChannelBan&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel from which the <code>AppInstanceUser</code> was banned.
let memberArn = "memberArn_example"; // String | The ARN of the <code>AppInstanceUser</code> that you want to reinstate.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.deleteChannelBan(channelArn, memberArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel from which the &lt;code&gt;AppInstanceUser&lt;/code&gt; was banned. | 
 **memberArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; that you want to reinstate. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannelMembership

> deleteChannelMembership(channelArn, memberArn, opts)



&lt;p&gt;Removes a member from a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMembership.html\&quot;&gt;DeleteChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel from which you want to remove the user.
let memberArn = "memberArn_example"; // String | The ARN of the member that you're removing from the channel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.deleteChannelMembership(channelArn, memberArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel from which you want to remove the user. | 
 **memberArn** | **String**| The ARN of the member that you&#39;re removing from the channel. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannelMessage

> deleteChannelMessage(channelArn, messageId, opts)



&lt;p&gt;Deletes a channel message. Only admins can perform this action. Deletion makes messages inaccessible immediately. A background process deletes any revisions created by &lt;code&gt;UpdateChannelMessage&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMessage.html\&quot;&gt;DeleteChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let messageId = "messageId_example"; // String | The ID of the message being deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.deleteChannelMessage(channelArn, messageId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **messageId** | **String**| The ID of the message being deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChannelModerator

> deleteChannelModerator(channelArn, channelModeratorArn, opts)



&lt;p&gt;Deletes a channel moderator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelModerator.html\&quot;&gt;DeleteChannelModerator&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let channelModeratorArn = "channelModeratorArn_example"; // String | The ARN of the moderator being deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.deleteChannelModerator(channelArn, channelModeratorArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **channelModeratorArn** | **String**| The ARN of the moderator being deleted. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEventsConfiguration

> deleteEventsConfiguration(accountId, botId, opts)



Deletes the events configuration that allows a bot to receive outgoing events.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let botId = "botId_example"; // String | The bot ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEventsConfiguration(accountId, botId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **botId** | **String**| The bot ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMediaCapturePipeline

> deleteMediaCapturePipeline(mediaPipelineId, opts)



&lt;p&gt;Deletes the media capture pipeline.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaCapturePipeline.html\&quot;&gt;DeleteMediaCapturePipeline&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let mediaPipelineId = "mediaPipelineId_example"; // String | The ID of the media capture pipeline being deleted. 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMediaCapturePipeline(mediaPipelineId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaPipelineId** | **String**| The ID of the media capture pipeline being deleted.  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMeeting

> deleteMeeting(meetingId, opts)



&lt;p&gt;Deletes the specified Amazon Chime SDK meeting. The operation deletes all attendees, disconnects all clients, and prevents new clients from joining the meeting. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteMeeting.html\&quot;&gt;DeleteMeeting&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMeeting(meetingId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePhoneNumber

> deletePhoneNumber(phoneNumberId, opts)



&lt;p&gt;Moves the specified phone number into the &lt;b&gt;Deletion queue&lt;/b&gt;. A phone number must be disassociated from any users or Amazon Chime Voice Connectors before it can be deleted.&lt;/p&gt; &lt;p&gt;Deleted phone numbers remain in the &lt;b&gt;Deletion queue&lt;/b&gt; for 7 days before they are deleted permanently.&lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let phoneNumberId = "phoneNumberId_example"; // String | The phone number ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deletePhoneNumber(phoneNumberId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumberId** | **String**| The phone number ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteProxySession

> deleteProxySession(voiceConnectorId, proxySessionId, opts)



&lt;p&gt;Deletes the specified proxy session from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteProxySession.html\&quot;&gt;DeleteProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
let proxySessionId = "proxySessionId_example"; // String | The proxy session ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteProxySession(voiceConnectorId, proxySessionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | 
 **proxySessionId** | **String**| The proxy session ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRoom

> deleteRoom(accountId, roomId, opts)



Deletes a chat room in an Amazon Chime Enterprise account.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let roomId = "roomId_example"; // String | The chat room ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRoom(accountId, roomId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **roomId** | **String**| The chat room ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRoomMembership

> deleteRoomMembership(accountId, roomId, memberId, opts)



Removes a member from a chat room in an Amazon Chime Enterprise account.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let roomId = "roomId_example"; // String | The room ID.
let memberId = "memberId_example"; // String | The member ID (user ID or bot ID).
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRoomMembership(accountId, roomId, memberId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **roomId** | **String**| The room ID. | 
 **memberId** | **String**| The member ID (user ID or bot ID). | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSipMediaApplication

> deleteSipMediaApplication(sipMediaApplicationId, opts)



&lt;p&gt;Deletes a SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipMediaApplication.html\&quot;&gt;DeleteSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The SIP media application ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSipMediaApplication(sipMediaApplicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sipMediaApplicationId** | **String**| The SIP media application ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSipRule

> deleteSipRule(sipRuleId, opts)



&lt;p&gt;Deletes a SIP rule. You must disable a SIP rule before you can delete it.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipRule.html\&quot;&gt;DeleteSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let sipRuleId = "sipRuleId_example"; // String | The SIP rule ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSipRule(sipRuleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sipRuleId** | **String**| The SIP rule ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVoiceConnector

> deleteVoiceConnector(voiceConnectorId, opts)



&lt;p&gt;Deletes the specified Amazon Chime Voice Connector. Any phone numbers associated with the Amazon Chime Voice Connector must be disassociated from it before it can be deleted.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnector.html\&quot;&gt;DeleteVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVoiceConnector(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVoiceConnectorEmergencyCallingConfiguration

> deleteVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, opts)



&lt;p&gt;Deletes the emergency calling configuration details from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorEmergencyCallingConfiguration.html\&quot;&gt;DeleteVoiceConnectorEmergencyCallingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVoiceConnectorGroup

> deleteVoiceConnectorGroup(voiceConnectorGroupId, opts)



&lt;p&gt;Deletes the specified Amazon Chime Voice Connector group. Any &lt;code&gt;VoiceConnectorItems&lt;/code&gt; and phone numbers associated with the group must be removed before it can be deleted.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorGroup.html\&quot;&gt;DeleteVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorGroupId = "voiceConnectorGroupId_example"; // String | The Amazon Chime Voice Connector group ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVoiceConnectorGroup(voiceConnectorGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorGroupId** | **String**| The Amazon Chime Voice Connector group ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVoiceConnectorOrigination

> deleteVoiceConnectorOrigination(voiceConnectorId, opts)



&lt;p&gt;Deletes the origination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to deleting the origination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorOrigination.html\&quot;&gt;DeleteVoiceConnectorOrigination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVoiceConnectorOrigination(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVoiceConnectorProxy

> deleteVoiceConnectorProxy(voiceConnectorId, opts)



&lt;p&gt;Deletes the proxy configuration from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorProxy.html\&quot;&gt;DeleteVoiceProxy&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVoiceConnectorProxy(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVoiceConnectorStreamingConfiguration

> deleteVoiceConnectorStreamingConfiguration(voiceConnectorId, opts)



&lt;p&gt;Deletes the streaming configuration for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorStreamingConfiguration.html\&quot;&gt;DeleteVoiceConnectorStreamingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVoiceConnectorStreamingConfiguration(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVoiceConnectorTermination

> deleteVoiceConnectorTermination(voiceConnectorId, opts)



&lt;p&gt;Deletes the termination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to deleting the termination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTermination.html\&quot;&gt;DeleteVoiceConnectorTermination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVoiceConnectorTermination(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVoiceConnectorTerminationCredentials

> deleteVoiceConnectorTerminationCredentials(voiceConnectorId, operation, deleteVoiceConnectorTerminationCredentialsRequest, opts)



&lt;p&gt;Deletes the specified SIP credentials used by your equipment to authenticate during call termination.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTerminationCredentials.html\&quot;&gt;DeleteVoiceConnectorTerminationCredentials&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let operation = "operation_example"; // String | 
let deleteVoiceConnectorTerminationCredentialsRequest = new AmazonChime.DeleteVoiceConnectorTerminationCredentialsRequest(); // DeleteVoiceConnectorTerminationCredentialsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVoiceConnectorTerminationCredentials(voiceConnectorId, operation, deleteVoiceConnectorTerminationCredentialsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **operation** | **String**|  | 
 **deleteVoiceConnectorTerminationCredentialsRequest** | [**DeleteVoiceConnectorTerminationCredentialsRequest**](DeleteVoiceConnectorTerminationCredentialsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAppInstance

> DescribeAppInstanceResponse describeAppInstance(appInstanceArn, opts)



&lt;p&gt;Returns the full details of an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstance.html\&quot;&gt;DescribeAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAppInstance(appInstanceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAppInstanceResponse**](DescribeAppInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeAppInstanceAdmin

> DescribeAppInstanceAdminResponse describeAppInstanceAdmin(appInstanceAdminArn, appInstanceArn, opts)



&lt;p&gt;Returns the full details of an &lt;code&gt;AppInstanceAdmin&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceAdmin.html\&quot;&gt;DescribeAppInstanceAdmin&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceAdminArn = "appInstanceAdminArn_example"; // String | The ARN of the <code>AppInstanceAdmin</code>.
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAppInstanceAdmin(appInstanceAdminArn, appInstanceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceAdminArn** | **String**| The ARN of the &lt;code&gt;AppInstanceAdmin&lt;/code&gt;. | 
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAppInstanceAdminResponse**](DescribeAppInstanceAdminResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeAppInstanceUser

> DescribeAppInstanceUserResponse describeAppInstanceUser(appInstanceUserArn, opts)



&lt;p&gt;Returns the full details of an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceUser.html\&quot;&gt;DescribeAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the <code>AppInstanceUser</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAppInstanceUser(appInstanceUserArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceUserArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAppInstanceUserResponse**](DescribeAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannel

> DescribeChannelResponse describeChannel(channelArn, opts)



&lt;p&gt;Returns the full details of a channel in an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannel.html\&quot;&gt;DescribeChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.describeChannel(channelArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**DescribeChannelResponse**](DescribeChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannelBan

> DescribeChannelBanResponse describeChannelBan(channelArn, memberArn, opts)



&lt;p&gt;Returns the full details of a channel ban.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelBan.html\&quot;&gt;DescribeChannelBan&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel from which the user is banned.
let memberArn = "memberArn_example"; // String | The ARN of the member being banned.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.describeChannelBan(channelArn, memberArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel from which the user is banned. | 
 **memberArn** | **String**| The ARN of the member being banned. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**DescribeChannelBanResponse**](DescribeChannelBanResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannelMembership

> DescribeChannelMembershipResponse describeChannelMembership(channelArn, memberArn, opts)



&lt;p&gt;Returns the full details of a user&#39;s channel membership.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembership.html\&quot;&gt;DescribeChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let memberArn = "memberArn_example"; // String | The ARN of the member.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.describeChannelMembership(channelArn, memberArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **memberArn** | **String**| The ARN of the member. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**DescribeChannelMembershipResponse**](DescribeChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannelMembershipForAppInstanceUser

> DescribeChannelMembershipForAppInstanceUserResponse describeChannelMembershipForAppInstanceUser(channelArn, appInstanceUserArn, scope, opts)



&lt;p&gt; Returns the details of a channel based on the membership of the specified &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembershipForAppInstanceUser.html\&quot;&gt;DescribeChannelMembershipForAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel to which the user belongs.
let appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the user in a channel.
let scope = "scope_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.describeChannelMembershipForAppInstanceUser(channelArn, appInstanceUserArn, scope, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel to which the user belongs. | 
 **appInstanceUserArn** | **String**| The ARN of the user in a channel. | 
 **scope** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**DescribeChannelMembershipForAppInstanceUserResponse**](DescribeChannelMembershipForAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannelModeratedByAppInstanceUser

> DescribeChannelModeratedByAppInstanceUserResponse describeChannelModeratedByAppInstanceUser(channelArn, appInstanceUserArn, scope, opts)



&lt;p&gt;Returns the full details of a channel moderated by the specified &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModeratedByAppInstanceUser.html\&quot;&gt;DescribeChannelModeratedByAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the moderated channel.
let appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the <code>AppInstanceUser</code> in the moderated channel.
let scope = "scope_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.describeChannelModeratedByAppInstanceUser(channelArn, appInstanceUserArn, scope, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the moderated channel. | 
 **appInstanceUserArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; in the moderated channel. | 
 **scope** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**DescribeChannelModeratedByAppInstanceUserResponse**](DescribeChannelModeratedByAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannelModerator

> DescribeChannelModeratorResponse describeChannelModerator(channelArn, channelModeratorArn, opts)



&lt;p&gt;Returns the full details of a single ChannelModerator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModerator.html\&quot;&gt;DescribeChannelModerator&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let channelModeratorArn = "channelModeratorArn_example"; // String | The ARN of the channel moderator.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.describeChannelModerator(channelArn, channelModeratorArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **channelModeratorArn** | **String**| The ARN of the channel moderator. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**DescribeChannelModeratorResponse**](DescribeChannelModeratorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociatePhoneNumberFromUser

> Object disassociatePhoneNumberFromUser(accountId, userId, operation, opts)



Disassociates the primary provisioned phone number from the specified Amazon Chime user.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let userId = "userId_example"; // String | The user ID.
let operation = "operation_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociatePhoneNumberFromUser(accountId, userId, operation, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **userId** | **String**| The user ID. | 
 **operation** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disassociatePhoneNumbersFromVoiceConnector

> DisassociatePhoneNumbersFromVoiceConnectorResponse disassociatePhoneNumbersFromVoiceConnector(voiceConnectorId, operation, disassociatePhoneNumbersFromVoiceConnectorRequest, opts)



&lt;p&gt;Disassociates the specified phone numbers from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnector.html\&quot;&gt;DisassociatePhoneNumbersFromVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let operation = "operation_example"; // String | 
let disassociatePhoneNumbersFromVoiceConnectorRequest = new AmazonChime.DisassociatePhoneNumbersFromVoiceConnectorRequest(); // DisassociatePhoneNumbersFromVoiceConnectorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociatePhoneNumbersFromVoiceConnector(voiceConnectorId, operation, disassociatePhoneNumbersFromVoiceConnectorRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **operation** | **String**|  | 
 **disassociatePhoneNumbersFromVoiceConnectorRequest** | [**DisassociatePhoneNumbersFromVoiceConnectorRequest**](DisassociatePhoneNumbersFromVoiceConnectorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociatePhoneNumbersFromVoiceConnectorResponse**](DisassociatePhoneNumbersFromVoiceConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociatePhoneNumbersFromVoiceConnectorGroup

> DisassociatePhoneNumbersFromVoiceConnectorGroupResponse disassociatePhoneNumbersFromVoiceConnectorGroup(voiceConnectorGroupId, operation, disassociatePhoneNumbersFromVoiceConnectorRequest, opts)



&lt;p&gt;Disassociates the specified phone numbers from the specified Amazon Chime Voice Connector group.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnectorGroup.html\&quot;&gt;DisassociatePhoneNumbersFromVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorGroupId = "voiceConnectorGroupId_example"; // String | The Amazon Chime Voice Connector group ID.
let operation = "operation_example"; // String | 
let disassociatePhoneNumbersFromVoiceConnectorRequest = new AmazonChime.DisassociatePhoneNumbersFromVoiceConnectorRequest(); // DisassociatePhoneNumbersFromVoiceConnectorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociatePhoneNumbersFromVoiceConnectorGroup(voiceConnectorGroupId, operation, disassociatePhoneNumbersFromVoiceConnectorRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorGroupId** | **String**| The Amazon Chime Voice Connector group ID. | 
 **operation** | **String**|  | 
 **disassociatePhoneNumbersFromVoiceConnectorRequest** | [**DisassociatePhoneNumbersFromVoiceConnectorRequest**](DisassociatePhoneNumbersFromVoiceConnectorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociatePhoneNumbersFromVoiceConnectorGroupResponse**](DisassociatePhoneNumbersFromVoiceConnectorGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateSigninDelegateGroupsFromAccount

> Object disassociateSigninDelegateGroupsFromAccount(accountId, operation, disassociateSigninDelegateGroupsFromAccountRequest, opts)



Disassociates the specified sign-in delegate groups from the specified Amazon Chime account.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let operation = "operation_example"; // String | 
let disassociateSigninDelegateGroupsFromAccountRequest = new AmazonChime.DisassociateSigninDelegateGroupsFromAccountRequest(); // DisassociateSigninDelegateGroupsFromAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateSigninDelegateGroupsFromAccount(accountId, operation, disassociateSigninDelegateGroupsFromAccountRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **operation** | **String**|  | 
 **disassociateSigninDelegateGroupsFromAccountRequest** | [**DisassociateSigninDelegateGroupsFromAccountRequest**](DisassociateSigninDelegateGroupsFromAccountRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAccount

> GetAccountResponse getAccount(accountId, opts)



Retrieves details for the specified Amazon Chime account, such as account type and supported licenses.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccount(accountId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccountResponse**](GetAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAccountSettings

> GetAccountSettingsResponse getAccountSettings(accountId, opts)



Retrieves account settings for the specified Amazon Chime account ID, such as remote control and dialout settings. For more information about these settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/policies.html\&quot;&gt;Use the Policies Page&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;. 

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccountSettings(accountId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAccountSettingsResponse**](GetAccountSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAppInstanceRetentionSettings

> GetAppInstanceRetentionSettingsResponse getAppInstanceRetentionSettings(appInstanceArn, opts)



&lt;p&gt;Gets the retention settings for an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_GetAppInstanceRetentionSettings.html\&quot;&gt;GetMessagingRetentionSettings&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAppInstanceRetentionSettings(appInstanceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAppInstanceRetentionSettingsResponse**](GetAppInstanceRetentionSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAppInstanceStreamingConfigurations

> GetAppInstanceStreamingConfigurationsResponse getAppInstanceStreamingConfigurations(appInstanceArn, opts)



&lt;p&gt;Gets the streaming settings for an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingStreamingConfigurations.html\&quot;&gt;GetMessagingStreamingConfigurations&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAppInstanceStreamingConfigurations(appInstanceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAppInstanceStreamingConfigurationsResponse**](GetAppInstanceStreamingConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAttendee

> GetAttendeeResponse getAttendee(meetingId, attendeeId, opts)



&lt;p&gt; Gets the Amazon Chime SDK attendee details for a specified meeting ID and attendee ID. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetAttendee.html\&quot;&gt;GetAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let attendeeId = "attendeeId_example"; // String | The Amazon Chime SDK attendee ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAttendee(meetingId, attendeeId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **attendeeId** | **String**| The Amazon Chime SDK attendee ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAttendeeResponse**](GetAttendeeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBot

> GetBotResponse getBot(accountId, botId, opts)



Retrieves details for the specified bot, such as bot email address, bot type, status, and display name.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let botId = "botId_example"; // String | The bot ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBot(accountId, botId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **botId** | **String**| The bot ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBotResponse**](GetBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannelMessage

> GetChannelMessageResponse getChannelMessage(channelArn, messageId, opts)



&lt;p&gt;Gets the full details of a channel message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The x-amz-chime-bearer request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessage.html\&quot;&gt;GetChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let messageId = "messageId_example"; // String | The ID of the message.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.getChannelMessage(channelArn, messageId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **messageId** | **String**| The ID of the message. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**GetChannelMessageResponse**](GetChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventsConfiguration

> GetEventsConfigurationResponse getEventsConfiguration(accountId, botId, opts)



Gets details for an events configuration that allows a bot to receive outgoing events, such as an HTTPS endpoint or Lambda function ARN.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let botId = "botId_example"; // String | The bot ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEventsConfiguration(accountId, botId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **botId** | **String**| The bot ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEventsConfigurationResponse**](GetEventsConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGlobalSettings

> GetGlobalSettingsResponse getGlobalSettings(opts)



Retrieves global settings for the administrator&#39;s AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getGlobalSettings(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetGlobalSettingsResponse**](GetGlobalSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMediaCapturePipeline

> GetMediaCapturePipelineResponse getMediaCapturePipeline(mediaPipelineId, opts)



&lt;p&gt;Gets an existing media capture pipeline.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaCapturePipeline.html\&quot;&gt;GetMediaCapturePipeline&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let mediaPipelineId = "mediaPipelineId_example"; // String | The ID of the pipeline that you want to get.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMediaCapturePipeline(mediaPipelineId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mediaPipelineId** | **String**| The ID of the pipeline that you want to get. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMediaCapturePipelineResponse**](GetMediaCapturePipelineResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMeeting

> GetMeetingResponse getMeeting(meetingId, opts)



&lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetMeeting.html\&quot;&gt;GetMeeting&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; Gets the Amazon Chime SDK meeting details for the specified meeting ID. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . &lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMeeting(meetingId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMeetingResponse**](GetMeetingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessagingSessionEndpoint

> GetMessagingSessionEndpointResponse getMessagingSessionEndpoint(opts)



&lt;p&gt;The details of the endpoint for the messaging session.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingSessionEndpoint.html\&quot;&gt;GetMessagingSessionEndpoint&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getMessagingSessionEndpoint(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetMessagingSessionEndpointResponse**](GetMessagingSessionEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhoneNumber

> GetPhoneNumberResponse getPhoneNumber(phoneNumberId, opts)



Retrieves details for the specified phone number ID, such as associations, capabilities, and product type.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let phoneNumberId = "phoneNumberId_example"; // String | The phone number ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPhoneNumber(phoneNumberId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumberId** | **String**| The phone number ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPhoneNumberResponse**](GetPhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhoneNumberOrder

> GetPhoneNumberOrderResponse getPhoneNumberOrder(phoneNumberOrderId, opts)



Retrieves details for the specified phone number order, such as the order creation timestamp, phone numbers in E.164 format, product type, and order status.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let phoneNumberOrderId = "phoneNumberOrderId_example"; // String | The ID for the phone number order.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPhoneNumberOrder(phoneNumberOrderId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumberOrderId** | **String**| The ID for the phone number order. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPhoneNumberOrderResponse**](GetPhoneNumberOrderResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPhoneNumberSettings

> GetPhoneNumberSettingsResponse getPhoneNumberSettings(opts)



Retrieves the phone number settings for the administrator&#39;s AWS account, such as the default outbound calling name.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getPhoneNumberSettings(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetPhoneNumberSettingsResponse**](GetPhoneNumberSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProxySession

> GetProxySessionResponse getProxySession(voiceConnectorId, proxySessionId, opts)



&lt;p&gt;Gets the specified proxy session details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetProxySession.html\&quot;&gt;GetProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
let proxySessionId = "proxySessionId_example"; // String | The proxy session ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getProxySession(voiceConnectorId, proxySessionId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | 
 **proxySessionId** | **String**| The proxy session ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetProxySessionResponse**](GetProxySessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRetentionSettings

> GetRetentionSettingsResponse getRetentionSettings(accountId, opts)



 Gets the retention settings for the specified Amazon Chime Enterprise account. For more information about retention settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/chat-retention.html\&quot;&gt;Managing Chat Retention Policies&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;. 

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRetentionSettings(accountId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRetentionSettingsResponse**](GetRetentionSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRoom

> GetRoomResponse getRoom(accountId, roomId, opts)



Retrieves room details, such as the room name, for a room in an Amazon Chime Enterprise account.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let roomId = "roomId_example"; // String | The room ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRoom(accountId, roomId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **roomId** | **String**| The room ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRoomResponse**](GetRoomResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSipMediaApplication

> GetSipMediaApplicationResponse getSipMediaApplication(sipMediaApplicationId, opts)



&lt;p&gt;Retrieves the information for a SIP media application, including name, AWS Region, and endpoints.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplication.html\&quot;&gt;GetSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The SIP media application ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSipMediaApplication(sipMediaApplicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sipMediaApplicationId** | **String**| The SIP media application ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSipMediaApplicationResponse**](GetSipMediaApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSipMediaApplicationLoggingConfiguration

> GetSipMediaApplicationLoggingConfigurationResponse getSipMediaApplicationLoggingConfiguration(sipMediaApplicationId, opts)



&lt;p&gt;Returns the logging configuration for the specified SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplicationLoggingConfiguration.html\&quot;&gt;GetSipMediaApplicationLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The SIP media application ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSipMediaApplicationLoggingConfiguration(sipMediaApplicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sipMediaApplicationId** | **String**| The SIP media application ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSipMediaApplicationLoggingConfigurationResponse**](GetSipMediaApplicationLoggingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSipRule

> GetSipRuleResponse getSipRule(sipRuleId, opts)



&lt;p&gt;Retrieves the details of a SIP rule, such as the rule ID, name, triggers, and target endpoints.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipRule.html\&quot;&gt;GetSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let sipRuleId = "sipRuleId_example"; // String | The SIP rule ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSipRule(sipRuleId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sipRuleId** | **String**| The SIP rule ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSipRuleResponse**](GetSipRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUser

> GetUserResponse getUser(accountId, userId, opts)



&lt;p&gt;Retrieves details for the specified user ID, such as primary email address, license type,and personal meeting PIN.&lt;/p&gt; &lt;p&gt; To retrieve user details with an email address instead of a user ID, use the &lt;a&gt;ListUsers&lt;/a&gt; action, and then filter by email address. &lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let userId = "userId_example"; // String | The user ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getUser(accountId, userId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **userId** | **String**| The user ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserSettings

> GetUserSettingsResponse getUserSettings(accountId, userId, opts)



Retrieves settings for the specified user ID, such as any associated phone number settings.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let userId = "userId_example"; // String | The user ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getUserSettings(accountId, userId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **userId** | **String**| The user ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetUserSettingsResponse**](GetUserSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceConnector

> GetVoiceConnectorResponse getVoiceConnector(voiceConnectorId, opts)



&lt;p&gt;Retrieves details for the specified Amazon Chime Voice Connector, such as timestamps,name, outbound host, and encryption requirements.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnector.html\&quot;&gt;GetVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVoiceConnector(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVoiceConnectorResponse**](GetVoiceConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceConnectorEmergencyCallingConfiguration

> GetVoiceConnectorEmergencyCallingConfigurationResponse getVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, opts)



&lt;p&gt;Gets the emergency calling configuration details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration.html\&quot;&gt;GetVoiceConnectorEmergencyCallingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVoiceConnectorEmergencyCallingConfigurationResponse**](GetVoiceConnectorEmergencyCallingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceConnectorGroup

> GetVoiceConnectorGroupResponse getVoiceConnectorGroup(voiceConnectorGroupId, opts)



&lt;p&gt; Retrieves details for the specified Amazon Chime Voice Connector group, such as timestamps,name, and associated &lt;code&gt;VoiceConnectorItems&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorGroup.html\&quot;&gt;GetVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorGroupId = "voiceConnectorGroupId_example"; // String | The Amazon Chime Voice Connector group ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVoiceConnectorGroup(voiceConnectorGroupId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorGroupId** | **String**| The Amazon Chime Voice Connector group ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVoiceConnectorGroupResponse**](GetVoiceConnectorGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceConnectorLoggingConfiguration

> GetVoiceConnectorLoggingConfigurationResponse getVoiceConnectorLoggingConfiguration(voiceConnectorId, opts)



&lt;p&gt;Retrieves the logging configuration details for the specified Amazon Chime Voice Connector. Shows whether SIP message logs are enabled for sending to Amazon CloudWatch Logs.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorLoggingConfiguration.html\&quot;&gt;GetVoiceConnectorLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVoiceConnectorLoggingConfiguration(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVoiceConnectorLoggingConfigurationResponse**](GetVoiceConnectorLoggingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceConnectorOrigination

> GetVoiceConnectorOriginationResponse getVoiceConnectorOrigination(voiceConnectorId, opts)



&lt;p&gt;Retrieves origination setting details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorOrigination.html\&quot;&gt;GetVoiceConnectorOrigination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVoiceConnectorOrigination(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVoiceConnectorOriginationResponse**](GetVoiceConnectorOriginationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceConnectorProxy

> GetVoiceConnectorProxyResponse getVoiceConnectorProxy(voiceConnectorId, opts)



&lt;p&gt;Gets the proxy configuration details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorProxy.html\&quot;&gt;GetVoiceConnectorProxy&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVoiceConnectorProxy(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVoiceConnectorProxyResponse**](GetVoiceConnectorProxyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceConnectorStreamingConfiguration

> GetVoiceConnectorStreamingConfigurationResponse getVoiceConnectorStreamingConfiguration(voiceConnectorId, opts)



&lt;p&gt;Retrieves the streaming configuration details for the specified Amazon Chime Voice Connector. Shows whether media streaming is enabled for sending to Amazon Kinesis. It also shows the retention period, in hours, for the Amazon Kinesis data.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorStreamingConfiguration.html\&quot;&gt;GetVoiceConnectorStreamingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVoiceConnectorStreamingConfiguration(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVoiceConnectorStreamingConfigurationResponse**](GetVoiceConnectorStreamingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceConnectorTermination

> GetVoiceConnectorTerminationResponse getVoiceConnectorTermination(voiceConnectorId, opts)



&lt;p&gt;Retrieves termination setting details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTermination.html\&quot;&gt;GetVoiceConnectorTermination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVoiceConnectorTermination(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVoiceConnectorTerminationResponse**](GetVoiceConnectorTerminationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceConnectorTerminationHealth

> GetVoiceConnectorTerminationHealthResponse getVoiceConnectorTerminationHealth(voiceConnectorId, opts)



&lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTerminationHealth.html\&quot;&gt;GetVoiceConnectorTerminationHealth&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Retrieves information about the last time a SIP &lt;code&gt;OPTIONS&lt;/code&gt; ping was received from your SIP infrastructure for the specified Amazon Chime Voice Connector.&lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVoiceConnectorTerminationHealth(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVoiceConnectorTerminationHealthResponse**](GetVoiceConnectorTerminationHealthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## inviteUsers

> InviteUsersResponse inviteUsers(accountId, operation, inviteUsersRequest, opts)



Sends email to a maximum of 50 users, inviting them to the specified Amazon Chime &lt;code&gt;Team&lt;/code&gt; account. Only &lt;code&gt;Team&lt;/code&gt; account types are currently supported for this action.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let operation = "operation_example"; // String | 
let inviteUsersRequest = new AmazonChime.InviteUsersRequest(); // InviteUsersRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.inviteUsers(accountId, operation, inviteUsersRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **operation** | **String**|  | 
 **inviteUsersRequest** | [**InviteUsersRequest**](InviteUsersRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**InviteUsersResponse**](InviteUsersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAccounts

> ListAccountsResponse listAccounts(opts)



Lists the Amazon Chime accounts under the administrator&#39;s AWS account. You can filter accounts by account name prefix. To find out which Amazon Chime account a user belongs to, you can filter by the user&#39;s email address, which returns one account result.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'name': "name_example", // String | Amazon Chime account name prefix with which to filter results.
  'userEmail': "userEmail_example", // String | User email address with which to filter results.
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of results to return in a single call. Defaults to 100.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listAccounts(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **name** | **String**| Amazon Chime account name prefix with which to filter results. | [optional] 
 **userEmail** | **String**| User email address with which to filter results. | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. Defaults to 100. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListAccountsResponse**](ListAccountsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAppInstanceAdmins

> ListAppInstanceAdminsResponse listAppInstanceAdmins(appInstanceArn, opts)



&lt;p&gt;Returns a list of the administrators in the &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceAdmins.html\&quot;&gt;ListAppInstanceAdmins&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of administrators that you want to return.
  'nextToken': "nextToken_example", // String | The token returned from previous API requests until the number of administrators is reached.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listAppInstanceAdmins(appInstanceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of administrators that you want to return. | [optional] 
 **nextToken** | **String**| The token returned from previous API requests until the number of administrators is reached. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListAppInstanceAdminsResponse**](ListAppInstanceAdminsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAppInstanceUsers

> ListAppInstanceUsersResponse listAppInstanceUsers(appInstanceArn, opts)



&lt;p&gt;List all &lt;code&gt;AppInstanceUsers&lt;/code&gt; created under a single &lt;code&gt;AppInstance&lt;/code&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceUsers.html\&quot;&gt;ListAppInstanceUsers&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of requests that you want returned.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested users are returned.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listAppInstanceUsers(appInstanceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of requests that you want returned. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested users are returned. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListAppInstanceUsersResponse**](ListAppInstanceUsersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAppInstances

> ListAppInstancesResponse listAppInstances(opts)



&lt;p&gt;Lists all Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;s created under a single AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstances.html\&quot;&gt;ListAppInstances&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of <code>AppInstance</code>s that you want to return.
  'nextToken': "nextToken_example", // String | The token passed by previous API requests until you reach the maximum number of <code>AppInstance</code>s.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listAppInstances(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of &lt;code&gt;AppInstance&lt;/code&gt;s that you want to return. | [optional] 
 **nextToken** | **String**| The token passed by previous API requests until you reach the maximum number of &lt;code&gt;AppInstance&lt;/code&gt;s. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListAppInstancesResponse**](ListAppInstancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAttendeeTags

> ListAttendeeTagsResponse listAttendeeTags(meetingId, attendeeId, opts)



&lt;p&gt;Lists the tags applied to an Amazon Chime SDK attendee resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt;ListAttendeeTags is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let attendeeId = "attendeeId_example"; // String | The Amazon Chime SDK attendee ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listAttendeeTags(meetingId, attendeeId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **attendeeId** | **String**| The Amazon Chime SDK attendee ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListAttendeeTagsResponse**](ListAttendeeTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAttendees

> ListAttendeesResponse listAttendees(meetingId, opts)



&lt;p&gt; Lists the attendees for the specified Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListAttendees.html\&quot;&gt;ListAttendees&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of results to return in a single call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listAttendees(meetingId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListAttendeesResponse**](ListAttendeesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBots

> ListBotsResponse listBots(accountId, opts)



Lists the bots associated with the administrator&#39;s Amazon Chime Enterprise account ID.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in a single call. The default is 10.
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listBots(accountId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. The default is 10. | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListBotsResponse**](ListBotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelBans

> ListChannelBansResponse listChannelBans(channelArn, opts)



&lt;p&gt;Lists all the users banned from a particular channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelBans.html\&quot;&gt;ListChannelBans&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of bans that you want returned.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested bans are returned.
  'xAmzChimeBearer': "xAmzChimeBearer_example", // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelBans(channelArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of bans that you want returned. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested bans are returned. | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelBansResponse**](ListChannelBansResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelMemberships

> ListChannelMembershipsResponse listChannelMemberships(channelArn, opts)



&lt;p&gt;Lists all channel memberships in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMemberships.html\&quot;&gt;ListChannelMemberships&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The maximum number of channel memberships that you want returned.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'type': "type_example", // String | The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are always returned as part of <code>ListChannelMemberships</code>. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>. Otherwise hidden members are not returned.
  'maxResults': 56, // Number | The maximum number of channel memberships that you want returned.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested channel memberships are returned.
  'xAmzChimeBearer': "xAmzChimeBearer_example", // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelMemberships(channelArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The maximum number of channel memberships that you want returned. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **type** | **String**| The membership type of a user, &lt;code&gt;DEFAULT&lt;/code&gt; or &lt;code&gt;HIDDEN&lt;/code&gt;. Default members are always returned as part of &lt;code&gt;ListChannelMemberships&lt;/code&gt;. Hidden members are only returned if the type filter in &lt;code&gt;ListChannelMemberships&lt;/code&gt; equals &lt;code&gt;HIDDEN&lt;/code&gt;. Otherwise hidden members are not returned. | [optional] 
 **maxResults** | **Number**| The maximum number of channel memberships that you want returned. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested channel memberships are returned. | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelMembershipsResponse**](ListChannelMembershipsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelMembershipsForAppInstanceUser

> ListChannelMembershipsForAppInstanceUserResponse listChannelMembershipsForAppInstanceUser(scope, opts)



&lt;p&gt; Lists all channels that a particular &lt;code&gt;AppInstanceUser&lt;/code&gt; is a part of. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can call the API with a user ARN that is not their own. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html\&quot;&gt;ListChannelMembershipsForAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let scope = "scope_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'appInstanceUserArn': "appInstanceUserArn_example", // String | The ARN of the <code>AppInstanceUser</code>s
  'maxResults': 56, // Number | The maximum number of users that you want returned.
  'nextToken': "nextToken_example", // String | The token returned from previous API requests until the number of channel memberships is reached.
  'xAmzChimeBearer': "xAmzChimeBearer_example", // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelMembershipsForAppInstanceUser(scope, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **appInstanceUserArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;s | [optional] 
 **maxResults** | **Number**| The maximum number of users that you want returned. | [optional] 
 **nextToken** | **String**| The token returned from previous API requests until the number of channel memberships is reached. | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelMembershipsForAppInstanceUserResponse**](ListChannelMembershipsForAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelMessages

> ListChannelMessagesResponse listChannelMessages(channelArn, opts)



&lt;p&gt;List all the messages in a channel. Returns a paginated list of &lt;code&gt;ChannelMessages&lt;/code&gt;. By default, sorted by creation timestamp in descending order.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Redacted messages appear in the results as empty, since they are only redacted, not deleted. Deleted messages do not appear in the results. This action always returns the latest version of an edited message.&lt;/p&gt; &lt;p&gt;Also, the x-amz-chime-bearer request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMessages.html\&quot;&gt;ListChannelMessages&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'sortOrder': "sortOrder_example", // String | The order in which you want messages sorted. Default is Descending, based on time created.
  'notBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | The initial or starting time stamp for your requested messages.
  'notAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | The final or ending time stamp for your requested messages.
  'maxResults': 56, // Number | The maximum number of messages that you want returned.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested messages are returned.
  'xAmzChimeBearer': "xAmzChimeBearer_example", // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelMessages(channelArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **sortOrder** | **String**| The order in which you want messages sorted. Default is Descending, based on time created. | [optional] 
 **notBefore** | **Date**| The initial or starting time stamp for your requested messages. | [optional] 
 **notAfter** | **Date**| The final or ending time stamp for your requested messages. | [optional] 
 **maxResults** | **Number**| The maximum number of messages that you want returned. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested messages are returned. | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelMessagesResponse**](ListChannelMessagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelModerators

> ListChannelModeratorsResponse listChannelModerators(channelArn, opts)



&lt;p&gt;Lists all the moderators for a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelModerators.html\&quot;&gt;ListChannelModerators&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of moderators that you want returned.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested moderators are returned.
  'xAmzChimeBearer': "xAmzChimeBearer_example", // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelModerators(channelArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of moderators that you want returned. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested moderators are returned. | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelModeratorsResponse**](ListChannelModeratorsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannels

> ListChannelsResponse listChannels(appInstanceArn, opts)



&lt;p&gt;Lists all Channels created under a single Chime App as a paginated list. You can specify filters to narrow results.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Functionality &amp;amp; restrictions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use privacy &#x3D; &lt;code&gt;PUBLIC&lt;/code&gt; to retrieve all public channels in the account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can set privacy &#x3D; &lt;code&gt;PRIVATE&lt;/code&gt; to list the private channels in an account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannels.html\&quot;&gt;ListChannels&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'privacy': "privacy_example", // String | The privacy setting. <code>PUBLIC</code> retrieves all the public channels. <code>PRIVATE</code> retrieves private channels. Only an <code>AppInstanceAdmin</code> can retrieve private channels. 
  'maxResults': 56, // Number | The maximum number of channels that you want to return.
  'nextToken': "nextToken_example", // String | The token passed by previous API calls until all requested channels are returned.
  'xAmzChimeBearer': "xAmzChimeBearer_example", // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannels(appInstanceArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **privacy** | **String**| The privacy setting. &lt;code&gt;PUBLIC&lt;/code&gt; retrieves all the public channels. &lt;code&gt;PRIVATE&lt;/code&gt; retrieves private channels. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can retrieve private channels.  | [optional] 
 **maxResults** | **Number**| The maximum number of channels that you want to return. | [optional] 
 **nextToken** | **String**| The token passed by previous API calls until all requested channels are returned. | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelsResponse**](ListChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannelsModeratedByAppInstanceUser

> ListChannelsModeratedByAppInstanceUserResponse listChannelsModeratedByAppInstanceUser(scope, opts)



&lt;p&gt;A list of the channels moderated by an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelsModeratedByAppInstanceUser.html\&quot;&gt;ListChannelsModeratedByAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let scope = "scope_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'appInstanceUserArn': "appInstanceUserArn_example", // String | The ARN of the user in the moderated channel.
  'maxResults': 56, // Number | The maximum number of channels in the request.
  'nextToken': "nextToken_example", // String | The token returned from previous API requests until the number of channels moderated by the user is reached.
  'xAmzChimeBearer': "xAmzChimeBearer_example", // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannelsModeratedByAppInstanceUser(scope, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **appInstanceUserArn** | **String**| The ARN of the user in the moderated channel. | [optional] 
 **maxResults** | **Number**| The maximum number of channels in the request. | [optional] 
 **nextToken** | **String**| The token returned from previous API requests until the number of channels moderated by the user is reached. | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelsModeratedByAppInstanceUserResponse**](ListChannelsModeratedByAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMediaCapturePipelines

> ListMediaCapturePipelinesResponse listMediaCapturePipelines(opts)



&lt;p&gt;Returns a list of media capture pipelines.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaCapturePipelines.html\&quot;&gt;ListMediaCapturePipelines&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token used to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of results to return in a single call. Valid Range: 1 - 99.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listMediaCapturePipelines(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token used to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. Valid Range: 1 - 99. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListMediaCapturePipelinesResponse**](ListMediaCapturePipelinesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMeetingTags

> ListMeetingTagsResponse listMeetingTags(meetingId, opts)



&lt;p&gt;Lists the tags applied to an Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listMeetingTags(meetingId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListMeetingTagsResponse**](ListMeetingTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMeetings

> ListMeetingsResponse listMeetings(opts)



&lt;p&gt;Lists up to 100 active Amazon Chime SDK meetings.&lt;/p&gt; &lt;important&gt; &lt;p&gt;ListMeetings is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of results to return in a single call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listMeetings(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListMeetingsResponse**](ListMeetingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPhoneNumberOrders

> ListPhoneNumberOrdersResponse listPhoneNumberOrders(opts)



Lists the phone number orders for the administrator&#39;s Amazon Chime account.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of results to return in a single call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listPhoneNumberOrders(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListPhoneNumberOrdersResponse**](ListPhoneNumberOrdersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPhoneNumbers

> ListPhoneNumbersResponse listPhoneNumbers(opts)



Lists the phone numbers for the specified Amazon Chime account, Amazon Chime user, Amazon Chime Voice Connector, or Amazon Chime Voice Connector group.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'status': "status_example", // String | The phone number status.
  'productType': "productType_example", // String | The phone number product type.
  'filterName': "filterName_example", // String | The filter to use to limit the number of results.
  'filterValue': "filterValue_example", // String | The value to use for the filter.
  'maxResults': 56, // Number | The maximum number of results to return in a single call.
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listPhoneNumbers(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **status** | **String**| The phone number status. | [optional] 
 **productType** | **String**| The phone number product type. | [optional] 
 **filterName** | **String**| The filter to use to limit the number of results. | [optional] 
 **filterValue** | **String**| The value to use for the filter. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListPhoneNumbersResponse**](ListPhoneNumbersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProxySessions

> ListProxySessionsResponse listProxySessions(voiceConnectorId, opts)



&lt;p&gt;Lists the proxy sessions for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListProxySessions.html\&quot;&gt;ListProxySessions&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'status': "status_example", // String | The proxy session status.
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of results to return in a single call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listProxySessions(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **status** | **String**| The proxy session status. | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListProxySessionsResponse**](ListProxySessionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoomMemberships

> ListRoomMembershipsResponse listRoomMemberships(accountId, roomId, opts)



Lists the membership details for the specified room in an Amazon Chime Enterprise account, such as the members&#39; IDs, email addresses, and names.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let roomId = "roomId_example"; // String | The room ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in a single call.
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRoomMemberships(accountId, roomId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **roomId** | **String**| The room ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRoomMembershipsResponse**](ListRoomMembershipsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRooms

> ListRoomsResponse listRooms(accountId, opts)



Lists the room details for the specified Amazon Chime Enterprise account. Optionally, filter the results by a member ID (user ID or bot ID) to see a list of rooms that the member belongs to.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'memberId': "memberId_example", // String | The member ID (user ID or bot ID).
  'maxResults': 56, // Number | The maximum number of results to return in a single call.
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listRooms(accountId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **memberId** | **String**| The member ID (user ID or bot ID). | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListRoomsResponse**](ListRoomsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSipMediaApplications

> ListSipMediaApplicationsResponse listSipMediaApplications(opts)



&lt;p&gt;Lists the SIP media applications under the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipMediaApplications.html\&quot;&gt;ListSipMediaApplications&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return in a single call. Defaults to 100.
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listSipMediaApplications(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. Defaults to 100. | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListSipMediaApplicationsResponse**](ListSipMediaApplicationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSipRules

> ListSipRulesResponse listSipRules(opts)



&lt;p&gt;Lists the SIP rules under the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipRules.html\&quot;&gt;ListSipRules&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'sipMediaApplication': "sipMediaApplication_example", // String | The SIP media application ID.
  'maxResults': 56, // Number | The maximum number of results to return in a single call. Defaults to 100.
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listSipRules(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **sipMediaApplication** | **String**| The SIP media application ID. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. Defaults to 100. | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListSipRulesResponse**](ListSipRulesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSupportedPhoneNumberCountries

> ListSupportedPhoneNumberCountriesResponse listSupportedPhoneNumberCountries(productType, opts)



Lists supported phone number countries.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let productType = "productType_example"; // String | The phone number product type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listSupportedPhoneNumberCountries(productType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **productType** | **String**| The phone number product type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListSupportedPhoneNumberCountriesResponse**](ListSupportedPhoneNumberCountriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(arn, opts)



&lt;p&gt;Lists the tags applied to an Amazon Chime SDK meeting and messaging resources.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the applicable latest version in the Amazon Chime SDK.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For meetings: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For messaging: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let arn = "arn_example"; // String | The resource ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(arn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arn** | **String**| The resource ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsers

> ListUsersResponse listUsers(accountId, opts)



Lists the users that belong to the specified Amazon Chime account. You can specify an email address to list only the user that the email address belongs to.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'userEmail': "userEmail_example", // String | Optional. The user email address used to filter results. Maximum 1.
  'userType': "userType_example", // String | The user type.
  'maxResults': 56, // Number | The maximum number of results to return in a single call. Defaults to 100.
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listUsers(accountId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **userEmail** | **String**| Optional. The user email address used to filter results. Maximum 1. | [optional] 
 **userType** | **String**| The user type. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. Defaults to 100. | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVoiceConnectorGroups

> ListVoiceConnectorGroupsResponse listVoiceConnectorGroups(opts)



&lt;p&gt;Lists the Amazon Chime Voice Connector groups for the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorGroups.html\&quot;&gt;ListVoiceConnectorGroups&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of results to return in a single call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listVoiceConnectorGroups(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListVoiceConnectorGroupsResponse**](ListVoiceConnectorGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVoiceConnectorTerminationCredentials

> ListVoiceConnectorTerminationCredentialsResponse listVoiceConnectorTerminationCredentials(voiceConnectorId, opts)



&lt;p&gt;Lists the SIP credentials for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorTerminationCredentials.html\&quot;&gt;ListVoiceConnectorTerminationCredentials&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listVoiceConnectorTerminationCredentials(voiceConnectorId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListVoiceConnectorTerminationCredentialsResponse**](ListVoiceConnectorTerminationCredentialsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVoiceConnectors

> ListVoiceConnectorsResponse listVoiceConnectors(opts)



&lt;p&gt;Lists the Amazon Chime Voice Connectors for the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectors.html\&quot;&gt;ListVoiceConnectors&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token to use to retrieve the next page of results.
  'maxResults': 56, // Number | The maximum number of results to return in a single call.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listVoiceConnectors(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListVoiceConnectorsResponse**](ListVoiceConnectorsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## logoutUser

> Object logoutUser(accountId, userId, operation, opts)



Logs out the specified user from all of the devices they are currently logged into.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let userId = "userId_example"; // String | The user ID.
let operation = "operation_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.logoutUser(accountId, userId, operation, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **userId** | **String**| The user ID. | 
 **operation** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putAppInstanceRetentionSettings

> PutAppInstanceRetentionSettingsResponse putAppInstanceRetentionSettings(appInstanceArn, putAppInstanceRetentionSettingsRequest, opts)



&lt;p&gt;Sets the amount of time in days that a given &lt;code&gt;AppInstance&lt;/code&gt; retains data.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_PutAppInstanceRetentionSettings.html\&quot;&gt;PutAppInstanceRetentionSettings&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let putAppInstanceRetentionSettingsRequest = new AmazonChime.PutAppInstanceRetentionSettingsRequest(); // PutAppInstanceRetentionSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAppInstanceRetentionSettings(appInstanceArn, putAppInstanceRetentionSettingsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **putAppInstanceRetentionSettingsRequest** | [**PutAppInstanceRetentionSettingsRequest**](PutAppInstanceRetentionSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutAppInstanceRetentionSettingsResponse**](PutAppInstanceRetentionSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putAppInstanceStreamingConfigurations

> PutAppInstanceStreamingConfigurationsResponse putAppInstanceStreamingConfigurations(appInstanceArn, putAppInstanceStreamingConfigurationsRequest, opts)



&lt;p&gt;The data streaming configurations of an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutMessagingStreamingConfigurations.html\&quot;&gt;PutMessagingStreamingConfigurations&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let putAppInstanceStreamingConfigurationsRequest = new AmazonChime.PutAppInstanceStreamingConfigurationsRequest(); // PutAppInstanceStreamingConfigurationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAppInstanceStreamingConfigurations(appInstanceArn, putAppInstanceStreamingConfigurationsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **putAppInstanceStreamingConfigurationsRequest** | [**PutAppInstanceStreamingConfigurationsRequest**](PutAppInstanceStreamingConfigurationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutAppInstanceStreamingConfigurationsResponse**](PutAppInstanceStreamingConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putEventsConfiguration

> PutEventsConfigurationResponse putEventsConfiguration(accountId, botId, putEventsConfigurationRequest, opts)



Creates an events configuration that allows a bot to receive outgoing events sent by Amazon Chime. Choose either an HTTPS endpoint or a Lambda function ARN. For more information, see &lt;a&gt;Bot&lt;/a&gt;.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let botId = "botId_example"; // String | The bot ID.
let putEventsConfigurationRequest = new AmazonChime.PutEventsConfigurationRequest(); // PutEventsConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putEventsConfiguration(accountId, botId, putEventsConfigurationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **botId** | **String**| The bot ID. | 
 **putEventsConfigurationRequest** | [**PutEventsConfigurationRequest**](PutEventsConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutEventsConfigurationResponse**](PutEventsConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putRetentionSettings

> PutRetentionSettingsResponse putRetentionSettings(accountId, putRetentionSettingsRequest, opts)



&lt;p&gt; Puts retention settings for the specified Amazon Chime Enterprise account. We recommend using AWS CloudTrail to monitor usage of this API for your account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/cloudtrail.html\&quot;&gt;Logging Amazon Chime API Calls with AWS CloudTrail&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; To turn off existing retention settings, remove the number of days from the corresponding &lt;b&gt;RetentionDays&lt;/b&gt; field in the &lt;b&gt;RetentionSettings&lt;/b&gt; object. For more information about retention settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/chat-retention.html\&quot;&gt;Managing Chat Retention Policies&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let putRetentionSettingsRequest = new AmazonChime.PutRetentionSettingsRequest(); // PutRetentionSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putRetentionSettings(accountId, putRetentionSettingsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **putRetentionSettingsRequest** | [**PutRetentionSettingsRequest**](PutRetentionSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutRetentionSettingsResponse**](PutRetentionSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putSipMediaApplicationLoggingConfiguration

> PutSipMediaApplicationLoggingConfigurationResponse putSipMediaApplicationLoggingConfiguration(sipMediaApplicationId, putSipMediaApplicationLoggingConfigurationRequest, opts)



&lt;p&gt;Updates the logging configuration for the specified SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutSipMediaApplicationLoggingConfiguration.html\&quot;&gt;PutSipMediaApplicationLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The SIP media application ID.
let putSipMediaApplicationLoggingConfigurationRequest = new AmazonChime.PutSipMediaApplicationLoggingConfigurationRequest(); // PutSipMediaApplicationLoggingConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putSipMediaApplicationLoggingConfiguration(sipMediaApplicationId, putSipMediaApplicationLoggingConfigurationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sipMediaApplicationId** | **String**| The SIP media application ID. | 
 **putSipMediaApplicationLoggingConfigurationRequest** | [**PutSipMediaApplicationLoggingConfigurationRequest**](PutSipMediaApplicationLoggingConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutSipMediaApplicationLoggingConfigurationResponse**](PutSipMediaApplicationLoggingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putVoiceConnectorEmergencyCallingConfiguration

> PutVoiceConnectorEmergencyCallingConfigurationResponse putVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, putVoiceConnectorEmergencyCallingConfigurationRequest, opts)



&lt;p&gt;Puts emergency calling configuration details to the specified Amazon Chime Voice Connector, such as emergency phone numbers and calling countries. Origination and termination settings must be enabled for the Amazon Chime Voice Connector before emergency calling can be configured.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorEmergencyCallingConfiguration.html\&quot;&gt;PutVoiceConnectorEmergencyCallingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let putVoiceConnectorEmergencyCallingConfigurationRequest = new AmazonChime.PutVoiceConnectorEmergencyCallingConfigurationRequest(); // PutVoiceConnectorEmergencyCallingConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, putVoiceConnectorEmergencyCallingConfigurationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **putVoiceConnectorEmergencyCallingConfigurationRequest** | [**PutVoiceConnectorEmergencyCallingConfigurationRequest**](PutVoiceConnectorEmergencyCallingConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutVoiceConnectorEmergencyCallingConfigurationResponse**](PutVoiceConnectorEmergencyCallingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putVoiceConnectorLoggingConfiguration

> PutVoiceConnectorLoggingConfigurationResponse putVoiceConnectorLoggingConfiguration(voiceConnectorId, putVoiceConnectorLoggingConfigurationRequest, opts)



&lt;p&gt;Adds a logging configuration for the specified Amazon Chime Voice Connector. The logging configuration specifies whether SIP message logs are enabled for sending to Amazon CloudWatch Logs.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorLoggingConfiguration.html\&quot;&gt;PutVoiceConnectorLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let putVoiceConnectorLoggingConfigurationRequest = new AmazonChime.PutVoiceConnectorLoggingConfigurationRequest(); // PutVoiceConnectorLoggingConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putVoiceConnectorLoggingConfiguration(voiceConnectorId, putVoiceConnectorLoggingConfigurationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **putVoiceConnectorLoggingConfigurationRequest** | [**PutVoiceConnectorLoggingConfigurationRequest**](PutVoiceConnectorLoggingConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutVoiceConnectorLoggingConfigurationResponse**](PutVoiceConnectorLoggingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putVoiceConnectorOrigination

> PutVoiceConnectorOriginationResponse putVoiceConnectorOrigination(voiceConnectorId, putVoiceConnectorOriginationRequest, opts)



&lt;p&gt;Adds origination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to turning off origination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorOrigination.html\&quot;&gt;PutVoiceConnectorOrigination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let putVoiceConnectorOriginationRequest = new AmazonChime.PutVoiceConnectorOriginationRequest(); // PutVoiceConnectorOriginationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putVoiceConnectorOrigination(voiceConnectorId, putVoiceConnectorOriginationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **putVoiceConnectorOriginationRequest** | [**PutVoiceConnectorOriginationRequest**](PutVoiceConnectorOriginationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutVoiceConnectorOriginationResponse**](PutVoiceConnectorOriginationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putVoiceConnectorProxy

> PutVoiceConnectorProxyResponse putVoiceConnectorProxy(voiceConnectorId, putVoiceConnectorProxyRequest, opts)



&lt;p&gt;Puts the specified proxy configuration to the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorProxy.html\&quot;&gt;PutVoiceConnectorProxy&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
let putVoiceConnectorProxyRequest = new AmazonChime.PutVoiceConnectorProxyRequest(); // PutVoiceConnectorProxyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putVoiceConnectorProxy(voiceConnectorId, putVoiceConnectorProxyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | 
 **putVoiceConnectorProxyRequest** | [**PutVoiceConnectorProxyRequest**](PutVoiceConnectorProxyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutVoiceConnectorProxyResponse**](PutVoiceConnectorProxyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putVoiceConnectorStreamingConfiguration

> PutVoiceConnectorStreamingConfigurationResponse putVoiceConnectorStreamingConfiguration(voiceConnectorId, putVoiceConnectorStreamingConfigurationRequest, opts)



&lt;p&gt;Adds a streaming configuration for the specified Amazon Chime Voice Connector. The streaming configuration specifies whether media streaming is enabled for sending to Kinesis. It also sets the retention period, in hours, for the Amazon Kinesis data.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorStreamingConfiguration.html\&quot;&gt;PutVoiceConnectorStreamingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let putVoiceConnectorStreamingConfigurationRequest = new AmazonChime.PutVoiceConnectorStreamingConfigurationRequest(); // PutVoiceConnectorStreamingConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putVoiceConnectorStreamingConfiguration(voiceConnectorId, putVoiceConnectorStreamingConfigurationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **putVoiceConnectorStreamingConfigurationRequest** | [**PutVoiceConnectorStreamingConfigurationRequest**](PutVoiceConnectorStreamingConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutVoiceConnectorStreamingConfigurationResponse**](PutVoiceConnectorStreamingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putVoiceConnectorTermination

> PutVoiceConnectorTerminationResponse putVoiceConnectorTermination(voiceConnectorId, putVoiceConnectorTerminationRequest, opts)



&lt;p&gt;Adds termination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to turning off termination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTermination.html\&quot;&gt;PutVoiceConnectorTermination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let putVoiceConnectorTerminationRequest = new AmazonChime.PutVoiceConnectorTerminationRequest(); // PutVoiceConnectorTerminationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putVoiceConnectorTermination(voiceConnectorId, putVoiceConnectorTerminationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **putVoiceConnectorTerminationRequest** | [**PutVoiceConnectorTerminationRequest**](PutVoiceConnectorTerminationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutVoiceConnectorTerminationResponse**](PutVoiceConnectorTerminationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putVoiceConnectorTerminationCredentials

> putVoiceConnectorTerminationCredentials(voiceConnectorId, operation, putVoiceConnectorTerminationCredentialsRequest, opts)



&lt;p&gt;Adds termination SIP credentials for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTerminationCredentials.html\&quot;&gt;PutVoiceConnectorTerminationCredentials&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let operation = "operation_example"; // String | 
let putVoiceConnectorTerminationCredentialsRequest = new AmazonChime.PutVoiceConnectorTerminationCredentialsRequest(); // PutVoiceConnectorTerminationCredentialsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putVoiceConnectorTerminationCredentials(voiceConnectorId, operation, putVoiceConnectorTerminationCredentialsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **operation** | **String**|  | 
 **putVoiceConnectorTerminationCredentialsRequest** | [**PutVoiceConnectorTerminationCredentialsRequest**](PutVoiceConnectorTerminationCredentialsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## redactChannelMessage

> RedactChannelMessageResponse redactChannelMessage(channelArn, messageId, operation, opts)



&lt;p&gt;Redacts message content, but not metadata. The message exists in the back end, but the action returns null content, and the state shows as redacted.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_RedactChannelMessage.html\&quot;&gt;RedactChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel containing the messages that you want to redact.
let messageId = "messageId_example"; // String | The ID of the message being redacted.
let operation = "operation_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.redactChannelMessage(channelArn, messageId, operation, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel containing the messages that you want to redact. | 
 **messageId** | **String**| The ID of the message being redacted. | 
 **operation** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**RedactChannelMessageResponse**](RedactChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redactConversationMessage

> Object redactConversationMessage(accountId, conversationId, messageId, operation, opts)



Redacts the specified message from the specified Amazon Chime conversation.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let conversationId = "conversationId_example"; // String | The conversation ID.
let messageId = "messageId_example"; // String | The message ID.
let operation = "operation_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.redactConversationMessage(accountId, conversationId, messageId, operation, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **conversationId** | **String**| The conversation ID. | 
 **messageId** | **String**| The message ID. | 
 **operation** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## redactRoomMessage

> Object redactRoomMessage(accountId, roomId, messageId, operation, opts)



Redacts the specified message from the specified Amazon Chime channel.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let roomId = "roomId_example"; // String | The room ID.
let messageId = "messageId_example"; // String | The message ID.
let operation = "operation_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.redactRoomMessage(accountId, roomId, messageId, operation, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **roomId** | **String**| The room ID. | 
 **messageId** | **String**| The message ID. | 
 **operation** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## regenerateSecurityToken

> RegenerateSecurityTokenResponse regenerateSecurityToken(accountId, botId, operation, opts)



Regenerates the security token for a bot.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let botId = "botId_example"; // String | The bot ID.
let operation = "operation_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.regenerateSecurityToken(accountId, botId, operation, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **botId** | **String**| The bot ID. | 
 **operation** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RegenerateSecurityTokenResponse**](RegenerateSecurityTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetPersonalPIN

> ResetPersonalPINResponse resetPersonalPIN(accountId, userId, operation, opts)



Resets the personal meeting PIN for the specified user on an Amazon Chime account. Returns the &lt;a&gt;User&lt;/a&gt; object with the updated personal meeting PIN.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let userId = "userId_example"; // String | The user ID.
let operation = "operation_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.resetPersonalPIN(accountId, userId, operation, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **userId** | **String**| The user ID. | 
 **operation** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ResetPersonalPINResponse**](ResetPersonalPINResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restorePhoneNumber

> RestorePhoneNumberResponse restorePhoneNumber(phoneNumberId, operation, opts)



Moves a phone number from the &lt;b&gt;Deletion queue&lt;/b&gt; back into the phone number &lt;b&gt;Inventory&lt;/b&gt;.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let phoneNumberId = "phoneNumberId_example"; // String | The phone number.
let operation = "operation_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.restorePhoneNumber(phoneNumberId, operation, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumberId** | **String**| The phone number. | 
 **operation** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RestorePhoneNumberResponse**](RestorePhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchAvailablePhoneNumbers

> SearchAvailablePhoneNumbersResponse searchAvailablePhoneNumbers(type, opts)



Searches for phone numbers that can be ordered. For US numbers, provide at least one of the following search filters: &lt;code&gt;AreaCode&lt;/code&gt;, &lt;code&gt;City&lt;/code&gt;, &lt;code&gt;State&lt;/code&gt;, or &lt;code&gt;TollFreePrefix&lt;/code&gt;. If you provide &lt;code&gt;City&lt;/code&gt;, you must also provide &lt;code&gt;State&lt;/code&gt;. Numbers outside the US only support the &lt;code&gt;PhoneNumberType&lt;/code&gt; filter, which you must use.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let type = "type_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'areaCode': "areaCode_example", // String | The area code used to filter results. Only applies to the US.
  'city': "city_example", // String | The city used to filter results. Only applies to the US.
  'country': "country_example", // String | The country used to filter results. Defaults to the US Format: ISO 3166-1 alpha-2.
  'state': "state_example", // String | The state used to filter results. Required only if you provide <code>City</code>. Only applies to the US.
  'tollFreePrefix': "tollFreePrefix_example", // String | The toll-free prefix that you use to filter results. Only applies to the US.
  'phoneNumberType': "phoneNumberType_example", // String | The phone number type used to filter results. Required for non-US numbers.
  'maxResults': 56, // Number | The maximum number of results to return in a single call.
  'nextToken': "nextToken_example", // String | The token used to retrieve the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.searchAvailablePhoneNumbers(type, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **areaCode** | **String**| The area code used to filter results. Only applies to the US. | [optional] 
 **city** | **String**| The city used to filter results. Only applies to the US. | [optional] 
 **country** | **String**| The country used to filter results. Defaults to the US Format: ISO 3166-1 alpha-2. | [optional] 
 **state** | **String**| The state used to filter results. Required only if you provide &lt;code&gt;City&lt;/code&gt;. Only applies to the US. | [optional] 
 **tollFreePrefix** | **String**| The toll-free prefix that you use to filter results. Only applies to the US. | [optional] 
 **phoneNumberType** | **String**| The phone number type used to filter results. Required for non-US numbers. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return in a single call. | [optional] 
 **nextToken** | **String**| The token used to retrieve the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**SearchAvailablePhoneNumbersResponse**](SearchAvailablePhoneNumbersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendChannelMessage

> SendChannelMessageResponse sendChannelMessage(channelArn, sendChannelMessageRequest, opts)



&lt;p&gt;Sends a message to a particular channel that the member is a part of.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;p&gt;Also, &lt;code&gt;STANDARD&lt;/code&gt; messages can contain 4KB of data and the 1KB of metadata. &lt;code&gt;CONTROL&lt;/code&gt; messages can contain 30 bytes of data and no metadata.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SendChannelMessage.html\&quot;&gt;SendChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let sendChannelMessageRequest = new AmazonChime.SendChannelMessageRequest(); // SendChannelMessageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.sendChannelMessage(channelArn, sendChannelMessageRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **sendChannelMessageRequest** | [**SendChannelMessageRequest**](SendChannelMessageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**SendChannelMessageResponse**](SendChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startMeetingTranscription

> Object startMeetingTranscription(meetingId, operation, startMeetingTranscriptionRequest, opts)



&lt;p&gt;Starts transcription for the specified &lt;code&gt;meetingId&lt;/code&gt;. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-transcription.html\&quot;&gt; Using Amazon Chime SDK live transcription &lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify an invalid configuration, a &lt;code&gt;TranscriptFailed&lt;/code&gt; event will be sent with the contents of the &lt;code&gt;BadRequestException&lt;/code&gt; generated by Amazon Transcribe. For more information on each parameter and which combinations are valid, refer to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html\&quot;&gt;StartStreamTranscription&lt;/a&gt; API in the &lt;i&gt;Amazon Transcribe Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Chime SDK live transcription is powered by Amazon Transcribe. Use of Amazon Transcribe is subject to the &lt;a href&#x3D;\&quot;https://aws.amazon.com/service-terms/\&quot;&gt;AWS Service Terms&lt;/a&gt;, including the terms specific to the AWS Machine Learning and Artificial Intelligence Services.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StartMeetingTranscription.html\&quot;&gt;StartMeetingTranscription&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The unique ID of the meeting being transcribed.
let operation = "operation_example"; // String | 
let startMeetingTranscriptionRequest = new AmazonChime.StartMeetingTranscriptionRequest(); // StartMeetingTranscriptionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startMeetingTranscription(meetingId, operation, startMeetingTranscriptionRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The unique ID of the meeting being transcribed. | 
 **operation** | **String**|  | 
 **startMeetingTranscriptionRequest** | [**StartMeetingTranscriptionRequest**](StartMeetingTranscriptionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopMeetingTranscription

> Object stopMeetingTranscription(meetingId, operation, opts)



&lt;p&gt;Stops transcription for the specified &lt;code&gt;meetingId&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StopMeetingTranscription.html\&quot;&gt;StopMeetingTranscription&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The unique ID of the meeting for which you stop transcription.
let operation = "operation_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopMeetingTranscription(meetingId, operation, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The unique ID of the meeting for which you stop transcription. | 
 **operation** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tagAttendee

> tagAttendee(meetingId, attendeeId, operation, tagAttendeeRequest, opts)



&lt;p&gt;Applies the specified tags to the specified Amazon Chime attendee.&lt;/p&gt; &lt;important&gt; &lt;p&gt;TagAttendee is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let attendeeId = "attendeeId_example"; // String | The Amazon Chime SDK attendee ID.
let operation = "operation_example"; // String | 
let tagAttendeeRequest = new AmazonChime.TagAttendeeRequest(); // TagAttendeeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagAttendee(meetingId, attendeeId, operation, tagAttendeeRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **attendeeId** | **String**| The Amazon Chime SDK attendee ID. | 
 **operation** | **String**|  | 
 **tagAttendeeRequest** | [**TagAttendeeRequest**](TagAttendeeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagMeeting

> tagMeeting(meetingId, operation, tagMeetingRequest, opts)



&lt;p&gt;Applies the specified tags to the specified Amazon Chime SDK meeting.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let operation = "operation_example"; // String | 
let tagMeetingRequest = new AmazonChime.TagMeetingRequest(); // TagMeetingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagMeeting(meetingId, operation, tagMeetingRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **operation** | **String**|  | 
 **tagMeetingRequest** | [**TagMeetingRequest**](TagMeetingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> tagResource(operation, tagResourceRequest, opts)



&lt;p&gt;Applies the specified tags to the specified Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let operation = "operation_example"; // String | 
let tagResourceRequest = new AmazonChime.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(operation, tagResourceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **String**|  | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagAttendee

> untagAttendee(meetingId, attendeeId, operation, untagAttendeeRequest, opts)



&lt;p&gt;Untags the specified tags from the specified Amazon Chime SDK attendee.&lt;/p&gt; &lt;important&gt; &lt;p&gt;UntagAttendee is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let attendeeId = "attendeeId_example"; // String | The Amazon Chime SDK attendee ID.
let operation = "operation_example"; // String | 
let untagAttendeeRequest = new AmazonChime.UntagAttendeeRequest(); // UntagAttendeeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagAttendee(meetingId, attendeeId, operation, untagAttendeeRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **attendeeId** | **String**| The Amazon Chime SDK attendee ID. | 
 **operation** | **String**|  | 
 **untagAttendeeRequest** | [**UntagAttendeeRequest**](UntagAttendeeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagMeeting

> untagMeeting(meetingId, operation, untagMeetingRequest, opts)



&lt;p&gt;Untags the specified tags from the specified Amazon Chime SDK meeting.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
let operation = "operation_example"; // String | 
let untagMeetingRequest = new AmazonChime.UntagMeetingRequest(); // UntagMeetingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagMeeting(meetingId, operation, untagMeetingRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meetingId** | **String**| The Amazon Chime SDK meeting ID. | 
 **operation** | **String**|  | 
 **untagMeetingRequest** | [**UntagMeetingRequest**](UntagMeetingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> untagResource(operation, untagResourceRequest, opts)



&lt;p&gt;Untags the specified tags from the specified Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;p&gt;Applies the specified tags to the specified Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let operation = "operation_example"; // String | 
let untagResourceRequest = new AmazonChime.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(operation, untagResourceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation** | **String**|  | 
 **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAccount

> UpdateAccountResponse updateAccount(accountId, updateAccountRequest, opts)



Updates account details for the specified Amazon Chime account. Currently, only account name and default license updates are supported for this action.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let updateAccountRequest = new AmazonChime.UpdateAccountRequest(); // UpdateAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAccount(accountId, updateAccountRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **updateAccountRequest** | [**UpdateAccountRequest**](UpdateAccountRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAccountResponse**](UpdateAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAccountSettings

> Object updateAccountSettings(accountId, updateAccountSettingsRequest, opts)



Updates the settings for the specified Amazon Chime account. You can update settings for remote control of shared screens, or for the dial-out option. For more information about these settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/policies.html\&quot;&gt;Use the Policies Page&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let updateAccountSettingsRequest = new AmazonChime.UpdateAccountSettingsRequest(); // UpdateAccountSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAccountSettings(accountId, updateAccountSettingsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **updateAccountSettingsRequest** | [**UpdateAccountSettingsRequest**](UpdateAccountSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAppInstance

> UpdateAppInstanceResponse updateAppInstance(appInstanceArn, updateAppInstanceRequest, opts)



&lt;p&gt;Updates &lt;code&gt;AppInstance&lt;/code&gt; metadata.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_UpdateAppInstance.html\&quot;&gt;UpdateAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
let updateAppInstanceRequest = new AmazonChime.UpdateAppInstanceRequest(); // UpdateAppInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAppInstance(appInstanceArn, updateAppInstanceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | 
 **updateAppInstanceRequest** | [**UpdateAppInstanceRequest**](UpdateAppInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAppInstanceResponse**](UpdateAppInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAppInstanceUser

> UpdateAppInstanceUserResponse updateAppInstanceUser(appInstanceUserArn, updateAppInstanceUserRequest, opts)



&lt;p&gt;Updates the details of an &lt;code&gt;AppInstanceUser&lt;/code&gt;. You can update names and metadata.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_UpdateAppInstanceUser.html\&quot;&gt;UpdateAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the <code>AppInstanceUser</code>.
let updateAppInstanceUserRequest = new AmazonChime.UpdateAppInstanceUserRequest(); // UpdateAppInstanceUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAppInstanceUser(appInstanceUserArn, updateAppInstanceUserRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appInstanceUserArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;. | 
 **updateAppInstanceUserRequest** | [**UpdateAppInstanceUserRequest**](UpdateAppInstanceUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAppInstanceUserResponse**](UpdateAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBot

> UpdateBotResponse updateBot(accountId, botId, updateBotRequest, opts)



Updates the status of the specified bot, such as starting or stopping the bot from running in your Amazon Chime Enterprise account.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let botId = "botId_example"; // String | The bot ID.
let updateBotRequest = new AmazonChime.UpdateBotRequest(); // UpdateBotRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBot(accountId, botId, updateBotRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **botId** | **String**| The bot ID. | 
 **updateBotRequest** | [**UpdateBotRequest**](UpdateBotRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBotResponse**](UpdateBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannel

> UpdateChannelResponse updateChannel(channelArn, updateChannelRequest, opts)



&lt;p&gt;Update a channel&#39;s attributes.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannel.html\&quot;&gt;UpdateChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let updateChannelRequest = new AmazonChime.UpdateChannelRequest(); // UpdateChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.updateChannel(channelArn, updateChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **updateChannelRequest** | [**UpdateChannelRequest**](UpdateChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**UpdateChannelResponse**](UpdateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannelMessage

> UpdateChannelMessageResponse updateChannelMessage(channelArn, messageId, updateChannelMessageRequest, opts)



&lt;p&gt;Updates the content of a message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelMessage.html\&quot;&gt;UpdateChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let messageId = "messageId_example"; // String | The ID string of the message being updated.
let updateChannelMessageRequest = new AmazonChime.UpdateChannelMessageRequest(); // UpdateChannelMessageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.updateChannelMessage(channelArn, messageId, updateChannelMessageRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **messageId** | **String**| The ID string of the message being updated. | 
 **updateChannelMessageRequest** | [**UpdateChannelMessageRequest**](UpdateChannelMessageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**UpdateChannelMessageResponse**](UpdateChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannelReadMarker

> UpdateChannelReadMarkerResponse updateChannelReadMarker(channelArn, opts)



&lt;p&gt;The details of the time when a user last read messages in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelReadMarker.html\&quot;&gt;UpdateChannelReadMarker&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let channelArn = "channelArn_example"; // String | The ARN of the channel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzChimeBearer': "xAmzChimeBearer_example" // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
};
apiInstance.updateChannelReadMarker(channelArn, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channelArn** | **String**| The ARN of the channel. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] 

### Return type

[**UpdateChannelReadMarkerResponse**](UpdateChannelReadMarkerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateGlobalSettings

> updateGlobalSettings(updateGlobalSettingsRequest, opts)



Updates global settings for the administrator&#39;s AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let updateGlobalSettingsRequest = new AmazonChime.UpdateGlobalSettingsRequest(); // UpdateGlobalSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateGlobalSettings(updateGlobalSettingsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateGlobalSettingsRequest** | [**UpdateGlobalSettingsRequest**](UpdateGlobalSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePhoneNumber

> UpdatePhoneNumberResponse updatePhoneNumber(phoneNumberId, updatePhoneNumberRequest, opts)



&lt;p&gt;Updates phone number details, such as product type or calling name, for the specified phone number ID. You can update one phone number detail at a time. For example, you can update either the product type or the calling name in one action.&lt;/p&gt; &lt;p&gt;For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.&lt;/p&gt; &lt;p&gt;Updates to outbound calling names can take 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.&lt;/p&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let phoneNumberId = "phoneNumberId_example"; // String | The phone number ID.
let updatePhoneNumberRequest = new AmazonChime.UpdatePhoneNumberRequest(); // UpdatePhoneNumberRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePhoneNumber(phoneNumberId, updatePhoneNumberRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumberId** | **String**| The phone number ID. | 
 **updatePhoneNumberRequest** | [**UpdatePhoneNumberRequest**](UpdatePhoneNumberRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdatePhoneNumberResponse**](UpdatePhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePhoneNumberSettings

> updatePhoneNumberSettings(updatePhoneNumberSettingsRequest, opts)



Updates the phone number settings for the administrator&#39;s AWS account, such as the default outbound calling name. You can update the default outbound calling name once every seven days. Outbound calling names can take up to 72 hours to update.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let updatePhoneNumberSettingsRequest = new AmazonChime.UpdatePhoneNumberSettingsRequest(); // UpdatePhoneNumberSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updatePhoneNumberSettings(updatePhoneNumberSettingsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updatePhoneNumberSettingsRequest** | [**UpdatePhoneNumberSettingsRequest**](UpdatePhoneNumberSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProxySession

> UpdateProxySessionResponse updateProxySession(voiceConnectorId, proxySessionId, updateProxySessionRequest, opts)



&lt;p&gt;Updates the specified proxy session details, such as voice or SMS capabilities.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateProxySession.html\&quot;&gt;UpdateProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
let proxySessionId = "proxySessionId_example"; // String | The proxy session ID.
let updateProxySessionRequest = new AmazonChime.UpdateProxySessionRequest(); // UpdateProxySessionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateProxySession(voiceConnectorId, proxySessionId, updateProxySessionRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | 
 **proxySessionId** | **String**| The proxy session ID. | 
 **updateProxySessionRequest** | [**UpdateProxySessionRequest**](UpdateProxySessionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateProxySessionResponse**](UpdateProxySessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoom

> UpdateRoomResponse updateRoom(accountId, roomId, updateRoomRequest, opts)



Updates room details, such as the room name, for a room in an Amazon Chime Enterprise account.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let roomId = "roomId_example"; // String | The room ID.
let updateRoomRequest = new AmazonChime.UpdateRoomRequest(); // UpdateRoomRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRoom(accountId, roomId, updateRoomRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **roomId** | **String**| The room ID. | 
 **updateRoomRequest** | [**UpdateRoomRequest**](UpdateRoomRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateRoomResponse**](UpdateRoomResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRoomMembership

> UpdateRoomMembershipResponse updateRoomMembership(accountId, roomId, memberId, updateRoomMembershipRequest, opts)



Updates room membership details, such as the member role, for a room in an Amazon Chime Enterprise account. The member role designates whether the member is a chat room administrator or a general chat room member. The member role can be updated only for user IDs.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let roomId = "roomId_example"; // String | The room ID.
let memberId = "memberId_example"; // String | The member ID.
let updateRoomMembershipRequest = new AmazonChime.UpdateRoomMembershipRequest(); // UpdateRoomMembershipRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRoomMembership(accountId, roomId, memberId, updateRoomMembershipRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **roomId** | **String**| The room ID. | 
 **memberId** | **String**| The member ID. | 
 **updateRoomMembershipRequest** | [**UpdateRoomMembershipRequest**](UpdateRoomMembershipRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateRoomMembershipResponse**](UpdateRoomMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSipMediaApplication

> UpdateSipMediaApplicationResponse updateSipMediaApplication(sipMediaApplicationId, updateSipMediaApplicationRequest, opts)



&lt;p&gt;Updates the details of the specified SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplication.html\&quot;&gt;UpdateSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The SIP media application ID.
let updateSipMediaApplicationRequest = new AmazonChime.UpdateSipMediaApplicationRequest(); // UpdateSipMediaApplicationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSipMediaApplication(sipMediaApplicationId, updateSipMediaApplicationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sipMediaApplicationId** | **String**| The SIP media application ID. | 
 **updateSipMediaApplicationRequest** | [**UpdateSipMediaApplicationRequest**](UpdateSipMediaApplicationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSipMediaApplicationResponse**](UpdateSipMediaApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSipMediaApplicationCall

> UpdateSipMediaApplicationCallResponse updateSipMediaApplicationCall(sipMediaApplicationId, transactionId, updateSipMediaApplicationCallRequest, opts)



&lt;p&gt;Invokes the AWS Lambda function associated with the SIP media application and transaction ID in an update request. The Lambda function can then return a new set of actions.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplicationCall.html\&quot;&gt;UpdateSipMediaApplicationCall&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The ID of the SIP media application handling the call.
let transactionId = "transactionId_example"; // String | The ID of the call transaction.
let updateSipMediaApplicationCallRequest = new AmazonChime.UpdateSipMediaApplicationCallRequest(); // UpdateSipMediaApplicationCallRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSipMediaApplicationCall(sipMediaApplicationId, transactionId, updateSipMediaApplicationCallRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sipMediaApplicationId** | **String**| The ID of the SIP media application handling the call. | 
 **transactionId** | **String**| The ID of the call transaction. | 
 **updateSipMediaApplicationCallRequest** | [**UpdateSipMediaApplicationCallRequest**](UpdateSipMediaApplicationCallRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSipMediaApplicationCallResponse**](UpdateSipMediaApplicationCallResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSipRule

> UpdateSipRuleResponse updateSipRule(sipRuleId, updateSipRuleRequest, opts)



&lt;p&gt;Updates the details of the specified SIP rule.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipRule.html\&quot;&gt;UpdateSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let sipRuleId = "sipRuleId_example"; // String | The SIP rule ID.
let updateSipRuleRequest = new AmazonChime.UpdateSipRuleRequest(); // UpdateSipRuleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSipRule(sipRuleId, updateSipRuleRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sipRuleId** | **String**| The SIP rule ID. | 
 **updateSipRuleRequest** | [**UpdateSipRuleRequest**](UpdateSipRuleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSipRuleResponse**](UpdateSipRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUser

> UpdateUserResponse updateUser(accountId, userId, updateUserRequest, opts)



Updates user details for a specified user ID. Currently, only &lt;code&gt;LicenseType&lt;/code&gt; updates are supported for this action.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let userId = "userId_example"; // String | The user ID.
let updateUserRequest = new AmazonChime.UpdateUserRequest(); // UpdateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUser(accountId, userId, updateUserRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **userId** | **String**| The user ID. | 
 **updateUserRequest** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateUserResponse**](UpdateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateUserSettings

> updateUserSettings(accountId, userId, updateUserSettingsRequest, opts)



Updates the settings for the specified user, such as phone number settings.

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let accountId = "accountId_example"; // String | The Amazon Chime account ID.
let userId = "userId_example"; // String | The user ID.
let updateUserSettingsRequest = new AmazonChime.UpdateUserSettingsRequest(); // UpdateUserSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateUserSettings(accountId, userId, updateUserSettingsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accountId** | **String**| The Amazon Chime account ID. | 
 **userId** | **String**| The user ID. | 
 **updateUserSettingsRequest** | [**UpdateUserSettingsRequest**](UpdateUserSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVoiceConnector

> UpdateVoiceConnectorResponse updateVoiceConnector(voiceConnectorId, updateVoiceConnectorRequest, opts)



&lt;p&gt;Updates details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnector.html\&quot;&gt;UpdateVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
let updateVoiceConnectorRequest = new AmazonChime.UpdateVoiceConnectorRequest(); // UpdateVoiceConnectorRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVoiceConnector(voiceConnectorId, updateVoiceConnectorRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | 
 **updateVoiceConnectorRequest** | [**UpdateVoiceConnectorRequest**](UpdateVoiceConnectorRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateVoiceConnectorResponse**](UpdateVoiceConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVoiceConnectorGroup

> UpdateVoiceConnectorGroupResponse updateVoiceConnectorGroup(voiceConnectorGroupId, updateVoiceConnectorGroupRequest, opts)



&lt;p&gt;Updates details of the specified Amazon Chime Voice Connector group, such as the name and Amazon Chime Voice Connector priority ranking.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnectorGroup.html\&quot;&gt;UpdateVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let voiceConnectorGroupId = "voiceConnectorGroupId_example"; // String | The Amazon Chime Voice Connector group ID.
let updateVoiceConnectorGroupRequest = new AmazonChime.UpdateVoiceConnectorGroupRequest(); // UpdateVoiceConnectorGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVoiceConnectorGroup(voiceConnectorGroupId, updateVoiceConnectorGroupRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voiceConnectorGroupId** | **String**| The Amazon Chime Voice Connector group ID. | 
 **updateVoiceConnectorGroupRequest** | [**UpdateVoiceConnectorGroupRequest**](UpdateVoiceConnectorGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateVoiceConnectorGroupResponse**](UpdateVoiceConnectorGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## validateE911Address

> ValidateE911AddressResponse validateE911Address(validateE911AddressRequest, opts)



&lt;p&gt;Validates an address to be used for 911 calls made with Amazon Chime Voice Connectors. You can use validated addresses in a Presence Information Data Format Location Object file that you include in SIP requests. That helps ensure that addresses are routed to the appropriate Public Safety Answering Point.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ValidateE911Address.html\&quot;&gt;ValidateE911Address&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonChime from 'amazon_chime';
let defaultClient = AmazonChime.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonChime.DefaultApi();
let validateE911AddressRequest = new AmazonChime.ValidateE911AddressRequest(); // ValidateE911AddressRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.validateE911Address(validateE911AddressRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validateE911AddressRequest** | [**ValidateE911AddressRequest**](ValidateE911AddressRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ValidateE911AddressResponse**](ValidateE911AddressResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

