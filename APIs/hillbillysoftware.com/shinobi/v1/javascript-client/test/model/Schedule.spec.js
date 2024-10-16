/**
 * shinobiapi
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
    factory(root.expect, root.Shinobiapi);
  }
}(this, function(expect, Shinobiapi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Shinobiapi.Schedule();
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

  describe('Schedule', function() {
    it('should create an instance of Schedule', function() {
      // uncomment below and update the code to test Schedule
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be.a(Shinobiapi.Schedule);
    });

    it('should have the property airDate (base name: "AirDate")', function() {
      // uncomment below and update the code to test the property airDate
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property airTime (base name: "AirTime")', function() {
      // uncomment below and update the code to test the property airTime
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property country (base name: "Country")', function() {
      // uncomment below and update the code to test the property country
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property daysOn (base name: "DaysOn")', function() {
      // uncomment below and update the code to test the property daysOn
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property episode (base name: "Episode")', function() {
      // uncomment below and update the code to test the property episode
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property ID (base name: "ID")', function() {
      // uncomment below and update the code to test the property ID
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property image (base name: "Image")', function() {
      // uncomment below and update the code to test the property image
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property network (base name: "Network")', function() {
      // uncomment below and update the code to test the property network
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property premiereDate (base name: "PremiereDate")', function() {
      // uncomment below and update the code to test the property premiereDate
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property runtime (base name: "Runtime")', function() {
      // uncomment below and update the code to test the property runtime
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property season (base name: "Season")', function() {
      // uncomment below and update the code to test the property season
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property showName (base name: "ShowName")', function() {
      // uncomment below and update the code to test the property showName
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property summary (base name: "Summary")', function() {
      // uncomment below and update the code to test the property summary
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "Title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new Shinobiapi.Schedule();
      //expect(instance).to.be();
    });

  });

}));
