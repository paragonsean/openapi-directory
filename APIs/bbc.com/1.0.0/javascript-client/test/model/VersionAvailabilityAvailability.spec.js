/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
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
    factory(root.expect, root.BbcNitroApi);
  }
}(this, function(expect, BbcNitroApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new BbcNitroApi.VersionAvailabilityAvailability();
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

  describe('VersionAvailabilityAvailability', function() {
    it('should create an instance of VersionAvailabilityAvailability', function() {
      // uncomment below and update the code to test VersionAvailabilityAvailability
      //var instance = new BbcNitroApi.VersionAvailabilityAvailability();
      //expect(instance).to.be.a(BbcNitroApi.VersionAvailabilityAvailability);
    });

    it('should have the property availability (base name: "availability")', function() {
      // uncomment below and update the code to test the property availability
      //var instance = new BbcNitroApi.VersionAvailabilityAvailability();
      //expect(instance).to.be();
    });

    it('should have the property availabilityEnd (base name: "availability_end")', function() {
      // uncomment below and update the code to test the property availabilityEnd
      //var instance = new BbcNitroApi.VersionAvailabilityAvailability();
      //expect(instance).to.be();
    });

    it('should have the property availabilityStart (base name: "availability_start")', function() {
      // uncomment below and update the code to test the property availabilityStart
      //var instance = new BbcNitroApi.VersionAvailabilityAvailability();
      //expect(instance).to.be();
    });

    it('should have the property availableMediaSets (base name: "available_media_sets")', function() {
      // uncomment below and update the code to test the property availableMediaSets
      //var instance = new BbcNitroApi.VersionAvailabilityAvailability();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new BbcNitroApi.VersionAvailabilityAvailability();
      //expect(instance).to.be();
    });

  });

}));
