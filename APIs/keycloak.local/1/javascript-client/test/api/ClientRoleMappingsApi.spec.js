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
    instance = new KeycloakAdminRestApi.ClientRoleMappingsApi();
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

  describe('ClientRoleMappingsApi', function() {
    describe('realmGroupsIdRoleMappingsClientsClientAvailableGet', function() {
      it('should call realmGroupsIdRoleMappingsClientsClientAvailableGet successfully', function(done) {
        //uncomment below and update the code to test realmGroupsIdRoleMappingsClientsClientAvailableGet
        //instance.realmGroupsIdRoleMappingsClientsClientAvailableGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmGroupsIdRoleMappingsClientsClientCompositeGet', function() {
      it('should call realmGroupsIdRoleMappingsClientsClientCompositeGet successfully', function(done) {
        //uncomment below and update the code to test realmGroupsIdRoleMappingsClientsClientCompositeGet
        //instance.realmGroupsIdRoleMappingsClientsClientCompositeGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmGroupsIdRoleMappingsClientsClientDelete', function() {
      it('should call realmGroupsIdRoleMappingsClientsClientDelete successfully', function(done) {
        //uncomment below and update the code to test realmGroupsIdRoleMappingsClientsClientDelete
        //instance.realmGroupsIdRoleMappingsClientsClientDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmGroupsIdRoleMappingsClientsClientGet', function() {
      it('should call realmGroupsIdRoleMappingsClientsClientGet successfully', function(done) {
        //uncomment below and update the code to test realmGroupsIdRoleMappingsClientsClientGet
        //instance.realmGroupsIdRoleMappingsClientsClientGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmGroupsIdRoleMappingsClientsClientPost', function() {
      it('should call realmGroupsIdRoleMappingsClientsClientPost successfully', function(done) {
        //uncomment below and update the code to test realmGroupsIdRoleMappingsClientsClientPost
        //instance.realmGroupsIdRoleMappingsClientsClientPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmUsersIdRoleMappingsClientsClientAvailableGet', function() {
      it('should call realmUsersIdRoleMappingsClientsClientAvailableGet successfully', function(done) {
        //uncomment below and update the code to test realmUsersIdRoleMappingsClientsClientAvailableGet
        //instance.realmUsersIdRoleMappingsClientsClientAvailableGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmUsersIdRoleMappingsClientsClientCompositeGet', function() {
      it('should call realmUsersIdRoleMappingsClientsClientCompositeGet successfully', function(done) {
        //uncomment below and update the code to test realmUsersIdRoleMappingsClientsClientCompositeGet
        //instance.realmUsersIdRoleMappingsClientsClientCompositeGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmUsersIdRoleMappingsClientsClientDelete', function() {
      it('should call realmUsersIdRoleMappingsClientsClientDelete successfully', function(done) {
        //uncomment below and update the code to test realmUsersIdRoleMappingsClientsClientDelete
        //instance.realmUsersIdRoleMappingsClientsClientDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmUsersIdRoleMappingsClientsClientGet', function() {
      it('should call realmUsersIdRoleMappingsClientsClientGet successfully', function(done) {
        //uncomment below and update the code to test realmUsersIdRoleMappingsClientsClientGet
        //instance.realmUsersIdRoleMappingsClientsClientGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realmUsersIdRoleMappingsClientsClientPost', function() {
      it('should call realmUsersIdRoleMappingsClientsClientPost successfully', function(done) {
        //uncomment below and update the code to test realmUsersIdRoleMappingsClientsClientPost
        //instance.realmUsersIdRoleMappingsClientsClientPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
