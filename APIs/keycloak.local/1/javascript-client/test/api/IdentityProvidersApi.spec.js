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
    instance = new KeycloakAdminRestApi.IdentityProvidersApi();
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

  describe('IdentityProvidersApi', function() {
    describe('realmIdentityProviderImportConfigPost', function() {
      it('should call realmIdentityProviderImportConfigPost successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderImportConfigPost
        //instance.realmIdentityProviderImportConfigPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasDelete', function() {
      it('should call realmIdentityProviderInstancesAliasDelete successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasDelete
        //instance.realmIdentityProviderInstancesAliasDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasExportGet', function() {
      it('should call realmIdentityProviderInstancesAliasExportGet successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasExportGet
        //instance.realmIdentityProviderInstancesAliasExportGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasGet', function() {
      it('should call realmIdentityProviderInstancesAliasGet successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasGet
        //instance.realmIdentityProviderInstancesAliasGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasManagementPermissionsGet', function() {
      it('should call realmIdentityProviderInstancesAliasManagementPermissionsGet successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasManagementPermissionsGet
        //instance.realmIdentityProviderInstancesAliasManagementPermissionsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasManagementPermissionsPut', function() {
      it('should call realmIdentityProviderInstancesAliasManagementPermissionsPut successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasManagementPermissionsPut
        //instance.realmIdentityProviderInstancesAliasManagementPermissionsPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasMapperTypesGet', function() {
      it('should call realmIdentityProviderInstancesAliasMapperTypesGet successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasMapperTypesGet
        //instance.realmIdentityProviderInstancesAliasMapperTypesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasMappersGet', function() {
      it('should call realmIdentityProviderInstancesAliasMappersGet successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasMappersGet
        //instance.realmIdentityProviderInstancesAliasMappersGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasMappersIdDelete', function() {
      it('should call realmIdentityProviderInstancesAliasMappersIdDelete successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasMappersIdDelete
        //instance.realmIdentityProviderInstancesAliasMappersIdDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasMappersIdGet', function() {
      it('should call realmIdentityProviderInstancesAliasMappersIdGet successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasMappersIdGet
        //instance.realmIdentityProviderInstancesAliasMappersIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasMappersIdPut', function() {
      it('should call realmIdentityProviderInstancesAliasMappersIdPut successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasMappersIdPut
        //instance.realmIdentityProviderInstancesAliasMappersIdPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasMappersPost', function() {
      it('should call realmIdentityProviderInstancesAliasMappersPost successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasMappersPost
        //instance.realmIdentityProviderInstancesAliasMappersPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesAliasPut', function() {
      it('should call realmIdentityProviderInstancesAliasPut successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesAliasPut
        //instance.realmIdentityProviderInstancesAliasPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesGet', function() {
      it('should call realmIdentityProviderInstancesGet successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesGet
        //instance.realmIdentityProviderInstancesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderInstancesPost', function() {
      it('should call realmIdentityProviderInstancesPost successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderInstancesPost
        //instance.realmIdentityProviderInstancesPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmIdentityProviderProvidersProviderIdGet', function() {
      it('should call realmIdentityProviderProvidersProviderIdGet successfully', function(done) {
        //uncomment below and update the code to test realmIdentityProviderProvidersProviderIdGet
        //instance.realmIdentityProviderProvidersProviderIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
