/**
 * NASCAR v2
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.NascarV2);
  }
}(this, function(expect, NascarV2) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NascarV2.Driver();
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

  describe('Driver', function() {
    it('should create an instance of Driver', function() {
      // uncomment below and update the code to test Driver
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be.a(NascarV2.Driver);
    });

    it('should have the property birthDate (base name: "BirthDate")', function() {
      // uncomment below and update the code to test the property birthDate
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property birthPlace (base name: "BirthPlace")', function() {
      // uncomment below and update the code to test the property birthPlace
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property chassis (base name: "Chassis")', function() {
      // uncomment below and update the code to test the property chassis
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property created (base name: "Created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property crewChief (base name: "CrewChief")', function() {
      // uncomment below and update the code to test the property crewChief
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property driverID (base name: "DriverID")', function() {
      // uncomment below and update the code to test the property driverID
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property engine (base name: "Engine")', function() {
      // uncomment below and update the code to test the property engine
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "FirstName")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property gender (base name: "Gender")', function() {
      // uncomment below and update the code to test the property gender
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property height (base name: "Height")', function() {
      // uncomment below and update the code to test the property height
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "LastName")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property manufacturer (base name: "Manufacturer")', function() {
      // uncomment below and update the code to test the property manufacturer
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property number (base name: "Number")', function() {
      // uncomment below and update the code to test the property number
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property numberDisplay (base name: "NumberDisplay")', function() {
      // uncomment below and update the code to test the property numberDisplay
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property photoUrl (base name: "PhotoUrl")', function() {
      // uncomment below and update the code to test the property photoUrl
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property sponsors (base name: "Sponsors")', function() {
      // uncomment below and update the code to test the property sponsors
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "Team")', function() {
      // uncomment below and update the code to test the property team
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property updated (base name: "Updated")', function() {
      // uncomment below and update the code to test the property updated
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

    it('should have the property weight (base name: "Weight")', function() {
      // uncomment below and update the code to test the property weight
      //var instance = new NascarV2.Driver();
      //expect(instance).to.be();
    });

  });

}));
