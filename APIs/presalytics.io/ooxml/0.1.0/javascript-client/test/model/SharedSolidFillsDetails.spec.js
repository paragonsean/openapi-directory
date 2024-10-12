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
    instance = new OoxmlAutomation.SharedSolidFillsDetails();
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

  describe('SharedSolidFillsDetails', function() {
    it('should create an instance of SharedSolidFillsDetails', function() {
      // uncomment below and update the code to test SharedSolidFillsDetails
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be.a(OoxmlAutomation.SharedSolidFillsDetails);
    });

    it('should have the property colorTransformations (base name: "colorTransformations")', function() {
      // uncomment below and update the code to test the property colorTransformations
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property colorTypeId (base name: "colorTypeId")', function() {
      // uncomment below and update the code to test the property colorTypeId
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property dateCreated (base name: "dateCreated")', function() {
      // uncomment below and update the code to test the property dateCreated
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property dateModified (base name: "dateModified")', function() {
      // uncomment below and update the code to test the property dateModified
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property fillMapId (base name: "fillMapId")', function() {
      // uncomment below and update the code to test the property fillMapId
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property hexValue (base name: "hexValue")', function() {
      // uncomment below and update the code to test the property hexValue
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property isUserColor (base name: "isUserColor")', function() {
      // uncomment below and update the code to test the property isUserColor
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property parentFillMap (base name: "parentFillMap")', function() {
      // uncomment below and update the code to test the property parentFillMap
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property parentGradientStop (base name: "parentGradientStop")', function() {
      // uncomment below and update the code to test the property parentGradientStop
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property parentGradientStopId (base name: "parentGradientStopId")', function() {
      // uncomment below and update the code to test the property parentGradientStopId
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property parentLine (base name: "parentLine")', function() {
      // uncomment below and update the code to test the property parentLine
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property parentLineId (base name: "parentLineId")', function() {
      // uncomment below and update the code to test the property parentLineId
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property parentText (base name: "parentText")', function() {
      // uncomment below and update the code to test the property parentText
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property parentTextId (base name: "parentTextId")', function() {
      // uncomment below and update the code to test the property parentTextId
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property userCreated (base name: "userCreated")', function() {
      // uncomment below and update the code to test the property userCreated
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property userModified (base name: "userModified")', function() {
      // uncomment below and update the code to test the property userModified
      //var instance = new OoxmlAutomation.SharedSolidFillsDetails();
      //expect(instance).to.be();
    });

  });

}));
