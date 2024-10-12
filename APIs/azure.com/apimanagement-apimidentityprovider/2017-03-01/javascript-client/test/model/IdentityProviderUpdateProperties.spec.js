/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2017-03-01
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
    factory(root.expect, root.ApiManagementClient);
  }
}(this, function(expect, ApiManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ApiManagementClient.IdentityProviderUpdateProperties();
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

  describe('IdentityProviderUpdateProperties', function() {
    it('should create an instance of IdentityProviderUpdateProperties', function() {
      // uncomment below and update the code to test IdentityProviderUpdateProperties
      //var instance = new ApiManagementClient.IdentityProviderUpdateProperties();
      //expect(instance).to.be.a(ApiManagementClient.IdentityProviderUpdateProperties);
    });

    it('should have the property clientId (base name: "clientId")', function() {
      // uncomment below and update the code to test the property clientId
      //var instance = new ApiManagementClient.IdentityProviderUpdateProperties();
      //expect(instance).to.be();
    });

    it('should have the property clientSecret (base name: "clientSecret")', function() {
      // uncomment below and update the code to test the property clientSecret
      //var instance = new ApiManagementClient.IdentityProviderUpdateProperties();
      //expect(instance).to.be();
    });

    it('should have the property allowedTenants (base name: "allowedTenants")', function() {
      // uncomment below and update the code to test the property allowedTenants
      //var instance = new ApiManagementClient.IdentityProviderUpdateProperties();
      //expect(instance).to.be();
    });

    it('should have the property passwordResetPolicyName (base name: "passwordResetPolicyName")', function() {
      // uncomment below and update the code to test the property passwordResetPolicyName
      //var instance = new ApiManagementClient.IdentityProviderUpdateProperties();
      //expect(instance).to.be();
    });

    it('should have the property profileEditingPolicyName (base name: "profileEditingPolicyName")', function() {
      // uncomment below and update the code to test the property profileEditingPolicyName
      //var instance = new ApiManagementClient.IdentityProviderUpdateProperties();
      //expect(instance).to.be();
    });

    it('should have the property signinPolicyName (base name: "signinPolicyName")', function() {
      // uncomment below and update the code to test the property signinPolicyName
      //var instance = new ApiManagementClient.IdentityProviderUpdateProperties();
      //expect(instance).to.be();
    });

    it('should have the property signupPolicyName (base name: "signupPolicyName")', function() {
      // uncomment below and update the code to test the property signupPolicyName
      //var instance = new ApiManagementClient.IdentityProviderUpdateProperties();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new ApiManagementClient.IdentityProviderUpdateProperties();
      //expect(instance).to.be();
    });

  });

}));
