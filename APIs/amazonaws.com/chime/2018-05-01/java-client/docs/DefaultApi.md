# DefaultApi

All URIs are relative to *http://service.chime.aws.amazon.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**associatePhoneNumberWithUser**](DefaultApi.md#associatePhoneNumberWithUser) | **POST** /accounts/{accountId}/users/{userId}#operation&#x3D;associate-phone-number |  |
| [**associatePhoneNumbersWithVoiceConnector**](DefaultApi.md#associatePhoneNumbersWithVoiceConnector) | **POST** /voice-connectors/{voiceConnectorId}#operation&#x3D;associate-phone-numbers |  |
| [**associatePhoneNumbersWithVoiceConnectorGroup**](DefaultApi.md#associatePhoneNumbersWithVoiceConnectorGroup) | **POST** /voice-connector-groups/{voiceConnectorGroupId}#operation&#x3D;associate-phone-numbers |  |
| [**associateSigninDelegateGroupsWithAccount**](DefaultApi.md#associateSigninDelegateGroupsWithAccount) | **POST** /accounts/{accountId}#operation&#x3D;associate-signin-delegate-groups |  |
| [**batchCreateAttendee**](DefaultApi.md#batchCreateAttendee) | **POST** /meetings/{meetingId}/attendees#operation&#x3D;batch-create |  |
| [**batchCreateChannelMembership**](DefaultApi.md#batchCreateChannelMembership) | **POST** /channels/{channelArn}/memberships#operation&#x3D;batch-create |  |
| [**batchCreateRoomMembership**](DefaultApi.md#batchCreateRoomMembership) | **POST** /accounts/{accountId}/rooms/{roomId}/memberships#operation&#x3D;batch-create |  |
| [**batchDeletePhoneNumber**](DefaultApi.md#batchDeletePhoneNumber) | **POST** /phone-numbers#operation&#x3D;batch-delete |  |
| [**batchSuspendUser**](DefaultApi.md#batchSuspendUser) | **POST** /accounts/{accountId}/users#operation&#x3D;suspend |  |
| [**batchUnsuspendUser**](DefaultApi.md#batchUnsuspendUser) | **POST** /accounts/{accountId}/users#operation&#x3D;unsuspend |  |
| [**batchUpdatePhoneNumber**](DefaultApi.md#batchUpdatePhoneNumber) | **POST** /phone-numbers#operation&#x3D;batch-update |  |
| [**batchUpdateUser**](DefaultApi.md#batchUpdateUser) | **POST** /accounts/{accountId}/users |  |
| [**createAccount**](DefaultApi.md#createAccount) | **POST** /accounts |  |
| [**createAppInstance**](DefaultApi.md#createAppInstance) | **POST** /app-instances |  |
| [**createAppInstanceAdmin**](DefaultApi.md#createAppInstanceAdmin) | **POST** /app-instances/{appInstanceArn}/admins |  |
| [**createAppInstanceUser**](DefaultApi.md#createAppInstanceUser) | **POST** /app-instance-users |  |
| [**createAttendee**](DefaultApi.md#createAttendee) | **POST** /meetings/{meetingId}/attendees |  |
| [**createBot**](DefaultApi.md#createBot) | **POST** /accounts/{accountId}/bots |  |
| [**createChannel**](DefaultApi.md#createChannel) | **POST** /channels |  |
| [**createChannelBan**](DefaultApi.md#createChannelBan) | **POST** /channels/{channelArn}/bans |  |
| [**createChannelMembership**](DefaultApi.md#createChannelMembership) | **POST** /channels/{channelArn}/memberships |  |
| [**createChannelModerator**](DefaultApi.md#createChannelModerator) | **POST** /channels/{channelArn}/moderators |  |
| [**createMediaCapturePipeline**](DefaultApi.md#createMediaCapturePipeline) | **POST** /media-capture-pipelines |  |
| [**createMeeting**](DefaultApi.md#createMeeting) | **POST** /meetings |  |
| [**createMeetingDialOut**](DefaultApi.md#createMeetingDialOut) | **POST** /meetings/{meetingId}/dial-outs |  |
| [**createMeetingWithAttendees**](DefaultApi.md#createMeetingWithAttendees) | **POST** /meetings#operation&#x3D;create-attendees |  |
| [**createPhoneNumberOrder**](DefaultApi.md#createPhoneNumberOrder) | **POST** /phone-number-orders |  |
| [**createProxySession**](DefaultApi.md#createProxySession) | **POST** /voice-connectors/{voiceConnectorId}/proxy-sessions |  |
| [**createRoom**](DefaultApi.md#createRoom) | **POST** /accounts/{accountId}/rooms |  |
| [**createRoomMembership**](DefaultApi.md#createRoomMembership) | **POST** /accounts/{accountId}/rooms/{roomId}/memberships |  |
| [**createSipMediaApplication**](DefaultApi.md#createSipMediaApplication) | **POST** /sip-media-applications |  |
| [**createSipMediaApplicationCall**](DefaultApi.md#createSipMediaApplicationCall) | **POST** /sip-media-applications/{sipMediaApplicationId}/calls |  |
| [**createSipRule**](DefaultApi.md#createSipRule) | **POST** /sip-rules |  |
| [**createUser**](DefaultApi.md#createUser) | **POST** /accounts/{accountId}/users#operation&#x3D;create |  |
| [**createVoiceConnector**](DefaultApi.md#createVoiceConnector) | **POST** /voice-connectors |  |
| [**createVoiceConnectorGroup**](DefaultApi.md#createVoiceConnectorGroup) | **POST** /voice-connector-groups |  |
| [**deleteAccount**](DefaultApi.md#deleteAccount) | **DELETE** /accounts/{accountId} |  |
| [**deleteAppInstance**](DefaultApi.md#deleteAppInstance) | **DELETE** /app-instances/{appInstanceArn} |  |
| [**deleteAppInstanceAdmin**](DefaultApi.md#deleteAppInstanceAdmin) | **DELETE** /app-instances/{appInstanceArn}/admins/{appInstanceAdminArn} |  |
| [**deleteAppInstanceStreamingConfigurations**](DefaultApi.md#deleteAppInstanceStreamingConfigurations) | **DELETE** /app-instances/{appInstanceArn}/streaming-configurations |  |
| [**deleteAppInstanceUser**](DefaultApi.md#deleteAppInstanceUser) | **DELETE** /app-instance-users/{appInstanceUserArn} |  |
| [**deleteAttendee**](DefaultApi.md#deleteAttendee) | **DELETE** /meetings/{meetingId}/attendees/{attendeeId} |  |
| [**deleteChannel**](DefaultApi.md#deleteChannel) | **DELETE** /channels/{channelArn} |  |
| [**deleteChannelBan**](DefaultApi.md#deleteChannelBan) | **DELETE** /channels/{channelArn}/bans/{memberArn} |  |
| [**deleteChannelMembership**](DefaultApi.md#deleteChannelMembership) | **DELETE** /channels/{channelArn}/memberships/{memberArn} |  |
| [**deleteChannelMessage**](DefaultApi.md#deleteChannelMessage) | **DELETE** /channels/{channelArn}/messages/{messageId} |  |
| [**deleteChannelModerator**](DefaultApi.md#deleteChannelModerator) | **DELETE** /channels/{channelArn}/moderators/{channelModeratorArn} |  |
| [**deleteEventsConfiguration**](DefaultApi.md#deleteEventsConfiguration) | **DELETE** /accounts/{accountId}/bots/{botId}/events-configuration |  |
| [**deleteMediaCapturePipeline**](DefaultApi.md#deleteMediaCapturePipeline) | **DELETE** /media-capture-pipelines/{mediaPipelineId} |  |
| [**deleteMeeting**](DefaultApi.md#deleteMeeting) | **DELETE** /meetings/{meetingId} |  |
| [**deletePhoneNumber**](DefaultApi.md#deletePhoneNumber) | **DELETE** /phone-numbers/{phoneNumberId} |  |
| [**deleteProxySession**](DefaultApi.md#deleteProxySession) | **DELETE** /voice-connectors/{voiceConnectorId}/proxy-sessions/{proxySessionId} |  |
| [**deleteRoom**](DefaultApi.md#deleteRoom) | **DELETE** /accounts/{accountId}/rooms/{roomId} |  |
| [**deleteRoomMembership**](DefaultApi.md#deleteRoomMembership) | **DELETE** /accounts/{accountId}/rooms/{roomId}/memberships/{memberId} |  |
| [**deleteSipMediaApplication**](DefaultApi.md#deleteSipMediaApplication) | **DELETE** /sip-media-applications/{sipMediaApplicationId} |  |
| [**deleteSipRule**](DefaultApi.md#deleteSipRule) | **DELETE** /sip-rules/{sipRuleId} |  |
| [**deleteVoiceConnector**](DefaultApi.md#deleteVoiceConnector) | **DELETE** /voice-connectors/{voiceConnectorId} |  |
| [**deleteVoiceConnectorEmergencyCallingConfiguration**](DefaultApi.md#deleteVoiceConnectorEmergencyCallingConfiguration) | **DELETE** /voice-connectors/{voiceConnectorId}/emergency-calling-configuration |  |
| [**deleteVoiceConnectorGroup**](DefaultApi.md#deleteVoiceConnectorGroup) | **DELETE** /voice-connector-groups/{voiceConnectorGroupId} |  |
| [**deleteVoiceConnectorOrigination**](DefaultApi.md#deleteVoiceConnectorOrigination) | **DELETE** /voice-connectors/{voiceConnectorId}/origination |  |
| [**deleteVoiceConnectorProxy**](DefaultApi.md#deleteVoiceConnectorProxy) | **DELETE** /voice-connectors/{voiceConnectorId}/programmable-numbers/proxy |  |
| [**deleteVoiceConnectorStreamingConfiguration**](DefaultApi.md#deleteVoiceConnectorStreamingConfiguration) | **DELETE** /voice-connectors/{voiceConnectorId}/streaming-configuration |  |
| [**deleteVoiceConnectorTermination**](DefaultApi.md#deleteVoiceConnectorTermination) | **DELETE** /voice-connectors/{voiceConnectorId}/termination |  |
| [**deleteVoiceConnectorTerminationCredentials**](DefaultApi.md#deleteVoiceConnectorTerminationCredentials) | **POST** /voice-connectors/{voiceConnectorId}/termination/credentials#operation&#x3D;delete |  |
| [**describeAppInstance**](DefaultApi.md#describeAppInstance) | **GET** /app-instances/{appInstanceArn} |  |
| [**describeAppInstanceAdmin**](DefaultApi.md#describeAppInstanceAdmin) | **GET** /app-instances/{appInstanceArn}/admins/{appInstanceAdminArn} |  |
| [**describeAppInstanceUser**](DefaultApi.md#describeAppInstanceUser) | **GET** /app-instance-users/{appInstanceUserArn} |  |
| [**describeChannel**](DefaultApi.md#describeChannel) | **GET** /channels/{channelArn} |  |
| [**describeChannelBan**](DefaultApi.md#describeChannelBan) | **GET** /channels/{channelArn}/bans/{memberArn} |  |
| [**describeChannelMembership**](DefaultApi.md#describeChannelMembership) | **GET** /channels/{channelArn}/memberships/{memberArn} |  |
| [**describeChannelMembershipForAppInstanceUser**](DefaultApi.md#describeChannelMembershipForAppInstanceUser) | **GET** /channels/{channelArn}#scope&#x3D;app-instance-user-membership&amp;app-instance-user-arn |  |
| [**describeChannelModeratedByAppInstanceUser**](DefaultApi.md#describeChannelModeratedByAppInstanceUser) | **GET** /channels/{channelArn}#scope&#x3D;app-instance-user-moderated-channel&amp;app-instance-user-arn |  |
| [**describeChannelModerator**](DefaultApi.md#describeChannelModerator) | **GET** /channels/{channelArn}/moderators/{channelModeratorArn} |  |
| [**disassociatePhoneNumberFromUser**](DefaultApi.md#disassociatePhoneNumberFromUser) | **POST** /accounts/{accountId}/users/{userId}#operation&#x3D;disassociate-phone-number |  |
| [**disassociatePhoneNumbersFromVoiceConnector**](DefaultApi.md#disassociatePhoneNumbersFromVoiceConnector) | **POST** /voice-connectors/{voiceConnectorId}#operation&#x3D;disassociate-phone-numbers |  |
| [**disassociatePhoneNumbersFromVoiceConnectorGroup**](DefaultApi.md#disassociatePhoneNumbersFromVoiceConnectorGroup) | **POST** /voice-connector-groups/{voiceConnectorGroupId}#operation&#x3D;disassociate-phone-numbers |  |
| [**disassociateSigninDelegateGroupsFromAccount**](DefaultApi.md#disassociateSigninDelegateGroupsFromAccount) | **POST** /accounts/{accountId}#operation&#x3D;disassociate-signin-delegate-groups |  |
| [**getAccount**](DefaultApi.md#getAccount) | **GET** /accounts/{accountId} |  |
| [**getAccountSettings**](DefaultApi.md#getAccountSettings) | **GET** /accounts/{accountId}/settings |  |
| [**getAppInstanceRetentionSettings**](DefaultApi.md#getAppInstanceRetentionSettings) | **GET** /app-instances/{appInstanceArn}/retention-settings |  |
| [**getAppInstanceStreamingConfigurations**](DefaultApi.md#getAppInstanceStreamingConfigurations) | **GET** /app-instances/{appInstanceArn}/streaming-configurations |  |
| [**getAttendee**](DefaultApi.md#getAttendee) | **GET** /meetings/{meetingId}/attendees/{attendeeId} |  |
| [**getBot**](DefaultApi.md#getBot) | **GET** /accounts/{accountId}/bots/{botId} |  |
| [**getChannelMessage**](DefaultApi.md#getChannelMessage) | **GET** /channels/{channelArn}/messages/{messageId} |  |
| [**getEventsConfiguration**](DefaultApi.md#getEventsConfiguration) | **GET** /accounts/{accountId}/bots/{botId}/events-configuration |  |
| [**getGlobalSettings**](DefaultApi.md#getGlobalSettings) | **GET** /settings |  |
| [**getMediaCapturePipeline**](DefaultApi.md#getMediaCapturePipeline) | **GET** /media-capture-pipelines/{mediaPipelineId} |  |
| [**getMeeting**](DefaultApi.md#getMeeting) | **GET** /meetings/{meetingId} |  |
| [**getMessagingSessionEndpoint**](DefaultApi.md#getMessagingSessionEndpoint) | **GET** /endpoints/messaging-session |  |
| [**getPhoneNumber**](DefaultApi.md#getPhoneNumber) | **GET** /phone-numbers/{phoneNumberId} |  |
| [**getPhoneNumberOrder**](DefaultApi.md#getPhoneNumberOrder) | **GET** /phone-number-orders/{phoneNumberOrderId} |  |
| [**getPhoneNumberSettings**](DefaultApi.md#getPhoneNumberSettings) | **GET** /settings/phone-number |  |
| [**getProxySession**](DefaultApi.md#getProxySession) | **GET** /voice-connectors/{voiceConnectorId}/proxy-sessions/{proxySessionId} |  |
| [**getRetentionSettings**](DefaultApi.md#getRetentionSettings) | **GET** /accounts/{accountId}/retention-settings |  |
| [**getRoom**](DefaultApi.md#getRoom) | **GET** /accounts/{accountId}/rooms/{roomId} |  |
| [**getSipMediaApplication**](DefaultApi.md#getSipMediaApplication) | **GET** /sip-media-applications/{sipMediaApplicationId} |  |
| [**getSipMediaApplicationLoggingConfiguration**](DefaultApi.md#getSipMediaApplicationLoggingConfiguration) | **GET** /sip-media-applications/{sipMediaApplicationId}/logging-configuration |  |
| [**getSipRule**](DefaultApi.md#getSipRule) | **GET** /sip-rules/{sipRuleId} |  |
| [**getUser**](DefaultApi.md#getUser) | **GET** /accounts/{accountId}/users/{userId} |  |
| [**getUserSettings**](DefaultApi.md#getUserSettings) | **GET** /accounts/{accountId}/users/{userId}/settings |  |
| [**getVoiceConnector**](DefaultApi.md#getVoiceConnector) | **GET** /voice-connectors/{voiceConnectorId} |  |
| [**getVoiceConnectorEmergencyCallingConfiguration**](DefaultApi.md#getVoiceConnectorEmergencyCallingConfiguration) | **GET** /voice-connectors/{voiceConnectorId}/emergency-calling-configuration |  |
| [**getVoiceConnectorGroup**](DefaultApi.md#getVoiceConnectorGroup) | **GET** /voice-connector-groups/{voiceConnectorGroupId} |  |
| [**getVoiceConnectorLoggingConfiguration**](DefaultApi.md#getVoiceConnectorLoggingConfiguration) | **GET** /voice-connectors/{voiceConnectorId}/logging-configuration |  |
| [**getVoiceConnectorOrigination**](DefaultApi.md#getVoiceConnectorOrigination) | **GET** /voice-connectors/{voiceConnectorId}/origination |  |
| [**getVoiceConnectorProxy**](DefaultApi.md#getVoiceConnectorProxy) | **GET** /voice-connectors/{voiceConnectorId}/programmable-numbers/proxy |  |
| [**getVoiceConnectorStreamingConfiguration**](DefaultApi.md#getVoiceConnectorStreamingConfiguration) | **GET** /voice-connectors/{voiceConnectorId}/streaming-configuration |  |
| [**getVoiceConnectorTermination**](DefaultApi.md#getVoiceConnectorTermination) | **GET** /voice-connectors/{voiceConnectorId}/termination |  |
| [**getVoiceConnectorTerminationHealth**](DefaultApi.md#getVoiceConnectorTerminationHealth) | **GET** /voice-connectors/{voiceConnectorId}/termination/health |  |
| [**inviteUsers**](DefaultApi.md#inviteUsers) | **POST** /accounts/{accountId}/users#operation&#x3D;add |  |
| [**listAccounts**](DefaultApi.md#listAccounts) | **GET** /accounts |  |
| [**listAppInstanceAdmins**](DefaultApi.md#listAppInstanceAdmins) | **GET** /app-instances/{appInstanceArn}/admins |  |
| [**listAppInstanceUsers**](DefaultApi.md#listAppInstanceUsers) | **GET** /app-instance-users#app-instance-arn |  |
| [**listAppInstances**](DefaultApi.md#listAppInstances) | **GET** /app-instances |  |
| [**listAttendeeTags**](DefaultApi.md#listAttendeeTags) | **GET** /meetings/{meetingId}/attendees/{attendeeId}/tags |  |
| [**listAttendees**](DefaultApi.md#listAttendees) | **GET** /meetings/{meetingId}/attendees |  |
| [**listBots**](DefaultApi.md#listBots) | **GET** /accounts/{accountId}/bots |  |
| [**listChannelBans**](DefaultApi.md#listChannelBans) | **GET** /channels/{channelArn}/bans |  |
| [**listChannelMemberships**](DefaultApi.md#listChannelMemberships) | **GET** /channels/{channelArn}/memberships |  |
| [**listChannelMembershipsForAppInstanceUser**](DefaultApi.md#listChannelMembershipsForAppInstanceUser) | **GET** /channels#scope&#x3D;app-instance-user-memberships |  |
| [**listChannelMessages**](DefaultApi.md#listChannelMessages) | **GET** /channels/{channelArn}/messages |  |
| [**listChannelModerators**](DefaultApi.md#listChannelModerators) | **GET** /channels/{channelArn}/moderators |  |
| [**listChannels**](DefaultApi.md#listChannels) | **GET** /channels#app-instance-arn |  |
| [**listChannelsModeratedByAppInstanceUser**](DefaultApi.md#listChannelsModeratedByAppInstanceUser) | **GET** /channels#scope&#x3D;app-instance-user-moderated-channels |  |
| [**listMediaCapturePipelines**](DefaultApi.md#listMediaCapturePipelines) | **GET** /media-capture-pipelines |  |
| [**listMeetingTags**](DefaultApi.md#listMeetingTags) | **GET** /meetings/{meetingId}/tags |  |
| [**listMeetings**](DefaultApi.md#listMeetings) | **GET** /meetings |  |
| [**listPhoneNumberOrders**](DefaultApi.md#listPhoneNumberOrders) | **GET** /phone-number-orders |  |
| [**listPhoneNumbers**](DefaultApi.md#listPhoneNumbers) | **GET** /phone-numbers |  |
| [**listProxySessions**](DefaultApi.md#listProxySessions) | **GET** /voice-connectors/{voiceConnectorId}/proxy-sessions |  |
| [**listRoomMemberships**](DefaultApi.md#listRoomMemberships) | **GET** /accounts/{accountId}/rooms/{roomId}/memberships |  |
| [**listRooms**](DefaultApi.md#listRooms) | **GET** /accounts/{accountId}/rooms |  |
| [**listSipMediaApplications**](DefaultApi.md#listSipMediaApplications) | **GET** /sip-media-applications |  |
| [**listSipRules**](DefaultApi.md#listSipRules) | **GET** /sip-rules |  |
| [**listSupportedPhoneNumberCountries**](DefaultApi.md#listSupportedPhoneNumberCountries) | **GET** /phone-number-countries#product-type |  |
| [**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags#arn |  |
| [**listUsers**](DefaultApi.md#listUsers) | **GET** /accounts/{accountId}/users |  |
| [**listVoiceConnectorGroups**](DefaultApi.md#listVoiceConnectorGroups) | **GET** /voice-connector-groups |  |
| [**listVoiceConnectorTerminationCredentials**](DefaultApi.md#listVoiceConnectorTerminationCredentials) | **GET** /voice-connectors/{voiceConnectorId}/termination/credentials |  |
| [**listVoiceConnectors**](DefaultApi.md#listVoiceConnectors) | **GET** /voice-connectors |  |
| [**logoutUser**](DefaultApi.md#logoutUser) | **POST** /accounts/{accountId}/users/{userId}#operation&#x3D;logout |  |
| [**putAppInstanceRetentionSettings**](DefaultApi.md#putAppInstanceRetentionSettings) | **PUT** /app-instances/{appInstanceArn}/retention-settings |  |
| [**putAppInstanceStreamingConfigurations**](DefaultApi.md#putAppInstanceStreamingConfigurations) | **PUT** /app-instances/{appInstanceArn}/streaming-configurations |  |
| [**putEventsConfiguration**](DefaultApi.md#putEventsConfiguration) | **PUT** /accounts/{accountId}/bots/{botId}/events-configuration |  |
| [**putRetentionSettings**](DefaultApi.md#putRetentionSettings) | **PUT** /accounts/{accountId}/retention-settings |  |
| [**putSipMediaApplicationLoggingConfiguration**](DefaultApi.md#putSipMediaApplicationLoggingConfiguration) | **PUT** /sip-media-applications/{sipMediaApplicationId}/logging-configuration |  |
| [**putVoiceConnectorEmergencyCallingConfiguration**](DefaultApi.md#putVoiceConnectorEmergencyCallingConfiguration) | **PUT** /voice-connectors/{voiceConnectorId}/emergency-calling-configuration |  |
| [**putVoiceConnectorLoggingConfiguration**](DefaultApi.md#putVoiceConnectorLoggingConfiguration) | **PUT** /voice-connectors/{voiceConnectorId}/logging-configuration |  |
| [**putVoiceConnectorOrigination**](DefaultApi.md#putVoiceConnectorOrigination) | **PUT** /voice-connectors/{voiceConnectorId}/origination |  |
| [**putVoiceConnectorProxy**](DefaultApi.md#putVoiceConnectorProxy) | **PUT** /voice-connectors/{voiceConnectorId}/programmable-numbers/proxy |  |
| [**putVoiceConnectorStreamingConfiguration**](DefaultApi.md#putVoiceConnectorStreamingConfiguration) | **PUT** /voice-connectors/{voiceConnectorId}/streaming-configuration |  |
| [**putVoiceConnectorTermination**](DefaultApi.md#putVoiceConnectorTermination) | **PUT** /voice-connectors/{voiceConnectorId}/termination |  |
| [**putVoiceConnectorTerminationCredentials**](DefaultApi.md#putVoiceConnectorTerminationCredentials) | **POST** /voice-connectors/{voiceConnectorId}/termination/credentials#operation&#x3D;put |  |
| [**redactChannelMessage**](DefaultApi.md#redactChannelMessage) | **POST** /channels/{channelArn}/messages/{messageId}#operation&#x3D;redact |  |
| [**redactConversationMessage**](DefaultApi.md#redactConversationMessage) | **POST** /accounts/{accountId}/conversations/{conversationId}/messages/{messageId}#operation&#x3D;redact |  |
| [**redactRoomMessage**](DefaultApi.md#redactRoomMessage) | **POST** /accounts/{accountId}/rooms/{roomId}/messages/{messageId}#operation&#x3D;redact |  |
| [**regenerateSecurityToken**](DefaultApi.md#regenerateSecurityToken) | **POST** /accounts/{accountId}/bots/{botId}#operation&#x3D;regenerate-security-token |  |
| [**resetPersonalPIN**](DefaultApi.md#resetPersonalPIN) | **POST** /accounts/{accountId}/users/{userId}#operation&#x3D;reset-personal-pin |  |
| [**restorePhoneNumber**](DefaultApi.md#restorePhoneNumber) | **POST** /phone-numbers/{phoneNumberId}#operation&#x3D;restore |  |
| [**searchAvailablePhoneNumbers**](DefaultApi.md#searchAvailablePhoneNumbers) | **GET** /search#type&#x3D;phone-numbers |  |
| [**sendChannelMessage**](DefaultApi.md#sendChannelMessage) | **POST** /channels/{channelArn}/messages |  |
| [**startMeetingTranscription**](DefaultApi.md#startMeetingTranscription) | **POST** /meetings/{meetingId}/transcription#operation&#x3D;start |  |
| [**stopMeetingTranscription**](DefaultApi.md#stopMeetingTranscription) | **POST** /meetings/{meetingId}/transcription#operation&#x3D;stop |  |
| [**tagAttendee**](DefaultApi.md#tagAttendee) | **POST** /meetings/{meetingId}/attendees/{attendeeId}/tags#operation&#x3D;add |  |
| [**tagMeeting**](DefaultApi.md#tagMeeting) | **POST** /meetings/{meetingId}/tags#operation&#x3D;add |  |
| [**tagResource**](DefaultApi.md#tagResource) | **POST** /tags#operation&#x3D;tag-resource |  |
| [**untagAttendee**](DefaultApi.md#untagAttendee) | **POST** /meetings/{meetingId}/attendees/{attendeeId}/tags#operation&#x3D;delete |  |
| [**untagMeeting**](DefaultApi.md#untagMeeting) | **POST** /meetings/{meetingId}/tags#operation&#x3D;delete |  |
| [**untagResource**](DefaultApi.md#untagResource) | **POST** /tags#operation&#x3D;untag-resource |  |
| [**updateAccount**](DefaultApi.md#updateAccount) | **POST** /accounts/{accountId} |  |
| [**updateAccountSettings**](DefaultApi.md#updateAccountSettings) | **PUT** /accounts/{accountId}/settings |  |
| [**updateAppInstance**](DefaultApi.md#updateAppInstance) | **PUT** /app-instances/{appInstanceArn} |  |
| [**updateAppInstanceUser**](DefaultApi.md#updateAppInstanceUser) | **PUT** /app-instance-users/{appInstanceUserArn} |  |
| [**updateBot**](DefaultApi.md#updateBot) | **POST** /accounts/{accountId}/bots/{botId} |  |
| [**updateChannel**](DefaultApi.md#updateChannel) | **PUT** /channels/{channelArn} |  |
| [**updateChannelMessage**](DefaultApi.md#updateChannelMessage) | **PUT** /channels/{channelArn}/messages/{messageId} |  |
| [**updateChannelReadMarker**](DefaultApi.md#updateChannelReadMarker) | **PUT** /channels/{channelArn}/readMarker |  |
| [**updateGlobalSettings**](DefaultApi.md#updateGlobalSettings) | **PUT** /settings |  |
| [**updatePhoneNumber**](DefaultApi.md#updatePhoneNumber) | **POST** /phone-numbers/{phoneNumberId} |  |
| [**updatePhoneNumberSettings**](DefaultApi.md#updatePhoneNumberSettings) | **PUT** /settings/phone-number |  |
| [**updateProxySession**](DefaultApi.md#updateProxySession) | **POST** /voice-connectors/{voiceConnectorId}/proxy-sessions/{proxySessionId} |  |
| [**updateRoom**](DefaultApi.md#updateRoom) | **POST** /accounts/{accountId}/rooms/{roomId} |  |
| [**updateRoomMembership**](DefaultApi.md#updateRoomMembership) | **POST** /accounts/{accountId}/rooms/{roomId}/memberships/{memberId} |  |
| [**updateSipMediaApplication**](DefaultApi.md#updateSipMediaApplication) | **PUT** /sip-media-applications/{sipMediaApplicationId} |  |
| [**updateSipMediaApplicationCall**](DefaultApi.md#updateSipMediaApplicationCall) | **POST** /sip-media-applications/{sipMediaApplicationId}/calls/{transactionId} |  |
| [**updateSipRule**](DefaultApi.md#updateSipRule) | **PUT** /sip-rules/{sipRuleId} |  |
| [**updateUser**](DefaultApi.md#updateUser) | **POST** /accounts/{accountId}/users/{userId} |  |
| [**updateUserSettings**](DefaultApi.md#updateUserSettings) | **PUT** /accounts/{accountId}/users/{userId}/settings |  |
| [**updateVoiceConnector**](DefaultApi.md#updateVoiceConnector) | **PUT** /voice-connectors/{voiceConnectorId} |  |
| [**updateVoiceConnectorGroup**](DefaultApi.md#updateVoiceConnectorGroup) | **PUT** /voice-connector-groups/{voiceConnectorGroupId} |  |
| [**validateE911Address**](DefaultApi.md#validateE911Address) | **POST** /emergency-calling/address |  |


<a id="associatePhoneNumberWithUser"></a>
# **associatePhoneNumberWithUser**
> Object associatePhoneNumberWithUser(accountId, userId, operation, associatePhoneNumberWithUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Associates a phone number with the specified Amazon Chime user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String userId = "userId_example"; // String | The user ID.
    String operation = "associate-phone-number"; // String | 
    AssociatePhoneNumberWithUserRequest associatePhoneNumberWithUserRequest = new AssociatePhoneNumberWithUserRequest(); // AssociatePhoneNumberWithUserRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.associatePhoneNumberWithUser(accountId, userId, operation, associatePhoneNumberWithUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associatePhoneNumberWithUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **userId** | **String**| The user ID. | |
| **operation** | **String**|  | [enum: associate-phone-number] |
| **associatePhoneNumberWithUserRequest** | [**AssociatePhoneNumberWithUserRequest**](AssociatePhoneNumberWithUserRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | AccessDeniedException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="associatePhoneNumbersWithVoiceConnector"></a>
# **associatePhoneNumbersWithVoiceConnector**
> AssociatePhoneNumbersWithVoiceConnectorResponse associatePhoneNumbersWithVoiceConnector(voiceConnectorId, operation, associatePhoneNumbersWithVoiceConnectorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Associates phone numbers with the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnector.html\&quot;&gt;AssociatePhoneNumbersWithVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String operation = "associate-phone-numbers"; // String | 
    AssociatePhoneNumbersWithVoiceConnectorRequest associatePhoneNumbersWithVoiceConnectorRequest = new AssociatePhoneNumbersWithVoiceConnectorRequest(); // AssociatePhoneNumbersWithVoiceConnectorRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AssociatePhoneNumbersWithVoiceConnectorResponse result = apiInstance.associatePhoneNumbersWithVoiceConnector(voiceConnectorId, operation, associatePhoneNumbersWithVoiceConnectorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associatePhoneNumbersWithVoiceConnector");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **operation** | **String**|  | [enum: associate-phone-numbers] |
| **associatePhoneNumbersWithVoiceConnectorRequest** | [**AssociatePhoneNumbersWithVoiceConnectorRequest**](AssociatePhoneNumbersWithVoiceConnectorRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AssociatePhoneNumbersWithVoiceConnectorResponse**](AssociatePhoneNumbersWithVoiceConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | AccessDeniedException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="associatePhoneNumbersWithVoiceConnectorGroup"></a>
# **associatePhoneNumbersWithVoiceConnectorGroup**
> AssociatePhoneNumbersWithVoiceConnectorGroupResponse associatePhoneNumbersWithVoiceConnectorGroup(voiceConnectorGroupId, operation, associatePhoneNumbersWithVoiceConnectorGroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Associates phone numbers with the specified Amazon Chime Voice Connector group.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_AssociatePhoneNumbersWithVoiceConnectorGroup.html\&quot;&gt;AssociatePhoneNumbersWithVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorGroupId = "voiceConnectorGroupId_example"; // String | The Amazon Chime Voice Connector group ID.
    String operation = "associate-phone-numbers"; // String | 
    AssociatePhoneNumbersWithVoiceConnectorGroupRequest associatePhoneNumbersWithVoiceConnectorGroupRequest = new AssociatePhoneNumbersWithVoiceConnectorGroupRequest(); // AssociatePhoneNumbersWithVoiceConnectorGroupRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      AssociatePhoneNumbersWithVoiceConnectorGroupResponse result = apiInstance.associatePhoneNumbersWithVoiceConnectorGroup(voiceConnectorGroupId, operation, associatePhoneNumbersWithVoiceConnectorGroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associatePhoneNumbersWithVoiceConnectorGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorGroupId** | **String**| The Amazon Chime Voice Connector group ID. | |
| **operation** | **String**|  | [enum: associate-phone-numbers] |
| **associatePhoneNumbersWithVoiceConnectorGroupRequest** | [**AssociatePhoneNumbersWithVoiceConnectorGroupRequest**](AssociatePhoneNumbersWithVoiceConnectorGroupRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**AssociatePhoneNumbersWithVoiceConnectorGroupResponse**](AssociatePhoneNumbersWithVoiceConnectorGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | AccessDeniedException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="associateSigninDelegateGroupsWithAccount"></a>
# **associateSigninDelegateGroupsWithAccount**
> Object associateSigninDelegateGroupsWithAccount(accountId, operation, associateSigninDelegateGroupsWithAccountRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Associates the specified sign-in delegate groups with the specified Amazon Chime account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String operation = "associate-signin-delegate-groups"; // String | 
    AssociateSigninDelegateGroupsWithAccountRequest associateSigninDelegateGroupsWithAccountRequest = new AssociateSigninDelegateGroupsWithAccountRequest(); // AssociateSigninDelegateGroupsWithAccountRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.associateSigninDelegateGroupsWithAccount(accountId, operation, associateSigninDelegateGroupsWithAccountRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#associateSigninDelegateGroupsWithAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **operation** | **String**|  | [enum: associate-signin-delegate-groups] |
| **associateSigninDelegateGroupsWithAccountRequest** | [**AssociateSigninDelegateGroupsWithAccountRequest**](AssociateSigninDelegateGroupsWithAccountRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="batchCreateAttendee"></a>
# **batchCreateAttendee**
> BatchCreateAttendeeResponse batchCreateAttendee(meetingId, operation, batchCreateAttendeeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates up to 100 new attendees for an active Amazon Chime SDK meeting.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_BatchCreateAttendee.html\&quot;&gt;BatchCreateAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String operation = "batch-create"; // String | 
    BatchCreateAttendeeRequest batchCreateAttendeeRequest = new BatchCreateAttendeeRequest(); // BatchCreateAttendeeRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchCreateAttendeeResponse result = apiInstance.batchCreateAttendee(meetingId, operation, batchCreateAttendeeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchCreateAttendee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **operation** | **String**|  | [enum: batch-create] |
| **batchCreateAttendeeRequest** | [**BatchCreateAttendeeRequest**](BatchCreateAttendeeRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchCreateAttendeeResponse**](BatchCreateAttendeeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | ResourceLimitExceededException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | UnauthorizedClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="batchCreateChannelMembership"></a>
# **batchCreateChannelMembership**
> BatchCreateChannelMembershipResponse batchCreateChannelMembership(channelArn, operation, batchCreateChannelMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Adds a specified number of users to a channel.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_BatchCreateChannelMembership.html\&quot;&gt;BatchCreateChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel to which you're adding users.
    String operation = "batch-create"; // String | 
    BatchCreateChannelMembershipRequest batchCreateChannelMembershipRequest = new BatchCreateChannelMembershipRequest(); // BatchCreateChannelMembershipRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      BatchCreateChannelMembershipResponse result = apiInstance.batchCreateChannelMembership(channelArn, operation, batchCreateChannelMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchCreateChannelMembership");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel to which you&#39;re adding users. | |
| **operation** | **String**|  | [enum: batch-create] |
| **batchCreateChannelMembershipRequest** | [**BatchCreateChannelMembershipRequest**](BatchCreateChannelMembershipRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**BatchCreateChannelMembershipResponse**](BatchCreateChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceFailureException |  -  |
| **481** | ServiceUnavailableException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ThrottledClientException |  -  |

<a id="batchCreateRoomMembership"></a>
# **batchCreateRoomMembership**
> BatchCreateRoomMembershipResponse batchCreateRoomMembership(accountId, roomId, operation, batchCreateRoomMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Adds up to 50 members to a chat room in an Amazon Chime Enterprise account. Members can be users or bots. The member role designates whether the member is a chat room administrator or a general chat room member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String roomId = "roomId_example"; // String | The room ID.
    String operation = "batch-create"; // String | 
    BatchCreateRoomMembershipRequest batchCreateRoomMembershipRequest = new BatchCreateRoomMembershipRequest(); // BatchCreateRoomMembershipRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchCreateRoomMembershipResponse result = apiInstance.batchCreateRoomMembership(accountId, roomId, operation, batchCreateRoomMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchCreateRoomMembership");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **roomId** | **String**| The room ID. | |
| **operation** | **String**|  | [enum: batch-create] |
| **batchCreateRoomMembershipRequest** | [**BatchCreateRoomMembershipRequest**](BatchCreateRoomMembershipRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchCreateRoomMembershipResponse**](BatchCreateRoomMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="batchDeletePhoneNumber"></a>
# **batchDeletePhoneNumber**
> BatchDeletePhoneNumberResponse batchDeletePhoneNumber(operation, batchDeletePhoneNumberRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Moves phone numbers into the &lt;b&gt;Deletion queue&lt;/b&gt;. Phone numbers must be disassociated from any users or Amazon Chime Voice Connectors before they can be deleted. &lt;/p&gt; &lt;p&gt; Phone numbers remain in the &lt;b&gt;Deletion queue&lt;/b&gt; for 7 days before they are deleted permanently. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operation = "batch-delete"; // String | 
    BatchDeletePhoneNumberRequest batchDeletePhoneNumberRequest = new BatchDeletePhoneNumberRequest(); // BatchDeletePhoneNumberRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchDeletePhoneNumberResponse result = apiInstance.batchDeletePhoneNumber(operation, batchDeletePhoneNumberRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchDeletePhoneNumber");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **operation** | **String**|  | [enum: batch-delete] |
| **batchDeletePhoneNumberRequest** | [**BatchDeletePhoneNumberRequest**](BatchDeletePhoneNumberRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchDeletePhoneNumberResponse**](BatchDeletePhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="batchSuspendUser"></a>
# **batchSuspendUser**
> BatchSuspendUserResponse batchSuspendUser(accountId, operation, batchSuspendUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Suspends up to 50 users from a &lt;code&gt;Team&lt;/code&gt; or &lt;code&gt;EnterpriseLWA&lt;/code&gt; Amazon Chime account. For more information about different account types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\&quot;&gt;Managing Your Amazon Chime Accounts&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Users suspended from a &lt;code&gt;Team&lt;/code&gt; account are disassociated from the account,but they can continue to use Amazon Chime as free users. To remove the suspension from suspended &lt;code&gt;Team&lt;/code&gt; account users, invite them to the &lt;code&gt;Team&lt;/code&gt; account again. You can use the &lt;a&gt;InviteUsers&lt;/a&gt; action to do so.&lt;/p&gt; &lt;p&gt;Users suspended from an &lt;code&gt;EnterpriseLWA&lt;/code&gt; account are immediately signed out of Amazon Chime and can no longer sign in. To remove the suspension from suspended &lt;code&gt;EnterpriseLWA&lt;/code&gt; account users, use the &lt;a&gt;BatchUnsuspendUser&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt; To sign out users without suspending them, use the &lt;a&gt;LogoutUser&lt;/a&gt; action.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String operation = "suspend"; // String | 
    BatchSuspendUserRequest batchSuspendUserRequest = new BatchSuspendUserRequest(); // BatchSuspendUserRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchSuspendUserResponse result = apiInstance.batchSuspendUser(accountId, operation, batchSuspendUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchSuspendUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **operation** | **String**|  | [enum: suspend] |
| **batchSuspendUserRequest** | [**BatchSuspendUserRequest**](BatchSuspendUserRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchSuspendUserResponse**](BatchSuspendUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="batchUnsuspendUser"></a>
# **batchUnsuspendUser**
> BatchUnsuspendUserResponse batchUnsuspendUser(accountId, operation, batchUnsuspendUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Removes the suspension from up to 50 previously suspended users for the specified Amazon Chime &lt;code&gt;EnterpriseLWA&lt;/code&gt; account. Only users on &lt;code&gt;EnterpriseLWA&lt;/code&gt; accounts can be unsuspended using this action. For more information about different account types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\&quot;&gt; Managing Your Amazon Chime Accounts &lt;/a&gt; in the account types, in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;Previously suspended users who are unsuspended using this action are returned to &lt;code&gt;Registered&lt;/code&gt; status. Users who are not previously suspended are ignored.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String operation = "unsuspend"; // String | 
    BatchUnsuspendUserRequest batchUnsuspendUserRequest = new BatchUnsuspendUserRequest(); // BatchUnsuspendUserRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchUnsuspendUserResponse result = apiInstance.batchUnsuspendUser(accountId, operation, batchUnsuspendUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchUnsuspendUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **operation** | **String**|  | [enum: unsuspend] |
| **batchUnsuspendUserRequest** | [**BatchUnsuspendUserRequest**](BatchUnsuspendUserRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchUnsuspendUserResponse**](BatchUnsuspendUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="batchUpdatePhoneNumber"></a>
# **batchUpdatePhoneNumber**
> BatchUpdatePhoneNumberResponse batchUpdatePhoneNumber(operation, batchUpdatePhoneNumberRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates phone number product types or calling names. You can update one attribute at a time for each &lt;code&gt;UpdatePhoneNumberRequestItem&lt;/code&gt;. For example, you can update the product type or the calling name.&lt;/p&gt; &lt;p&gt;For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.&lt;/p&gt; &lt;p&gt;Updates to outbound calling names can take up to 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operation = "batch-update"; // String | 
    BatchUpdatePhoneNumberRequest batchUpdatePhoneNumberRequest = new BatchUpdatePhoneNumberRequest(); // BatchUpdatePhoneNumberRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchUpdatePhoneNumberResponse result = apiInstance.batchUpdatePhoneNumber(operation, batchUpdatePhoneNumberRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchUpdatePhoneNumber");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **operation** | **String**|  | [enum: batch-update] |
| **batchUpdatePhoneNumberRequest** | [**BatchUpdatePhoneNumberRequest**](BatchUpdatePhoneNumberRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchUpdatePhoneNumberResponse**](BatchUpdatePhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="batchUpdateUser"></a>
# **batchUpdateUser**
> BatchUpdateUserResponse batchUpdateUser(accountId, batchUpdateUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates user details within the &lt;a&gt;UpdateUserRequestItem&lt;/a&gt; object for up to 20 users for the specified Amazon Chime account. Currently, only &lt;code&gt;LicenseType&lt;/code&gt; updates are supported for this action.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    BatchUpdateUserRequest batchUpdateUserRequest = new BatchUpdateUserRequest(); // BatchUpdateUserRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      BatchUpdateUserResponse result = apiInstance.batchUpdateUser(accountId, batchUpdateUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#batchUpdateUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **batchUpdateUserRequest** | [**BatchUpdateUserRequest**](BatchUpdateUserRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**BatchUpdateUserResponse**](BatchUpdateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="createAccount"></a>
# **createAccount**
> CreateAccountResponse createAccount(createAccountRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates an Amazon Chime account under the administrator&#39;s AWS account. Only &lt;code&gt;Team&lt;/code&gt; account types are currently supported for this action. For more information about different account types, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html\&quot;&gt;Managing Your Amazon Chime Accounts&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAccountRequest createAccountRequest = new CreateAccountRequest(); // CreateAccountRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateAccountResponse result = apiInstance.createAccount(createAccountRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAccountRequest** | [**CreateAccountRequest**](CreateAccountRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateAccountResponse**](CreateAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="createAppInstance"></a>
# **createAppInstance**
> CreateAppInstanceResponse createAppInstance(createAppInstanceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an Amazon Chime SDK messaging &lt;code&gt;AppInstance&lt;/code&gt; under an AWS account. Only SDK messaging customers use this API. &lt;code&gt;CreateAppInstance&lt;/code&gt; supports idempotency behavior as described in the AWS API Standard.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_CreateAppInstance.html\&quot;&gt;CreateAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAppInstanceRequest createAppInstanceRequest = new CreateAppInstanceRequest(); // CreateAppInstanceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateAppInstanceResponse result = apiInstance.createAppInstance(createAppInstanceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAppInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAppInstanceRequest** | [**CreateAppInstanceRequest**](CreateAppInstanceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateAppInstanceResponse**](CreateAppInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | ResourceLimitExceededException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | UnauthorizedClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createAppInstanceAdmin"></a>
# **createAppInstanceAdmin**
> CreateAppInstanceAdminResponse createAppInstanceAdmin(appInstanceArn, createAppInstanceAdminRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Promotes an &lt;code&gt;AppInstanceUser&lt;/code&gt; to an &lt;code&gt;AppInstanceAdmin&lt;/code&gt;. The promoted user can perform the following actions. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_CreateAppInstanceAdmin.html\&quot;&gt;CreateAppInstanceAdmin&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ChannelModerator&lt;/code&gt; actions across all channels in the &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DeleteChannelMessage&lt;/code&gt; actions.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Only an &lt;code&gt;AppInstanceUser&lt;/code&gt; can be promoted to an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; role.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    CreateAppInstanceAdminRequest createAppInstanceAdminRequest = new CreateAppInstanceAdminRequest(); // CreateAppInstanceAdminRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateAppInstanceAdminResponse result = apiInstance.createAppInstanceAdmin(appInstanceArn, createAppInstanceAdminRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAppInstanceAdmin");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **createAppInstanceAdminRequest** | [**CreateAppInstanceAdminRequest**](CreateAppInstanceAdminRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateAppInstanceAdminResponse**](CreateAppInstanceAdminResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | ResourceLimitExceededException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | UnauthorizedClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createAppInstanceUser"></a>
# **createAppInstanceUser**
> CreateAppInstanceUserResponse createAppInstanceUser(createAppInstanceUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a user under an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;. The request consists of a unique &lt;code&gt;appInstanceUserId&lt;/code&gt; and &lt;code&gt;Name&lt;/code&gt; for that user.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_CreateAppInstanceUser.html\&quot;&gt;CreateAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateAppInstanceUserRequest createAppInstanceUserRequest = new CreateAppInstanceUserRequest(); // CreateAppInstanceUserRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateAppInstanceUserResponse result = apiInstance.createAppInstanceUser(createAppInstanceUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAppInstanceUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createAppInstanceUserRequest** | [**CreateAppInstanceUserRequest**](CreateAppInstanceUserRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateAppInstanceUserResponse**](CreateAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | ResourceLimitExceededException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | UnauthorizedClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createAttendee"></a>
# **createAttendee**
> CreateAttendeeResponse createAttendee(meetingId, createAttendeeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Creates a new attendee for an active Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateAttendee.html\&quot;&gt;CreateAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    CreateAttendeeRequest createAttendeeRequest = new CreateAttendeeRequest(); // CreateAttendeeRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateAttendeeResponse result = apiInstance.createAttendee(meetingId, createAttendeeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createAttendee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **createAttendeeRequest** | [**CreateAttendeeRequest**](CreateAttendeeRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateAttendeeResponse**](CreateAttendeeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | ResourceLimitExceededException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | UnauthorizedClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createBot"></a>
# **createBot**
> CreateBotResponse createBot(accountId, createBotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a bot for an Amazon Chime Enterprise account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    CreateBotRequest createBotRequest = new CreateBotRequest(); // CreateBotRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateBotResponse result = apiInstance.createBot(accountId, createBotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createBot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **createBotRequest** | [**CreateBotRequest**](CreateBotRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateBotResponse**](CreateBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceFailureException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ResourceLimitExceededException |  -  |
| **486** | NotFoundException |  -  |
| **487** | ThrottledClientException |  -  |

<a id="createChannel"></a>
# **createChannel**
> CreateChannelResponse createChannel(createChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Creates a channel to which you can add users and send messages.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannel.html\&quot;&gt;CreateChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateChannelRequest createChannelRequest = new CreateChannelRequest(); // CreateChannelRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      CreateChannelResponse result = apiInstance.createChannel(createChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createChannel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createChannelRequest** | [**CreateChannelRequest**](CreateChannelRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**CreateChannelResponse**](CreateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ResourceLimitExceededException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createChannelBan"></a>
# **createChannelBan**
> CreateChannelBanResponse createChannelBan(channelArn, createChannelBanRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Permanently bans a member from a channel. Moderators can&#39;t add banned members to a channel. To undo a ban, you first have to &lt;code&gt;DeleteChannelBan&lt;/code&gt;, and then &lt;code&gt;CreateChannelMembership&lt;/code&gt;. Bans are cleaned up when you delete users or channels.&lt;/p&gt; &lt;p&gt;If you ban a user who is already part of a channel, that user is automatically kicked from the channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelBan.html\&quot;&gt;CreateChannelBan&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the ban request.
    CreateChannelBanRequest createChannelBanRequest = new CreateChannelBanRequest(); // CreateChannelBanRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      CreateChannelBanResponse result = apiInstance.createChannelBan(channelArn, createChannelBanRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createChannelBan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the ban request. | |
| **createChannelBanRequest** | [**CreateChannelBanRequest**](CreateChannelBanRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**CreateChannelBanResponse**](CreateChannelBanResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ResourceLimitExceededException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createChannelMembership"></a>
# **createChannelMembership**
> CreateChannelMembershipResponse createChannelMembership(channelArn, createChannelMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Adds a user to a channel. The &lt;code&gt;InvitedBy&lt;/code&gt; response field is derived from the request header. A channel member can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Send messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Receive messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Edit their own messages&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Leave the channel&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Privacy settings impact this action as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Public Channels: You do not need to be a member to list messages, but you must be a member to send messages.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Private Channels: You must be a member to list or send messages.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelMembership.html\&quot;&gt;CreateChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel to which you're adding users.
    CreateChannelMembershipRequest createChannelMembershipRequest = new CreateChannelMembershipRequest(); // CreateChannelMembershipRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      CreateChannelMembershipResponse result = apiInstance.createChannelMembership(channelArn, createChannelMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createChannelMembership");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel to which you&#39;re adding users. | |
| **createChannelMembershipRequest** | [**CreateChannelMembershipRequest**](CreateChannelMembershipRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**CreateChannelMembershipResponse**](CreateChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ResourceLimitExceededException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createChannelModerator"></a>
# **createChannelModerator**
> CreateChannelModeratorResponse createChannelModerator(channelArn, createChannelModeratorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Creates a new &lt;code&gt;ChannelModerator&lt;/code&gt;. A channel moderator can:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Add and remove other members of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove other moderators of the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add and remove user bans for the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Redact messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List messages in the channel.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_CreateChannelModerator.html\&quot;&gt;CreateChannelModerator&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    CreateChannelModeratorRequest createChannelModeratorRequest = new CreateChannelModeratorRequest(); // CreateChannelModeratorRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      CreateChannelModeratorResponse result = apiInstance.createChannelModerator(channelArn, createChannelModeratorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createChannelModerator");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **createChannelModeratorRequest** | [**CreateChannelModeratorRequest**](CreateChannelModeratorRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**CreateChannelModeratorResponse**](CreateChannelModeratorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ResourceLimitExceededException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createMediaCapturePipeline"></a>
# **createMediaCapturePipeline**
> CreateMediaCapturePipelineResponse createMediaCapturePipeline(createMediaCapturePipelineRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a media capture pipeline.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_CreateMediaCapturePipeline\&quot;&gt;CreateMediaCapturePipeline&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateMediaCapturePipelineRequest createMediaCapturePipelineRequest = new CreateMediaCapturePipelineRequest(); // CreateMediaCapturePipelineRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateMediaCapturePipelineResponse result = apiInstance.createMediaCapturePipeline(createMediaCapturePipelineRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createMediaCapturePipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createMediaCapturePipelineRequest** | [**CreateMediaCapturePipelineRequest**](CreateMediaCapturePipelineRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateMediaCapturePipelineResponse**](CreateMediaCapturePipelineResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | ResourceLimitExceededException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="createMeeting"></a>
# **createMeeting**
> CreateMeetingResponse createMeeting(createMeetingRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a new Amazon Chime SDK meeting in the specified media Region with no initial attendees. For more information about specifying media Regions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/chime-sdk-meetings-regions.html\&quot;&gt;Amazon Chime SDK Media Regions&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html\&quot;&gt;CreateMeeting&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateMeetingRequest createMeetingRequest = new CreateMeetingRequest(); // CreateMeetingRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateMeetingResponse result = apiInstance.createMeeting(createMeetingRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createMeeting");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createMeetingRequest** | [**CreateMeetingRequest**](CreateMeetingRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateMeetingResponse**](CreateMeetingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ResourceLimitExceededException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="createMeetingDialOut"></a>
# **createMeetingDialOut**
> CreateMeetingDialOutResponse createMeetingDialOut(meetingId, createMeetingDialOutRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Uses the join token and call metadata in a meeting request (From number, To number, and so forth) to initiate an outbound call to a public switched telephone network (PSTN) and join them into a Chime meeting. Also ensures that the From number belongs to the customer.&lt;/p&gt; &lt;p&gt;To play welcome audio or implement an interactive voice response (IVR), use the &lt;code&gt;CreateSipMediaApplicationCall&lt;/code&gt; action with the corresponding SIP media application ID.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is not available in a dedicated namespace.&lt;/b&gt; &lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    CreateMeetingDialOutRequest createMeetingDialOutRequest = new CreateMeetingDialOutRequest(); // CreateMeetingDialOutRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateMeetingDialOutResponse result = apiInstance.createMeetingDialOut(meetingId, createMeetingDialOutRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createMeetingDialOut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **createMeetingDialOutRequest** | [**CreateMeetingDialOutRequest**](CreateMeetingDialOutRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateMeetingDialOutResponse**](CreateMeetingDialOutResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ResourceLimitExceededException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createMeetingWithAttendees"></a>
# **createMeetingWithAttendees**
> CreateMeetingWithAttendeesResponse createMeetingWithAttendees(operation, createMeetingWithAttendeesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Creates a new Amazon Chime SDK meeting in the specified media Region, with attendees. For more information about specifying media Regions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/chime-sdk-meetings-regions.html\&quot;&gt;Amazon Chime SDK Media Regions&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeetingWithAttendees.html\&quot;&gt;CreateMeetingWithAttendees&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operation = "create-attendees"; // String | 
    CreateMeetingWithAttendeesRequest createMeetingWithAttendeesRequest = new CreateMeetingWithAttendeesRequest(); // CreateMeetingWithAttendeesRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateMeetingWithAttendeesResponse result = apiInstance.createMeetingWithAttendees(operation, createMeetingWithAttendeesRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createMeetingWithAttendees");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **operation** | **String**|  | [enum: create-attendees] |
| **createMeetingWithAttendeesRequest** | [**CreateMeetingWithAttendeesRequest**](CreateMeetingWithAttendeesRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateMeetingWithAttendeesResponse**](CreateMeetingWithAttendeesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ResourceLimitExceededException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="createPhoneNumberOrder"></a>
# **createPhoneNumberOrder**
> CreatePhoneNumberOrderResponse createPhoneNumberOrder(createPhoneNumberOrderRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates an order for phone numbers to be provisioned. For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreatePhoneNumberOrderRequest createPhoneNumberOrderRequest = new CreatePhoneNumberOrderRequest(); // CreatePhoneNumberOrderRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreatePhoneNumberOrderResponse result = apiInstance.createPhoneNumberOrder(createPhoneNumberOrderRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createPhoneNumberOrder");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createPhoneNumberOrderRequest** | [**CreatePhoneNumberOrderRequest**](CreatePhoneNumberOrderRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreatePhoneNumberOrderResponse**](CreatePhoneNumberOrderResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | AccessDeniedException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ResourceLimitExceededException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createProxySession"></a>
# **createProxySession**
> CreateProxySessionResponse createProxySession(voiceConnectorId, createProxySessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a proxy session on the specified Amazon Chime Voice Connector for the specified participant phone numbers.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateProxySession.html\&quot;&gt;CreateProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
    CreateProxySessionRequest createProxySessionRequest = new CreateProxySessionRequest(); // CreateProxySessionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateProxySessionResponse result = apiInstance.createProxySession(voiceConnectorId, createProxySessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createProxySession");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | |
| **createProxySessionRequest** | [**CreateProxySessionRequest**](CreateProxySessionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateProxySessionResponse**](CreateProxySessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="createRoom"></a>
# **createRoom**
> CreateRoomResponse createRoom(accountId, createRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a chat room for the specified Amazon Chime Enterprise account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    CreateRoomRequest createRoomRequest = new CreateRoomRequest(); // CreateRoomRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateRoomResponse result = apiInstance.createRoom(accountId, createRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createRoom");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **createRoomRequest** | [**CreateRoomRequest**](CreateRoomRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateRoomResponse**](CreateRoomResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ResourceLimitExceededException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createRoomMembership"></a>
# **createRoomMembership**
> CreateRoomMembershipResponse createRoomMembership(accountId, roomId, createRoomMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Adds a member to a chat room in an Amazon Chime Enterprise account. A member can be either a user or a bot. The member role designates whether the member is a chat room administrator or a general chat room member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String roomId = "roomId_example"; // String | The room ID.
    CreateRoomMembershipRequest createRoomMembershipRequest = new CreateRoomMembershipRequest(); // CreateRoomMembershipRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateRoomMembershipResponse result = apiInstance.createRoomMembership(accountId, roomId, createRoomMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createRoomMembership");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **roomId** | **String**| The room ID. | |
| **createRoomMembershipRequest** | [**CreateRoomMembershipRequest**](CreateRoomMembershipRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateRoomMembershipResponse**](CreateRoomMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | ConflictException |  -  |
| **481** | UnauthorizedClientException |  -  |
| **482** | NotFoundException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ForbiddenException |  -  |
| **485** | ResourceLimitExceededException |  -  |
| **486** | ThrottledClientException |  -  |
| **487** | ServiceUnavailableException |  -  |
| **488** | ServiceFailureException |  -  |

<a id="createSipMediaApplication"></a>
# **createSipMediaApplication**
> CreateSipMediaApplicationResponse createSipMediaApplication(createSipMediaApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplication.html\&quot;&gt;CreateSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateSipMediaApplicationRequest createSipMediaApplicationRequest = new CreateSipMediaApplicationRequest(); // CreateSipMediaApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateSipMediaApplicationResponse result = apiInstance.createSipMediaApplication(createSipMediaApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createSipMediaApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createSipMediaApplicationRequest** | [**CreateSipMediaApplicationRequest**](CreateSipMediaApplicationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateSipMediaApplicationResponse**](CreateSipMediaApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | AccessDeniedException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ResourceLimitExceededException |  -  |
| **486** | ConflictException |  -  |
| **487** | ServiceUnavailableException |  -  |
| **488** | ServiceFailureException |  -  |

<a id="createSipMediaApplicationCall"></a>
# **createSipMediaApplicationCall**
> CreateSipMediaApplicationCallResponse createSipMediaApplicationCall(sipMediaApplicationId, createSipMediaApplicationCallRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an outbound call to a phone number from the phone number specified in the request, and it invokes the endpoint of the specified &lt;code&gt;sipMediaApplicationId&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipMediaApplicationCall.html\&quot;&gt;CreateSipMediaApplicationCall&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The ID of the SIP media application.
    CreateSipMediaApplicationCallRequest createSipMediaApplicationCallRequest = new CreateSipMediaApplicationCallRequest(); // CreateSipMediaApplicationCallRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateSipMediaApplicationCallResponse result = apiInstance.createSipMediaApplicationCall(sipMediaApplicationId, createSipMediaApplicationCallRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createSipMediaApplicationCall");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sipMediaApplicationId** | **String**| The ID of the SIP media application. | |
| **createSipMediaApplicationCallRequest** | [**CreateSipMediaApplicationCallRequest**](CreateSipMediaApplicationCallRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateSipMediaApplicationCallResponse**](CreateSipMediaApplicationCallResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ResourceLimitExceededException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | AccessDeniedException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createSipRule"></a>
# **createSipRule**
> CreateSipRuleResponse createSipRule(createSipRuleRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates a SIP rule which can be used to run a SIP media application as a target for a specific trigger type.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateSipRule.html\&quot;&gt;CreateSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateSipRuleRequest createSipRuleRequest = new CreateSipRuleRequest(); // CreateSipRuleRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateSipRuleResponse result = apiInstance.createSipRule(createSipRuleRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createSipRule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createSipRuleRequest** | [**CreateSipRuleRequest**](CreateSipRuleRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateSipRuleResponse**](CreateSipRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | AccessDeniedException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ResourceLimitExceededException |  -  |
| **486** | ConflictException |  -  |
| **487** | ServiceUnavailableException |  -  |
| **488** | ServiceFailureException |  -  |

<a id="createUser"></a>
# **createUser**
> CreateUserResponse createUser(accountId, operation, createUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates a user under the specified Amazon Chime account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String operation = "create"; // String | 
    CreateUserRequest createUserRequest = new CreateUserRequest(); // CreateUserRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateUserResponse result = apiInstance.createUser(accountId, operation, createUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **operation** | **String**|  | [enum: create] |
| **createUserRequest** | [**CreateUserRequest**](CreateUserRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ConflictException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | BadRequestException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createVoiceConnector"></a>
# **createVoiceConnector**
> CreateVoiceConnectorResponse createVoiceConnector(createVoiceConnectorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an Amazon Chime Voice Connector under the administrator&#39;s AWS account. You can choose to create an Amazon Chime Voice Connector in a specific AWS Region.&lt;/p&gt; &lt;p&gt;Enabling &lt;a&gt;CreateVoiceConnectorRequest$RequireEncryption&lt;/a&gt; configures your Amazon Chime Voice Connector to use TLS transport for SIP signaling and Secure RTP (SRTP) for media. Inbound calls use TLS transport, and unencrypted outbound calls are blocked. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnector.html\&quot;&gt;CreateVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateVoiceConnectorRequest createVoiceConnectorRequest = new CreateVoiceConnectorRequest(); // CreateVoiceConnectorRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateVoiceConnectorResponse result = apiInstance.createVoiceConnector(createVoiceConnectorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createVoiceConnector");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createVoiceConnectorRequest** | [**CreateVoiceConnectorRequest**](CreateVoiceConnectorRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateVoiceConnectorResponse**](CreateVoiceConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | AccessDeniedException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ResourceLimitExceededException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="createVoiceConnectorGroup"></a>
# **createVoiceConnectorGroup**
> CreateVoiceConnectorGroupResponse createVoiceConnectorGroup(createVoiceConnectorGroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Creates an Amazon Chime Voice Connector group under the administrator&#39;s AWS account. You can associate Amazon Chime Voice Connectors with the Amazon Chime Voice Connector group by including &lt;code&gt;VoiceConnectorItems&lt;/code&gt; in the request.&lt;/p&gt; &lt;p&gt;You can include Amazon Chime Voice Connectors from different AWS Regions in your group. This creates a fault tolerant mechanism for fallback in case of availability events.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_CreateVoiceConnectorGroup.html\&quot;&gt;CreateVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateVoiceConnectorGroupRequest createVoiceConnectorGroupRequest = new CreateVoiceConnectorGroupRequest(); // CreateVoiceConnectorGroupRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      CreateVoiceConnectorGroupResponse result = apiInstance.createVoiceConnectorGroup(createVoiceConnectorGroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createVoiceConnectorGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **createVoiceConnectorGroupRequest** | [**CreateVoiceConnectorGroupRequest**](CreateVoiceConnectorGroupRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**CreateVoiceConnectorGroupResponse**](CreateVoiceConnectorGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | AccessDeniedException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ResourceLimitExceededException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="deleteAccount"></a>
# **deleteAccount**
> Object deleteAccount(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the specified Amazon Chime account. You must suspend all users before deleting &lt;code&gt;Team&lt;/code&gt; account. You can use the &lt;a&gt;BatchSuspendUser&lt;/a&gt; action to dodo.&lt;/p&gt; &lt;p&gt;For &lt;code&gt;EnterpriseLWA&lt;/code&gt; and &lt;code&gt;EnterpriseAD&lt;/code&gt; accounts, you must release the claimed domains for your Amazon Chime account before deletion. As soon as you release the domain, all users under that account are suspended.&lt;/p&gt; &lt;p&gt;Deleted accounts appear in your &lt;code&gt;Disabled&lt;/code&gt; accounts list for 90 days. To restore deleted account from your &lt;code&gt;Disabled&lt;/code&gt; accounts list, you must contact AWS Support.&lt;/p&gt; &lt;p&gt;After 90 days, deleted accounts are permanently removed from your &lt;code&gt;Disabled&lt;/code&gt; accounts list.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.deleteAccount(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | UnprocessableEntityException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="deleteAppInstance"></a>
# **deleteAppInstance**
> deleteAppInstance(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes an &lt;code&gt;AppInstance&lt;/code&gt; and all associated data asynchronously.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstance.html\&quot;&gt;DeleteAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteAppInstance(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAppInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="deleteAppInstanceAdmin"></a>
# **deleteAppInstanceAdmin**
> deleteAppInstanceAdmin(appInstanceAdminArn, appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Demotes an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; to an &lt;code&gt;AppInstanceUser&lt;/code&gt;. This action does not delete the user.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceAdmin.html\&quot;&gt;DeleteAppInstanceAdmin&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceAdminArn = "appInstanceAdminArn_example"; // String | The ARN of the <code>AppInstance</code>'s administrator.
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteAppInstanceAdmin(appInstanceAdminArn, appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAppInstanceAdmin");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceAdminArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;&#39;s administrator. | |
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteAppInstanceStreamingConfigurations"></a>
# **deleteAppInstanceStreamingConfigurations**
> deleteAppInstanceStreamingConfigurations(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the streaming configurations of an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceStreamingConfigurations.html\&quot;&gt;DeleteAppInstanceStreamingConfigurations&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the streaming configurations being deleted.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteAppInstanceStreamingConfigurations(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAppInstanceStreamingConfigurations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the streaming configurations being deleted. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteAppInstanceUser"></a>
# **deleteAppInstanceUser**
> deleteAppInstanceUser(appInstanceUserArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DeleteAppInstanceUser.html\&quot;&gt;DeleteAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the user request being deleted.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteAppInstanceUser(appInstanceUserArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAppInstanceUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceUserArn** | **String**| The ARN of the user request being deleted. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="deleteAttendee"></a>
# **deleteAttendee**
> deleteAttendee(meetingId, attendeeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes an attendee from the specified Amazon Chime SDK meeting and deletes their &lt;code&gt;JoinToken&lt;/code&gt;. Attendees are automatically deleted when a Amazon Chime SDK meeting is deleted. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteAttendee.html\&quot;&gt;DeleteAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String attendeeId = "attendeeId_example"; // String | The Amazon Chime SDK attendee ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteAttendee(meetingId, attendeeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAttendee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **attendeeId** | **String**| The Amazon Chime SDK attendee ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | NotFoundException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteChannel"></a>
# **deleteChannel**
> deleteChannel(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Immediately makes a channel and its memberships inaccessible and marks them for deletion. This is an irreversible process.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannel.html\&quot;&gt;DeleteChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel being deleted.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      apiInstance.deleteChannel(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteChannel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel being deleted. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="deleteChannelBan"></a>
# **deleteChannelBan**
> deleteChannelBan(channelArn, memberArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Removes a user from a channel&#39;s ban list.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelBan.html\&quot;&gt;DeleteChannelBan&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel from which the <code>AppInstanceUser</code> was banned.
    String memberArn = "memberArn_example"; // String | The ARN of the <code>AppInstanceUser</code> that you want to reinstate.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      apiInstance.deleteChannelBan(channelArn, memberArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteChannelBan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel from which the &lt;code&gt;AppInstanceUser&lt;/code&gt; was banned. | |
| **memberArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; that you want to reinstate. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="deleteChannelMembership"></a>
# **deleteChannelMembership**
> deleteChannelMembership(channelArn, memberArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Removes a member from a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMembership.html\&quot;&gt;DeleteChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel from which you want to remove the user.
    String memberArn = "memberArn_example"; // String | The ARN of the member that you're removing from the channel.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      apiInstance.deleteChannelMembership(channelArn, memberArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteChannelMembership");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel from which you want to remove the user. | |
| **memberArn** | **String**| The ARN of the member that you&#39;re removing from the channel. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ConflictException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteChannelMessage"></a>
# **deleteChannelMessage**
> deleteChannelMessage(channelArn, messageId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Deletes a channel message. Only admins can perform this action. Deletion makes messages inaccessible immediately. A background process deletes any revisions created by &lt;code&gt;UpdateChannelMessage&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelMessage.html\&quot;&gt;DeleteChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String messageId = "messageId_example"; // String | The ID of the message being deleted.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      apiInstance.deleteChannelMessage(channelArn, messageId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteChannelMessage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **messageId** | **String**| The ID of the message being deleted. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="deleteChannelModerator"></a>
# **deleteChannelModerator**
> deleteChannelModerator(channelArn, channelModeratorArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Deletes a channel moderator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DeleteChannelModerator.html\&quot;&gt;DeleteChannelModerator&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String channelModeratorArn = "channelModeratorArn_example"; // String | The ARN of the moderator being deleted.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      apiInstance.deleteChannelModerator(channelArn, channelModeratorArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteChannelModerator");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **channelModeratorArn** | **String**| The ARN of the moderator being deleted. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="deleteEventsConfiguration"></a>
# **deleteEventsConfiguration**
> deleteEventsConfiguration(accountId, botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes the events configuration that allows a bot to receive outgoing events.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String botId = "botId_example"; // String | The bot ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteEventsConfiguration(accountId, botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteEventsConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **botId** | **String**| The bot ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceFailureException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ResourceLimitExceededException |  -  |

<a id="deleteMediaCapturePipeline"></a>
# **deleteMediaCapturePipeline**
> deleteMediaCapturePipeline(mediaPipelineId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the media capture pipeline.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_DeleteMediaCapturePipeline.html\&quot;&gt;DeleteMediaCapturePipeline&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaPipelineId = "mediaPipelineId_example"; // String | The ID of the media capture pipeline being deleted. 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteMediaCapturePipeline(mediaPipelineId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteMediaCapturePipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mediaPipelineId** | **String**| The ID of the media capture pipeline being deleted.  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | ForbiddenException |  -  |
| **481** | NotFoundException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteMeeting"></a>
# **deleteMeeting**
> deleteMeeting(meetingId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the specified Amazon Chime SDK meeting. The operation deletes all attendees, disconnects all clients, and prevents new clients from joining the meeting. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_DeleteMeeting.html\&quot;&gt;DeleteMeeting&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteMeeting(meetingId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteMeeting");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | NotFoundException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deletePhoneNumber"></a>
# **deletePhoneNumber**
> deletePhoneNumber(phoneNumberId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Moves the specified phone number into the &lt;b&gt;Deletion queue&lt;/b&gt;. A phone number must be disassociated from any users or Amazon Chime Voice Connectors before it can be deleted.&lt;/p&gt; &lt;p&gt;Deleted phone numbers remain in the &lt;b&gt;Deletion queue&lt;/b&gt; for 7 days before they are deleted permanently.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String phoneNumberId = "phoneNumberId_example"; // String | The phone number ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deletePhoneNumber(phoneNumberId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePhoneNumber");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **phoneNumberId** | **String**| The phone number ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteProxySession"></a>
# **deleteProxySession**
> deleteProxySession(voiceConnectorId, proxySessionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the specified proxy session from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteProxySession.html\&quot;&gt;DeleteProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
    String proxySessionId = "proxySessionId_example"; // String | The proxy session ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteProxySession(voiceConnectorId, proxySessionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteProxySession");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | |
| **proxySessionId** | **String**| The proxy session ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteRoom"></a>
# **deleteRoom**
> deleteRoom(accountId, roomId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Deletes a chat room in an Amazon Chime Enterprise account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String roomId = "roomId_example"; // String | The chat room ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteRoom(accountId, roomId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRoom");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **roomId** | **String**| The chat room ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteRoomMembership"></a>
# **deleteRoomMembership**
> deleteRoomMembership(accountId, roomId, memberId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Removes a member from a chat room in an Amazon Chime Enterprise account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String roomId = "roomId_example"; // String | The room ID.
    String memberId = "memberId_example"; // String | The member ID (user ID or bot ID).
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteRoomMembership(accountId, roomId, memberId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRoomMembership");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **roomId** | **String**| The room ID. | |
| **memberId** | **String**| The member ID (user ID or bot ID). | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteSipMediaApplication"></a>
# **deleteSipMediaApplication**
> deleteSipMediaApplication(sipMediaApplicationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipMediaApplication.html\&quot;&gt;DeleteSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The SIP media application ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteSipMediaApplication(sipMediaApplicationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteSipMediaApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sipMediaApplicationId** | **String**| The SIP media application ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="deleteSipRule"></a>
# **deleteSipRule**
> deleteSipRule(sipRuleId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes a SIP rule. You must disable a SIP rule before you can delete it.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteSipRule.html\&quot;&gt;DeleteSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sipRuleId = "sipRuleId_example"; // String | The SIP rule ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteSipRule(sipRuleId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteSipRule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sipRuleId** | **String**| The SIP rule ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="deleteVoiceConnector"></a>
# **deleteVoiceConnector**
> deleteVoiceConnector(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the specified Amazon Chime Voice Connector. Any phone numbers associated with the Amazon Chime Voice Connector must be disassociated from it before it can be deleted.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnector.html\&quot;&gt;DeleteVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteVoiceConnector(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVoiceConnector");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="deleteVoiceConnectorEmergencyCallingConfiguration"></a>
# **deleteVoiceConnectorEmergencyCallingConfiguration**
> deleteVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the emergency calling configuration details from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorEmergencyCallingConfiguration.html\&quot;&gt;DeleteVoiceConnectorEmergencyCallingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVoiceConnectorEmergencyCallingConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteVoiceConnectorGroup"></a>
# **deleteVoiceConnectorGroup**
> deleteVoiceConnectorGroup(voiceConnectorGroupId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the specified Amazon Chime Voice Connector group. Any &lt;code&gt;VoiceConnectorItems&lt;/code&gt; and phone numbers associated with the group must be removed before it can be deleted.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorGroup.html\&quot;&gt;DeleteVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorGroupId = "voiceConnectorGroupId_example"; // String | The Amazon Chime Voice Connector group ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteVoiceConnectorGroup(voiceConnectorGroupId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVoiceConnectorGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorGroupId** | **String**| The Amazon Chime Voice Connector group ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="deleteVoiceConnectorOrigination"></a>
# **deleteVoiceConnectorOrigination**
> deleteVoiceConnectorOrigination(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the origination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to deleting the origination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorOrigination.html\&quot;&gt;DeleteVoiceConnectorOrigination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteVoiceConnectorOrigination(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVoiceConnectorOrigination");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteVoiceConnectorProxy"></a>
# **deleteVoiceConnectorProxy**
> deleteVoiceConnectorProxy(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the proxy configuration from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorProxy.html\&quot;&gt;DeleteVoiceProxy&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteVoiceConnectorProxy(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVoiceConnectorProxy");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteVoiceConnectorStreamingConfiguration"></a>
# **deleteVoiceConnectorStreamingConfiguration**
> deleteVoiceConnectorStreamingConfiguration(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the streaming configuration for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorStreamingConfiguration.html\&quot;&gt;DeleteVoiceConnectorStreamingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteVoiceConnectorStreamingConfiguration(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVoiceConnectorStreamingConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteVoiceConnectorTermination"></a>
# **deleteVoiceConnectorTermination**
> deleteVoiceConnectorTermination(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the termination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to deleting the termination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTermination.html\&quot;&gt;DeleteVoiceConnectorTermination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteVoiceConnectorTermination(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVoiceConnectorTermination");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="deleteVoiceConnectorTerminationCredentials"></a>
# **deleteVoiceConnectorTerminationCredentials**
> deleteVoiceConnectorTerminationCredentials(voiceConnectorId, operation, deleteVoiceConnectorTerminationCredentialsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Deletes the specified SIP credentials used by your equipment to authenticate during call termination.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DeleteVoiceConnectorTerminationCredentials.html\&quot;&gt;DeleteVoiceConnectorTerminationCredentials&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String operation = "delete"; // String | 
    DeleteVoiceConnectorTerminationCredentialsRequest deleteVoiceConnectorTerminationCredentialsRequest = new DeleteVoiceConnectorTerminationCredentialsRequest(); // DeleteVoiceConnectorTerminationCredentialsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.deleteVoiceConnectorTerminationCredentials(voiceConnectorId, operation, deleteVoiceConnectorTerminationCredentialsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteVoiceConnectorTerminationCredentials");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **operation** | **String**|  | [enum: delete] |
| **deleteVoiceConnectorTerminationCredentialsRequest** | [**DeleteVoiceConnectorTerminationCredentialsRequest**](DeleteVoiceConnectorTerminationCredentialsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="describeAppInstance"></a>
# **describeAppInstance**
> DescribeAppInstanceResponse describeAppInstance(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the full details of an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstance.html\&quot;&gt;DescribeAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeAppInstanceResponse result = apiInstance.describeAppInstance(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAppInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeAppInstanceResponse**](DescribeAppInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="describeAppInstanceAdmin"></a>
# **describeAppInstanceAdmin**
> DescribeAppInstanceAdminResponse describeAppInstanceAdmin(appInstanceAdminArn, appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the full details of an &lt;code&gt;AppInstanceAdmin&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceAdmin.html\&quot;&gt;DescribeAppInstanceAdmin&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceAdminArn = "appInstanceAdminArn_example"; // String | The ARN of the <code>AppInstanceAdmin</code>.
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeAppInstanceAdminResponse result = apiInstance.describeAppInstanceAdmin(appInstanceAdminArn, appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAppInstanceAdmin");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceAdminArn** | **String**| The ARN of the &lt;code&gt;AppInstanceAdmin&lt;/code&gt;. | |
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeAppInstanceAdminResponse**](DescribeAppInstanceAdminResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="describeAppInstanceUser"></a>
# **describeAppInstanceUser**
> DescribeAppInstanceUserResponse describeAppInstanceUser(appInstanceUserArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the full details of an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_DescribeAppInstanceUser.html\&quot;&gt;DescribeAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the <code>AppInstanceUser</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DescribeAppInstanceUserResponse result = apiInstance.describeAppInstanceUser(appInstanceUserArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeAppInstanceUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceUserArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DescribeAppInstanceUserResponse**](DescribeAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="describeChannel"></a>
# **describeChannel**
> DescribeChannelResponse describeChannel(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Returns the full details of a channel in an Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannel.html\&quot;&gt;DescribeChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      DescribeChannelResponse result = apiInstance.describeChannel(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**DescribeChannelResponse**](DescribeChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="describeChannelBan"></a>
# **describeChannelBan**
> DescribeChannelBanResponse describeChannelBan(channelArn, memberArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Returns the full details of a channel ban.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelBan.html\&quot;&gt;DescribeChannelBan&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel from which the user is banned.
    String memberArn = "memberArn_example"; // String | The ARN of the member being banned.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      DescribeChannelBanResponse result = apiInstance.describeChannelBan(channelArn, memberArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannelBan");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel from which the user is banned. | |
| **memberArn** | **String**| The ARN of the member being banned. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**DescribeChannelBanResponse**](DescribeChannelBanResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="describeChannelMembership"></a>
# **describeChannelMembership**
> DescribeChannelMembershipResponse describeChannelMembership(channelArn, memberArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Returns the full details of a user&#39;s channel membership.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembership.html\&quot;&gt;DescribeChannelMembership&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String memberArn = "memberArn_example"; // String | The ARN of the member.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      DescribeChannelMembershipResponse result = apiInstance.describeChannelMembership(channelArn, memberArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannelMembership");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **memberArn** | **String**| The ARN of the member. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**DescribeChannelMembershipResponse**](DescribeChannelMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="describeChannelMembershipForAppInstanceUser"></a>
# **describeChannelMembershipForAppInstanceUser**
> DescribeChannelMembershipForAppInstanceUserResponse describeChannelMembershipForAppInstanceUser(channelArn, appInstanceUserArn, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt; Returns the details of a channel based on the membership of the specified &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelMembershipForAppInstanceUser.html\&quot;&gt;DescribeChannelMembershipForAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel to which the user belongs.
    String appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the user in a channel.
    String scope = "app-instance-user-membership"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      DescribeChannelMembershipForAppInstanceUserResponse result = apiInstance.describeChannelMembershipForAppInstanceUser(channelArn, appInstanceUserArn, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannelMembershipForAppInstanceUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel to which the user belongs. | |
| **appInstanceUserArn** | **String**| The ARN of the user in a channel. | |
| **scope** | **String**|  | [enum: app-instance-user-membership] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**DescribeChannelMembershipForAppInstanceUserResponse**](DescribeChannelMembershipForAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="describeChannelModeratedByAppInstanceUser"></a>
# **describeChannelModeratedByAppInstanceUser**
> DescribeChannelModeratedByAppInstanceUserResponse describeChannelModeratedByAppInstanceUser(channelArn, appInstanceUserArn, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Returns the full details of a channel moderated by the specified &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModeratedByAppInstanceUser.html\&quot;&gt;DescribeChannelModeratedByAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the moderated channel.
    String appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the <code>AppInstanceUser</code> in the moderated channel.
    String scope = "app-instance-user-moderated-channel"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      DescribeChannelModeratedByAppInstanceUserResponse result = apiInstance.describeChannelModeratedByAppInstanceUser(channelArn, appInstanceUserArn, scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannelModeratedByAppInstanceUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the moderated channel. | |
| **appInstanceUserArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt; in the moderated channel. | |
| **scope** | **String**|  | [enum: app-instance-user-moderated-channel] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**DescribeChannelModeratedByAppInstanceUserResponse**](DescribeChannelModeratedByAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="describeChannelModerator"></a>
# **describeChannelModerator**
> DescribeChannelModeratorResponse describeChannelModerator(channelArn, channelModeratorArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Returns the full details of a single ChannelModerator.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_DescribeChannelModerator.html\&quot;&gt;DescribeChannelModerator&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String channelModeratorArn = "channelModeratorArn_example"; // String | The ARN of the channel moderator.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      DescribeChannelModeratorResponse result = apiInstance.describeChannelModerator(channelArn, channelModeratorArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#describeChannelModerator");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **channelModeratorArn** | **String**| The ARN of the channel moderator. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**DescribeChannelModeratorResponse**](DescribeChannelModeratorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="disassociatePhoneNumberFromUser"></a>
# **disassociatePhoneNumberFromUser**
> Object disassociatePhoneNumberFromUser(accountId, userId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Disassociates the primary provisioned phone number from the specified Amazon Chime user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String userId = "userId_example"; // String | The user ID.
    String operation = "disassociate-phone-number"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.disassociatePhoneNumberFromUser(accountId, userId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociatePhoneNumberFromUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **userId** | **String**| The user ID. | |
| **operation** | **String**|  | [enum: disassociate-phone-number] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="disassociatePhoneNumbersFromVoiceConnector"></a>
# **disassociatePhoneNumbersFromVoiceConnector**
> DisassociatePhoneNumbersFromVoiceConnectorResponse disassociatePhoneNumbersFromVoiceConnector(voiceConnectorId, operation, disassociatePhoneNumbersFromVoiceConnectorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Disassociates the specified phone numbers from the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnector.html\&quot;&gt;DisassociatePhoneNumbersFromVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String operation = "disassociate-phone-numbers"; // String | 
    DisassociatePhoneNumbersFromVoiceConnectorRequest disassociatePhoneNumbersFromVoiceConnectorRequest = new DisassociatePhoneNumbersFromVoiceConnectorRequest(); // DisassociatePhoneNumbersFromVoiceConnectorRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DisassociatePhoneNumbersFromVoiceConnectorResponse result = apiInstance.disassociatePhoneNumbersFromVoiceConnector(voiceConnectorId, operation, disassociatePhoneNumbersFromVoiceConnectorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociatePhoneNumbersFromVoiceConnector");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **operation** | **String**|  | [enum: disassociate-phone-numbers] |
| **disassociatePhoneNumbersFromVoiceConnectorRequest** | [**DisassociatePhoneNumbersFromVoiceConnectorRequest**](DisassociatePhoneNumbersFromVoiceConnectorRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DisassociatePhoneNumbersFromVoiceConnectorResponse**](DisassociatePhoneNumbersFromVoiceConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="disassociatePhoneNumbersFromVoiceConnectorGroup"></a>
# **disassociatePhoneNumbersFromVoiceConnectorGroup**
> DisassociatePhoneNumbersFromVoiceConnectorGroupResponse disassociatePhoneNumbersFromVoiceConnectorGroup(voiceConnectorGroupId, operation, disassociatePhoneNumbersFromVoiceConnectorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Disassociates the specified phone numbers from the specified Amazon Chime Voice Connector group.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_DisassociatePhoneNumbersFromVoiceConnectorGroup.html\&quot;&gt;DisassociatePhoneNumbersFromVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorGroupId = "voiceConnectorGroupId_example"; // String | The Amazon Chime Voice Connector group ID.
    String operation = "disassociate-phone-numbers"; // String | 
    DisassociatePhoneNumbersFromVoiceConnectorRequest disassociatePhoneNumbersFromVoiceConnectorRequest = new DisassociatePhoneNumbersFromVoiceConnectorRequest(); // DisassociatePhoneNumbersFromVoiceConnectorRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      DisassociatePhoneNumbersFromVoiceConnectorGroupResponse result = apiInstance.disassociatePhoneNumbersFromVoiceConnectorGroup(voiceConnectorGroupId, operation, disassociatePhoneNumbersFromVoiceConnectorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociatePhoneNumbersFromVoiceConnectorGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorGroupId** | **String**| The Amazon Chime Voice Connector group ID. | |
| **operation** | **String**|  | [enum: disassociate-phone-numbers] |
| **disassociatePhoneNumbersFromVoiceConnectorRequest** | [**DisassociatePhoneNumbersFromVoiceConnectorRequest**](DisassociatePhoneNumbersFromVoiceConnectorRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**DisassociatePhoneNumbersFromVoiceConnectorGroupResponse**](DisassociatePhoneNumbersFromVoiceConnectorGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="disassociateSigninDelegateGroupsFromAccount"></a>
# **disassociateSigninDelegateGroupsFromAccount**
> Object disassociateSigninDelegateGroupsFromAccount(accountId, operation, disassociateSigninDelegateGroupsFromAccountRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Disassociates the specified sign-in delegate groups from the specified Amazon Chime account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String operation = "disassociate-signin-delegate-groups"; // String | 
    DisassociateSigninDelegateGroupsFromAccountRequest disassociateSigninDelegateGroupsFromAccountRequest = new DisassociateSigninDelegateGroupsFromAccountRequest(); // DisassociateSigninDelegateGroupsFromAccountRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.disassociateSigninDelegateGroupsFromAccount(accountId, operation, disassociateSigninDelegateGroupsFromAccountRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disassociateSigninDelegateGroupsFromAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **operation** | **String**|  | [enum: disassociate-signin-delegate-groups] |
| **disassociateSigninDelegateGroupsFromAccountRequest** | [**DisassociateSigninDelegateGroupsFromAccountRequest**](DisassociateSigninDelegateGroupsFromAccountRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getAccount"></a>
# **getAccount**
> GetAccountResponse getAccount(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves details for the specified Amazon Chime account, such as account type and supported licenses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetAccountResponse result = apiInstance.getAccount(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetAccountResponse**](GetAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getAccountSettings"></a>
# **getAccountSettings**
> GetAccountSettingsResponse getAccountSettings(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves account settings for the specified Amazon Chime account ID, such as remote control and dialout settings. For more information about these settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/policies.html\&quot;&gt;Use the Policies Page&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetAccountSettingsResponse result = apiInstance.getAccountSettings(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAccountSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetAccountSettingsResponse**](GetAccountSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getAppInstanceRetentionSettings"></a>
# **getAppInstanceRetentionSettings**
> GetAppInstanceRetentionSettingsResponse getAppInstanceRetentionSettings(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the retention settings for an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_GetAppInstanceRetentionSettings.html\&quot;&gt;GetMessagingRetentionSettings&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetAppInstanceRetentionSettingsResponse result = apiInstance.getAppInstanceRetentionSettings(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAppInstanceRetentionSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetAppInstanceRetentionSettingsResponse**](GetAppInstanceRetentionSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getAppInstanceStreamingConfigurations"></a>
# **getAppInstanceStreamingConfigurations**
> GetAppInstanceStreamingConfigurationsResponse getAppInstanceStreamingConfigurations(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the streaming settings for an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingStreamingConfigurations.html\&quot;&gt;GetMessagingStreamingConfigurations&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetAppInstanceStreamingConfigurationsResponse result = apiInstance.getAppInstanceStreamingConfigurations(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAppInstanceStreamingConfigurations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetAppInstanceStreamingConfigurationsResponse**](GetAppInstanceStreamingConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getAttendee"></a>
# **getAttendee**
> GetAttendeeResponse getAttendee(meetingId, attendeeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Gets the Amazon Chime SDK attendee details for a specified meeting ID and attendee ID. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetAttendee.html\&quot;&gt;GetAttendee&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String attendeeId = "attendeeId_example"; // String | The Amazon Chime SDK attendee ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetAttendeeResponse result = apiInstance.getAttendee(meetingId, attendeeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAttendee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **attendeeId** | **String**| The Amazon Chime SDK attendee ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetAttendeeResponse**](GetAttendeeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getBot"></a>
# **getBot**
> GetBotResponse getBot(accountId, botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves details for the specified bot, such as bot email address, bot type, status, and display name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String botId = "botId_example"; // String | The bot ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetBotResponse result = apiInstance.getBot(accountId, botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **botId** | **String**| The bot ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetBotResponse**](GetBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceFailureException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | NotFoundException |  -  |
| **485** | BadRequestException |  -  |
| **486** | ThrottledClientException |  -  |

<a id="getChannelMessage"></a>
# **getChannelMessage**
> GetChannelMessageResponse getChannelMessage(channelArn, messageId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Gets the full details of a channel message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The x-amz-chime-bearer request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetChannelMessage.html\&quot;&gt;GetChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String messageId = "messageId_example"; // String | The ID of the message.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      GetChannelMessageResponse result = apiInstance.getChannelMessage(channelArn, messageId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getChannelMessage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **messageId** | **String**| The ID of the message. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**GetChannelMessageResponse**](GetChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getEventsConfiguration"></a>
# **getEventsConfiguration**
> GetEventsConfigurationResponse getEventsConfiguration(accountId, botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Gets details for an events configuration that allows a bot to receive outgoing events, such as an HTTPS endpoint or Lambda function ARN.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String botId = "botId_example"; // String | The bot ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetEventsConfigurationResponse result = apiInstance.getEventsConfiguration(accountId, botId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getEventsConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **botId** | **String**| The bot ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetEventsConfigurationResponse**](GetEventsConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceFailureException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ResourceLimitExceededException |  -  |
| **486** | NotFoundException |  -  |

<a id="getGlobalSettings"></a>
# **getGlobalSettings**
> GetGlobalSettingsResponse getGlobalSettings(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves global settings for the administrator&#39;s AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetGlobalSettingsResponse result = apiInstance.getGlobalSettings(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getGlobalSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetGlobalSettingsResponse**](GetGlobalSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="getMediaCapturePipeline"></a>
# **getMediaCapturePipeline**
> GetMediaCapturePipelineResponse getMediaCapturePipeline(mediaPipelineId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets an existing media capture pipeline.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_GetMediaCapturePipeline.html\&quot;&gt;GetMediaCapturePipeline&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String mediaPipelineId = "mediaPipelineId_example"; // String | The ID of the pipeline that you want to get.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetMediaCapturePipelineResponse result = apiInstance.getMediaCapturePipeline(mediaPipelineId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMediaCapturePipeline");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mediaPipelineId** | **String**| The ID of the pipeline that you want to get. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetMediaCapturePipelineResponse**](GetMediaCapturePipelineResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getMeeting"></a>
# **getMeeting**
> GetMeetingResponse getMeeting(meetingId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_GetMeeting.html\&quot;&gt;GetMeeting&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; Gets the Amazon Chime SDK meeting details for the specified meeting ID. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt; . &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetMeetingResponse result = apiInstance.getMeeting(meetingId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMeeting");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetMeetingResponse**](GetMeetingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getMessagingSessionEndpoint"></a>
# **getMessagingSessionEndpoint**
> GetMessagingSessionEndpointResponse getMessagingSessionEndpoint(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;The details of the endpoint for the messaging session.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_GetMessagingSessionEndpoint.html\&quot;&gt;GetMessagingSessionEndpoint&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetMessagingSessionEndpointResponse result = apiInstance.getMessagingSessionEndpoint(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMessagingSessionEndpoint");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetMessagingSessionEndpointResponse**](GetMessagingSessionEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | ServiceUnavailableException |  -  |
| **484** | ServiceFailureException |  -  |

<a id="getPhoneNumber"></a>
# **getPhoneNumber**
> GetPhoneNumberResponse getPhoneNumber(phoneNumberId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves details for the specified phone number ID, such as associations, capabilities, and product type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String phoneNumberId = "phoneNumberId_example"; // String | The phone number ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetPhoneNumberResponse result = apiInstance.getPhoneNumber(phoneNumberId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPhoneNumber");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **phoneNumberId** | **String**| The phone number ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetPhoneNumberResponse**](GetPhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getPhoneNumberOrder"></a>
# **getPhoneNumberOrder**
> GetPhoneNumberOrderResponse getPhoneNumberOrder(phoneNumberOrderId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves details for the specified phone number order, such as the order creation timestamp, phone numbers in E.164 format, product type, and order status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String phoneNumberOrderId = "phoneNumberOrderId_example"; // String | The ID for the phone number order.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetPhoneNumberOrderResponse result = apiInstance.getPhoneNumberOrder(phoneNumberOrderId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPhoneNumberOrder");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **phoneNumberOrderId** | **String**| The ID for the phone number order. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetPhoneNumberOrderResponse**](GetPhoneNumberOrderResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getPhoneNumberSettings"></a>
# **getPhoneNumberSettings**
> GetPhoneNumberSettingsResponse getPhoneNumberSettings(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves the phone number settings for the administrator&#39;s AWS account, such as the default outbound calling name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetPhoneNumberSettingsResponse result = apiInstance.getPhoneNumberSettings(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPhoneNumberSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetPhoneNumberSettingsResponse**](GetPhoneNumberSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="getProxySession"></a>
# **getProxySession**
> GetProxySessionResponse getProxySession(voiceConnectorId, proxySessionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the specified proxy session details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetProxySession.html\&quot;&gt;GetProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
    String proxySessionId = "proxySessionId_example"; // String | The proxy session ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetProxySessionResponse result = apiInstance.getProxySession(voiceConnectorId, proxySessionId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProxySession");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | |
| **proxySessionId** | **String**| The proxy session ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetProxySessionResponse**](GetProxySessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getRetentionSettings"></a>
# **getRetentionSettings**
> GetRetentionSettingsResponse getRetentionSettings(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



 Gets the retention settings for the specified Amazon Chime Enterprise account. For more information about retention settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/chat-retention.html\&quot;&gt;Managing Chat Retention Policies&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetRetentionSettingsResponse result = apiInstance.getRetentionSettings(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRetentionSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetRetentionSettingsResponse**](GetRetentionSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getRoom"></a>
# **getRoom**
> GetRoomResponse getRoom(accountId, roomId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves room details, such as the room name, for a room in an Amazon Chime Enterprise account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String roomId = "roomId_example"; // String | The room ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetRoomResponse result = apiInstance.getRoom(accountId, roomId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRoom");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **roomId** | **String**| The room ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetRoomResponse**](GetRoomResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getSipMediaApplication"></a>
# **getSipMediaApplication**
> GetSipMediaApplicationResponse getSipMediaApplication(sipMediaApplicationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves the information for a SIP media application, including name, AWS Region, and endpoints.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplication.html\&quot;&gt;GetSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The SIP media application ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetSipMediaApplicationResponse result = apiInstance.getSipMediaApplication(sipMediaApplicationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSipMediaApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sipMediaApplicationId** | **String**| The SIP media application ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetSipMediaApplicationResponse**](GetSipMediaApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getSipMediaApplicationLoggingConfiguration"></a>
# **getSipMediaApplicationLoggingConfiguration**
> GetSipMediaApplicationLoggingConfigurationResponse getSipMediaApplicationLoggingConfiguration(sipMediaApplicationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Returns the logging configuration for the specified SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipMediaApplicationLoggingConfiguration.html\&quot;&gt;GetSipMediaApplicationLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The SIP media application ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetSipMediaApplicationLoggingConfigurationResponse result = apiInstance.getSipMediaApplicationLoggingConfiguration(sipMediaApplicationId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSipMediaApplicationLoggingConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sipMediaApplicationId** | **String**| The SIP media application ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetSipMediaApplicationLoggingConfigurationResponse**](GetSipMediaApplicationLoggingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getSipRule"></a>
# **getSipRule**
> GetSipRuleResponse getSipRule(sipRuleId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves the details of a SIP rule, such as the rule ID, name, triggers, and target endpoints.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetSipRule.html\&quot;&gt;GetSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sipRuleId = "sipRuleId_example"; // String | The SIP rule ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetSipRuleResponse result = apiInstance.getSipRule(sipRuleId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSipRule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sipRuleId** | **String**| The SIP rule ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetSipRuleResponse**](GetSipRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getUser"></a>
# **getUser**
> GetUserResponse getUser(accountId, userId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves details for the specified user ID, such as primary email address, license type,and personal meeting PIN.&lt;/p&gt; &lt;p&gt; To retrieve user details with an email address instead of a user ID, use the &lt;a&gt;ListUsers&lt;/a&gt; action, and then filter by email address. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String userId = "userId_example"; // String | The user ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetUserResponse result = apiInstance.getUser(accountId, userId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **userId** | **String**| The user ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getUserSettings"></a>
# **getUserSettings**
> GetUserSettingsResponse getUserSettings(accountId, userId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Retrieves settings for the specified user ID, such as any associated phone number settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String userId = "userId_example"; // String | The user ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetUserSettingsResponse result = apiInstance.getUserSettings(accountId, userId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getUserSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **userId** | **String**| The user ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetUserSettingsResponse**](GetUserSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getVoiceConnector"></a>
# **getVoiceConnector**
> GetVoiceConnectorResponse getVoiceConnector(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves details for the specified Amazon Chime Voice Connector, such as timestamps,name, outbound host, and encryption requirements.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnector.html\&quot;&gt;GetVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVoiceConnectorResponse result = apiInstance.getVoiceConnector(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVoiceConnector");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVoiceConnectorResponse**](GetVoiceConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getVoiceConnectorEmergencyCallingConfiguration"></a>
# **getVoiceConnectorEmergencyCallingConfiguration**
> GetVoiceConnectorEmergencyCallingConfigurationResponse getVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the emergency calling configuration details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorEmergencyCallingConfiguration.html\&quot;&gt;GetVoiceConnectorEmergencyCallingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVoiceConnectorEmergencyCallingConfigurationResponse result = apiInstance.getVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVoiceConnectorEmergencyCallingConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVoiceConnectorEmergencyCallingConfigurationResponse**](GetVoiceConnectorEmergencyCallingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getVoiceConnectorGroup"></a>
# **getVoiceConnectorGroup**
> GetVoiceConnectorGroupResponse getVoiceConnectorGroup(voiceConnectorGroupId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Retrieves details for the specified Amazon Chime Voice Connector group, such as timestamps,name, and associated &lt;code&gt;VoiceConnectorItems&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorGroup.html\&quot;&gt;GetVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorGroupId = "voiceConnectorGroupId_example"; // String | The Amazon Chime Voice Connector group ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVoiceConnectorGroupResponse result = apiInstance.getVoiceConnectorGroup(voiceConnectorGroupId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVoiceConnectorGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorGroupId** | **String**| The Amazon Chime Voice Connector group ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVoiceConnectorGroupResponse**](GetVoiceConnectorGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getVoiceConnectorLoggingConfiguration"></a>
# **getVoiceConnectorLoggingConfiguration**
> GetVoiceConnectorLoggingConfigurationResponse getVoiceConnectorLoggingConfiguration(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves the logging configuration details for the specified Amazon Chime Voice Connector. Shows whether SIP message logs are enabled for sending to Amazon CloudWatch Logs.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorLoggingConfiguration.html\&quot;&gt;GetVoiceConnectorLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVoiceConnectorLoggingConfigurationResponse result = apiInstance.getVoiceConnectorLoggingConfiguration(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVoiceConnectorLoggingConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVoiceConnectorLoggingConfigurationResponse**](GetVoiceConnectorLoggingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getVoiceConnectorOrigination"></a>
# **getVoiceConnectorOrigination**
> GetVoiceConnectorOriginationResponse getVoiceConnectorOrigination(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves origination setting details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorOrigination.html\&quot;&gt;GetVoiceConnectorOrigination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVoiceConnectorOriginationResponse result = apiInstance.getVoiceConnectorOrigination(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVoiceConnectorOrigination");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVoiceConnectorOriginationResponse**](GetVoiceConnectorOriginationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getVoiceConnectorProxy"></a>
# **getVoiceConnectorProxy**
> GetVoiceConnectorProxyResponse getVoiceConnectorProxy(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Gets the proxy configuration details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorProxy.html\&quot;&gt;GetVoiceConnectorProxy&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVoiceConnectorProxyResponse result = apiInstance.getVoiceConnectorProxy(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVoiceConnectorProxy");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVoiceConnectorProxyResponse**](GetVoiceConnectorProxyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getVoiceConnectorStreamingConfiguration"></a>
# **getVoiceConnectorStreamingConfiguration**
> GetVoiceConnectorStreamingConfigurationResponse getVoiceConnectorStreamingConfiguration(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves the streaming configuration details for the specified Amazon Chime Voice Connector. Shows whether media streaming is enabled for sending to Amazon Kinesis. It also shows the retention period, in hours, for the Amazon Kinesis data.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorStreamingConfiguration.html\&quot;&gt;GetVoiceConnectorStreamingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVoiceConnectorStreamingConfigurationResponse result = apiInstance.getVoiceConnectorStreamingConfiguration(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVoiceConnectorStreamingConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVoiceConnectorStreamingConfigurationResponse**](GetVoiceConnectorStreamingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getVoiceConnectorTermination"></a>
# **getVoiceConnectorTermination**
> GetVoiceConnectorTerminationResponse getVoiceConnectorTermination(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Retrieves termination setting details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTermination.html\&quot;&gt;GetVoiceConnectorTermination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVoiceConnectorTerminationResponse result = apiInstance.getVoiceConnectorTermination(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVoiceConnectorTermination");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVoiceConnectorTerminationResponse**](GetVoiceConnectorTerminationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="getVoiceConnectorTerminationHealth"></a>
# **getVoiceConnectorTerminationHealth**
> GetVoiceConnectorTerminationHealthResponse getVoiceConnectorTerminationHealth(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_GetVoiceConnectorTerminationHealth.html\&quot;&gt;GetVoiceConnectorTerminationHealth&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Retrieves information about the last time a SIP &lt;code&gt;OPTIONS&lt;/code&gt; ping was received from your SIP infrastructure for the specified Amazon Chime Voice Connector.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      GetVoiceConnectorTerminationHealthResponse result = apiInstance.getVoiceConnectorTerminationHealth(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVoiceConnectorTerminationHealth");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**GetVoiceConnectorTerminationHealthResponse**](GetVoiceConnectorTerminationHealthResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="inviteUsers"></a>
# **inviteUsers**
> InviteUsersResponse inviteUsers(accountId, operation, inviteUsersRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Sends email to a maximum of 50 users, inviting them to the specified Amazon Chime &lt;code&gt;Team&lt;/code&gt; account. Only &lt;code&gt;Team&lt;/code&gt; account types are currently supported for this action.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String operation = "add"; // String | 
    InviteUsersRequest inviteUsersRequest = new InviteUsersRequest(); // InviteUsersRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      InviteUsersResponse result = apiInstance.inviteUsers(accountId, operation, inviteUsersRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#inviteUsers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **operation** | **String**|  | [enum: add] |
| **inviteUsersRequest** | [**InviteUsersRequest**](InviteUsersRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**InviteUsersResponse**](InviteUsersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listAccounts"></a>
# **listAccounts**
> ListAccountsResponse listAccounts(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, name, userEmail, nextToken, maxResults, maxResults2, nextToken2)



Lists the Amazon Chime accounts under the administrator&#39;s AWS account. You can filter accounts by account name prefix. To find out which Amazon Chime account a user belongs to, you can filter by the user&#39;s email address, which returns one account result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String name = "name_example"; // String | Amazon Chime account name prefix with which to filter results.
    String userEmail = "userEmail_example"; // String | User email address with which to filter results.
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call. Defaults to 100.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListAccountsResponse result = apiInstance.listAccounts(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, name, userEmail, nextToken, maxResults, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAccounts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **name** | **String**| Amazon Chime account name prefix with which to filter results. | [optional] |
| **userEmail** | **String**| User email address with which to filter results. | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. Defaults to 100. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListAccountsResponse**](ListAccountsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listAppInstanceAdmins"></a>
# **listAppInstanceAdmins**
> ListAppInstanceAdminsResponse listAppInstanceAdmins(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



&lt;p&gt;Returns a list of the administrators in the &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceAdmins.html\&quot;&gt;ListAppInstanceAdmins&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of administrators that you want to return.
    String nextToken = "nextToken_example"; // String | The token returned from previous API requests until the number of administrators is reached.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListAppInstanceAdminsResponse result = apiInstance.listAppInstanceAdmins(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAppInstanceAdmins");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of administrators that you want to return. | [optional] |
| **nextToken** | **String**| The token returned from previous API requests until the number of administrators is reached. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListAppInstanceAdminsResponse**](ListAppInstanceAdminsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listAppInstanceUsers"></a>
# **listAppInstanceUsers**
> ListAppInstanceUsersResponse listAppInstanceUsers(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



&lt;p&gt;List all &lt;code&gt;AppInstanceUsers&lt;/code&gt; created under a single &lt;code&gt;AppInstance&lt;/code&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstanceUsers.html\&quot;&gt;ListAppInstanceUsers&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of requests that you want returned.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested users are returned.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListAppInstanceUsersResponse result = apiInstance.listAppInstanceUsers(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAppInstanceUsers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of requests that you want returned. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested users are returned. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListAppInstanceUsersResponse**](ListAppInstanceUsersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listAppInstances"></a>
# **listAppInstances**
> ListAppInstancesResponse listAppInstances(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



&lt;p&gt;Lists all Amazon Chime &lt;code&gt;AppInstance&lt;/code&gt;s created under a single AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_ListAppInstances.html\&quot;&gt;ListAppInstances&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of <code>AppInstance</code>s that you want to return.
    String nextToken = "nextToken_example"; // String | The token passed by previous API requests until you reach the maximum number of <code>AppInstance</code>s.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListAppInstancesResponse result = apiInstance.listAppInstances(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAppInstances");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of &lt;code&gt;AppInstance&lt;/code&gt;s that you want to return. | [optional] |
| **nextToken** | **String**| The token passed by previous API requests until you reach the maximum number of &lt;code&gt;AppInstance&lt;/code&gt;s. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListAppInstancesResponse**](ListAppInstancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listAttendeeTags"></a>
# **listAttendeeTags**
> ListAttendeeTagsResponse listAttendeeTags(meetingId, attendeeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Lists the tags applied to an Amazon Chime SDK attendee resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt;ListAttendeeTags is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String attendeeId = "attendeeId_example"; // String | The Amazon Chime SDK attendee ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListAttendeeTagsResponse result = apiInstance.listAttendeeTags(meetingId, attendeeId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAttendeeTags");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **attendeeId** | **String**| The Amazon Chime SDK attendee ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListAttendeeTagsResponse**](ListAttendeeTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listAttendees"></a>
# **listAttendees**
> ListAttendeesResponse listAttendees(meetingId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2)



&lt;p&gt; Lists the attendees for the specified Amazon Chime SDK meeting. For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListAttendees.html\&quot;&gt;ListAttendees&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListAttendeesResponse result = apiInstance.listAttendees(meetingId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAttendees");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListAttendeesResponse**](ListAttendeesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listBots"></a>
# **listBots**
> ListBotsResponse listBots(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



Lists the bots associated with the administrator&#39;s Amazon Chime Enterprise account ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call. The default is 10.
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListBotsResponse result = apiInstance.listBots(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBots");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. The default is 10. | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListBotsResponse**](ListBotsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceFailureException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | BadRequestException |  -  |
| **485** | NotFoundException |  -  |
| **486** | ThrottledClientException |  -  |

<a id="listChannelBans"></a>
# **listChannelBans**
> ListChannelBansResponse listChannelBans(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2)



&lt;p&gt;Lists all the users banned from a particular channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelBans.html\&quot;&gt;ListChannelBans&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of bans that you want returned.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested bans are returned.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelBansResponse result = apiInstance.listChannelBans(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelBans");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of bans that you want returned. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested bans are returned. | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelBansResponse**](ListChannelBansResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelMemberships"></a>
# **listChannelMemberships**
> ListChannelMembershipsResponse listChannelMemberships(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, type, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2)



&lt;p&gt;Lists all channel memberships in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMemberships.html\&quot;&gt;ListChannelMemberships&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The maximum number of channel memberships that you want returned.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String type = "DEFAULT"; // String | The membership type of a user, <code>DEFAULT</code> or <code>HIDDEN</code>. Default members are always returned as part of <code>ListChannelMemberships</code>. Hidden members are only returned if the type filter in <code>ListChannelMemberships</code> equals <code>HIDDEN</code>. Otherwise hidden members are not returned.
    Integer maxResults = 56; // Integer | The maximum number of channel memberships that you want returned.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested channel memberships are returned.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelMembershipsResponse result = apiInstance.listChannelMemberships(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, type, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelMemberships");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The maximum number of channel memberships that you want returned. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **type** | **String**| The membership type of a user, &lt;code&gt;DEFAULT&lt;/code&gt; or &lt;code&gt;HIDDEN&lt;/code&gt;. Default members are always returned as part of &lt;code&gt;ListChannelMemberships&lt;/code&gt;. Hidden members are only returned if the type filter in &lt;code&gt;ListChannelMemberships&lt;/code&gt; equals &lt;code&gt;HIDDEN&lt;/code&gt;. Otherwise hidden members are not returned. | [optional] [enum: DEFAULT, HIDDEN] |
| **maxResults** | **Integer**| The maximum number of channel memberships that you want returned. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested channel memberships are returned. | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelMembershipsResponse**](ListChannelMembershipsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelMembershipsForAppInstanceUser"></a>
# **listChannelMembershipsForAppInstanceUser**
> ListChannelMembershipsForAppInstanceUserResponse listChannelMembershipsForAppInstanceUser(scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, appInstanceUserArn, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2)



&lt;p&gt; Lists all channels that a particular &lt;code&gt;AppInstanceUser&lt;/code&gt; is a part of. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can call the API with a user ARN that is not their own. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html\&quot;&gt;ListChannelMembershipsForAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String scope = "app-instance-user-memberships"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the <code>AppInstanceUser</code>s
    Integer maxResults = 56; // Integer | The maximum number of users that you want returned.
    String nextToken = "nextToken_example"; // String | The token returned from previous API requests until the number of channel memberships is reached.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelMembershipsForAppInstanceUserResponse result = apiInstance.listChannelMembershipsForAppInstanceUser(scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, appInstanceUserArn, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelMembershipsForAppInstanceUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scope** | **String**|  | [enum: app-instance-user-memberships] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **appInstanceUserArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;s | [optional] |
| **maxResults** | **Integer**| The maximum number of users that you want returned. | [optional] |
| **nextToken** | **String**| The token returned from previous API requests until the number of channel memberships is reached. | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelMembershipsForAppInstanceUserResponse**](ListChannelMembershipsForAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelMessages"></a>
# **listChannelMessages**
> ListChannelMessagesResponse listChannelMessages(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, sortOrder, notBefore, notAfter, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2)



&lt;p&gt;List all the messages in a channel. Returns a paginated list of &lt;code&gt;ChannelMessages&lt;/code&gt;. By default, sorted by creation timestamp in descending order.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Redacted messages appear in the results as empty, since they are only redacted, not deleted. Deleted messages do not appear in the results. This action always returns the latest version of an edited message.&lt;/p&gt; &lt;p&gt;Also, the x-amz-chime-bearer request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelMessages.html\&quot;&gt;ListChannelMessages&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String sortOrder = "ASCENDING"; // String | The order in which you want messages sorted. Default is Descending, based on time created.
    OffsetDateTime notBefore = OffsetDateTime.now(); // OffsetDateTime | The initial or starting time stamp for your requested messages.
    OffsetDateTime notAfter = OffsetDateTime.now(); // OffsetDateTime | The final or ending time stamp for your requested messages.
    Integer maxResults = 56; // Integer | The maximum number of messages that you want returned.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested messages are returned.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelMessagesResponse result = apiInstance.listChannelMessages(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, sortOrder, notBefore, notAfter, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelMessages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **sortOrder** | **String**| The order in which you want messages sorted. Default is Descending, based on time created. | [optional] [enum: ASCENDING, DESCENDING] |
| **notBefore** | **OffsetDateTime**| The initial or starting time stamp for your requested messages. | [optional] |
| **notAfter** | **OffsetDateTime**| The final or ending time stamp for your requested messages. | [optional] |
| **maxResults** | **Integer**| The maximum number of messages that you want returned. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested messages are returned. | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelMessagesResponse**](ListChannelMessagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelModerators"></a>
# **listChannelModerators**
> ListChannelModeratorsResponse listChannelModerators(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2)



&lt;p&gt;Lists all the moderators for a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelModerators.html\&quot;&gt;ListChannelModerators&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of moderators that you want returned.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested moderators are returned.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelModeratorsResponse result = apiInstance.listChannelModerators(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelModerators");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of moderators that you want returned. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested moderators are returned. | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelModeratorsResponse**](ListChannelModeratorsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannels"></a>
# **listChannels**
> ListChannelsResponse listChannels(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, privacy, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2)



&lt;p&gt;Lists all Channels created under a single Chime App as a paginated list. You can specify filters to narrow results.&lt;/p&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Functionality &amp;amp; restrictions&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use privacy &#x3D; &lt;code&gt;PUBLIC&lt;/code&gt; to retrieve all public channels in the account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can set privacy &#x3D; &lt;code&gt;PRIVATE&lt;/code&gt; to list the private channels in an account.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannels.html\&quot;&gt;ListChannels&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String privacy = "PUBLIC"; // String | The privacy setting. <code>PUBLIC</code> retrieves all the public channels. <code>PRIVATE</code> retrieves private channels. Only an <code>AppInstanceAdmin</code> can retrieve private channels. 
    Integer maxResults = 56; // Integer | The maximum number of channels that you want to return.
    String nextToken = "nextToken_example"; // String | The token passed by previous API calls until all requested channels are returned.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelsResponse result = apiInstance.listChannels(appInstanceArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, privacy, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannels");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **privacy** | **String**| The privacy setting. &lt;code&gt;PUBLIC&lt;/code&gt; retrieves all the public channels. &lt;code&gt;PRIVATE&lt;/code&gt; retrieves private channels. Only an &lt;code&gt;AppInstanceAdmin&lt;/code&gt; can retrieve private channels.  | [optional] [enum: PUBLIC, PRIVATE] |
| **maxResults** | **Integer**| The maximum number of channels that you want to return. | [optional] |
| **nextToken** | **String**| The token passed by previous API calls until all requested channels are returned. | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelsResponse**](ListChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listChannelsModeratedByAppInstanceUser"></a>
# **listChannelsModeratedByAppInstanceUser**
> ListChannelsModeratedByAppInstanceUserResponse listChannelsModeratedByAppInstanceUser(scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, appInstanceUserArn, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2)



&lt;p&gt;A list of the channels moderated by an &lt;code&gt;AppInstanceUser&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListChannelsModeratedByAppInstanceUser.html\&quot;&gt;ListChannelsModeratedByAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String scope = "app-instance-user-moderated-channels"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the user in the moderated channel.
    Integer maxResults = 56; // Integer | The maximum number of channels in the request.
    String nextToken = "nextToken_example"; // String | The token returned from previous API requests until the number of channels moderated by the user is reached.
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListChannelsModeratedByAppInstanceUserResponse result = apiInstance.listChannelsModeratedByAppInstanceUser(scope, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, appInstanceUserArn, maxResults, nextToken, xAmzChimeBearer, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listChannelsModeratedByAppInstanceUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **scope** | **String**|  | [enum: app-instance-user-moderated-channels] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **appInstanceUserArn** | **String**| The ARN of the user in the moderated channel. | [optional] |
| **maxResults** | **Integer**| The maximum number of channels in the request. | [optional] |
| **nextToken** | **String**| The token returned from previous API requests until the number of channels moderated by the user is reached. | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListChannelsModeratedByAppInstanceUserResponse**](ListChannelsModeratedByAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listMediaCapturePipelines"></a>
# **listMediaCapturePipelines**
> ListMediaCapturePipelinesResponse listMediaCapturePipelines(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2)



&lt;p&gt;Returns a list of media capture pipelines.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_media-pipelines-chime_ListMediaCapturePipelines.html\&quot;&gt;ListMediaCapturePipelines&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token used to retrieve the next page of results.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call. Valid Range: 1 - 99.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListMediaCapturePipelinesResponse result = apiInstance.listMediaCapturePipelines(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listMediaCapturePipelines");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token used to retrieve the next page of results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. Valid Range: 1 - 99. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListMediaCapturePipelinesResponse**](ListMediaCapturePipelinesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listMeetingTags"></a>
# **listMeetingTags**
> ListMeetingTagsResponse listMeetingTags(meetingId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Lists the tags applied to an Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListMeetingTagsResponse result = apiInstance.listMeetingTags(meetingId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listMeetingTags");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListMeetingTagsResponse**](ListMeetingTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listMeetings"></a>
# **listMeetings**
> ListMeetingsResponse listMeetings(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2)



&lt;p&gt;Lists up to 100 active Amazon Chime SDK meetings.&lt;/p&gt; &lt;important&gt; &lt;p&gt;ListMeetings is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about the Amazon Chime SDK, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meetings-sdk.html\&quot;&gt;Using the Amazon Chime SDK&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListMeetingsResponse result = apiInstance.listMeetings(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listMeetings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListMeetingsResponse**](ListMeetingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listPhoneNumberOrders"></a>
# **listPhoneNumberOrders**
> ListPhoneNumberOrdersResponse listPhoneNumberOrders(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2)



Lists the phone number orders for the administrator&#39;s Amazon Chime account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListPhoneNumberOrdersResponse result = apiInstance.listPhoneNumberOrders(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPhoneNumberOrders");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListPhoneNumberOrdersResponse**](ListPhoneNumberOrdersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listPhoneNumbers"></a>
# **listPhoneNumbers**
> ListPhoneNumbersResponse listPhoneNumbers(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, status, productType, filterName, filterValue, maxResults, nextToken, maxResults2, nextToken2)



Lists the phone numbers for the specified Amazon Chime account, Amazon Chime user, Amazon Chime Voice Connector, or Amazon Chime Voice Connector group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String status = "AcquireInProgress"; // String | The phone number status.
    String productType = "BusinessCalling"; // String | The phone number product type.
    String filterName = "AccountId"; // String | The filter to use to limit the number of results.
    String filterValue = "filterValue_example"; // String | The value to use for the filter.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call.
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListPhoneNumbersResponse result = apiInstance.listPhoneNumbers(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, status, productType, filterName, filterValue, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPhoneNumbers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **status** | **String**| The phone number status. | [optional] [enum: AcquireInProgress, AcquireFailed, Unassigned, Assigned, ReleaseInProgress, DeleteInProgress, ReleaseFailed, DeleteFailed] |
| **productType** | **String**| The phone number product type. | [optional] [enum: BusinessCalling, VoiceConnector, SipMediaApplicationDialIn] |
| **filterName** | **String**| The filter to use to limit the number of results. | [optional] [enum: AccountId, UserId, VoiceConnectorId, VoiceConnectorGroupId, SipRuleId] |
| **filterValue** | **String**| The value to use for the filter. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListPhoneNumbersResponse**](ListPhoneNumbersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | NotFoundException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listProxySessions"></a>
# **listProxySessions**
> ListProxySessionsResponse listProxySessions(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, status, nextToken, maxResults, maxResults2, nextToken2)



&lt;p&gt;Lists the proxy sessions for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListProxySessions.html\&quot;&gt;ListProxySessions&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String status = "Open"; // String | The proxy session status.
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListProxySessionsResponse result = apiInstance.listProxySessions(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, status, nextToken, maxResults, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listProxySessions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **status** | **String**| The proxy session status. | [optional] [enum: Open, InProgress, Closed] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListProxySessionsResponse**](ListProxySessionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listRoomMemberships"></a>
# **listRoomMemberships**
> ListRoomMembershipsResponse listRoomMemberships(accountId, roomId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



Lists the membership details for the specified room in an Amazon Chime Enterprise account, such as the members&#39; IDs, email addresses, and names.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String roomId = "roomId_example"; // String | The room ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call.
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListRoomMembershipsResponse result = apiInstance.listRoomMemberships(accountId, roomId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRoomMemberships");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **roomId** | **String**| The room ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListRoomMembershipsResponse**](ListRoomMembershipsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listRooms"></a>
# **listRooms**
> ListRoomsResponse listRooms(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, memberId, maxResults, nextToken, maxResults2, nextToken2)



Lists the room details for the specified Amazon Chime Enterprise account. Optionally, filter the results by a member ID (user ID or bot ID) to see a list of rooms that the member belongs to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String memberId = "memberId_example"; // String | The member ID (user ID or bot ID).
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call.
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListRoomsResponse result = apiInstance.listRooms(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, memberId, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRooms");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **memberId** | **String**| The member ID (user ID or bot ID). | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListRoomsResponse**](ListRoomsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listSipMediaApplications"></a>
# **listSipMediaApplications**
> ListSipMediaApplicationsResponse listSipMediaApplications(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2)



&lt;p&gt;Lists the SIP media applications under the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipMediaApplications.html\&quot;&gt;ListSipMediaApplications&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call. Defaults to 100.
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListSipMediaApplicationsResponse result = apiInstance.listSipMediaApplications(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSipMediaApplications");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. Defaults to 100. | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListSipMediaApplicationsResponse**](ListSipMediaApplicationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listSipRules"></a>
# **listSipRules**
> ListSipRulesResponse listSipRules(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, sipMediaApplication, maxResults, nextToken, maxResults2, nextToken2)



&lt;p&gt;Lists the SIP rules under the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListSipRules.html\&quot;&gt;ListSipRules&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String sipMediaApplication = "sipMediaApplication_example"; // String | The SIP media application ID.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call. Defaults to 100.
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListSipRulesResponse result = apiInstance.listSipRules(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, sipMediaApplication, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSipRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **sipMediaApplication** | **String**| The SIP media application ID. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. Defaults to 100. | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListSipRulesResponse**](ListSipRulesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listSupportedPhoneNumberCountries"></a>
# **listSupportedPhoneNumberCountries**
> ListSupportedPhoneNumberCountriesResponse listSupportedPhoneNumberCountries(productType, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Lists supported phone number countries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String productType = "BusinessCalling"; // String | The phone number product type.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListSupportedPhoneNumberCountriesResponse result = apiInstance.listSupportedPhoneNumberCountries(productType, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSupportedPhoneNumberCountries");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **productType** | **String**| The phone number product type. | [enum: BusinessCalling, VoiceConnector, SipMediaApplicationDialIn] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListSupportedPhoneNumberCountriesResponse**](ListSupportedPhoneNumberCountriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | AccessDeniedException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listTagsForResource"></a>
# **listTagsForResource**
> ListTagsForResourceResponse listTagsForResource(arn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Lists the tags applied to an Amazon Chime SDK meeting and messaging resources.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the applicable latest version in the Amazon Chime SDK.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;For meetings: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For messaging: &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListTagsForResource.html\&quot;&gt;ListTagsForResource&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String arn = "arn_example"; // String | The resource ARN.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListTagsForResourceResponse result = apiInstance.listTagsForResource(arn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listTagsForResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **arn** | **String**| The resource ARN. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listUsers"></a>
# **listUsers**
> ListUsersResponse listUsers(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, userEmail, userType, maxResults, nextToken, maxResults2, nextToken2)



Lists the users that belong to the specified Amazon Chime account. You can specify an email address to list only the user that the email address belongs to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String userEmail = "userEmail_example"; // String | Optional. The user email address used to filter results. Maximum 1.
    String userType = "PrivateUser"; // String | The user type.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call. Defaults to 100.
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListUsersResponse result = apiInstance.listUsers(accountId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, userEmail, userType, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listUsers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **userEmail** | **String**| Optional. The user email address used to filter results. Maximum 1. | [optional] |
| **userType** | **String**| The user type. | [optional] [enum: PrivateUser, SharedDevice] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. Defaults to 100. | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listVoiceConnectorGroups"></a>
# **listVoiceConnectorGroups**
> ListVoiceConnectorGroupsResponse listVoiceConnectorGroups(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2)



&lt;p&gt;Lists the Amazon Chime Voice Connector groups for the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorGroups.html\&quot;&gt;ListVoiceConnectorGroups&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListVoiceConnectorGroupsResponse result = apiInstance.listVoiceConnectorGroups(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listVoiceConnectorGroups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListVoiceConnectorGroupsResponse**](ListVoiceConnectorGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="listVoiceConnectorTerminationCredentials"></a>
# **listVoiceConnectorTerminationCredentials**
> ListVoiceConnectorTerminationCredentialsResponse listVoiceConnectorTerminationCredentials(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Lists the SIP credentials for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectorTerminationCredentials.html\&quot;&gt;ListVoiceConnectorTerminationCredentials&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ListVoiceConnectorTerminationCredentialsResponse result = apiInstance.listVoiceConnectorTerminationCredentials(voiceConnectorId, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listVoiceConnectorTerminationCredentials");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ListVoiceConnectorTerminationCredentialsResponse**](ListVoiceConnectorTerminationCredentialsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="listVoiceConnectors"></a>
# **listVoiceConnectors**
> ListVoiceConnectorsResponse listVoiceConnectors(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2)



&lt;p&gt;Lists the Amazon Chime Voice Connectors for the administrator&#39;s AWS account.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ListVoiceConnectors.html\&quot;&gt;ListVoiceConnectors&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String nextToken = "nextToken_example"; // String | The token to use to retrieve the next page of results.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      ListVoiceConnectorsResponse result = apiInstance.listVoiceConnectors(xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, nextToken, maxResults, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listVoiceConnectors");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **nextToken** | **String**| The token to use to retrieve the next page of results. | [optional] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**ListVoiceConnectorsResponse**](ListVoiceConnectorsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="logoutUser"></a>
# **logoutUser**
> Object logoutUser(accountId, userId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Logs out the specified user from all of the devices they are currently logged into.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String userId = "userId_example"; // String | The user ID.
    String operation = "logout"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.logoutUser(accountId, userId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#logoutUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **userId** | **String**| The user ID. | |
| **operation** | **String**|  | [enum: logout] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="putAppInstanceRetentionSettings"></a>
# **putAppInstanceRetentionSettings**
> PutAppInstanceRetentionSettingsResponse putAppInstanceRetentionSettings(appInstanceArn, putAppInstanceRetentionSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Sets the amount of time in days that a given &lt;code&gt;AppInstance&lt;/code&gt; retains data.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_PutAppInstanceRetentionSettings.html\&quot;&gt;PutAppInstanceRetentionSettings&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    PutAppInstanceRetentionSettingsRequest putAppInstanceRetentionSettingsRequest = new PutAppInstanceRetentionSettingsRequest(); // PutAppInstanceRetentionSettingsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutAppInstanceRetentionSettingsResponse result = apiInstance.putAppInstanceRetentionSettings(appInstanceArn, putAppInstanceRetentionSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putAppInstanceRetentionSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **putAppInstanceRetentionSettingsRequest** | [**PutAppInstanceRetentionSettingsRequest**](PutAppInstanceRetentionSettingsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutAppInstanceRetentionSettingsResponse**](PutAppInstanceRetentionSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="putAppInstanceStreamingConfigurations"></a>
# **putAppInstanceStreamingConfigurations**
> PutAppInstanceStreamingConfigurationsResponse putAppInstanceStreamingConfigurations(appInstanceArn, putAppInstanceStreamingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;The data streaming configurations of an &lt;code&gt;AppInstance&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutMessagingStreamingConfigurations.html\&quot;&gt;PutMessagingStreamingConfigurations&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    PutAppInstanceStreamingConfigurationsRequest putAppInstanceStreamingConfigurationsRequest = new PutAppInstanceStreamingConfigurationsRequest(); // PutAppInstanceStreamingConfigurationsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutAppInstanceStreamingConfigurationsResponse result = apiInstance.putAppInstanceStreamingConfigurations(appInstanceArn, putAppInstanceStreamingConfigurationsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putAppInstanceStreamingConfigurations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **putAppInstanceStreamingConfigurationsRequest** | [**PutAppInstanceStreamingConfigurationsRequest**](PutAppInstanceStreamingConfigurationsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutAppInstanceStreamingConfigurationsResponse**](PutAppInstanceStreamingConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | BadRequestException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="putEventsConfiguration"></a>
# **putEventsConfiguration**
> PutEventsConfigurationResponse putEventsConfiguration(accountId, botId, putEventsConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Creates an events configuration that allows a bot to receive outgoing events sent by Amazon Chime. Choose either an HTTPS endpoint or a Lambda function ARN. For more information, see &lt;a&gt;Bot&lt;/a&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String botId = "botId_example"; // String | The bot ID.
    PutEventsConfigurationRequest putEventsConfigurationRequest = new PutEventsConfigurationRequest(); // PutEventsConfigurationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutEventsConfigurationResponse result = apiInstance.putEventsConfiguration(accountId, botId, putEventsConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putEventsConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **botId** | **String**| The bot ID. | |
| **putEventsConfigurationRequest** | [**PutEventsConfigurationRequest**](PutEventsConfigurationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutEventsConfigurationResponse**](PutEventsConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceFailureException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ResourceLimitExceededException |  -  |
| **486** | NotFoundException |  -  |

<a id="putRetentionSettings"></a>
# **putRetentionSettings**
> PutRetentionSettingsResponse putRetentionSettings(accountId, putRetentionSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt; Puts retention settings for the specified Amazon Chime Enterprise account. We recommend using AWS CloudTrail to monitor usage of this API for your account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/cloudtrail.html\&quot;&gt;Logging Amazon Chime API Calls with AWS CloudTrail&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; To turn off existing retention settings, remove the number of days from the corresponding &lt;b&gt;RetentionDays&lt;/b&gt; field in the &lt;b&gt;RetentionSettings&lt;/b&gt; object. For more information about retention settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/chat-retention.html\&quot;&gt;Managing Chat Retention Policies&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    PutRetentionSettingsRequest putRetentionSettingsRequest = new PutRetentionSettingsRequest(); // PutRetentionSettingsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutRetentionSettingsResponse result = apiInstance.putRetentionSettings(accountId, putRetentionSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putRetentionSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **putRetentionSettingsRequest** | [**PutRetentionSettingsRequest**](PutRetentionSettingsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutRetentionSettingsResponse**](PutRetentionSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="putSipMediaApplicationLoggingConfiguration"></a>
# **putSipMediaApplicationLoggingConfiguration**
> PutSipMediaApplicationLoggingConfigurationResponse putSipMediaApplicationLoggingConfiguration(sipMediaApplicationId, putSipMediaApplicationLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the logging configuration for the specified SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutSipMediaApplicationLoggingConfiguration.html\&quot;&gt;PutSipMediaApplicationLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The SIP media application ID.
    PutSipMediaApplicationLoggingConfigurationRequest putSipMediaApplicationLoggingConfigurationRequest = new PutSipMediaApplicationLoggingConfigurationRequest(); // PutSipMediaApplicationLoggingConfigurationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutSipMediaApplicationLoggingConfigurationResponse result = apiInstance.putSipMediaApplicationLoggingConfiguration(sipMediaApplicationId, putSipMediaApplicationLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putSipMediaApplicationLoggingConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sipMediaApplicationId** | **String**| The SIP media application ID. | |
| **putSipMediaApplicationLoggingConfigurationRequest** | [**PutSipMediaApplicationLoggingConfigurationRequest**](PutSipMediaApplicationLoggingConfigurationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutSipMediaApplicationLoggingConfigurationResponse**](PutSipMediaApplicationLoggingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="putVoiceConnectorEmergencyCallingConfiguration"></a>
# **putVoiceConnectorEmergencyCallingConfiguration**
> PutVoiceConnectorEmergencyCallingConfigurationResponse putVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, putVoiceConnectorEmergencyCallingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Puts emergency calling configuration details to the specified Amazon Chime Voice Connector, such as emergency phone numbers and calling countries. Origination and termination settings must be enabled for the Amazon Chime Voice Connector before emergency calling can be configured.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorEmergencyCallingConfiguration.html\&quot;&gt;PutVoiceConnectorEmergencyCallingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    PutVoiceConnectorEmergencyCallingConfigurationRequest putVoiceConnectorEmergencyCallingConfigurationRequest = new PutVoiceConnectorEmergencyCallingConfigurationRequest(); // PutVoiceConnectorEmergencyCallingConfigurationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutVoiceConnectorEmergencyCallingConfigurationResponse result = apiInstance.putVoiceConnectorEmergencyCallingConfiguration(voiceConnectorId, putVoiceConnectorEmergencyCallingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putVoiceConnectorEmergencyCallingConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **putVoiceConnectorEmergencyCallingConfigurationRequest** | [**PutVoiceConnectorEmergencyCallingConfigurationRequest**](PutVoiceConnectorEmergencyCallingConfigurationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutVoiceConnectorEmergencyCallingConfigurationResponse**](PutVoiceConnectorEmergencyCallingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="putVoiceConnectorLoggingConfiguration"></a>
# **putVoiceConnectorLoggingConfiguration**
> PutVoiceConnectorLoggingConfigurationResponse putVoiceConnectorLoggingConfiguration(voiceConnectorId, putVoiceConnectorLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Adds a logging configuration for the specified Amazon Chime Voice Connector. The logging configuration specifies whether SIP message logs are enabled for sending to Amazon CloudWatch Logs.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorLoggingConfiguration.html\&quot;&gt;PutVoiceConnectorLoggingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    PutVoiceConnectorLoggingConfigurationRequest putVoiceConnectorLoggingConfigurationRequest = new PutVoiceConnectorLoggingConfigurationRequest(); // PutVoiceConnectorLoggingConfigurationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutVoiceConnectorLoggingConfigurationResponse result = apiInstance.putVoiceConnectorLoggingConfiguration(voiceConnectorId, putVoiceConnectorLoggingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putVoiceConnectorLoggingConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **putVoiceConnectorLoggingConfigurationRequest** | [**PutVoiceConnectorLoggingConfigurationRequest**](PutVoiceConnectorLoggingConfigurationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutVoiceConnectorLoggingConfigurationResponse**](PutVoiceConnectorLoggingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="putVoiceConnectorOrigination"></a>
# **putVoiceConnectorOrigination**
> PutVoiceConnectorOriginationResponse putVoiceConnectorOrigination(voiceConnectorId, putVoiceConnectorOriginationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Adds origination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to turning off origination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorOrigination.html\&quot;&gt;PutVoiceConnectorOrigination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    PutVoiceConnectorOriginationRequest putVoiceConnectorOriginationRequest = new PutVoiceConnectorOriginationRequest(); // PutVoiceConnectorOriginationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutVoiceConnectorOriginationResponse result = apiInstance.putVoiceConnectorOrigination(voiceConnectorId, putVoiceConnectorOriginationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putVoiceConnectorOrigination");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **putVoiceConnectorOriginationRequest** | [**PutVoiceConnectorOriginationRequest**](PutVoiceConnectorOriginationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutVoiceConnectorOriginationResponse**](PutVoiceConnectorOriginationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="putVoiceConnectorProxy"></a>
# **putVoiceConnectorProxy**
> PutVoiceConnectorProxyResponse putVoiceConnectorProxy(voiceConnectorId, putVoiceConnectorProxyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Puts the specified proxy configuration to the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorProxy.html\&quot;&gt;PutVoiceConnectorProxy&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
    PutVoiceConnectorProxyRequest putVoiceConnectorProxyRequest = new PutVoiceConnectorProxyRequest(); // PutVoiceConnectorProxyRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutVoiceConnectorProxyResponse result = apiInstance.putVoiceConnectorProxy(voiceConnectorId, putVoiceConnectorProxyRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putVoiceConnectorProxy");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | |
| **putVoiceConnectorProxyRequest** | [**PutVoiceConnectorProxyRequest**](PutVoiceConnectorProxyRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutVoiceConnectorProxyResponse**](PutVoiceConnectorProxyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | AccessDeniedException |  -  |
| **482** | NotFoundException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | BadRequestException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="putVoiceConnectorStreamingConfiguration"></a>
# **putVoiceConnectorStreamingConfiguration**
> PutVoiceConnectorStreamingConfigurationResponse putVoiceConnectorStreamingConfiguration(voiceConnectorId, putVoiceConnectorStreamingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Adds a streaming configuration for the specified Amazon Chime Voice Connector. The streaming configuration specifies whether media streaming is enabled for sending to Kinesis. It also sets the retention period, in hours, for the Amazon Kinesis data.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorStreamingConfiguration.html\&quot;&gt;PutVoiceConnectorStreamingConfiguration&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    PutVoiceConnectorStreamingConfigurationRequest putVoiceConnectorStreamingConfigurationRequest = new PutVoiceConnectorStreamingConfigurationRequest(); // PutVoiceConnectorStreamingConfigurationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutVoiceConnectorStreamingConfigurationResponse result = apiInstance.putVoiceConnectorStreamingConfiguration(voiceConnectorId, putVoiceConnectorStreamingConfigurationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putVoiceConnectorStreamingConfiguration");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **putVoiceConnectorStreamingConfigurationRequest** | [**PutVoiceConnectorStreamingConfigurationRequest**](PutVoiceConnectorStreamingConfigurationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutVoiceConnectorStreamingConfigurationResponse**](PutVoiceConnectorStreamingConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="putVoiceConnectorTermination"></a>
# **putVoiceConnectorTermination**
> PutVoiceConnectorTerminationResponse putVoiceConnectorTermination(voiceConnectorId, putVoiceConnectorTerminationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Adds termination settings for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;note&gt; &lt;p&gt;If emergency calling is configured for the Amazon Chime Voice Connector, it must be deleted prior to turning off termination settings.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTermination.html\&quot;&gt;PutVoiceConnectorTermination&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    PutVoiceConnectorTerminationRequest putVoiceConnectorTerminationRequest = new PutVoiceConnectorTerminationRequest(); // PutVoiceConnectorTerminationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      PutVoiceConnectorTerminationResponse result = apiInstance.putVoiceConnectorTermination(voiceConnectorId, putVoiceConnectorTerminationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putVoiceConnectorTermination");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **putVoiceConnectorTerminationRequest** | [**PutVoiceConnectorTerminationRequest**](PutVoiceConnectorTerminationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**PutVoiceConnectorTerminationResponse**](PutVoiceConnectorTerminationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | AccessDeniedException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="putVoiceConnectorTerminationCredentials"></a>
# **putVoiceConnectorTerminationCredentials**
> putVoiceConnectorTerminationCredentials(voiceConnectorId, operation, putVoiceConnectorTerminationCredentialsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Adds termination SIP credentials for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_PutVoiceConnectorTerminationCredentials.html\&quot;&gt;PutVoiceConnectorTerminationCredentials&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    String operation = "put"; // String | 
    PutVoiceConnectorTerminationCredentialsRequest putVoiceConnectorTerminationCredentialsRequest = new PutVoiceConnectorTerminationCredentialsRequest(); // PutVoiceConnectorTerminationCredentialsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.putVoiceConnectorTerminationCredentials(voiceConnectorId, operation, putVoiceConnectorTerminationCredentialsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#putVoiceConnectorTerminationCredentials");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **operation** | **String**|  | [enum: put] |
| **putVoiceConnectorTerminationCredentialsRequest** | [**PutVoiceConnectorTerminationCredentialsRequest**](PutVoiceConnectorTerminationCredentialsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="redactChannelMessage"></a>
# **redactChannelMessage**
> RedactChannelMessageResponse redactChannelMessage(channelArn, messageId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Redacts message content, but not metadata. The message exists in the back end, but the action returns null content, and the state shows as redacted.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_RedactChannelMessage.html\&quot;&gt;RedactChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel containing the messages that you want to redact.
    String messageId = "messageId_example"; // String | The ID of the message being redacted.
    String operation = "redact"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      RedactChannelMessageResponse result = apiInstance.redactChannelMessage(channelArn, messageId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#redactChannelMessage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel containing the messages that you want to redact. | |
| **messageId** | **String**| The ID of the message being redacted. | |
| **operation** | **String**|  | [enum: redact] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**RedactChannelMessageResponse**](RedactChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="redactConversationMessage"></a>
# **redactConversationMessage**
> Object redactConversationMessage(accountId, conversationId, messageId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Redacts the specified message from the specified Amazon Chime conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String conversationId = "conversationId_example"; // String | The conversation ID.
    String messageId = "messageId_example"; // String | The message ID.
    String operation = "redact"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.redactConversationMessage(accountId, conversationId, messageId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#redactConversationMessage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **conversationId** | **String**| The conversation ID. | |
| **messageId** | **String**| The message ID. | |
| **operation** | **String**|  | [enum: redact] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | BadRequestException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="redactRoomMessage"></a>
# **redactRoomMessage**
> Object redactRoomMessage(accountId, roomId, messageId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Redacts the specified message from the specified Amazon Chime channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String roomId = "roomId_example"; // String | The room ID.
    String messageId = "messageId_example"; // String | The message ID.
    String operation = "redact"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.redactRoomMessage(accountId, roomId, messageId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#redactRoomMessage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **roomId** | **String**| The room ID. | |
| **messageId** | **String**| The message ID. | |
| **operation** | **String**|  | [enum: redact] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | UnauthorizedClientException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | BadRequestException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="regenerateSecurityToken"></a>
# **regenerateSecurityToken**
> RegenerateSecurityTokenResponse regenerateSecurityToken(accountId, botId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Regenerates the security token for a bot.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String botId = "botId_example"; // String | The bot ID.
    String operation = "regenerate-security-token"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      RegenerateSecurityTokenResponse result = apiInstance.regenerateSecurityToken(accountId, botId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#regenerateSecurityToken");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **botId** | **String**| The bot ID. | |
| **operation** | **String**|  | [enum: regenerate-security-token] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**RegenerateSecurityTokenResponse**](RegenerateSecurityTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceFailureException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | NotFoundException |  -  |
| **486** | ThrottledClientException |  -  |

<a id="resetPersonalPIN"></a>
# **resetPersonalPIN**
> ResetPersonalPINResponse resetPersonalPIN(accountId, userId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Resets the personal meeting PIN for the specified user on an Amazon Chime account. Returns the &lt;a&gt;User&lt;/a&gt; object with the updated personal meeting PIN.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String userId = "userId_example"; // String | The user ID.
    String operation = "reset-personal-pin"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ResetPersonalPINResponse result = apiInstance.resetPersonalPIN(accountId, userId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#resetPersonalPIN");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **userId** | **String**| The user ID. | |
| **operation** | **String**|  | [enum: reset-personal-pin] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ResetPersonalPINResponse**](ResetPersonalPINResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="restorePhoneNumber"></a>
# **restorePhoneNumber**
> RestorePhoneNumberResponse restorePhoneNumber(phoneNumberId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Moves a phone number from the &lt;b&gt;Deletion queue&lt;/b&gt; back into the phone number &lt;b&gt;Inventory&lt;/b&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String phoneNumberId = "phoneNumberId_example"; // String | The phone number.
    String operation = "restore"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      RestorePhoneNumberResponse result = apiInstance.restorePhoneNumber(phoneNumberId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restorePhoneNumber");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **phoneNumberId** | **String**| The phone number. | |
| **operation** | **String**|  | [enum: restore] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**RestorePhoneNumberResponse**](RestorePhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ResourceLimitExceededException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="searchAvailablePhoneNumbers"></a>
# **searchAvailablePhoneNumbers**
> SearchAvailablePhoneNumbersResponse searchAvailablePhoneNumbers(type, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, areaCode, city, country, state, tollFreePrefix, phoneNumberType, maxResults, nextToken, maxResults2, nextToken2)



Searches for phone numbers that can be ordered. For US numbers, provide at least one of the following search filters: &lt;code&gt;AreaCode&lt;/code&gt;, &lt;code&gt;City&lt;/code&gt;, &lt;code&gt;State&lt;/code&gt;, or &lt;code&gt;TollFreePrefix&lt;/code&gt;. If you provide &lt;code&gt;City&lt;/code&gt;, you must also provide &lt;code&gt;State&lt;/code&gt;. Numbers outside the US only support the &lt;code&gt;PhoneNumberType&lt;/code&gt; filter, which you must use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "phone-numbers"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String areaCode = "areaCode_example"; // String | The area code used to filter results. Only applies to the US.
    String city = "city_example"; // String | The city used to filter results. Only applies to the US.
    String country = "country_example"; // String | The country used to filter results. Defaults to the US Format: ISO 3166-1 alpha-2.
    String state = "state_example"; // String | The state used to filter results. Required only if you provide <code>City</code>. Only applies to the US.
    String tollFreePrefix = "tollFreePrefix_example"; // String | The toll-free prefix that you use to filter results. Only applies to the US.
    String phoneNumberType = "Local"; // String | The phone number type used to filter results. Required for non-US numbers.
    Integer maxResults = 56; // Integer | The maximum number of results to return in a single call.
    String nextToken = "nextToken_example"; // String | The token used to retrieve the next page of results.
    String maxResults2 = "maxResults_example"; // String | Pagination limit
    String nextToken2 = "nextToken_example"; // String | Pagination token
    try {
      SearchAvailablePhoneNumbersResponse result = apiInstance.searchAvailablePhoneNumbers(type, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, areaCode, city, country, state, tollFreePrefix, phoneNumberType, maxResults, nextToken, maxResults2, nextToken2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#searchAvailablePhoneNumbers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**|  | [enum: phone-numbers] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **areaCode** | **String**| The area code used to filter results. Only applies to the US. | [optional] |
| **city** | **String**| The city used to filter results. Only applies to the US. | [optional] |
| **country** | **String**| The country used to filter results. Defaults to the US Format: ISO 3166-1 alpha-2. | [optional] |
| **state** | **String**| The state used to filter results. Required only if you provide &lt;code&gt;City&lt;/code&gt;. Only applies to the US. | [optional] |
| **tollFreePrefix** | **String**| The toll-free prefix that you use to filter results. Only applies to the US. | [optional] |
| **phoneNumberType** | **String**| The phone number type used to filter results. Required for non-US numbers. | [optional] [enum: Local, TollFree] |
| **maxResults** | **Integer**| The maximum number of results to return in a single call. | [optional] |
| **nextToken** | **String**| The token used to retrieve the next page of results. | [optional] |
| **maxResults2** | **String**| Pagination limit | [optional] |
| **nextToken2** | **String**| Pagination token | [optional] |

### Return type

[**SearchAvailablePhoneNumbersResponse**](SearchAvailablePhoneNumbersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | AccessDeniedException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="sendChannelMessage"></a>
# **sendChannelMessage**
> SendChannelMessageResponse sendChannelMessage(channelArn, sendChannelMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Sends a message to a particular channel that the member is a part of.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;p&gt;Also, &lt;code&gt;STANDARD&lt;/code&gt; messages can contain 4KB of data and the 1KB of metadata. &lt;code&gt;CONTROL&lt;/code&gt; messages can contain 30 bytes of data and no metadata.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SendChannelMessage.html\&quot;&gt;SendChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    SendChannelMessageRequest sendChannelMessageRequest = new SendChannelMessageRequest(); // SendChannelMessageRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      SendChannelMessageResponse result = apiInstance.sendChannelMessage(channelArn, sendChannelMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendChannelMessage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **sendChannelMessageRequest** | [**SendChannelMessageRequest**](SendChannelMessageRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**SendChannelMessageResponse**](SendChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="startMeetingTranscription"></a>
# **startMeetingTranscription**
> Object startMeetingTranscription(meetingId, operation, startMeetingTranscriptionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Starts transcription for the specified &lt;code&gt;meetingId&lt;/code&gt;. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-transcription.html\&quot;&gt; Using Amazon Chime SDK live transcription &lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you specify an invalid configuration, a &lt;code&gt;TranscriptFailed&lt;/code&gt; event will be sent with the contents of the &lt;code&gt;BadRequestException&lt;/code&gt; generated by Amazon Transcribe. For more information on each parameter and which combinations are valid, refer to the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_StartStreamTranscription.html\&quot;&gt;StartStreamTranscription&lt;/a&gt; API in the &lt;i&gt;Amazon Transcribe Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Chime SDK live transcription is powered by Amazon Transcribe. Use of Amazon Transcribe is subject to the &lt;a href&#x3D;\&quot;https://aws.amazon.com/service-terms/\&quot;&gt;AWS Service Terms&lt;/a&gt;, including the terms specific to the AWS Machine Learning and Artificial Intelligence Services.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StartMeetingTranscription.html\&quot;&gt;StartMeetingTranscription&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The unique ID of the meeting being transcribed.
    String operation = "start"; // String | 
    StartMeetingTranscriptionRequest startMeetingTranscriptionRequest = new StartMeetingTranscriptionRequest(); // StartMeetingTranscriptionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.startMeetingTranscription(meetingId, operation, startMeetingTranscriptionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startMeetingTranscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The unique ID of the meeting being transcribed. | |
| **operation** | **String**|  | [enum: start] |
| **startMeetingTranscriptionRequest** | [**StartMeetingTranscriptionRequest**](StartMeetingTranscriptionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | NotFoundException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ResourceLimitExceededException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | UnauthorizedClientException |  -  |
| **486** | UnprocessableEntityException |  -  |
| **487** | ServiceUnavailableException |  -  |
| **488** | ServiceFailureException |  -  |

<a id="stopMeetingTranscription"></a>
# **stopMeetingTranscription**
> Object stopMeetingTranscription(meetingId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Stops transcription for the specified &lt;code&gt;meetingId&lt;/code&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StopMeetingTranscription.html\&quot;&gt;StopMeetingTranscription&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The unique ID of the meeting for which you stop transcription.
    String operation = "stop"; // String | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.stopMeetingTranscription(meetingId, operation, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopMeetingTranscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The unique ID of the meeting for which you stop transcription. | |
| **operation** | **String**|  | [enum: stop] |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ForbiddenException |  -  |
| **481** | NotFoundException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | UnprocessableEntityException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="tagAttendee"></a>
# **tagAttendee**
> tagAttendee(meetingId, attendeeId, operation, tagAttendeeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Applies the specified tags to the specified Amazon Chime attendee.&lt;/p&gt; &lt;important&gt; &lt;p&gt;TagAttendee is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String attendeeId = "attendeeId_example"; // String | The Amazon Chime SDK attendee ID.
    String operation = "add"; // String | 
    TagAttendeeRequest tagAttendeeRequest = new TagAttendeeRequest(); // TagAttendeeRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.tagAttendee(meetingId, attendeeId, operation, tagAttendeeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagAttendee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **attendeeId** | **String**| The Amazon Chime SDK attendee ID. | |
| **operation** | **String**|  | [enum: add] |
| **tagAttendeeRequest** | [**TagAttendeeRequest**](TagAttendeeRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | ResourceLimitExceededException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | UnauthorizedClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="tagMeeting"></a>
# **tagMeeting**
> tagMeeting(meetingId, operation, tagMeetingRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Applies the specified tags to the specified Amazon Chime SDK meeting.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String operation = "add"; // String | 
    TagMeetingRequest tagMeetingRequest = new TagMeetingRequest(); // TagMeetingRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.tagMeeting(meetingId, operation, tagMeetingRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagMeeting");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **operation** | **String**|  | [enum: add] |
| **tagMeetingRequest** | [**TagMeetingRequest**](TagMeetingRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | ResourceLimitExceededException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | UnauthorizedClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="tagResource"></a>
# **tagResource**
> tagResource(operation, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Applies the specified tags to the specified Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operation = "tag-resource"; // String | 
    TagResourceRequest tagResourceRequest = new TagResourceRequest(); // TagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.tagResource(operation, tagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#tagResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **operation** | **String**|  | [enum: tag-resource] |
| **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="untagAttendee"></a>
# **untagAttendee**
> untagAttendee(meetingId, attendeeId, operation, untagAttendeeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Untags the specified tags from the specified Amazon Chime SDK attendee.&lt;/p&gt; &lt;important&gt; &lt;p&gt;UntagAttendee is not supported in the Amazon Chime SDK Meetings Namespace. Update your application to remove calls to this API.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String attendeeId = "attendeeId_example"; // String | The Amazon Chime SDK attendee ID.
    String operation = "delete"; // String | 
    UntagAttendeeRequest untagAttendeeRequest = new UntagAttendeeRequest(); // UntagAttendeeRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.untagAttendee(meetingId, attendeeId, operation, untagAttendeeRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagAttendee");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **attendeeId** | **String**| The Amazon Chime SDK attendee ID. | |
| **operation** | **String**|  | [enum: delete] |
| **untagAttendeeRequest** | [**UntagAttendeeRequest**](UntagAttendeeRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | NotFoundException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="untagMeeting"></a>
# **untagMeeting**
> untagMeeting(meetingId, operation, untagMeetingRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Untags the specified tags from the specified Amazon Chime SDK meeting.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String meetingId = "meetingId_example"; // String | The Amazon Chime SDK meeting ID.
    String operation = "delete"; // String | 
    UntagMeetingRequest untagMeetingRequest = new UntagMeetingRequest(); // UntagMeetingRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.untagMeeting(meetingId, operation, untagMeetingRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagMeeting");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **meetingId** | **String**| The Amazon Chime SDK meeting ID. | |
| **operation** | **String**|  | [enum: delete] |
| **untagMeetingRequest** | [**UntagMeetingRequest**](UntagMeetingRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ThrottledClientException |  -  |
| **483** | NotFoundException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="untagResource"></a>
# **untagResource**
> untagResource(operation, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Untags the specified tags from the specified Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;p&gt;Applies the specified tags to the specified Amazon Chime SDK meeting resource.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String operation = "untag-resource"; // String | 
    UntagResourceRequest untagResourceRequest = new UntagResourceRequest(); // UntagResourceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.untagResource(operation, untagResourceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#untagResource");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **operation** | **String**|  | [enum: untag-resource] |
| **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="updateAccount"></a>
# **updateAccount**
> UpdateAccountResponse updateAccount(accountId, updateAccountRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates account details for the specified Amazon Chime account. Currently, only account name and default license updates are supported for this action.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    UpdateAccountRequest updateAccountRequest = new UpdateAccountRequest(); // UpdateAccountRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateAccountResponse result = apiInstance.updateAccount(accountId, updateAccountRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAccount");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **updateAccountRequest** | [**UpdateAccountRequest**](UpdateAccountRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateAccountResponse**](UpdateAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateAccountSettings"></a>
# **updateAccountSettings**
> Object updateAccountSettings(accountId, updateAccountSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the settings for the specified Amazon Chime account. You can update settings for remote control of shared screens, or for the dial-out option. For more information about these settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime/latest/ag/policies.html\&quot;&gt;Use the Policies Page&lt;/a&gt; in the &lt;i&gt;Amazon Chime Administration Guide&lt;/i&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    UpdateAccountSettingsRequest updateAccountSettingsRequest = new UpdateAccountSettingsRequest(); // UpdateAccountSettingsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      Object result = apiInstance.updateAccountSettings(accountId, updateAccountSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAccountSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **updateAccountSettingsRequest** | [**UpdateAccountSettingsRequest**](UpdateAccountSettingsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="updateAppInstance"></a>
# **updateAppInstance**
> UpdateAppInstanceResponse updateAppInstance(appInstanceArn, updateAppInstanceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates &lt;code&gt;AppInstance&lt;/code&gt; metadata.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_UpdateAppInstance.html\&quot;&gt;UpdateAppInstance&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceArn = "appInstanceArn_example"; // String | The ARN of the <code>AppInstance</code>.
    UpdateAppInstanceRequest updateAppInstanceRequest = new UpdateAppInstanceRequest(); // UpdateAppInstanceRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateAppInstanceResponse result = apiInstance.updateAppInstance(appInstanceArn, updateAppInstanceRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAppInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceArn** | **String**| The ARN of the &lt;code&gt;AppInstance&lt;/code&gt;. | |
| **updateAppInstanceRequest** | [**UpdateAppInstanceRequest**](UpdateAppInstanceRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateAppInstanceResponse**](UpdateAppInstanceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateAppInstanceUser"></a>
# **updateAppInstanceUser**
> UpdateAppInstanceUserResponse updateAppInstanceUser(appInstanceUserArn, updateAppInstanceUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the details of an &lt;code&gt;AppInstanceUser&lt;/code&gt;. You can update names and metadata.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_identity-chime_UpdateAppInstanceUser.html\&quot;&gt;UpdateAppInstanceUser&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String appInstanceUserArn = "appInstanceUserArn_example"; // String | The ARN of the <code>AppInstanceUser</code>.
    UpdateAppInstanceUserRequest updateAppInstanceUserRequest = new UpdateAppInstanceUserRequest(); // UpdateAppInstanceUserRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateAppInstanceUserResponse result = apiInstance.updateAppInstanceUser(appInstanceUserArn, updateAppInstanceUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateAppInstanceUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **appInstanceUserArn** | **String**| The ARN of the &lt;code&gt;AppInstanceUser&lt;/code&gt;. | |
| **updateAppInstanceUserRequest** | [**UpdateAppInstanceUserRequest**](UpdateAppInstanceUserRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateAppInstanceUserResponse**](UpdateAppInstanceUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateBot"></a>
# **updateBot**
> UpdateBotResponse updateBot(accountId, botId, updateBotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the status of the specified bot, such as starting or stopping the bot from running in your Amazon Chime Enterprise account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String botId = "botId_example"; // String | The bot ID.
    UpdateBotRequest updateBotRequest = new UpdateBotRequest(); // UpdateBotRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateBotResponse result = apiInstance.updateBot(accountId, botId, updateBotRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateBot");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **botId** | **String**| The bot ID. | |
| **updateBotRequest** | [**UpdateBotRequest**](UpdateBotRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateBotResponse**](UpdateBotResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | ServiceUnavailableException |  -  |
| **481** | ServiceFailureException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | UnauthorizedClientException |  -  |
| **485** | NotFoundException |  -  |
| **486** | ThrottledClientException |  -  |

<a id="updateChannel"></a>
# **updateChannel**
> UpdateChannelResponse updateChannel(channelArn, updateChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Update a channel&#39;s attributes.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Restriction&lt;/b&gt;: You can&#39;t change a channel&#39;s privacy. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannel.html\&quot;&gt;UpdateChannel&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    UpdateChannelRequest updateChannelRequest = new UpdateChannelRequest(); // UpdateChannelRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      UpdateChannelResponse result = apiInstance.updateChannel(channelArn, updateChannelRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateChannel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **updateChannelRequest** | [**UpdateChannelRequest**](UpdateChannelRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**UpdateChannelResponse**](UpdateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ConflictException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateChannelMessage"></a>
# **updateChannelMessage**
> UpdateChannelMessageResponse updateChannelMessage(channelArn, messageId, updateChannelMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;Updates the content of a message.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelMessage.html\&quot;&gt;UpdateChannelMessage&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String messageId = "messageId_example"; // String | The ID string of the message being updated.
    UpdateChannelMessageRequest updateChannelMessageRequest = new UpdateChannelMessageRequest(); // UpdateChannelMessageRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      UpdateChannelMessageResponse result = apiInstance.updateChannelMessage(channelArn, messageId, updateChannelMessageRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateChannelMessage");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **messageId** | **String**| The ID string of the message being updated. | |
| **updateChannelMessageRequest** | [**UpdateChannelMessageRequest**](UpdateChannelMessageRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**UpdateChannelMessageResponse**](UpdateChannelMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ConflictException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateChannelReadMarker"></a>
# **updateChannelReadMarker**
> UpdateChannelReadMarkerResponse updateChannelReadMarker(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer)



&lt;p&gt;The details of the time when a user last read messages in a channel.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The &lt;code&gt;x-amz-chime-bearer&lt;/code&gt; request header is mandatory. Use the &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call as the value in the header.&lt;/p&gt; &lt;/note&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_UpdateChannelReadMarker.html\&quot;&gt;UpdateChannelReadMarker&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String channelArn = "channelArn_example"; // String | The ARN of the channel.
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    String xAmzChimeBearer = "xAmzChimeBearer_example"; // String | The <code>AppInstanceUserArn</code> of the user that makes the API call.
    try {
      UpdateChannelReadMarkerResponse result = apiInstance.updateChannelReadMarker(channelArn, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders, xAmzChimeBearer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateChannelReadMarker");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **channelArn** | **String**| The ARN of the channel. | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |
| **xAmzChimeBearer** | **String**| The &lt;code&gt;AppInstanceUserArn&lt;/code&gt; of the user that makes the API call. | [optional] |

### Return type

[**UpdateChannelReadMarkerResponse**](UpdateChannelReadMarkerResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | ConflictException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateGlobalSettings"></a>
# **updateGlobalSettings**
> updateGlobalSettings(updateGlobalSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates global settings for the administrator&#39;s AWS account, such as Amazon Chime Business Calling and Amazon Chime Voice Connector settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UpdateGlobalSettingsRequest updateGlobalSettingsRequest = new UpdateGlobalSettingsRequest(); // UpdateGlobalSettingsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.updateGlobalSettings(updateGlobalSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateGlobalSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **updateGlobalSettingsRequest** | [**UpdateGlobalSettingsRequest**](UpdateGlobalSettingsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="updatePhoneNumber"></a>
# **updatePhoneNumber**
> UpdatePhoneNumberResponse updatePhoneNumber(phoneNumberId, updatePhoneNumberRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates phone number details, such as product type or calling name, for the specified phone number ID. You can update one phone number detail at a time. For example, you can update either the product type or the calling name in one action.&lt;/p&gt; &lt;p&gt;For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.&lt;/p&gt; &lt;p&gt;Updates to outbound calling names can take 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String phoneNumberId = "phoneNumberId_example"; // String | The phone number ID.
    UpdatePhoneNumberRequest updatePhoneNumberRequest = new UpdatePhoneNumberRequest(); // UpdatePhoneNumberRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdatePhoneNumberResponse result = apiInstance.updatePhoneNumber(phoneNumberId, updatePhoneNumberRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatePhoneNumber");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **phoneNumberId** | **String**| The phone number ID. | |
| **updatePhoneNumberRequest** | [**UpdatePhoneNumberRequest**](UpdatePhoneNumberRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdatePhoneNumberResponse**](UpdatePhoneNumberResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ConflictException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="updatePhoneNumberSettings"></a>
# **updatePhoneNumberSettings**
> updatePhoneNumberSettings(updatePhoneNumberSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the phone number settings for the administrator&#39;s AWS account, such as the default outbound calling name. You can update the default outbound calling name once every seven days. Outbound calling names can take up to 72 hours to update.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    UpdatePhoneNumberSettingsRequest updatePhoneNumberSettingsRequest = new UpdatePhoneNumberSettingsRequest(); // UpdatePhoneNumberSettingsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.updatePhoneNumberSettings(updatePhoneNumberSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatePhoneNumberSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **updatePhoneNumberSettingsRequest** | [**UpdatePhoneNumberSettingsRequest**](UpdatePhoneNumberSettingsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ThrottledClientException |  -  |
| **484** | ServiceUnavailableException |  -  |
| **485** | ServiceFailureException |  -  |

<a id="updateProxySession"></a>
# **updateProxySession**
> UpdateProxySessionResponse updateProxySession(voiceConnectorId, proxySessionId, updateProxySessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the specified proxy session details, such as voice or SMS capabilities.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateProxySession.html\&quot;&gt;UpdateProxySession&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime voice connector ID.
    String proxySessionId = "proxySessionId_example"; // String | The proxy session ID.
    UpdateProxySessionRequest updateProxySessionRequest = new UpdateProxySessionRequest(); // UpdateProxySessionRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateProxySessionResponse result = apiInstance.updateProxySession(voiceConnectorId, proxySessionId, updateProxySessionRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateProxySession");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime voice connector ID. | |
| **proxySessionId** | **String**| The proxy session ID. | |
| **updateProxySessionRequest** | [**UpdateProxySessionRequest**](UpdateProxySessionRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateProxySessionResponse**](UpdateProxySessionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateRoom"></a>
# **updateRoom**
> UpdateRoomResponse updateRoom(accountId, roomId, updateRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates room details, such as the room name, for a room in an Amazon Chime Enterprise account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String roomId = "roomId_example"; // String | The room ID.
    UpdateRoomRequest updateRoomRequest = new UpdateRoomRequest(); // UpdateRoomRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateRoomResponse result = apiInstance.updateRoom(accountId, roomId, updateRoomRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateRoom");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **roomId** | **String**| The room ID. | |
| **updateRoomRequest** | [**UpdateRoomRequest**](UpdateRoomRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateRoomResponse**](UpdateRoomResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | ForbiddenException |  -  |
| **482** | NotFoundException |  -  |
| **483** | UnauthorizedClientException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateRoomMembership"></a>
# **updateRoomMembership**
> UpdateRoomMembershipResponse updateRoomMembership(accountId, roomId, memberId, updateRoomMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates room membership details, such as the member role, for a room in an Amazon Chime Enterprise account. The member role designates whether the member is a chat room administrator or a general chat room member. The member role can be updated only for user IDs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String roomId = "roomId_example"; // String | The room ID.
    String memberId = "memberId_example"; // String | The member ID.
    UpdateRoomMembershipRequest updateRoomMembershipRequest = new UpdateRoomMembershipRequest(); // UpdateRoomMembershipRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateRoomMembershipResponse result = apiInstance.updateRoomMembership(accountId, roomId, memberId, updateRoomMembershipRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateRoomMembership");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **roomId** | **String**| The room ID. | |
| **memberId** | **String**| The member ID. | |
| **updateRoomMembershipRequest** | [**UpdateRoomMembershipRequest**](UpdateRoomMembershipRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateRoomMembershipResponse**](UpdateRoomMembershipResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | BadRequestException |  -  |
| **483** | ForbiddenException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateSipMediaApplication"></a>
# **updateSipMediaApplication**
> UpdateSipMediaApplicationResponse updateSipMediaApplication(sipMediaApplicationId, updateSipMediaApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the details of the specified SIP media application.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplication.html\&quot;&gt;UpdateSipMediaApplication&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The SIP media application ID.
    UpdateSipMediaApplicationRequest updateSipMediaApplicationRequest = new UpdateSipMediaApplicationRequest(); // UpdateSipMediaApplicationRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateSipMediaApplicationResponse result = apiInstance.updateSipMediaApplication(sipMediaApplicationId, updateSipMediaApplicationRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateSipMediaApplication");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sipMediaApplicationId** | **String**| The SIP media application ID. | |
| **updateSipMediaApplicationRequest** | [**UpdateSipMediaApplicationRequest**](UpdateSipMediaApplicationRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateSipMediaApplicationResponse**](UpdateSipMediaApplicationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="updateSipMediaApplicationCall"></a>
# **updateSipMediaApplicationCall**
> UpdateSipMediaApplicationCallResponse updateSipMediaApplicationCall(sipMediaApplicationId, transactionId, updateSipMediaApplicationCallRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Invokes the AWS Lambda function associated with the SIP media application and transaction ID in an update request. The Lambda function can then return a new set of actions.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipMediaApplicationCall.html\&quot;&gt;UpdateSipMediaApplicationCall&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sipMediaApplicationId = "sipMediaApplicationId_example"; // String | The ID of the SIP media application handling the call.
    String transactionId = "transactionId_example"; // String | The ID of the call transaction.
    UpdateSipMediaApplicationCallRequest updateSipMediaApplicationCallRequest = new UpdateSipMediaApplicationCallRequest(); // UpdateSipMediaApplicationCallRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateSipMediaApplicationCallResponse result = apiInstance.updateSipMediaApplicationCall(sipMediaApplicationId, transactionId, updateSipMediaApplicationCallRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateSipMediaApplicationCall");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sipMediaApplicationId** | **String**| The ID of the SIP media application handling the call. | |
| **transactionId** | **String**| The ID of the call transaction. | |
| **updateSipMediaApplicationCallRequest** | [**UpdateSipMediaApplicationCallRequest**](UpdateSipMediaApplicationCallRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateSipMediaApplicationCallResponse**](UpdateSipMediaApplicationCallResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | BadRequestException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | ResourceLimitExceededException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | UnauthorizedClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="updateSipRule"></a>
# **updateSipRule**
> UpdateSipRuleResponse updateSipRule(sipRuleId, updateSipRuleRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates the details of the specified SIP rule.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateSipRule.html\&quot;&gt;UpdateSipRule&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sipRuleId = "sipRuleId_example"; // String | The SIP rule ID.
    UpdateSipRuleRequest updateSipRuleRequest = new UpdateSipRuleRequest(); // UpdateSipRuleRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateSipRuleResponse result = apiInstance.updateSipRule(sipRuleId, updateSipRuleRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateSipRule");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sipRuleId** | **String**| The SIP rule ID. | |
| **updateSipRuleRequest** | [**UpdateSipRuleRequest**](UpdateSipRuleRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateSipRuleResponse**](UpdateSipRuleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ResourceLimitExceededException |  -  |
| **487** | ServiceUnavailableException |  -  |
| **488** | ServiceFailureException |  -  |

<a id="updateUser"></a>
# **updateUser**
> UpdateUserResponse updateUser(accountId, userId, updateUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates user details for a specified user ID. Currently, only &lt;code&gt;LicenseType&lt;/code&gt; updates are supported for this action.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String userId = "userId_example"; // String | The user ID.
    UpdateUserRequest updateUserRequest = new UpdateUserRequest(); // UpdateUserRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateUserResponse result = apiInstance.updateUser(accountId, userId, updateUserRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **userId** | **String**| The user ID. | |
| **updateUserRequest** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateUserResponse**](UpdateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateUserSettings"></a>
# **updateUserSettings**
> updateUserSettings(accountId, userId, updateUserSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



Updates the settings for the specified user, such as phone number settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "accountId_example"; // String | The Amazon Chime account ID.
    String userId = "userId_example"; // String | The user ID.
    UpdateUserSettingsRequest updateUserSettingsRequest = new UpdateUserSettingsRequest(); // UpdateUserSettingsRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      apiInstance.updateUserSettings(accountId, userId, updateUserSettingsRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateUserSettings");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accountId** | **String**| The Amazon Chime account ID. | |
| **userId** | **String**| The user ID. | |
| **updateUserSettingsRequest** | [**UpdateUserSettingsRequest**](UpdateUserSettingsRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateVoiceConnector"></a>
# **updateVoiceConnector**
> UpdateVoiceConnectorResponse updateVoiceConnector(voiceConnectorId, updateVoiceConnectorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates details for the specified Amazon Chime Voice Connector.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnector.html\&quot;&gt;UpdateVoiceConnector&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorId = "voiceConnectorId_example"; // String | The Amazon Chime Voice Connector ID.
    UpdateVoiceConnectorRequest updateVoiceConnectorRequest = new UpdateVoiceConnectorRequest(); // UpdateVoiceConnectorRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateVoiceConnectorResponse result = apiInstance.updateVoiceConnector(voiceConnectorId, updateVoiceConnectorRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateVoiceConnector");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorId** | **String**| The Amazon Chime Voice Connector ID. | |
| **updateVoiceConnectorRequest** | [**UpdateVoiceConnectorRequest**](UpdateVoiceConnectorRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateVoiceConnectorResponse**](UpdateVoiceConnectorResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

<a id="updateVoiceConnectorGroup"></a>
# **updateVoiceConnectorGroup**
> UpdateVoiceConnectorGroupResponse updateVoiceConnectorGroup(voiceConnectorGroupId, updateVoiceConnectorGroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Updates details of the specified Amazon Chime Voice Connector group, such as the name and Amazon Chime Voice Connector priority ranking.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_UpdateVoiceConnectorGroup.html\&quot;&gt;UpdateVoiceConnectorGroup&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String voiceConnectorGroupId = "voiceConnectorGroupId_example"; // String | The Amazon Chime Voice Connector group ID.
    UpdateVoiceConnectorGroupRequest updateVoiceConnectorGroupRequest = new UpdateVoiceConnectorGroupRequest(); // UpdateVoiceConnectorGroupRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      UpdateVoiceConnectorGroupResponse result = apiInstance.updateVoiceConnectorGroup(voiceConnectorGroupId, updateVoiceConnectorGroupRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateVoiceConnectorGroup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **voiceConnectorGroupId** | **String**| The Amazon Chime Voice Connector group ID. | |
| **updateVoiceConnectorGroupRequest** | [**UpdateVoiceConnectorGroupRequest**](UpdateVoiceConnectorGroupRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**UpdateVoiceConnectorGroupResponse**](UpdateVoiceConnectorGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ConflictException |  -  |
| **485** | ThrottledClientException |  -  |
| **486** | ServiceUnavailableException |  -  |
| **487** | ServiceFailureException |  -  |

<a id="validateE911Address"></a>
# **validateE911Address**
> ValidateE911AddressResponse validateE911Address(validateE911AddressRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders)



&lt;p&gt;Validates an address to be used for 911 calls made with Amazon Chime Voice Connectors. You can use validated addresses in a Presence Information Data Format Location Object file that you include in SIP requests. That helps ensure that addresses are routed to the appropriate Public Safety Answering Point.&lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;b&gt;This API is is no longer supported and will not be updated.&lt;/b&gt; We recommend using the latest version, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_voice-chime_ValidateE911Address.html\&quot;&gt;ValidateE911Address&lt;/a&gt;, in the Amazon Chime SDK.&lt;/p&gt; &lt;p&gt;Using the latest version requires migrating to a dedicated namespace. For more information, refer to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/chime-sdk/latest/dg/migrate-from-chm-namespace.html\&quot;&gt;Migrating from the Amazon Chime namespace&lt;/a&gt; in the &lt;i&gt;Amazon Chime SDK Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://service.chime.aws.amazon.com");
    
    // Configure API key authorization: hmac
    ApiKeyAuth hmac = (ApiKeyAuth) defaultClient.getAuthentication("hmac");
    hmac.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //hmac.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ValidateE911AddressRequest validateE911AddressRequest = new ValidateE911AddressRequest(); // ValidateE911AddressRequest | 
    String xAmzContentSha256 = "xAmzContentSha256_example"; // String | 
    String xAmzDate = "xAmzDate_example"; // String | 
    String xAmzAlgorithm = "xAmzAlgorithm_example"; // String | 
    String xAmzCredential = "xAmzCredential_example"; // String | 
    String xAmzSecurityToken = "xAmzSecurityToken_example"; // String | 
    String xAmzSignature = "xAmzSignature_example"; // String | 
    String xAmzSignedHeaders = "xAmzSignedHeaders_example"; // String | 
    try {
      ValidateE911AddressResponse result = apiInstance.validateE911Address(validateE911AddressRequest, xAmzContentSha256, xAmzDate, xAmzAlgorithm, xAmzCredential, xAmzSecurityToken, xAmzSignature, xAmzSignedHeaders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#validateE911Address");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **validateE911AddressRequest** | [**ValidateE911AddressRequest**](ValidateE911AddressRequest.md)|  | |
| **xAmzContentSha256** | **String**|  | [optional] |
| **xAmzDate** | **String**|  | [optional] |
| **xAmzAlgorithm** | **String**|  | [optional] |
| **xAmzCredential** | **String**|  | [optional] |
| **xAmzSecurityToken** | **String**|  | [optional] |
| **xAmzSignature** | **String**|  | [optional] |
| **xAmzSignedHeaders** | **String**|  | [optional] |

### Return type

[**ValidateE911AddressResponse**](ValidateE911AddressResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **480** | UnauthorizedClientException |  -  |
| **481** | NotFoundException |  -  |
| **482** | ForbiddenException |  -  |
| **483** | BadRequestException |  -  |
| **484** | ThrottledClientException |  -  |
| **485** | ServiceUnavailableException |  -  |
| **486** | ServiceFailureException |  -  |

