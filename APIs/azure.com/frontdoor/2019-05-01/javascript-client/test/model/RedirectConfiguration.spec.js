/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
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
    factory(root.expect, root.FrontDoorManagementClient);
  }
}(this, function(expect, FrontDoorManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FrontDoorManagementClient.RedirectConfiguration();
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

  describe('RedirectConfiguration', function() {
    it('should create an instance of RedirectConfiguration', function() {
      // uncomment below and update the code to test RedirectConfiguration
      //var instance = new FrontDoorManagementClient.RedirectConfiguration();
      //expect(instance).to.be.a(FrontDoorManagementClient.RedirectConfiguration);
    });

    it('should have the property customFragment (base name: "customFragment")', function() {
      // uncomment below and update the code to test the property customFragment
      //var instance = new FrontDoorManagementClient.RedirectConfiguration();
      //expect(instance).to.be();
    });

    it('should have the property customHost (base name: "customHost")', function() {
      // uncomment below and update the code to test the property customHost
      //var instance = new FrontDoorManagementClient.RedirectConfiguration();
      //expect(instance).to.be();
    });

    it('should have the property customPath (base name: "customPath")', function() {
      // uncomment below and update the code to test the property customPath
      //var instance = new FrontDoorManagementClient.RedirectConfiguration();
      //expect(instance).to.be();
    });

    it('should have the property customQueryString (base name: "customQueryString")', function() {
      // uncomment below and update the code to test the property customQueryString
      //var instance = new FrontDoorManagementClient.RedirectConfiguration();
      //expect(instance).to.be();
    });

    it('should have the property redirectProtocol (base name: "redirectProtocol")', function() {
      // uncomment below and update the code to test the property redirectProtocol
      //var instance = new FrontDoorManagementClient.RedirectConfiguration();
      //expect(instance).to.be();
    });

    it('should have the property redirectType (base name: "redirectType")', function() {
      // uncomment below and update the code to test the property redirectType
      //var instance = new FrontDoorManagementClient.RedirectConfiguration();
      //expect(instance).to.be();
    });

  });

}));
