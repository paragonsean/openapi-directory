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
    instance = new KeycloakAdminRestApi.ClientsApi();
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

  describe('ClientsApi', function() {
    describe('realmClientsGet', function() {
      it('should call realmClientsGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsGet
        //instance.realmClientsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdClientSecretGet', function() {
      it('should call realmClientsIdClientSecretGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdClientSecretGet
        //instance.realmClientsIdClientSecretGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdClientSecretPost', function() {
      it('should call realmClientsIdClientSecretPost successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdClientSecretPost
        //instance.realmClientsIdClientSecretPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdDefaultClientScopesClientScopeIdDelete', function() {
      it('should call realmClientsIdDefaultClientScopesClientScopeIdDelete successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdDefaultClientScopesClientScopeIdDelete
        //instance.realmClientsIdDefaultClientScopesClientScopeIdDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdDefaultClientScopesClientScopeIdPut', function() {
      it('should call realmClientsIdDefaultClientScopesClientScopeIdPut successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdDefaultClientScopesClientScopeIdPut
        //instance.realmClientsIdDefaultClientScopesClientScopeIdPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdDefaultClientScopesGet', function() {
      it('should call realmClientsIdDefaultClientScopesGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdDefaultClientScopesGet
        //instance.realmClientsIdDefaultClientScopesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdDelete', function() {
      it('should call realmClientsIdDelete successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdDelete
        //instance.realmClientsIdDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet', function() {
      it('should call realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet
        //instance.realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdEvaluateScopesProtocolMappersGet', function() {
      it('should call realmClientsIdEvaluateScopesProtocolMappersGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdEvaluateScopesProtocolMappersGet
        //instance.realmClientsIdEvaluateScopesProtocolMappersGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet', function() {
      it('should call realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet
        //instance.realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet', function() {
      it('should call realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet
        //instance.realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdGet', function() {
      it('should call realmClientsIdGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdGet
        //instance.realmClientsIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdInstallationProvidersProviderIdGet', function() {
      it('should call realmClientsIdInstallationProvidersProviderIdGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdInstallationProvidersProviderIdGet
        //instance.realmClientsIdInstallationProvidersProviderIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdManagementPermissionsGet', function() {
      it('should call realmClientsIdManagementPermissionsGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdManagementPermissionsGet
        //instance.realmClientsIdManagementPermissionsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdManagementPermissionsPut', function() {
      it('should call realmClientsIdManagementPermissionsPut successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdManagementPermissionsPut
        //instance.realmClientsIdManagementPermissionsPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdNodesNodeDelete', function() {
      it('should call realmClientsIdNodesNodeDelete successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdNodesNodeDelete
        //instance.realmClientsIdNodesNodeDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdNodesPost', function() {
      it('should call realmClientsIdNodesPost successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdNodesPost
        //instance.realmClientsIdNodesPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdOfflineSessionCountGet', function() {
      it('should call realmClientsIdOfflineSessionCountGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdOfflineSessionCountGet
        //instance.realmClientsIdOfflineSessionCountGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdOfflineSessionsGet', function() {
      it('should call realmClientsIdOfflineSessionsGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdOfflineSessionsGet
        //instance.realmClientsIdOfflineSessionsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdOptionalClientScopesClientScopeIdDelete', function() {
      it('should call realmClientsIdOptionalClientScopesClientScopeIdDelete successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdOptionalClientScopesClientScopeIdDelete
        //instance.realmClientsIdOptionalClientScopesClientScopeIdDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdOptionalClientScopesClientScopeIdPut', function() {
      it('should call realmClientsIdOptionalClientScopesClientScopeIdPut successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdOptionalClientScopesClientScopeIdPut
        //instance.realmClientsIdOptionalClientScopesClientScopeIdPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdOptionalClientScopesGet', function() {
      it('should call realmClientsIdOptionalClientScopesGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdOptionalClientScopesGet
        //instance.realmClientsIdOptionalClientScopesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdPushRevocationPost', function() {
      it('should call realmClientsIdPushRevocationPost successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdPushRevocationPost
        //instance.realmClientsIdPushRevocationPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdPut', function() {
      it('should call realmClientsIdPut successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdPut
        //instance.realmClientsIdPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdRegistrationAccessTokenPost', function() {
      it('should call realmClientsIdRegistrationAccessTokenPost successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdRegistrationAccessTokenPost
        //instance.realmClientsIdRegistrationAccessTokenPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdServiceAccountUserGet', function() {
      it('should call realmClientsIdServiceAccountUserGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdServiceAccountUserGet
        //instance.realmClientsIdServiceAccountUserGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdSessionCountGet', function() {
      it('should call realmClientsIdSessionCountGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdSessionCountGet
        //instance.realmClientsIdSessionCountGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdTestNodesAvailableGet', function() {
      it('should call realmClientsIdTestNodesAvailableGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdTestNodesAvailableGet
        //instance.realmClientsIdTestNodesAvailableGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsIdUserSessionsGet', function() {
      it('should call realmClientsIdUserSessionsGet successfully', function(done) {
        //uncomment below and update the code to test realmClientsIdUserSessionsGet
        //instance.realmClientsIdUserSessionsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmClientsPost', function() {
      it('should call realmClientsPost successfully', function(done) {
        //uncomment below and update the code to test realmClientsPost
        //instance.realmClientsPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
