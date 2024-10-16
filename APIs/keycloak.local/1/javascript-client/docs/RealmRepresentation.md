# KeycloakAdminRestApi.RealmRepresentation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessCodeLifespan** | **Number** |  | [optional] 
**accessCodeLifespanLogin** | **Number** |  | [optional] 
**accessCodeLifespanUserAction** | **Number** |  | [optional] 
**accessTokenLifespan** | **Number** |  | [optional] 
**accessTokenLifespanForImplicitFlow** | **Number** |  | [optional] 
**accountTheme** | **String** |  | [optional] 
**actionTokenGeneratedByAdminLifespan** | **Number** |  | [optional] 
**actionTokenGeneratedByUserLifespan** | **Number** |  | [optional] 
**adminEventsDetailsEnabled** | **Boolean** |  | [optional] 
**adminEventsEnabled** | **Boolean** |  | [optional] 
**adminTheme** | **String** |  | [optional] 
**attributes** | **{String: Object}** |  | [optional] 
**authenticationFlows** | [**[AuthenticationFlowRepresentation]**](AuthenticationFlowRepresentation.md) |  | [optional] 
**authenticatorConfig** | [**[AuthenticatorConfigRepresentation]**](AuthenticatorConfigRepresentation.md) |  | [optional] 
**browserFlow** | **String** |  | [optional] 
**browserSecurityHeaders** | **{String: Object}** |  | [optional] 
**bruteForceProtected** | **Boolean** |  | [optional] 
**clientAuthenticationFlow** | **String** |  | [optional] 
**clientScopeMappings** | **{String: Object}** |  | [optional] 
**clientScopes** | [**[ClientScopeRepresentation]**](ClientScopeRepresentation.md) |  | [optional] 
**clientSessionIdleTimeout** | **Number** |  | [optional] 
**clientSessionMaxLifespan** | **Number** |  | [optional] 
**clients** | [**[ClientRepresentation]**](ClientRepresentation.md) |  | [optional] 
**components** | [**MultivaluedHashMap**](MultivaluedHashMap.md) |  | [optional] 
**defaultDefaultClientScopes** | **[String]** |  | [optional] 
**defaultGroups** | **[String]** |  | [optional] 
**defaultLocale** | **String** |  | [optional] 
**defaultOptionalClientScopes** | **[String]** |  | [optional] 
**defaultRoles** | **[String]** |  | [optional] 
**defaultSignatureAlgorithm** | **String** |  | [optional] 
**directGrantFlow** | **String** |  | [optional] 
**displayName** | **String** |  | [optional] 
**displayNameHtml** | **String** |  | [optional] 
**dockerAuthenticationFlow** | **String** |  | [optional] 
**duplicateEmailsAllowed** | **Boolean** |  | [optional] 
**editUsernameAllowed** | **Boolean** |  | [optional] 
**emailTheme** | **String** |  | [optional] 
**enabled** | **Boolean** |  | [optional] 
**enabledEventTypes** | **[String]** |  | [optional] 
**eventsEnabled** | **Boolean** |  | [optional] 
**eventsExpiration** | **Number** |  | [optional] 
**eventsListeners** | **[String]** |  | [optional] 
**failureFactor** | **Number** |  | [optional] 
**federatedUsers** | [**[UserRepresentation]**](UserRepresentation.md) |  | [optional] 
**groups** | [**[GroupRepresentation]**](GroupRepresentation.md) |  | [optional] 
**id** | **String** |  | [optional] 
**identityProviderMappers** | [**[IdentityProviderMapperRepresentation]**](IdentityProviderMapperRepresentation.md) |  | [optional] 
**identityProviders** | [**[IdentityProviderRepresentation]**](IdentityProviderRepresentation.md) |  | [optional] 
**internationalizationEnabled** | **Boolean** |  | [optional] 
**keycloakVersion** | **String** |  | [optional] 
**loginTheme** | **String** |  | [optional] 
**loginWithEmailAllowed** | **Boolean** |  | [optional] 
**maxDeltaTimeSeconds** | **Number** |  | [optional] 
**maxFailureWaitSeconds** | **Number** |  | [optional] 
**minimumQuickLoginWaitSeconds** | **Number** |  | [optional] 
**notBefore** | **Number** |  | [optional] 
**offlineSessionIdleTimeout** | **Number** |  | [optional] 
**offlineSessionMaxLifespan** | **Number** |  | [optional] 
**offlineSessionMaxLifespanEnabled** | **Boolean** |  | [optional] 
**otpPolicyAlgorithm** | **String** |  | [optional] 
**otpPolicyDigits** | **Number** |  | [optional] 
**otpPolicyInitialCounter** | **Number** |  | [optional] 
**otpPolicyLookAheadWindow** | **Number** |  | [optional] 
**otpPolicyPeriod** | **Number** |  | [optional] 
**otpPolicyType** | **String** |  | [optional] 
**otpSupportedApplications** | **[String]** |  | [optional] 
**passwordPolicy** | **String** |  | [optional] 
**permanentLockout** | **Boolean** |  | [optional] 
**protocolMappers** | [**[ProtocolMapperRepresentation]**](ProtocolMapperRepresentation.md) |  | [optional] 
**quickLoginCheckMilliSeconds** | **Number** |  | [optional] 
**realm** | **String** |  | [optional] 
**refreshTokenMaxReuse** | **Number** |  | [optional] 
**registrationAllowed** | **Boolean** |  | [optional] 
**registrationEmailAsUsername** | **Boolean** |  | [optional] 
**registrationFlow** | **String** |  | [optional] 
**rememberMe** | **Boolean** |  | [optional] 
**requiredActions** | [**[RequiredActionProviderRepresentation]**](RequiredActionProviderRepresentation.md) |  | [optional] 
**resetCredentialsFlow** | **String** |  | [optional] 
**resetPasswordAllowed** | **Boolean** |  | [optional] 
**revokeRefreshToken** | **Boolean** |  | [optional] 
**roles** | [**RolesRepresentation**](RolesRepresentation.md) |  | [optional] 
**scopeMappings** | [**[ScopeMappingRepresentation]**](ScopeMappingRepresentation.md) |  | [optional] 
**smtpServer** | **{String: Object}** |  | [optional] 
**sslRequired** | **String** |  | [optional] 
**ssoSessionIdleTimeout** | **Number** |  | [optional] 
**ssoSessionIdleTimeoutRememberMe** | **Number** |  | [optional] 
**ssoSessionMaxLifespan** | **Number** |  | [optional] 
**ssoSessionMaxLifespanRememberMe** | **Number** |  | [optional] 
**supportedLocales** | **[String]** |  | [optional] 
**userFederationMappers** | [**[UserFederationMapperRepresentation]**](UserFederationMapperRepresentation.md) |  | [optional] 
**userFederationProviders** | [**[UserFederationProviderRepresentation]**](UserFederationProviderRepresentation.md) |  | [optional] 
**userManagedAccessAllowed** | **Boolean** |  | [optional] 
**users** | [**[UserRepresentation]**](UserRepresentation.md) |  | [optional] 
**verifyEmail** | **Boolean** |  | [optional] 
**waitIncrementSeconds** | **Number** |  | [optional] 
**webAuthnPolicyAcceptableAaguids** | **[String]** |  | [optional] 
**webAuthnPolicyAttestationConveyancePreference** | **String** |  | [optional] 
**webAuthnPolicyAuthenticatorAttachment** | **String** |  | [optional] 
**webAuthnPolicyAvoidSameAuthenticatorRegister** | **Boolean** |  | [optional] 
**webAuthnPolicyCreateTimeout** | **Number** |  | [optional] 
**webAuthnPolicyPasswordlessAcceptableAaguids** | **[String]** |  | [optional] 
**webAuthnPolicyPasswordlessAttestationConveyancePreference** | **String** |  | [optional] 
**webAuthnPolicyPasswordlessAuthenticatorAttachment** | **String** |  | [optional] 
**webAuthnPolicyPasswordlessAvoidSameAuthenticatorRegister** | **Boolean** |  | [optional] 
**webAuthnPolicyPasswordlessCreateTimeout** | **Number** |  | [optional] 
**webAuthnPolicyPasswordlessRequireResidentKey** | **String** |  | [optional] 
**webAuthnPolicyPasswordlessRpEntityName** | **String** |  | [optional] 
**webAuthnPolicyPasswordlessRpId** | **String** |  | [optional] 
**webAuthnPolicyPasswordlessSignatureAlgorithms** | **[String]** |  | [optional] 
**webAuthnPolicyPasswordlessUserVerificationRequirement** | **String** |  | [optional] 
**webAuthnPolicyRequireResidentKey** | **String** |  | [optional] 
**webAuthnPolicyRpEntityName** | **String** |  | [optional] 
**webAuthnPolicyRpId** | **String** |  | [optional] 
**webAuthnPolicySignatureAlgorithms** | **[String]** |  | [optional] 
**webAuthnPolicyUserVerificationRequirement** | **String** |  | [optional] 


