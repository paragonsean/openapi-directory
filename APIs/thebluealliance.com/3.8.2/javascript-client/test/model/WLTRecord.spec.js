/**
 * The Blue Alliance API v3
 * # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).
 *
 * The version of the OpenAPI document: 3.8.2
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
    factory(root.expect, root.TheBlueAllianceApiV3);
  }
}(this, function(expect, TheBlueAllianceApiV3) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TheBlueAllianceApiV3.WLTRecord();
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

  describe('WLTRecord', function() {
    it('should create an instance of WLTRecord', function() {
      // uncomment below and update the code to test WLTRecord
      //var instance = new TheBlueAllianceApiV3.WLTRecord();
      //expect(instance).to.be.a(TheBlueAllianceApiV3.WLTRecord);
    });

    it('should have the property losses (base name: "losses")', function() {
      // uncomment below and update the code to test the property losses
      //var instance = new TheBlueAllianceApiV3.WLTRecord();
      //expect(instance).to.be();
    });

    it('should have the property ties (base name: "ties")', function() {
      // uncomment below and update the code to test the property ties
      //var instance = new TheBlueAllianceApiV3.WLTRecord();
      //expect(instance).to.be();
    });

    it('should have the property wins (base name: "wins")', function() {
      // uncomment below and update the code to test the property wins
      //var instance = new TheBlueAllianceApiV3.WLTRecord();
      //expect(instance).to.be();
    });

  });

}));
