/**
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.KeycloakAdminRestApi);
  }
}(this, function(expect, KeycloakAdminRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new KeycloakAdminRestApi.RealmRepresentation();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('RealmRepresentation', function() {
    it('should create an instance of RealmRepresentation', function() {
      // uncomment below and update the code to test RealmRepresentation
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be.a(KeycloakAdminRestApi.RealmRepresentation);
    });

    it('should have the property accessCodeLifespan (base name: "accessCodeLifespan")', function() {
      // uncomment below and update the code to test the property accessCodeLifespan
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property accessCodeLifespanLogin (base name: "accessCodeLifespanLogin")', function() {
      // uncomment below and update the code to test the property accessCodeLifespanLogin
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property accessCodeLifespanUserAction (base name: "accessCodeLifespanUserAction")', function() {
      // uncomment below and update the code to test the property accessCodeLifespanUserAction
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property accessTokenLifespan (base name: "accessTokenLifespan")', function() {
      // uncomment below and update the code to test the property accessTokenLifespan
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property accessTokenLifespanForImplicitFlow (base name: "accessTokenLifespanForImplicitFlow")', function() {
      // uncomment below and update the code to test the property accessTokenLifespanForImplicitFlow
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property accountTheme (base name: "accountTheme")', function() {
      // uncomment below and update the code to test the property accountTheme
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property actionTokenGeneratedByAdminLifespan (base name: "actionTokenGeneratedByAdminLifespan")', function() {
      // uncomment below and update the code to test the property actionTokenGeneratedByAdminLifespan
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property actionTokenGeneratedByUserLifespan (base name: "actionTokenGeneratedByUserLifespan")', function() {
      // uncomment below and update the code to test the property actionTokenGeneratedByUserLifespan
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property adminEventsDetailsEnabled (base name: "adminEventsDetailsEnabled")', function() {
      // uncomment below and update the code to test the property adminEventsDetailsEnabled
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property adminEventsEnabled (base name: "adminEventsEnabled")', function() {
      // uncomment below and update the code to test the property adminEventsEnabled
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property adminTheme (base name: "adminTheme")', function() {
      // uncomment below and update the code to test the property adminTheme
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property attributes (base name: "attributes")', function() {
      // uncomment below and update the code to test the property attributes
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property authenticationFlows (base name: "authenticationFlows")', function() {
      // uncomment below and update the code to test the property authenticationFlows
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property authenticatorConfig (base name: "authenticatorConfig")', function() {
      // uncomment below and update the code to test the property authenticatorConfig
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property browserFlow (base name: "browserFlow")', function() {
      // uncomment below and update the code to test the property browserFlow
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property browserSecurityHeaders (base name: "browserSecurityHeaders")', function() {
      // uncomment below and update the code to test the property browserSecurityHeaders
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property bruteForceProtected (base name: "bruteForceProtected")', function() {
      // uncomment below and update the code to test the property bruteForceProtected
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property clientAuthenticationFlow (base name: "clientAuthenticationFlow")', function() {
      // uncomment below and update the code to test the property clientAuthenticationFlow
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property clientScopeMappings (base name: "clientScopeMappings")', function() {
      // uncomment below and update the code to test the property clientScopeMappings
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property clientScopes (base name: "clientScopes")', function() {
      // uncomment below and update the code to test the property clientScopes
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property clientSessionIdleTimeout (base name: "clientSessionIdleTimeout")', function() {
      // uncomment below and update the code to test the property clientSessionIdleTimeout
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property clientSessionMaxLifespan (base name: "clientSessionMaxLifespan")', function() {
      // uncomment below and update the code to test the property clientSessionMaxLifespan
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property clients (base name: "clients")', function() {
      // uncomment below and update the code to test the property clients
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property components (base name: "components")', function() {
      // uncomment below and update the code to test the property components
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property defaultDefaultClientScopes (base name: "defaultDefaultClientScopes")', function() {
      // uncomment below and update the code to test the property defaultDefaultClientScopes
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property defaultGroups (base name: "defaultGroups")', function() {
      // uncomment below and update the code to test the property defaultGroups
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property defaultLocale (base name: "defaultLocale")', function() {
      // uncomment below and update the code to test the property defaultLocale
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property defaultOptionalClientScopes (base name: "defaultOptionalClientScopes")', function() {
      // uncomment below and update the code to test the property defaultOptionalClientScopes
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property defaultRoles (base name: "defaultRoles")', function() {
      // uncomment below and update the code to test the property defaultRoles
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property defaultSignatureAlgorithm (base name: "defaultSignatureAlgorithm")', function() {
      // uncomment below and update the code to test the property defaultSignatureAlgorithm
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property directGrantFlow (base name: "directGrantFlow")', function() {
      // uncomment below and update the code to test the property directGrantFlow
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property displayName (base name: "displayName")', function() {
      // uncomment below and update the code to test the property displayName
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property displayNameHtml (base name: "displayNameHtml")', function() {
      // uncomment below and update the code to test the property displayNameHtml
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property dockerAuthenticationFlow (base name: "dockerAuthenticationFlow")', function() {
      // uncomment below and update the code to test the property dockerAuthenticationFlow
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property duplicateEmailsAllowed (base name: "duplicateEmailsAllowed")', function() {
      // uncomment below and update the code to test the property duplicateEmailsAllowed
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property editUsernameAllowed (base name: "editUsernameAllowed")', function() {
      // uncomment below and update the code to test the property editUsernameAllowed
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property emailTheme (base name: "emailTheme")', function() {
      // uncomment below and update the code to test the property emailTheme
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property enabled (base name: "enabled")', function() {
      // uncomment below and update the code to test the property enabled
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property enabledEventTypes (base name: "enabledEventTypes")', function() {
      // uncomment below and update the code to test the property enabledEventTypes
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property eventsEnabled (base name: "eventsEnabled")', function() {
      // uncomment below and update the code to test the property eventsEnabled
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property eventsExpiration (base name: "eventsExpiration")', function() {
      // uncomment below and update the code to test the property eventsExpiration
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property eventsListeners (base name: "eventsListeners")', function() {
      // uncomment below and update the code to test the property eventsListeners
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property failureFactor (base name: "failureFactor")', function() {
      // uncomment below and update the code to test the property failureFactor
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property federatedUsers (base name: "federatedUsers")', function() {
      // uncomment below and update the code to test the property federatedUsers
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property groups (base name: "groups")', function() {
      // uncomment below and update the code to test the property groups
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property identityProviderMappers (base name: "identityProviderMappers")', function() {
      // uncomment below and update the code to test the property identityProviderMappers
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property identityProviders (base name: "identityProviders")', function() {
      // uncomment below and update the code to test the property identityProviders
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property internationalizationEnabled (base name: "internationalizationEnabled")', function() {
      // uncomment below and update the code to test the property internationalizationEnabled
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property keycloakVersion (base name: "keycloakVersion")', function() {
      // uncomment below and update the code to test the property keycloakVersion
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property loginTheme (base name: "loginTheme")', function() {
      // uncomment below and update the code to test the property loginTheme
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property loginWithEmailAllowed (base name: "loginWithEmailAllowed")', function() {
      // uncomment below and update the code to test the property loginWithEmailAllowed
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property maxDeltaTimeSeconds (base name: "maxDeltaTimeSeconds")', function() {
      // uncomment below and update the code to test the property maxDeltaTimeSeconds
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property maxFailureWaitSeconds (base name: "maxFailureWaitSeconds")', function() {
      // uncomment below and update the code to test the property maxFailureWaitSeconds
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property minimumQuickLoginWaitSeconds (base name: "minimumQuickLoginWaitSeconds")', function() {
      // uncomment below and update the code to test the property minimumQuickLoginWaitSeconds
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property notBefore (base name: "notBefore")', function() {
      // uncomment below and update the code to test the property notBefore
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property offlineSessionIdleTimeout (base name: "offlineSessionIdleTimeout")', function() {
      // uncomment below and update the code to test the property offlineSessionIdleTimeout
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property offlineSessionMaxLifespan (base name: "offlineSessionMaxLifespan")', function() {
      // uncomment below and update the code to test the property offlineSessionMaxLifespan
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property offlineSessionMaxLifespanEnabled (base name: "offlineSessionMaxLifespanEnabled")', function() {
      // uncomment below and update the code to test the property offlineSessionMaxLifespanEnabled
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property otpPolicyAlgorithm (base name: "otpPolicyAlgorithm")', function() {
      // uncomment below and update the code to test the property otpPolicyAlgorithm
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property otpPolicyDigits (base name: "otpPolicyDigits")', function() {
      // uncomment below and update the code to test the property otpPolicyDigits
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property otpPolicyInitialCounter (base name: "otpPolicyInitialCounter")', function() {
      // uncomment below and update the code to test the property otpPolicyInitialCounter
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property otpPolicyLookAheadWindow (base name: "otpPolicyLookAheadWindow")', function() {
      // uncomment below and update the code to test the property otpPolicyLookAheadWindow
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property otpPolicyPeriod (base name: "otpPolicyPeriod")', function() {
      // uncomment below and update the code to test the property otpPolicyPeriod
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property otpPolicyType (base name: "otpPolicyType")', function() {
      // uncomment below and update the code to test the property otpPolicyType
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property otpSupportedApplications (base name: "otpSupportedApplications")', function() {
      // uncomment below and update the code to test the property otpSupportedApplications
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property passwordPolicy (base name: "passwordPolicy")', function() {
      // uncomment below and update the code to test the property passwordPolicy
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property permanentLockout (base name: "permanentLockout")', function() {
      // uncomment below and update the code to test the property permanentLockout
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property protocolMappers (base name: "protocolMappers")', function() {
      // uncomment below and update the code to test the property protocolMappers
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property quickLoginCheckMilliSeconds (base name: "quickLoginCheckMilliSeconds")', function() {
      // uncomment below and update the code to test the property quickLoginCheckMilliSeconds
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property realm (base name: "realm")', function() {
      // uncomment below and update the code to test the property realm
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property refreshTokenMaxReuse (base name: "refreshTokenMaxReuse")', function() {
      // uncomment below and update the code to test the property refreshTokenMaxReuse
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property registrationAllowed (base name: "registrationAllowed")', function() {
      // uncomment below and update the code to test the property registrationAllowed
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property registrationEmailAsUsername (base name: "registrationEmailAsUsername")', function() {
      // uncomment below and update the code to test the property registrationEmailAsUsername
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property registrationFlow (base name: "registrationFlow")', function() {
      // uncomment below and update the code to test the property registrationFlow
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property rememberMe (base name: "rememberMe")', function() {
      // uncomment below and update the code to test the property rememberMe
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property requiredActions (base name: "requiredActions")', function() {
      // uncomment below and update the code to test the property requiredActions
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property resetCredentialsFlow (base name: "resetCredentialsFlow")', function() {
      // uncomment below and update the code to test the property resetCredentialsFlow
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property resetPasswordAllowed (base name: "resetPasswordAllowed")', function() {
      // uncomment below and update the code to test the property resetPasswordAllowed
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property revokeRefreshToken (base name: "revokeRefreshToken")', function() {
      // uncomment below and update the code to test the property revokeRefreshToken
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property roles (base name: "roles")', function() {
      // uncomment below and update the code to test the property roles
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property scopeMappings (base name: "scopeMappings")', function() {
      // uncomment below and update the code to test the property scopeMappings
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property smtpServer (base name: "smtpServer")', function() {
      // uncomment below and update the code to test the property smtpServer
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property sslRequired (base name: "sslRequired")', function() {
      // uncomment below and update the code to test the property sslRequired
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property ssoSessionIdleTimeout (base name: "ssoSessionIdleTimeout")', function() {
      // uncomment below and update the code to test the property ssoSessionIdleTimeout
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property ssoSessionIdleTimeoutRememberMe (base name: "ssoSessionIdleTimeoutRememberMe")', function() {
      // uncomment below and update the code to test the property ssoSessionIdleTimeoutRememberMe
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property ssoSessionMaxLifespan (base name: "ssoSessionMaxLifespan")', function() {
      // uncomment below and update the code to test the property ssoSessionMaxLifespan
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property ssoSessionMaxLifespanRememberMe (base name: "ssoSessionMaxLifespanRememberMe")', function() {
      // uncomment below and update the code to test the property ssoSessionMaxLifespanRememberMe
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property supportedLocales (base name: "supportedLocales")', function() {
      // uncomment below and update the code to test the property supportedLocales
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property userFederationMappers (base name: "userFederationMappers")', function() {
      // uncomment below and update the code to test the property userFederationMappers
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property userFederationProviders (base name: "userFederationProviders")', function() {
      // uncomment below and update the code to test the property userFederationProviders
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property userManagedAccessAllowed (base name: "userManagedAccessAllowed")', function() {
      // uncomment below and update the code to test the property userManagedAccessAllowed
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property users (base name: "users")', function() {
      // uncomment below and update the code to test the property users
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property verifyEmail (base name: "verifyEmail")', function() {
      // uncomment below and update the code to test the property verifyEmail
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property waitIncrementSeconds (base name: "waitIncrementSeconds")', function() {
      // uncomment below and update the code to test the property waitIncrementSeconds
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyAcceptableAaguids (base name: "webAuthnPolicyAcceptableAaguids")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyAcceptableAaguids
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyAttestationConveyancePreference (base name: "webAuthnPolicyAttestationConveyancePreference")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyAttestationConveyancePreference
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyAuthenticatorAttachment (base name: "webAuthnPolicyAuthenticatorAttachment")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyAuthenticatorAttachment
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyAvoidSameAuthenticatorRegister (base name: "webAuthnPolicyAvoidSameAuthenticatorRegister")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyAvoidSameAuthenticatorRegister
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyCreateTimeout (base name: "webAuthnPolicyCreateTimeout")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyCreateTimeout
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyPasswordlessAcceptableAaguids (base name: "webAuthnPolicyPasswordlessAcceptableAaguids")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyPasswordlessAcceptableAaguids
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyPasswordlessAttestationConveyancePreference (base name: "webAuthnPolicyPasswordlessAttestationConveyancePreference")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyPasswordlessAttestationConveyancePreference
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyPasswordlessAuthenticatorAttachment (base name: "webAuthnPolicyPasswordlessAuthenticatorAttachment")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyPasswordlessAuthenticatorAttachment
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyPasswordlessAvoidSameAuthenticatorRegister (base name: "webAuthnPolicyPasswordlessAvoidSameAuthenticatorRegister")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyPasswordlessAvoidSameAuthenticatorRegister
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyPasswordlessCreateTimeout (base name: "webAuthnPolicyPasswordlessCreateTimeout")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyPasswordlessCreateTimeout
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyPasswordlessRequireResidentKey (base name: "webAuthnPolicyPasswordlessRequireResidentKey")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyPasswordlessRequireResidentKey
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyPasswordlessRpEntityName (base name: "webAuthnPolicyPasswordlessRpEntityName")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyPasswordlessRpEntityName
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyPasswordlessRpId (base name: "webAuthnPolicyPasswordlessRpId")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyPasswordlessRpId
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyPasswordlessSignatureAlgorithms (base name: "webAuthnPolicyPasswordlessSignatureAlgorithms")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyPasswordlessSignatureAlgorithms
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyPasswordlessUserVerificationRequirement (base name: "webAuthnPolicyPasswordlessUserVerificationRequirement")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyPasswordlessUserVerificationRequirement
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyRequireResidentKey (base name: "webAuthnPolicyRequireResidentKey")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyRequireResidentKey
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyRpEntityName (base name: "webAuthnPolicyRpEntityName")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyRpEntityName
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyRpId (base name: "webAuthnPolicyRpId")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyRpId
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicySignatureAlgorithms (base name: "webAuthnPolicySignatureAlgorithms")', function() {
      // uncomment below and update the code to test the property webAuthnPolicySignatureAlgorithms
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

    it('should have the property webAuthnPolicyUserVerificationRequirement (base name: "webAuthnPolicyUserVerificationRequirement")', function() {
      // uncomment below and update the code to test the property webAuthnPolicyUserVerificationRequirement
      //var instance = new KeycloakAdminRestApi.RealmRepresentation();
      //expect(instance).to.be();
    });

  });

}));
