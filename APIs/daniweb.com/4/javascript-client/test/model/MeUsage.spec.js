/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
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
    factory(root.expect, root.DaniWebConnectApi);
  }
}(this, function(expect, DaniWebConnectApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DaniWebConnectApi.MeUsage();
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

  describe('MeUsage', function() {
    it('should create an instance of MeUsage', function() {
      // uncomment below and update the code to test MeUsage
      //var instance = new DaniWebConnectApi.MeUsage();
      //expect(instance).to.be.a(DaniWebConnectApi.MeUsage);
    });

    it('should have the property availableStatus (base name: "available_status")', function() {
      // uncomment below and update the code to test the property availableStatus
      //var instance = new DaniWebConnectApi.MeUsage();
      //expect(instance).to.be();
    });

    it('should have the property joinedTimestamp (base name: "joined_timestamp")', function() {
      // uncomment below and update the code to test the property joinedTimestamp
      //var instance = new DaniWebConnectApi.MeUsage();
      //expect(instance).to.be();
    });

    it('should have the property lastActivityTimestamp (base name: "last_activity_timestamp")', function() {
      // uncomment below and update the code to test the property lastActivityTimestamp
      //var instance = new DaniWebConnectApi.MeUsage();
      //expect(instance).to.be();
    });

    it('should have the property onlineStatus (base name: "online_status")', function() {
      // uncomment below and update the code to test the property onlineStatus
      //var instance = new DaniWebConnectApi.MeUsage();
      //expect(instance).to.be();
    });

  });

}));
