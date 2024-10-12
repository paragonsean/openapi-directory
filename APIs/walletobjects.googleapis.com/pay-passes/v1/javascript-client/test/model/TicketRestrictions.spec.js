/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
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
    factory(root.expect, root.GooglePayPassesApi);
  }
}(this, function(expect, GooglePayPassesApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new GooglePayPassesApi.TicketRestrictions();
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

  describe('TicketRestrictions', function() {
    it('should create an instance of TicketRestrictions', function() {
      // uncomment below and update the code to test TicketRestrictions
      //var instance = new GooglePayPassesApi.TicketRestrictions();
      //expect(instance).to.be.a(GooglePayPassesApi.TicketRestrictions);
    });

    it('should have the property otherRestrictions (base name: "otherRestrictions")', function() {
      // uncomment below and update the code to test the property otherRestrictions
      //var instance = new GooglePayPassesApi.TicketRestrictions();
      //expect(instance).to.be();
    });

    it('should have the property routeRestrictions (base name: "routeRestrictions")', function() {
      // uncomment below and update the code to test the property routeRestrictions
      //var instance = new GooglePayPassesApi.TicketRestrictions();
      //expect(instance).to.be();
    });

    it('should have the property routeRestrictionsDetails (base name: "routeRestrictionsDetails")', function() {
      // uncomment below and update the code to test the property routeRestrictionsDetails
      //var instance = new GooglePayPassesApi.TicketRestrictions();
      //expect(instance).to.be();
    });

    it('should have the property timeRestrictions (base name: "timeRestrictions")', function() {
      // uncomment below and update the code to test the property timeRestrictions
      //var instance = new GooglePayPassesApi.TicketRestrictions();
      //expect(instance).to.be();
    });

  });

}));
