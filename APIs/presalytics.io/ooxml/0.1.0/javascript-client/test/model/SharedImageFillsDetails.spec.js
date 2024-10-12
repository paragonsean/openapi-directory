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
    instance = new OoxmlAutomation.SharedImageFillsDetails();
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

  describe('SharedImageFillsDetails', function() {
    it('should create an instance of SharedImageFillsDetails', function() {
      // uncomment below and update the code to test SharedImageFillsDetails
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be.a(OoxmlAutomation.SharedImageFillsDetails);
    });

    it('should have the property compressionState (base name: "compressionState")', function() {
      // uncomment below and update the code to test the property compressionState
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property dateCreated (base name: "dateCreated")', function() {
      // uncomment below and update the code to test the property dateCreated
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property dateModified (base name: "dateModified")', function() {
      // uncomment below and update the code to test the property dateModified
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property dpi (base name: "dpi")', function() {
      // uncomment below and update the code to test the property dpi
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property effectsJson (base name: "effectsJson")', function() {
      // uncomment below and update the code to test the property effectsJson
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property fillMap (base name: "fillMap")', function() {
      // uncomment below and update the code to test the property fillMap
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property fillMapId (base name: "fillMapId")', function() {
      // uncomment below and update the code to test the property fillMapId
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property picture (base name: "picture")', function() {
      // uncomment below and update the code to test the property picture
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property rotateWithShape (base name: "rotateWithShape")', function() {
      // uncomment below and update the code to test the property rotateWithShape
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property sourceRectangle (base name: "sourceRectangle")', function() {
      // uncomment below and update the code to test the property sourceRectangle
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property stretch (base name: "stretch")', function() {
      // uncomment below and update the code to test the property stretch
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property tile (base name: "tile")', function() {
      // uncomment below and update the code to test the property tile
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property userCreated (base name: "userCreated")', function() {
      // uncomment below and update the code to test the property userCreated
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

    it('should have the property userModified (base name: "userModified")', function() {
      // uncomment below and update the code to test the property userModified
      //var instance = new OoxmlAutomation.SharedImageFillsDetails();
      //expect(instance).to.be();
    });

  });

}));
