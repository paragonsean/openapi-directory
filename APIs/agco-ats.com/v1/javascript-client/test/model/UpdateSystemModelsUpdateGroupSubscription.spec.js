/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.AgcoApi);
  }
}(this, function(expect, AgcoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AgcoApi.UpdateSystemModelsUpdateGroupSubscription();
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

  describe('UpdateSystemModelsUpdateGroupSubscription', function() {
    it('should create an instance of UpdateSystemModelsUpdateGroupSubscription', function() {
      // uncomment below and update the code to test UpdateSystemModelsUpdateGroupSubscription
      //var instance = new AgcoApi.UpdateSystemModelsUpdateGroupSubscription();
      //expect(instance).to.be.a(AgcoApi.UpdateSystemModelsUpdateGroupSubscription);
    });

    it('should have the property clientID (base name: "ClientID")', function() {
      // uncomment below and update the code to test the property clientID
      //var instance = new AgcoApi.UpdateSystemModelsUpdateGroupSubscription();
      //expect(instance).to.be();
    });

    it('should have the property include (base name: "Include")', function() {
      // uncomment below and update the code to test the property include
      //var instance = new AgcoApi.UpdateSystemModelsUpdateGroupSubscription();
      //expect(instance).to.be();
    });

    it('should have the property packageTypeID (base name: "PackageTypeID")', function() {
      // uncomment below and update the code to test the property packageTypeID
      //var instance = new AgcoApi.UpdateSystemModelsUpdateGroupSubscription();
      //expect(instance).to.be();
    });

    it('should have the property updateGroupID (base name: "UpdateGroupID")', function() {
      // uncomment below and update the code to test the property updateGroupID
      //var instance = new AgcoApi.UpdateSystemModelsUpdateGroupSubscription();
      //expect(instance).to.be();
    });

    it('should have the property updateGroupSubscriptionID (base name: "UpdateGroupSubscriptionID")', function() {
      // uncomment below and update the code to test the property updateGroupSubscriptionID
      //var instance = new AgcoApi.UpdateSystemModelsUpdateGroupSubscription();
      //expect(instance).to.be();
    });

  });

}));
