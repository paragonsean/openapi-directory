/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
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
    factory(root.expect, root.CallFireApiDocumentation);
  }
}(this, function(expect, CallFireApiDocumentation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CallFireApiDocumentation.Call();
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

  describe('Call', function() {
    it('should create an instance of Call', function() {
      // uncomment below and update the code to test Call
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be.a(CallFireApiDocumentation.Call);
    });

    it('should have the property agentCall (base name: "agentCall")', function() {
      // uncomment below and update the code to test the property agentCall
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property attributes (base name: "attributes")', function() {
      // uncomment below and update the code to test the property attributes
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property batchId (base name: "batchId")', function() {
      // uncomment below and update the code to test the property batchId
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property campaignId (base name: "campaignId")', function() {
      // uncomment below and update the code to test the property campaignId
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property contact (base name: "contact")', function() {
      // uncomment below and update the code to test the property contact
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property created (base name: "created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property finalCallResult (base name: "finalCallResult")', function() {
      // uncomment below and update the code to test the property finalCallResult
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property fromNumber (base name: "fromNumber")', function() {
      // uncomment below and update the code to test the property fromNumber
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property inbound (base name: "inbound")', function() {
      // uncomment below and update the code to test the property inbound
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property labels (base name: "labels")', function() {
      // uncomment below and update the code to test the property labels
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property modified (base name: "modified")', function() {
      // uncomment below and update the code to test the property modified
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property notes (base name: "notes")', function() {
      // uncomment below and update the code to test the property notes
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property records (base name: "records")', function() {
      // uncomment below and update the code to test the property records
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property state (base name: "state")', function() {
      // uncomment below and update the code to test the property state
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

    it('should have the property toNumber (base name: "toNumber")', function() {
      // uncomment below and update the code to test the property toNumber
      //var instance = new CallFireApiDocumentation.Call();
      //expect(instance).to.be();
    });

  });

}));
