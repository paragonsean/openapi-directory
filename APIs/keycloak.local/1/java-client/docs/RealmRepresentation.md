

# RealmRepresentation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessCodeLifespan** | **Integer** |  |  [optional] |
|**accessCodeLifespanLogin** | **Integer** |  |  [optional] |
|**accessCodeLifespanUserAction** | **Integer** |  |  [optional] |
|**accessTokenLifespan** | **Integer** |  |  [optional] |
|**accessTokenLifespanForImplicitFlow** | **Integer** |  |  [optional] |
|**accountTheme** | **String** |  |  [optional] |
|**actionTokenGeneratedByAdminLifespan** | **Integer** |  |  [optional] |
|**actionTokenGeneratedByUserLifespan** | **Integer** |  |  [optional] |
|**adminEventsDetailsEnabled** | **Boolean** |  |  [optional] |
|**adminEventsEnabled** | **Boolean** |  |  [optional] |
|**adminTheme** | **String** |  |  [optional] |
|**attributes** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**authenticationFlows** | [**List&lt;AuthenticationFlowRepresentation&gt;**](AuthenticationFlowRepresentation.md) |  |  [optional] |
|**authenticatorConfig** | [**List&lt;AuthenticatorConfigRepresentation&gt;**](AuthenticatorConfigRepresentation.md) |  |  [optional] |
|**browserFlow** | **String** |  |  [optional] |
|**browserSecurityHeaders** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**bruteForceProtected** | **Boolean** |  |  [optional] |
|**clientAuthenticationFlow** | **String** |  |  [optional] |
|**clientScopeMappings** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**clientScopes** | [**List&lt;ClientScopeRepresentation&gt;**](ClientScopeRepresentation.md) |  |  [optional] |
|**clientSessionIdleTimeout** | **Integer** |  |  [optional] |
|**clientSessionMaxLifespan** | **Integer** |  |  [optional] |
|**clients** | [**List&lt;ClientRepresentation&gt;**](ClientRepresentation.md) |  |  [optional] |
|**components** | [**MultivaluedHashMap**](MultivaluedHashMap.md) |  |  [optional] |
|**defaultDefaultClientScopes** | **List&lt;String&gt;** |  |  [optional] |
|**defaultGroups** | **List&lt;String&gt;** |  |  [optional] |
|**defaultLocale** | **String** |  |  [optional] |
|**defaultOptionalClientScopes** | **List&lt;String&gt;** |  |  [optional] |
|**defaultRoles** | **List&lt;String&gt;** |  |  [optional] |
|**defaultSignatureAlgorithm** | **String** |  |  [optional] |
|**directGrantFlow** | **String** |  |  [optional] |
|**displayName** | **String** |  |  [optional] |
|**displayNameHtml** | **String** |  |  [optional] |
|**dockerAuthenticationFlow** | **String** |  |  [optional] |
|**duplicateEmailsAllowed** | **Boolean** |  |  [optional] |
|**editUsernameAllowed** | **Boolean** |  |  [optional] |
|**emailTheme** | **String** |  |  [optional] |
|**enabled** | **Boolean** |  |  [optional] |
|**enabledEventTypes** | **List&lt;String&gt;** |  |  [optional] |
|**eventsEnabled** | **Boolean** |  |  [optional] |
|**eventsExpiration** | **Long** |  |  [optional] |
|**eventsListeners** | **List&lt;String&gt;** |  |  [optional] |
|**failureFactor** | **Integer** |  |  [optional] |
|**federatedUsers** | [**List&lt;UserRepresentation&gt;**](UserRepresentation.md) |  |  [optional] |
|**groups** | [**List&lt;GroupRepresentation&gt;**](GroupRepresentation.md) |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**identityProviderMappers** | [**List&lt;IdentityProviderMapperRepresentation&gt;**](IdentityProviderMapperRepresentation.md) |  |  [optional] |
|**identityProviders** | [**List&lt;IdentityProviderRepresentation&gt;**](IdentityProviderRepresentation.md) |  |  [optional] |
|**internationalizationEnabled** | **Boolean** |  |  [optional] |
|**keycloakVersion** | **String** |  |  [optional] |
|**loginTheme** | **String** |  |  [optional] |
|**loginWithEmailAllowed** | **Boolean** |  |  [optional] |
|**maxDeltaTimeSeconds** | **Integer** |  |  [optional] |
|**maxFailureWaitSeconds** | **Integer** |  |  [optional] |
|**minimumQuickLoginWaitSeconds** | **Integer** |  |  [optional] |
|**notBefore** | **Integer** |  |  [optional] |
|**offlineSessionIdleTimeout** | **Integer** |  |  [optional] |
|**offlineSessionMaxLifespan** | **Integer** |  |  [optional] |
|**offlineSessionMaxLifespanEnabled** | **Boolean** |  |  [optional] |
|**otpPolicyAlgorithm** | **String** |  |  [optional] |
|**otpPolicyDigits** | **Integer** |  |  [optional] |
|**otpPolicyInitialCounter** | **Integer** |  |  [optional] |
|**otpPolicyLookAheadWindow** | **Integer** |  |  [optional] |
|**otpPolicyPeriod** | **Integer** |  |  [optional] |
|**otpPolicyType** | **String** |  |  [optional] |
|**otpSupportedApplications** | **List&lt;String&gt;** |  |  [optional] |
|**passwordPolicy** | **String** |  |  [optional] |
|**permanentLockout** | **Boolean** |  |  [optional] |
|**protocolMappers** | [**List&lt;ProtocolMapperRepresentation&gt;**](ProtocolMapperRepresentation.md) |  |  [optional] |
|**quickLoginCheckMilliSeconds** | **Long** |  |  [optional] |
|**realm** | **String** |  |  [optional] |
|**refreshTokenMaxReuse** | **Integer** |  |  [optional] |
|**registrationAllowed** | **Boolean** |  |  [optional] |
|**registrationEmailAsUsername** | **Boolean** |  |  [optional] |
|**registrationFlow** | **String** |  |  [optional] |
|**rememberMe** | **Boolean** |  |  [optional] |
|**requiredActions** | [**List&lt;RequiredActionProviderRepresentation&gt;**](RequiredActionProviderRepresentation.md) |  |  [optional] |
|**resetCredentialsFlow** | **String** |  |  [optional] |
|**resetPasswordAllowed** | **Boolean** |  |  [optional] |
|**revokeRefreshToken** | **Boolean** |  |  [optional] |
|**roles** | [**RolesRepresentation**](RolesRepresentation.md) |  |  [optional] |
|**scopeMappings** | [**List&lt;ScopeMappingRepresentation&gt;**](ScopeMappingRepresentation.md) |  |  [optional] |
|**smtpServer** | **Map&lt;String, Object&gt;** |  |  [optional] |
|**sslRequired** | **String** |  |  [optional] |
|**ssoSessionIdleTimeout** | **Integer** |  |  [optional] |
|**ssoSessionIdleTimeoutRememberMe** | **Integer** |  |  [optional] |
|**ssoSessionMaxLifespan** | **Integer** |  |  [optional] |
|**ssoSessionMaxLifespanRememberMe** | **Integer** |  |  [optional] |
|**supportedLocales** | **List&lt;String&gt;** |  |  [optional] |
|**userFederationMappers** | [**List&lt;UserFederationMapperRepresentation&gt;**](UserFederationMapperRepresentation.md) |  |  [optional] |
|**userFederationProviders** | [**List&lt;UserFederationProviderRepresentation&gt;**](UserFederationProviderRepresentation.md) |  |  [optional] |
|**userManagedAccessAllowed** | **Boolean** |  |  [optional] |
|**users** | [**List&lt;UserRepresentation&gt;**](UserRepresentation.md) |  |  [optional] |
|**verifyEmail** | **Boolean** |  |  [optional] |
|**waitIncrementSeconds** | **Integer** |  |  [optional] |
|**webAuthnPolicyAcceptableAaguids** | **List&lt;String&gt;** |  |  [optional] |
|**webAuthnPolicyAttestationConveyancePreference** | **String** |  |  [optional] |
|**webAuthnPolicyAuthenticatorAttachment** | **String** |  |  [optional] |
|**webAuthnPolicyAvoidSameAuthenticatorRegister** | **Boolean** |  |  [optional] |
|**webAuthnPolicyCreateTimeout** | **Integer** |  |  [optional] |
|**webAuthnPolicyPasswordlessAcceptableAaguids** | **List&lt;String&gt;** |  |  [optional] |
|**webAuthnPolicyPasswordlessAttestationConveyancePreference** | **String** |  |  [optional] |
|**webAuthnPolicyPasswordlessAuthenticatorAttachment** | **String** |  |  [optional] |
|**webAuthnPolicyPasswordlessAvoidSameAuthenticatorRegister** | **Boolean** |  |  [optional] |
|**webAuthnPolicyPasswordlessCreateTimeout** | **Integer** |  |  [optional] |
|**webAuthnPolicyPasswordlessRequireResidentKey** | **String** |  |  [optional] |
|**webAuthnPolicyPasswordlessRpEntityName** | **String** |  |  [optional] |
|**webAuthnPolicyPasswordlessRpId** | **String** |  |  [optional] |
|**webAuthnPolicyPasswordlessSignatureAlgorithms** | **List&lt;String&gt;** |  |  [optional] |
|**webAuthnPolicyPasswordlessUserVerificationRequirement** | **String** |  |  [optional] |
|**webAuthnPolicyRequireResidentKey** | **String** |  |  [optional] |
|**webAuthnPolicyRpEntityName** | **String** |  |  [optional] |
|**webAuthnPolicyRpId** | **String** |  |  [optional] |
|**webAuthnPolicySignatureAlgorithms** | **List&lt;String&gt;** |  |  [optional] |
|**webAuthnPolicyUserVerificationRequirement** | **String** |  |  [optional] |



