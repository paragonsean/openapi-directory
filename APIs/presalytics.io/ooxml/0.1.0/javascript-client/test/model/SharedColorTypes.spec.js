/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
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
    factory(root.expect, root.OoxmlAutomation);
  }
}(this, function(expect, OoxmlAutomation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OoxmlAutomation.SharedColorTypes();
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

  describe('SharedColorTypes', function() {
    it('should create an instance of SharedColorTypes', function() {
      // uncomment below and update the code to test SharedColorTypes
      //var instance = new OoxmlAutomation.SharedColorTypes();
      //expect(instance).to.be.a(OoxmlAutomation.SharedColorTypes);
    });

    it('should have the property colorSchemeIndexValueEnum (base name: "colorSchemeIndexValueEnum")', function() {
      // uncomment below and update the code to test the property colorSchemeIndexValueEnum
      //var instance = new OoxmlAutomation.SharedColorTypes();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new OoxmlAutomation.SharedColorTypes();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new OoxmlAutomation.SharedColorTypes();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new OoxmlAutomation.SharedColorTypes();
      //expect(instance).to.be();
    });

    it('should have the property typeId (base name: "typeId")', function() {
      // uncomment below and update the code to test the property typeId
      //var instance = new OoxmlAutomation.SharedColorTypes();
      //expect(instance).to.be();
    });

  });

}));
