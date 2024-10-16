/**
 * Personnel Data
 * API for reading and writing personnel data incl. data about attendances and absences
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
    factory(root.expect, root.PersonnelData);
  }
}(this, function(expect, PersonnelData) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PersonnelData.CompanyTimeOffsPost201Response();
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

  describe('CompanyTimeOffsPost201Response', function() {
    it('should create an instance of CompanyTimeOffsPost201Response', function() {
      // uncomment below and update the code to test CompanyTimeOffsPost201Response
      //var instance = new PersonnelData.CompanyTimeOffsPost201Response();
      //expect(instance).to.be.a(PersonnelData.CompanyTimeOffsPost201Response);
    });

    it('should have the property data (base name: "data")', function() {
      // uncomment below and update the code to test the property data
      //var instance = new PersonnelData.CompanyTimeOffsPost201Response();
      //expect(instance).to.be();
    });

  });

}));
