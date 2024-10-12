/**
 * AuthorizationManagementClient
 * Role based access control provides you a way to apply granular level policy administration down to individual resources or resource groups. These operations enable you to manage role definitions and role assignments. A role definition describes the set of actions that can be performed on resources. A role assignment grants access to Azure Active Directory users.
 *
 * The version of the OpenAPI document: 2018-01-01-preview
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
    factory(root.expect, root.AuthorizationManagementClient);
  }
}(this, function(expect, AuthorizationManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AuthorizationManagementClient.ProviderOperationsMetadataApi();
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

  describe('ProviderOperationsMetadataApi', function() {
    describe('providerOperationsMetadataGet', function() {
      it('should call providerOperationsMetadataGet successfully', function(done) {
        //uncomment below and update the code to test providerOperationsMetadataGet
        //instance.providerOperationsMetadataGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('providerOperationsMetadataList', function() {
      it('should call providerOperationsMetadataList successfully', function(done) {
        //uncomment below and update the code to test providerOperationsMetadataList
        //instance.providerOperationsMetadataList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
