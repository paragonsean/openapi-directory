/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
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
    factory(root.expect, root.AppServicePlansApiClient);
  }
}(this, function(expect, AppServicePlansApiClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
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

  describe('AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig', function() {
    it('should create an instance of AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig', function() {
      // uncomment below and update the code to test AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be.a(AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig);
    });

    it('should have the property alwaysOn (base name: "alwaysOn")', function() {
      // uncomment below and update the code to test the property alwaysOn
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property apiDefinition (base name: "apiDefinition")', function() {
      // uncomment below and update the code to test the property apiDefinition
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property appCommandLine (base name: "appCommandLine")', function() {
      // uncomment below and update the code to test the property appCommandLine
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property appSettings (base name: "appSettings")', function() {
      // uncomment below and update the code to test the property appSettings
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property autoHealEnabled (base name: "autoHealEnabled")', function() {
      // uncomment below and update the code to test the property autoHealEnabled
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property autoHealRules (base name: "autoHealRules")', function() {
      // uncomment below and update the code to test the property autoHealRules
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property autoSwapSlotName (base name: "autoSwapSlotName")', function() {
      // uncomment below and update the code to test the property autoSwapSlotName
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property azureStorageAccounts (base name: "azureStorageAccounts")', function() {
      // uncomment below and update the code to test the property azureStorageAccounts
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property connectionStrings (base name: "connectionStrings")', function() {
      // uncomment below and update the code to test the property connectionStrings
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property cors (base name: "cors")', function() {
      // uncomment below and update the code to test the property cors
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property defaultDocuments (base name: "defaultDocuments")', function() {
      // uncomment below and update the code to test the property defaultDocuments
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property detailedErrorLoggingEnabled (base name: "detailedErrorLoggingEnabled")', function() {
      // uncomment below and update the code to test the property detailedErrorLoggingEnabled
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property documentRoot (base name: "documentRoot")', function() {
      // uncomment below and update the code to test the property documentRoot
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property experiments (base name: "experiments")', function() {
      // uncomment below and update the code to test the property experiments
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property ftpsState (base name: "ftpsState")', function() {
      // uncomment below and update the code to test the property ftpsState
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property handlerMappings (base name: "handlerMappings")', function() {
      // uncomment below and update the code to test the property handlerMappings
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property http20Enabled (base name: "http20Enabled")', function() {
      // uncomment below and update the code to test the property http20Enabled
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property httpLoggingEnabled (base name: "httpLoggingEnabled")', function() {
      // uncomment below and update the code to test the property httpLoggingEnabled
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property ipSecurityRestrictions (base name: "ipSecurityRestrictions")', function() {
      // uncomment below and update the code to test the property ipSecurityRestrictions
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property javaContainer (base name: "javaContainer")', function() {
      // uncomment below and update the code to test the property javaContainer
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property javaContainerVersion (base name: "javaContainerVersion")', function() {
      // uncomment below and update the code to test the property javaContainerVersion
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property javaVersion (base name: "javaVersion")', function() {
      // uncomment below and update the code to test the property javaVersion
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property limits (base name: "limits")', function() {
      // uncomment below and update the code to test the property limits
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property linuxFxVersion (base name: "linuxFxVersion")', function() {
      // uncomment below and update the code to test the property linuxFxVersion
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property loadBalancing (base name: "loadBalancing")', function() {
      // uncomment below and update the code to test the property loadBalancing
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property localMySqlEnabled (base name: "localMySqlEnabled")', function() {
      // uncomment below and update the code to test the property localMySqlEnabled
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property logsDirectorySizeLimit (base name: "logsDirectorySizeLimit")', function() {
      // uncomment below and update the code to test the property logsDirectorySizeLimit
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property machineKey (base name: "machineKey")', function() {
      // uncomment below and update the code to test the property machineKey
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property managedPipelineMode (base name: "managedPipelineMode")', function() {
      // uncomment below and update the code to test the property managedPipelineMode
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property managedServiceIdentityId (base name: "managedServiceIdentityId")', function() {
      // uncomment below and update the code to test the property managedServiceIdentityId
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property minTlsVersion (base name: "minTlsVersion")', function() {
      // uncomment below and update the code to test the property minTlsVersion
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property netFrameworkVersion (base name: "netFrameworkVersion")', function() {
      // uncomment below and update the code to test the property netFrameworkVersion
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property nodeVersion (base name: "nodeVersion")', function() {
      // uncomment below and update the code to test the property nodeVersion
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property numberOfWorkers (base name: "numberOfWorkers")', function() {
      // uncomment below and update the code to test the property numberOfWorkers
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property phpVersion (base name: "phpVersion")', function() {
      // uncomment below and update the code to test the property phpVersion
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property publishingUsername (base name: "publishingUsername")', function() {
      // uncomment below and update the code to test the property publishingUsername
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property push (base name: "push")', function() {
      // uncomment below and update the code to test the property push
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property pythonVersion (base name: "pythonVersion")', function() {
      // uncomment below and update the code to test the property pythonVersion
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property remoteDebuggingEnabled (base name: "remoteDebuggingEnabled")', function() {
      // uncomment below and update the code to test the property remoteDebuggingEnabled
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property remoteDebuggingVersion (base name: "remoteDebuggingVersion")', function() {
      // uncomment below and update the code to test the property remoteDebuggingVersion
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property requestTracingEnabled (base name: "requestTracingEnabled")', function() {
      // uncomment below and update the code to test the property requestTracingEnabled
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property requestTracingExpirationTime (base name: "requestTracingExpirationTime")', function() {
      // uncomment below and update the code to test the property requestTracingExpirationTime
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property reservedInstanceCount (base name: "reservedInstanceCount")', function() {
      // uncomment below and update the code to test the property reservedInstanceCount
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property scmIpSecurityRestrictions (base name: "scmIpSecurityRestrictions")', function() {
      // uncomment below and update the code to test the property scmIpSecurityRestrictions
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property scmIpSecurityRestrictionsUseMain (base name: "scmIpSecurityRestrictionsUseMain")', function() {
      // uncomment below and update the code to test the property scmIpSecurityRestrictionsUseMain
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property scmType (base name: "scmType")', function() {
      // uncomment below and update the code to test the property scmType
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property tracingOptions (base name: "tracingOptions")', function() {
      // uncomment below and update the code to test the property tracingOptions
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property use32BitWorkerProcess (base name: "use32BitWorkerProcess")', function() {
      // uncomment below and update the code to test the property use32BitWorkerProcess
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property virtualApplications (base name: "virtualApplications")', function() {
      // uncomment below and update the code to test the property virtualApplications
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property vnetName (base name: "vnetName")', function() {
      // uncomment below and update the code to test the property vnetName
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property webSocketsEnabled (base name: "webSocketsEnabled")', function() {
      // uncomment below and update the code to test the property webSocketsEnabled
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property windowsFxVersion (base name: "windowsFxVersion")', function() {
      // uncomment below and update the code to test the property windowsFxVersion
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

    it('should have the property xManagedServiceIdentityId (base name: "xManagedServiceIdentityId")', function() {
      // uncomment below and update the code to test the property xManagedServiceIdentityId
      //var instance = new AppServicePlansApiClient.AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig();
      //expect(instance).to.be();
    });

  });

}));
