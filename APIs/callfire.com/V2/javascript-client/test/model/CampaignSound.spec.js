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
    instance = new CallFireApiDocumentation.CampaignSound();
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

  describe('CampaignSound', function() {
    it('should create an instance of CampaignSound', function() {
      // uncomment below and update the code to test CampaignSound
      //var instance = new CallFireApiDocumentation.CampaignSound();
      //expect(instance).to.be.a(CallFireApiDocumentation.CampaignSound);
    });

    it('should have the property created (base name: "created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new CallFireApiDocumentation.CampaignSound();
      //expect(instance).to.be();
    });

    it('should have the property duplicate (base name: "duplicate")', function() {
      // uncomment below and update the code to test the property duplicate
      //var instance = new CallFireApiDocumentation.CampaignSound();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new CallFireApiDocumentation.CampaignSound();
      //expect(instance).to.be();
    });

    it('should have the property lengthInSeconds (base name: "lengthInSeconds")', function() {
      // uncomment below and update the code to test the property lengthInSeconds
      //var instance = new CallFireApiDocumentation.CampaignSound();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new CallFireApiDocumentation.CampaignSound();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new CallFireApiDocumentation.CampaignSound();
      //expect(instance).to.be();
    });

  });

}));
