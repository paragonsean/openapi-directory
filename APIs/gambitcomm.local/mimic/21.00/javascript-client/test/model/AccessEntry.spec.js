/**
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
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
    factory(root.expect, root.MimicRestApi);
  }
}(this, function(expect, MimicRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MimicRestApi.AccessEntry();
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

  describe('AccessEntry', function() {
    it('should create an instance of AccessEntry', function() {
      // uncomment below and update the code to test AccessEntry
      //var instance = new MimicRestApi.AccessEntry();
      //expect(instance).to.be.a(MimicRestApi.AccessEntry);
    });

    it('should have the property accessMask (base name: "access_mask")', function() {
      // uncomment below and update the code to test the property accessMask
      //var instance = new MimicRestApi.AccessEntry();
      //expect(instance).to.be();
    });

    it('should have the property agentRange (base name: "agent_range")', function() {
      // uncomment below and update the code to test the property agentRange
      //var instance = new MimicRestApi.AccessEntry();
      //expect(instance).to.be();
    });

    it('should have the property user (base name: "user")', function() {
      // uncomment below and update the code to test the property user
      //var instance = new MimicRestApi.AccessEntry();
      //expect(instance).to.be();
    });

  });

}));
