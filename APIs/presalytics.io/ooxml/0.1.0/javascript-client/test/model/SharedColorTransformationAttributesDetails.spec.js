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
    instance = new OoxmlAutomation.SharedColorTransformationAttributesDetails();
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

  describe('SharedColorTransformationAttributesDetails', function() {
    it('should create an instance of SharedColorTransformationAttributesDetails', function() {
      // uncomment below and update the code to test SharedColorTransformationAttributesDetails
      //var instance = new OoxmlAutomation.SharedColorTransformationAttributesDetails();
      //expect(instance).to.be.a(OoxmlAutomation.SharedColorTransformationAttributesDetails);
    });

    it('should have the property colorTransformation (base name: "colorTransformation")', function() {
      // uncomment below and update the code to test the property colorTransformation
      //var instance = new OoxmlAutomation.SharedColorTransformationAttributesDetails();
      //expect(instance).to.be();
    });

    it('should have the property colorTransformationsId (base name: "colorTransformationsId")', function() {
      // uncomment below and update the code to test the property colorTransformationsId
      //var instance = new OoxmlAutomation.SharedColorTransformationAttributesDetails();
      //expect(instance).to.be();
    });

    it('should have the property dateCreated (base name: "dateCreated")', function() {
      // uncomment below and update the code to test the property dateCreated
      //var instance = new OoxmlAutomation.SharedColorTransformationAttributesDetails();
      //expect(instance).to.be();
    });

    it('should have the property dateModified (base name: "dateModified")', function() {
      // uncomment below and update the code to test the property dateModified
      //var instance = new OoxmlAutomation.SharedColorTransformationAttributesDetails();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new OoxmlAutomation.SharedColorTransformationAttributesDetails();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new OoxmlAutomation.SharedColorTransformationAttributesDetails();
      //expect(instance).to.be();
    });

    it('should have the property userCreated (base name: "userCreated")', function() {
      // uncomment below and update the code to test the property userCreated
      //var instance = new OoxmlAutomation.SharedColorTransformationAttributesDetails();
      //expect(instance).to.be();
    });

    it('should have the property userModified (base name: "userModified")', function() {
      // uncomment below and update the code to test the property userModified
      //var instance = new OoxmlAutomation.SharedColorTransformationAttributesDetails();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new OoxmlAutomation.SharedColorTransformationAttributesDetails();
      //expect(instance).to.be();
    });

  });

}));
