QT += network

HEADERS += \
# Models
    $${PWD}/OAIActiveDirectory.h \
    $${PWD}/OAIActiveDirectoryAuthInfo.h \
    $${PWD}/OAIActiveDirectoryConfig.h \
    $${PWD}/OAIActiveDirectoryConfigList.h \
    $${PWD}/OAIAlgorithmVersionInfo.h \
    $${PWD}/OAIAlgorithmVersionInfoList.h \
    $${PWD}/OAIAttributesResponse.h \
    $${PWD}/OAIAuditNodeInfo.h \
    $${PWD}/OAIAuditNodeInfoResponse.h \
    $${PWD}/OAIAuditNodeResponse.h \
    $${PWD}/OAIAuditUserPermission.h \
    $${PWD}/OAIAuthConfig.h \
    $${PWD}/OAIAuthMethod.h \
    $${PWD}/OAIAuthTokenRestrictions.h \
    $${PWD}/OAIAvatar.h \
    $${PWD}/OAIChangeGroupMembersRequest.h \
    $${PWD}/OAIChangeNodeCommentRequest.h \
    $${PWD}/OAIChangeUserPasswordRequest.h \
    $${PWD}/OAICharacterRules.h \
    $${PWD}/OAIChunkUploadResponse.h \
    $${PWD}/OAIClassificationPoliciesConfig.h \
    $${PWD}/OAIComment.h \
    $${PWD}/OAICommentList.h \
    $${PWD}/OAICompleteS3FileUploadRequest.h \
    $${PWD}/OAICompleteS3ShareUploadRequest.h \
    $${PWD}/OAICompleteUploadRequest.h \
    $${PWD}/OAIConfigOptionList.h \
    $${PWD}/OAIConfigRoomRequest.h \
    $${PWD}/OAICopyNode.h \
    $${PWD}/OAICopyNodesRequest.h \
    $${PWD}/OAICreateActiveDirectoryConfigRequest.h \
    $${PWD}/OAICreateDownloadShareRequest.h \
    $${PWD}/OAICreateFileUploadRequest.h \
    $${PWD}/OAICreateFileUploadResponse.h \
    $${PWD}/OAICreateFolderRequest.h \
    $${PWD}/OAICreateGroupRequest.h \
    $${PWD}/OAICreateKeyPairRequest.h \
    $${PWD}/OAICreateNodeCommentRequest.h \
    $${PWD}/OAICreateOAuthClientRequest.h \
    $${PWD}/OAICreateOpenIdIdpConfigRequest.h \
    $${PWD}/OAICreateRoomRequest.h \
    $${PWD}/OAICreateShareUploadChannelRequest.h \
    $${PWD}/OAICreateShareUploadChannelResponse.h \
    $${PWD}/OAICreateUploadShareRequest.h \
    $${PWD}/OAICreateUserRequest.h \
    $${PWD}/OAICreateWebhookRequest.h \
    $${PWD}/OAICustomer.h \
    $${PWD}/OAICustomerAttributes.h \
    $${PWD}/OAICustomerData.h \
    $${PWD}/OAICustomerList.h \
    $${PWD}/OAICustomerSettingsRequest.h \
    $${PWD}/OAICustomerSettingsResponse.h \
    $${PWD}/OAIDeleteDeletedNodesRequest.h \
    $${PWD}/OAIDeleteDownloadSharesRequest.h \
    $${PWD}/OAIDeleteNodesRequest.h \
    $${PWD}/OAIDeleteUploadSharesRequest.h \
    $${PWD}/OAIDeletedNode.h \
    $${PWD}/OAIDeletedNodeSummary.h \
    $${PWD}/OAIDeletedNodeSummaryList.h \
    $${PWD}/OAIDeletedNodeVersionsList.h \
    $${PWD}/OAIDownloadShare.h \
    $${PWD}/OAIDownloadShareLinkEmail.h \
    $${PWD}/OAIDownloadShareList.h \
    $${PWD}/OAIDownloadTokenGenerateResponse.h \
    $${PWD}/OAIEmergencyMfaCodeResponse.h \
    $${PWD}/OAIEnableCustomerEncryptionRequest.h \
    $${PWD}/OAIEncryptRoomRequest.h \
    $${PWD}/OAIEncryptionInfo.h \
    $${PWD}/OAIEncryptionPasswordPolicies.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAIEventType.h \
    $${PWD}/OAIEventTypeList.h \
    $${PWD}/OAIEventlogConfig.h \
    $${PWD}/OAIFailoverServer.h \
    $${PWD}/OAIFeature.h \
    $${PWD}/OAIFeaturedOAuthClient.h \
    $${PWD}/OAIFileFileKeys.h \
    $${PWD}/OAIFileKey.h \
    $${PWD}/OAIFileKeyContainer.h \
    $${PWD}/OAIFileVersion.h \
    $${PWD}/OAIFileVersionList.h \
    $${PWD}/OAIFirstAdminUser.h \
    $${PWD}/OAIGeneralSettings.h \
    $${PWD}/OAIGeneralSettingsInfo.h \
    $${PWD}/OAIGeneratePresignedUrlsRequest.h \
    $${PWD}/OAIGroup.h \
    $${PWD}/OAIGroupIds.h \
    $${PWD}/OAIGroupInfo.h \
    $${PWD}/OAIGroupList.h \
    $${PWD}/OAIGroupUser.h \
    $${PWD}/OAIGroupUserList.h \
    $${PWD}/OAIGuestUsersPoliciesConfig.h \
    $${PWD}/OAIInfrastructureProperties.h \
    $${PWD}/OAIKeyValueEntry.h \
    $${PWD}/OAILastAdminGroupRoom.h \
    $${PWD}/OAILastAdminGroupRoomList.h \
    $${PWD}/OAILastAdminUserRoom.h \
    $${PWD}/OAILastAdminUserRoomList.h \
    $${PWD}/OAILogEvent.h \
    $${PWD}/OAILogEventList.h \
    $${PWD}/OAILogOperation.h \
    $${PWD}/OAILogOperationList.h \
    $${PWD}/OAILoginPasswordPolicies.h \
    $${PWD}/OAILoginRequest.h \
    $${PWD}/OAILoginResponse.h \
    $${PWD}/OAIMfaConfig.h \
    $${PWD}/OAIMfaPoliciesConfig.h \
    $${PWD}/OAIMfaSetupStatus.h \
    $${PWD}/OAIMfaTotpConfirmationRequest.h \
    $${PWD}/OAIMissingKeysResponse.h \
    $${PWD}/OAIMoveNode.h \
    $${PWD}/OAIMoveNodesRequest.h \
    $${PWD}/OAINewCustomerRequest.h \
    $${PWD}/OAINewCustomerResponse.h \
    $${PWD}/OAINode.h \
    $${PWD}/OAINodeList.h \
    $${PWD}/OAINodeParent.h \
    $${PWD}/OAINodeParentList.h \
    $${PWD}/OAINodePermissions.h \
    $${PWD}/OAINotificationChannel.h \
    $${PWD}/OAINotificationChannelActivationRequest.h \
    $${PWD}/OAINotificationChannelList.h \
    $${PWD}/OAINotificationConfig.h \
    $${PWD}/OAINotificationConfigChangeRequest.h \
    $${PWD}/OAINotificationConfigList.h \
    $${PWD}/OAINotificationScope.h \
    $${PWD}/OAINotificationScopeList.h \
    $${PWD}/OAIOAuthApproval.h \
    $${PWD}/OAIOAuthAuthorization.h \
    $${PWD}/OAIOAuthClient.h \
    $${PWD}/OAIObjectExpiration.h \
    $${PWD}/OAIOpenIdAuthInfo.h \
    $${PWD}/OAIOpenIdIdpConfig.h \
    $${PWD}/OAIOpenIdProvider.h \
    $${PWD}/OAIPasswordExpiration.h \
    $${PWD}/OAIPasswordPoliciesConfig.h \
    $${PWD}/OAIPasswordPolicyViolationResponse.h \
    $${PWD}/OAIPendingAssignment.h \
    $${PWD}/OAIPendingAssignmentData.h \
    $${PWD}/OAIPendingAssignmentList.h \
    $${PWD}/OAIPendingAssignmentsRequest.h \
    $${PWD}/OAIPendingGroupData.h \
    $${PWD}/OAIPendingUserData.h \
    $${PWD}/OAIPresignedUrl.h \
    $${PWD}/OAIPresignedUrlList.h \
    $${PWD}/OAIPrivateKeyContainer.h \
    $${PWD}/OAIProductPackageResponse.h \
    $${PWD}/OAIProductPackageResponseList.h \
    $${PWD}/OAIProfileAttributes.h \
    $${PWD}/OAIProfileAttributesRequest.h \
    $${PWD}/OAIPublicDownloadShare.h \
    $${PWD}/OAIPublicDownloadTokenGenerateRequest.h \
    $${PWD}/OAIPublicDownloadTokenGenerateResponse.h \
    $${PWD}/OAIPublicKeyContainer.h \
    $${PWD}/OAIPublicUploadShare.h \
    $${PWD}/OAIPublicUploadedFileData.h \
    $${PWD}/OAIRadiusChallengeResponse.h \
    $${PWD}/OAIRadiusConfig.h \
    $${PWD}/OAIRadiusConfigCreateRequest.h \
    $${PWD}/OAIRadiusConfigUpdateRequest.h \
    $${PWD}/OAIRange.h \
    $${PWD}/OAIRecoverUserNameRequest.h \
    $${PWD}/OAIResetPasswordRequest.h \
    $${PWD}/OAIResetPasswordTokenValidateResponse.h \
    $${PWD}/OAIResetPasswordWithTokenRequest.h \
    $${PWD}/OAIResetPassword_400_response.h \
    $${PWD}/OAIRestoreDeletedNodesRequest.h \
    $${PWD}/OAIRight.h \
    $${PWD}/OAIRole.h \
    $${PWD}/OAIRoleGroup.h \
    $${PWD}/OAIRoleGroupList.h \
    $${PWD}/OAIRoleList.h \
    $${PWD}/OAIRoleUser.h \
    $${PWD}/OAIRoleUserList.h \
    $${PWD}/OAIRoomData.h \
    $${PWD}/OAIRoomGroup.h \
    $${PWD}/OAIRoomGroupList.h \
    $${PWD}/OAIRoomGroupsAddBatchRequest.h \
    $${PWD}/OAIRoomGroupsAddBatchRequestItem.h \
    $${PWD}/OAIRoomGroupsDeleteBatchRequest.h \
    $${PWD}/OAIRoomGuestUserAddRequest.h \
    $${PWD}/OAIRoomGuestUserInvitation.h \
    $${PWD}/OAIRoomPolicies.h \
    $${PWD}/OAIRoomPoliciesRequest.h \
    $${PWD}/OAIRoomTreeDataList.h \
    $${PWD}/OAIRoomUser.h \
    $${PWD}/OAIRoomUserList.h \
    $${PWD}/OAIRoomUsersAddBatchRequest.h \
    $${PWD}/OAIRoomUsersAddBatchRequestItem.h \
    $${PWD}/OAIRoomUsersDeleteBatchRequest.h \
    $${PWD}/OAIRoomWebhook.h \
    $${PWD}/OAIRoomWebhookAssignment.h \
    $${PWD}/OAIRoomWebhookList.h \
    $${PWD}/OAIS3Config.h \
    $${PWD}/OAIS3ConfigCreateRequest.h \
    $${PWD}/OAIS3ConfigUpdateRequest.h \
    $${PWD}/OAIS3FileUploadPart.h \
    $${PWD}/OAIS3FileUploadStatus.h \
    $${PWD}/OAIS3ShareUploadStatus.h \
    $${PWD}/OAIS3Tag.h \
    $${PWD}/OAIS3TagCreateRequest.h \
    $${PWD}/OAIS3TagIds.h \
    $${PWD}/OAIS3TagList.h \
    $${PWD}/OAISdsServerTime.h \
    $${PWD}/OAIShareClassificationPolicies.h \
    $${PWD}/OAISharesPasswordPolicies.h \
    $${PWD}/OAISoftwareVersionData.h \
    $${PWD}/OAISubscribedDownloadShare.h \
    $${PWD}/OAISubscribedDownloadShareList.h \
    $${PWD}/OAISubscribedNode.h \
    $${PWD}/OAISubscribedNodeList.h \
    $${PWD}/OAISubscribedUploadShare.h \
    $${PWD}/OAISubscribedUploadShareList.h \
    $${PWD}/OAISubscriptionPlanRequest.h \
    $${PWD}/OAISubscriptionPlanResponse.h \
    $${PWD}/OAISyslogConfig.h \
    $${PWD}/OAISystemDefaults.h \
    $${PWD}/OAISystemInfo.h \
    $${PWD}/OAITestActiveDirectoryConfigRequest.h \
    $${PWD}/OAITestActiveDirectoryConfigResponse.h \
    $${PWD}/OAIThirdPartyDependenciesData.h \
    $${PWD}/OAITotpSetupResponse.h \
    $${PWD}/OAIUpdateActiveDirectoryConfigRequest.h \
    $${PWD}/OAIUpdateAuthTokenRestrictions.h \
    $${PWD}/OAIUpdateClassificationPoliciesConfig.h \
    $${PWD}/OAIUpdateCustomerRequest.h \
    $${PWD}/OAIUpdateCustomerResponse.h \
    $${PWD}/OAIUpdateDownloadShareRequest.h \
    $${PWD}/OAIUpdateDownloadSharesBulkRequest.h \
    $${PWD}/OAIUpdateEncryptionPasswordPolicies.h \
    $${PWD}/OAIUpdateEventlogConfig.h \
    $${PWD}/OAIUpdateFavoritesBulkRequest.h \
    $${PWD}/OAIUpdateFileRequest.h \
    $${PWD}/OAIUpdateFilesBulkRequest.h \
    $${PWD}/OAIUpdateFolderRequest.h \
    $${PWD}/OAIUpdateGeneralSettings.h \
    $${PWD}/OAIUpdateGroupRequest.h \
    $${PWD}/OAIUpdateGuestUsersPoliciesConfig.h \
    $${PWD}/OAIUpdateLoginPasswordPolicies.h \
    $${PWD}/OAIUpdateMfaPoliciesConfig.h \
    $${PWD}/OAIUpdateOAuthClientRequest.h \
    $${PWD}/OAIUpdateOpenIdIdpConfigRequest.h \
    $${PWD}/OAIUpdatePasswordPoliciesConfig.h \
    $${PWD}/OAIUpdateRoomRequest.h \
    $${PWD}/OAIUpdateRoomWebhookRequest.h \
    $${PWD}/OAIUpdateSharesPasswordPolicies.h \
    $${PWD}/OAIUpdateSubscriptionsBulkRequest.h \
    $${PWD}/OAIUpdateSyslogConfig.h \
    $${PWD}/OAIUpdateSystemDefaults.h \
    $${PWD}/OAIUpdateUploadShareRequest.h \
    $${PWD}/OAIUpdateUploadSharesBulkRequest.h \
    $${PWD}/OAIUpdateUserAccountRequest.h \
    $${PWD}/OAIUpdateUserRequest.h \
    $${PWD}/OAIUpdateWebhookRequest.h \
    $${PWD}/OAIUploadShare.h \
    $${PWD}/OAIUploadShareLinkEmail.h \
    $${PWD}/OAIUploadShareList.h \
    $${PWD}/OAIUserAccount.h \
    $${PWD}/OAIUserAttributes.h \
    $${PWD}/OAIUserAuthData.h \
    $${PWD}/OAIUserAuthDataUpdateRequest.h \
    $${PWD}/OAIUserAuthMethod.h \
    $${PWD}/OAIUserData.h \
    $${PWD}/OAIUserFileKey.h \
    $${PWD}/OAIUserFileKeyList.h \
    $${PWD}/OAIUserFileKeySetBatchRequest.h \
    $${PWD}/OAIUserFileKeySetRequest.h \
    $${PWD}/OAIUserGroup.h \
    $${PWD}/OAIUserGroupList.h \
    $${PWD}/OAIUserIdFileIdItem.h \
    $${PWD}/OAIUserIds.h \
    $${PWD}/OAIUserInfo.h \
    $${PWD}/OAIUserItem.h \
    $${PWD}/OAIUserKeyPairContainer.h \
    $${PWD}/OAIUserList.h \
    $${PWD}/OAIUserLockout.h \
    $${PWD}/OAIUserMfaStatusResponse.h \
    $${PWD}/OAIUserUserPublicKey.h \
    $${PWD}/OAIUserUserPublicKeyList.h \
    $${PWD}/OAIViolatedPasswordPolicy.h \
    $${PWD}/OAIWebhook.h \
    $${PWD}/OAIWebhookList.h \
    $${PWD}/OAIZipDownloadRequest.h \
# APIs
    $${PWD}/OAIAuthApi.h \
    $${PWD}/OAIConfigApi.h \
    $${PWD}/OAIDownloadsApi.h \
    $${PWD}/OAIEventlogApi.h \
    $${PWD}/OAIGroupsApi.h \
    $${PWD}/OAIInternalApi.h \
    $${PWD}/OAINodesApi.h \
    $${PWD}/OAIProvisioningApi.h \
    $${PWD}/OAIPublicApi.h \
    $${PWD}/OAIResourcesApi.h \
    $${PWD}/OAIRolesApi.h \
    $${PWD}/OAISettingsApi.h \
    $${PWD}/OAISharesApi.h \
    $${PWD}/OAISystemAuthConfigApi.h \
    $${PWD}/OAISystemPoliciesConfigApi.h \
    $${PWD}/OAISystemSettingsConfigApi.h \
    $${PWD}/OAISystemStorageConfigApi.h \
    $${PWD}/OAIUploadsApi.h \
    $${PWD}/OAIUserApi.h \
    $${PWD}/OAIUsersApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIActiveDirectory.cpp \
    $${PWD}/OAIActiveDirectoryAuthInfo.cpp \
    $${PWD}/OAIActiveDirectoryConfig.cpp \
    $${PWD}/OAIActiveDirectoryConfigList.cpp \
    $${PWD}/OAIAlgorithmVersionInfo.cpp \
    $${PWD}/OAIAlgorithmVersionInfoList.cpp \
    $${PWD}/OAIAttributesResponse.cpp \
    $${PWD}/OAIAuditNodeInfo.cpp \
    $${PWD}/OAIAuditNodeInfoResponse.cpp \
    $${PWD}/OAIAuditNodeResponse.cpp \
    $${PWD}/OAIAuditUserPermission.cpp \
    $${PWD}/OAIAuthConfig.cpp \
    $${PWD}/OAIAuthMethod.cpp \
    $${PWD}/OAIAuthTokenRestrictions.cpp \
    $${PWD}/OAIAvatar.cpp \
    $${PWD}/OAIChangeGroupMembersRequest.cpp \
    $${PWD}/OAIChangeNodeCommentRequest.cpp \
    $${PWD}/OAIChangeUserPasswordRequest.cpp \
    $${PWD}/OAICharacterRules.cpp \
    $${PWD}/OAIChunkUploadResponse.cpp \
    $${PWD}/OAIClassificationPoliciesConfig.cpp \
    $${PWD}/OAIComment.cpp \
    $${PWD}/OAICommentList.cpp \
    $${PWD}/OAICompleteS3FileUploadRequest.cpp \
    $${PWD}/OAICompleteS3ShareUploadRequest.cpp \
    $${PWD}/OAICompleteUploadRequest.cpp \
    $${PWD}/OAIConfigOptionList.cpp \
    $${PWD}/OAIConfigRoomRequest.cpp \
    $${PWD}/OAICopyNode.cpp \
    $${PWD}/OAICopyNodesRequest.cpp \
    $${PWD}/OAICreateActiveDirectoryConfigRequest.cpp \
    $${PWD}/OAICreateDownloadShareRequest.cpp \
    $${PWD}/OAICreateFileUploadRequest.cpp \
    $${PWD}/OAICreateFileUploadResponse.cpp \
    $${PWD}/OAICreateFolderRequest.cpp \
    $${PWD}/OAICreateGroupRequest.cpp \
    $${PWD}/OAICreateKeyPairRequest.cpp \
    $${PWD}/OAICreateNodeCommentRequest.cpp \
    $${PWD}/OAICreateOAuthClientRequest.cpp \
    $${PWD}/OAICreateOpenIdIdpConfigRequest.cpp \
    $${PWD}/OAICreateRoomRequest.cpp \
    $${PWD}/OAICreateShareUploadChannelRequest.cpp \
    $${PWD}/OAICreateShareUploadChannelResponse.cpp \
    $${PWD}/OAICreateUploadShareRequest.cpp \
    $${PWD}/OAICreateUserRequest.cpp \
    $${PWD}/OAICreateWebhookRequest.cpp \
    $${PWD}/OAICustomer.cpp \
    $${PWD}/OAICustomerAttributes.cpp \
    $${PWD}/OAICustomerData.cpp \
    $${PWD}/OAICustomerList.cpp \
    $${PWD}/OAICustomerSettingsRequest.cpp \
    $${PWD}/OAICustomerSettingsResponse.cpp \
    $${PWD}/OAIDeleteDeletedNodesRequest.cpp \
    $${PWD}/OAIDeleteDownloadSharesRequest.cpp \
    $${PWD}/OAIDeleteNodesRequest.cpp \
    $${PWD}/OAIDeleteUploadSharesRequest.cpp \
    $${PWD}/OAIDeletedNode.cpp \
    $${PWD}/OAIDeletedNodeSummary.cpp \
    $${PWD}/OAIDeletedNodeSummaryList.cpp \
    $${PWD}/OAIDeletedNodeVersionsList.cpp \
    $${PWD}/OAIDownloadShare.cpp \
    $${PWD}/OAIDownloadShareLinkEmail.cpp \
    $${PWD}/OAIDownloadShareList.cpp \
    $${PWD}/OAIDownloadTokenGenerateResponse.cpp \
    $${PWD}/OAIEmergencyMfaCodeResponse.cpp \
    $${PWD}/OAIEnableCustomerEncryptionRequest.cpp \
    $${PWD}/OAIEncryptRoomRequest.cpp \
    $${PWD}/OAIEncryptionInfo.cpp \
    $${PWD}/OAIEncryptionPasswordPolicies.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAIEventType.cpp \
    $${PWD}/OAIEventTypeList.cpp \
    $${PWD}/OAIEventlogConfig.cpp \
    $${PWD}/OAIFailoverServer.cpp \
    $${PWD}/OAIFeature.cpp \
    $${PWD}/OAIFeaturedOAuthClient.cpp \
    $${PWD}/OAIFileFileKeys.cpp \
    $${PWD}/OAIFileKey.cpp \
    $${PWD}/OAIFileKeyContainer.cpp \
    $${PWD}/OAIFileVersion.cpp \
    $${PWD}/OAIFileVersionList.cpp \
    $${PWD}/OAIFirstAdminUser.cpp \
    $${PWD}/OAIGeneralSettings.cpp \
    $${PWD}/OAIGeneralSettingsInfo.cpp \
    $${PWD}/OAIGeneratePresignedUrlsRequest.cpp \
    $${PWD}/OAIGroup.cpp \
    $${PWD}/OAIGroupIds.cpp \
    $${PWD}/OAIGroupInfo.cpp \
    $${PWD}/OAIGroupList.cpp \
    $${PWD}/OAIGroupUser.cpp \
    $${PWD}/OAIGroupUserList.cpp \
    $${PWD}/OAIGuestUsersPoliciesConfig.cpp \
    $${PWD}/OAIInfrastructureProperties.cpp \
    $${PWD}/OAIKeyValueEntry.cpp \
    $${PWD}/OAILastAdminGroupRoom.cpp \
    $${PWD}/OAILastAdminGroupRoomList.cpp \
    $${PWD}/OAILastAdminUserRoom.cpp \
    $${PWD}/OAILastAdminUserRoomList.cpp \
    $${PWD}/OAILogEvent.cpp \
    $${PWD}/OAILogEventList.cpp \
    $${PWD}/OAILogOperation.cpp \
    $${PWD}/OAILogOperationList.cpp \
    $${PWD}/OAILoginPasswordPolicies.cpp \
    $${PWD}/OAILoginRequest.cpp \
    $${PWD}/OAILoginResponse.cpp \
    $${PWD}/OAIMfaConfig.cpp \
    $${PWD}/OAIMfaPoliciesConfig.cpp \
    $${PWD}/OAIMfaSetupStatus.cpp \
    $${PWD}/OAIMfaTotpConfirmationRequest.cpp \
    $${PWD}/OAIMissingKeysResponse.cpp \
    $${PWD}/OAIMoveNode.cpp \
    $${PWD}/OAIMoveNodesRequest.cpp \
    $${PWD}/OAINewCustomerRequest.cpp \
    $${PWD}/OAINewCustomerResponse.cpp \
    $${PWD}/OAINode.cpp \
    $${PWD}/OAINodeList.cpp \
    $${PWD}/OAINodeParent.cpp \
    $${PWD}/OAINodeParentList.cpp \
    $${PWD}/OAINodePermissions.cpp \
    $${PWD}/OAINotificationChannel.cpp \
    $${PWD}/OAINotificationChannelActivationRequest.cpp \
    $${PWD}/OAINotificationChannelList.cpp \
    $${PWD}/OAINotificationConfig.cpp \
    $${PWD}/OAINotificationConfigChangeRequest.cpp \
    $${PWD}/OAINotificationConfigList.cpp \
    $${PWD}/OAINotificationScope.cpp \
    $${PWD}/OAINotificationScopeList.cpp \
    $${PWD}/OAIOAuthApproval.cpp \
    $${PWD}/OAIOAuthAuthorization.cpp \
    $${PWD}/OAIOAuthClient.cpp \
    $${PWD}/OAIObjectExpiration.cpp \
    $${PWD}/OAIOpenIdAuthInfo.cpp \
    $${PWD}/OAIOpenIdIdpConfig.cpp \
    $${PWD}/OAIOpenIdProvider.cpp \
    $${PWD}/OAIPasswordExpiration.cpp \
    $${PWD}/OAIPasswordPoliciesConfig.cpp \
    $${PWD}/OAIPasswordPolicyViolationResponse.cpp \
    $${PWD}/OAIPendingAssignment.cpp \
    $${PWD}/OAIPendingAssignmentData.cpp \
    $${PWD}/OAIPendingAssignmentList.cpp \
    $${PWD}/OAIPendingAssignmentsRequest.cpp \
    $${PWD}/OAIPendingGroupData.cpp \
    $${PWD}/OAIPendingUserData.cpp \
    $${PWD}/OAIPresignedUrl.cpp \
    $${PWD}/OAIPresignedUrlList.cpp \
    $${PWD}/OAIPrivateKeyContainer.cpp \
    $${PWD}/OAIProductPackageResponse.cpp \
    $${PWD}/OAIProductPackageResponseList.cpp \
    $${PWD}/OAIProfileAttributes.cpp \
    $${PWD}/OAIProfileAttributesRequest.cpp \
    $${PWD}/OAIPublicDownloadShare.cpp \
    $${PWD}/OAIPublicDownloadTokenGenerateRequest.cpp \
    $${PWD}/OAIPublicDownloadTokenGenerateResponse.cpp \
    $${PWD}/OAIPublicKeyContainer.cpp \
    $${PWD}/OAIPublicUploadShare.cpp \
    $${PWD}/OAIPublicUploadedFileData.cpp \
    $${PWD}/OAIRadiusChallengeResponse.cpp \
    $${PWD}/OAIRadiusConfig.cpp \
    $${PWD}/OAIRadiusConfigCreateRequest.cpp \
    $${PWD}/OAIRadiusConfigUpdateRequest.cpp \
    $${PWD}/OAIRange.cpp \
    $${PWD}/OAIRecoverUserNameRequest.cpp \
    $${PWD}/OAIResetPasswordRequest.cpp \
    $${PWD}/OAIResetPasswordTokenValidateResponse.cpp \
    $${PWD}/OAIResetPasswordWithTokenRequest.cpp \
    $${PWD}/OAIResetPassword_400_response.cpp \
    $${PWD}/OAIRestoreDeletedNodesRequest.cpp \
    $${PWD}/OAIRight.cpp \
    $${PWD}/OAIRole.cpp \
    $${PWD}/OAIRoleGroup.cpp \
    $${PWD}/OAIRoleGroupList.cpp \
    $${PWD}/OAIRoleList.cpp \
    $${PWD}/OAIRoleUser.cpp \
    $${PWD}/OAIRoleUserList.cpp \
    $${PWD}/OAIRoomData.cpp \
    $${PWD}/OAIRoomGroup.cpp \
    $${PWD}/OAIRoomGroupList.cpp \
    $${PWD}/OAIRoomGroupsAddBatchRequest.cpp \
    $${PWD}/OAIRoomGroupsAddBatchRequestItem.cpp \
    $${PWD}/OAIRoomGroupsDeleteBatchRequest.cpp \
    $${PWD}/OAIRoomGuestUserAddRequest.cpp \
    $${PWD}/OAIRoomGuestUserInvitation.cpp \
    $${PWD}/OAIRoomPolicies.cpp \
    $${PWD}/OAIRoomPoliciesRequest.cpp \
    $${PWD}/OAIRoomTreeDataList.cpp \
    $${PWD}/OAIRoomUser.cpp \
    $${PWD}/OAIRoomUserList.cpp \
    $${PWD}/OAIRoomUsersAddBatchRequest.cpp \
    $${PWD}/OAIRoomUsersAddBatchRequestItem.cpp \
    $${PWD}/OAIRoomUsersDeleteBatchRequest.cpp \
    $${PWD}/OAIRoomWebhook.cpp \
    $${PWD}/OAIRoomWebhookAssignment.cpp \
    $${PWD}/OAIRoomWebhookList.cpp \
    $${PWD}/OAIS3Config.cpp \
    $${PWD}/OAIS3ConfigCreateRequest.cpp \
    $${PWD}/OAIS3ConfigUpdateRequest.cpp \
    $${PWD}/OAIS3FileUploadPart.cpp \
    $${PWD}/OAIS3FileUploadStatus.cpp \
    $${PWD}/OAIS3ShareUploadStatus.cpp \
    $${PWD}/OAIS3Tag.cpp \
    $${PWD}/OAIS3TagCreateRequest.cpp \
    $${PWD}/OAIS3TagIds.cpp \
    $${PWD}/OAIS3TagList.cpp \
    $${PWD}/OAISdsServerTime.cpp \
    $${PWD}/OAIShareClassificationPolicies.cpp \
    $${PWD}/OAISharesPasswordPolicies.cpp \
    $${PWD}/OAISoftwareVersionData.cpp \
    $${PWD}/OAISubscribedDownloadShare.cpp \
    $${PWD}/OAISubscribedDownloadShareList.cpp \
    $${PWD}/OAISubscribedNode.cpp \
    $${PWD}/OAISubscribedNodeList.cpp \
    $${PWD}/OAISubscribedUploadShare.cpp \
    $${PWD}/OAISubscribedUploadShareList.cpp \
    $${PWD}/OAISubscriptionPlanRequest.cpp \
    $${PWD}/OAISubscriptionPlanResponse.cpp \
    $${PWD}/OAISyslogConfig.cpp \
    $${PWD}/OAISystemDefaults.cpp \
    $${PWD}/OAISystemInfo.cpp \
    $${PWD}/OAITestActiveDirectoryConfigRequest.cpp \
    $${PWD}/OAITestActiveDirectoryConfigResponse.cpp \
    $${PWD}/OAIThirdPartyDependenciesData.cpp \
    $${PWD}/OAITotpSetupResponse.cpp \
    $${PWD}/OAIUpdateActiveDirectoryConfigRequest.cpp \
    $${PWD}/OAIUpdateAuthTokenRestrictions.cpp \
    $${PWD}/OAIUpdateClassificationPoliciesConfig.cpp \
    $${PWD}/OAIUpdateCustomerRequest.cpp \
    $${PWD}/OAIUpdateCustomerResponse.cpp \
    $${PWD}/OAIUpdateDownloadShareRequest.cpp \
    $${PWD}/OAIUpdateDownloadSharesBulkRequest.cpp \
    $${PWD}/OAIUpdateEncryptionPasswordPolicies.cpp \
    $${PWD}/OAIUpdateEventlogConfig.cpp \
    $${PWD}/OAIUpdateFavoritesBulkRequest.cpp \
    $${PWD}/OAIUpdateFileRequest.cpp \
    $${PWD}/OAIUpdateFilesBulkRequest.cpp \
    $${PWD}/OAIUpdateFolderRequest.cpp \
    $${PWD}/OAIUpdateGeneralSettings.cpp \
    $${PWD}/OAIUpdateGroupRequest.cpp \
    $${PWD}/OAIUpdateGuestUsersPoliciesConfig.cpp \
    $${PWD}/OAIUpdateLoginPasswordPolicies.cpp \
    $${PWD}/OAIUpdateMfaPoliciesConfig.cpp \
    $${PWD}/OAIUpdateOAuthClientRequest.cpp \
    $${PWD}/OAIUpdateOpenIdIdpConfigRequest.cpp \
    $${PWD}/OAIUpdatePasswordPoliciesConfig.cpp \
    $${PWD}/OAIUpdateRoomRequest.cpp \
    $${PWD}/OAIUpdateRoomWebhookRequest.cpp \
    $${PWD}/OAIUpdateSharesPasswordPolicies.cpp \
    $${PWD}/OAIUpdateSubscriptionsBulkRequest.cpp \
    $${PWD}/OAIUpdateSyslogConfig.cpp \
    $${PWD}/OAIUpdateSystemDefaults.cpp \
    $${PWD}/OAIUpdateUploadShareRequest.cpp \
    $${PWD}/OAIUpdateUploadSharesBulkRequest.cpp \
    $${PWD}/OAIUpdateUserAccountRequest.cpp \
    $${PWD}/OAIUpdateUserRequest.cpp \
    $${PWD}/OAIUpdateWebhookRequest.cpp \
    $${PWD}/OAIUploadShare.cpp \
    $${PWD}/OAIUploadShareLinkEmail.cpp \
    $${PWD}/OAIUploadShareList.cpp \
    $${PWD}/OAIUserAccount.cpp \
    $${PWD}/OAIUserAttributes.cpp \
    $${PWD}/OAIUserAuthData.cpp \
    $${PWD}/OAIUserAuthDataUpdateRequest.cpp \
    $${PWD}/OAIUserAuthMethod.cpp \
    $${PWD}/OAIUserData.cpp \
    $${PWD}/OAIUserFileKey.cpp \
    $${PWD}/OAIUserFileKeyList.cpp \
    $${PWD}/OAIUserFileKeySetBatchRequest.cpp \
    $${PWD}/OAIUserFileKeySetRequest.cpp \
    $${PWD}/OAIUserGroup.cpp \
    $${PWD}/OAIUserGroupList.cpp \
    $${PWD}/OAIUserIdFileIdItem.cpp \
    $${PWD}/OAIUserIds.cpp \
    $${PWD}/OAIUserInfo.cpp \
    $${PWD}/OAIUserItem.cpp \
    $${PWD}/OAIUserKeyPairContainer.cpp \
    $${PWD}/OAIUserList.cpp \
    $${PWD}/OAIUserLockout.cpp \
    $${PWD}/OAIUserMfaStatusResponse.cpp \
    $${PWD}/OAIUserUserPublicKey.cpp \
    $${PWD}/OAIUserUserPublicKeyList.cpp \
    $${PWD}/OAIViolatedPasswordPolicy.cpp \
    $${PWD}/OAIWebhook.cpp \
    $${PWD}/OAIWebhookList.cpp \
    $${PWD}/OAIZipDownloadRequest.cpp \
# APIs
    $${PWD}/OAIAuthApi.cpp \
    $${PWD}/OAIConfigApi.cpp \
    $${PWD}/OAIDownloadsApi.cpp \
    $${PWD}/OAIEventlogApi.cpp \
    $${PWD}/OAIGroupsApi.cpp \
    $${PWD}/OAIInternalApi.cpp \
    $${PWD}/OAINodesApi.cpp \
    $${PWD}/OAIProvisioningApi.cpp \
    $${PWD}/OAIPublicApi.cpp \
    $${PWD}/OAIResourcesApi.cpp \
    $${PWD}/OAIRolesApi.cpp \
    $${PWD}/OAISettingsApi.cpp \
    $${PWD}/OAISharesApi.cpp \
    $${PWD}/OAISystemAuthConfigApi.cpp \
    $${PWD}/OAISystemPoliciesConfigApi.cpp \
    $${PWD}/OAISystemSettingsConfigApi.cpp \
    $${PWD}/OAISystemStorageConfigApi.cpp \
    $${PWD}/OAIUploadsApi.cpp \
    $${PWD}/OAIUserApi.cpp \
    $${PWD}/OAIUsersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
