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
    instance = new OoxmlAutomation.ThemeBackgroundFillsDetails();
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

  describe('ThemeBackgroundFillsDetails', function() {
    it('should create an instance of ThemeBackgroundFillsDetails', function() {
      // uncomment below and update the code to test ThemeBackgroundFillsDetails
      //var instance = new OoxmlAutomation.ThemeBackgroundFillsDetails();
      //expect(instance).to.be.a(OoxmlAutomation.ThemeBackgroundFillsDetails);
    });

    it('should have the property dateCreated (base name: "dateCreated")', function() {
      // uncomment below and update the code to test the property dateCreated
      //var instance = new OoxmlAutomation.ThemeBackgroundFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property dateModified (base name: "dateModified")', function() {
      // uncomment below and update the code to test the property dateModified
      //var instance = new OoxmlAutomation.ThemeBackgroundFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property fillMap (base name: "fillMap")', function() {
      // uncomment below and update the code to test the property fillMap
      //var instance = new OoxmlAutomation.ThemeBackgroundFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new OoxmlAutomation.ThemeBackgroundFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property intensityId (base name: "intensityId")', function() {
      // uncomment below and update the code to test the property intensityId
      //var instance = new OoxmlAutomation.ThemeBackgroundFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property theme (base name: "theme")', function() {
      // uncomment below and update the code to test the property theme
      //var instance = new OoxmlAutomation.ThemeBackgroundFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property themeId (base name: "themeId")', function() {
      // uncomment below and update the code to test the property themeId
      //var instance = new OoxmlAutomation.ThemeBackgroundFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property userCreated (base name: "userCreated")', function() {
      // uncomment below and update the code to test the property userCreated
      //var instance = new OoxmlAutomation.ThemeBackgroundFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property userModified (base name: "userModified")', function() {
      // uncomment below and update the code to test the property userModified
      //var instance = new OoxmlAutomation.ThemeBackgroundFillsDetails();
      //expect(instance).to.be();
    });

  });

}));
