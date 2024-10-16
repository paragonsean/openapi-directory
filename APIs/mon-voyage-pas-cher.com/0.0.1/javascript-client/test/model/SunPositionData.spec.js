/**
 * Mon-voyage-pas-cher.com Public API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.1
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
    factory(root.expect, root.MonVoyagePasCherComPublicApi);
  }
}(this, function(expect, MonVoyagePasCherComPublicApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MonVoyagePasCherComPublicApi.SunPositionData();
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

  describe('SunPositionData', function() {
    it('should create an instance of SunPositionData', function() {
      // uncomment below and update the code to test SunPositionData
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be.a(MonVoyagePasCherComPublicApi.SunPositionData);
    });

    it('should have the property dawn (base name: "dawn")', function() {
      // uncomment below and update the code to test the property dawn
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property dusk (base name: "dusk")', function() {
      // uncomment below and update the code to test the property dusk
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property goldenHour (base name: "goldenHour")', function() {
      // uncomment below and update the code to test the property goldenHour
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property goldenHourEnd (base name: "goldenHourEnd")', function() {
      // uncomment below and update the code to test the property goldenHourEnd
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property nadir (base name: "nadir")', function() {
      // uncomment below and update the code to test the property nadir
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property nauticalDawn (base name: "nauticalDawn")', function() {
      // uncomment below and update the code to test the property nauticalDawn
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property nauticalDusk (base name: "nauticalDusk")', function() {
      // uncomment below and update the code to test the property nauticalDusk
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property night (base name: "night")', function() {
      // uncomment below and update the code to test the property night
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property nightEnd (base name: "nightEnd")', function() {
      // uncomment below and update the code to test the property nightEnd
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property solarNoon (base name: "solarNoon")', function() {
      // uncomment below and update the code to test the property solarNoon
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property sunrise (base name: "sunrise")', function() {
      // uncomment below and update the code to test the property sunrise
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property sunriseEnd (base name: "sunriseEnd")', function() {
      // uncomment below and update the code to test the property sunriseEnd
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property sunset (base name: "sunset")', function() {
      // uncomment below and update the code to test the property sunset
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

    it('should have the property sunsetStart (base name: "sunsetStart")', function() {
      // uncomment below and update the code to test the property sunsetStart
      //var instance = new MonVoyagePasCherComPublicApi.SunPositionData();
      //expect(instance).to.be();
    });

  });

}));
