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
    instance = new OoxmlAutomation.SlideConnectorDetails();
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

  describe('SlideConnectorDetails', function() {
    it('should create an instance of SlideConnectorDetails', function() {
      // uncomment below and update the code to test SlideConnectorDetails
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be.a(OoxmlAutomation.SlideConnectorDetails);
    });

    it('should have the property baseElementBlobUrl (base name: "baseElementBlobUrl")', function() {
      // uncomment below and update the code to test the property baseElementBlobUrl
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property changedBaseElementBlobUrl (base name: "changedBaseElementBlobUrl")', function() {
      // uncomment below and update the code to test the property changedBaseElementBlobUrl
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property dateCreated (base name: "dateCreated")', function() {
      // uncomment below and update the code to test the property dateCreated
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property dateModified (base name: "dateModified")', function() {
      // uncomment below and update the code to test the property dateModified
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property effect (base name: "effect")', function() {
      // uncomment below and update the code to test the property effect
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property endConnectionIdx (base name: "endConnectionIdx")', function() {
      // uncomment below and update the code to test the property endConnectionIdx
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property endConnectionShape (base name: "endConnectionShape")', function() {
      // uncomment below and update the code to test the property endConnectionShape
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property endConnectionShapeId (base name: "endConnectionShapeId")', function() {
      // uncomment below and update the code to test the property endConnectionShapeId
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property fillMap (base name: "fillMap")', function() {
      // uncomment below and update the code to test the property fillMap
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property flipHorizontal (base name: "flipHorizontal")', function() {
      // uncomment below and update the code to test the property flipHorizontal
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property flipVertical (base name: "flipVertical")', function() {
      // uncomment below and update the code to test the property flipVertical
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property freeFormPathXml (base name: "freeFormPathXml")', function() {
      // uncomment below and update the code to test the property freeFormPathXml
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property groupElement (base name: "groupElement")', function() {
      // uncomment below and update the code to test the property groupElement
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property groupElementsId (base name: "groupElementsId")', function() {
      // uncomment below and update the code to test the property groupElementsId
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property hidden (base name: "hidden")', function() {
      // uncomment below and update the code to test the property hidden
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property isThemeEffect (base name: "isThemeEffect")', function() {
      // uncomment below and update the code to test the property isThemeEffect
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property isThemeFill (base name: "isThemeFill")', function() {
      // uncomment below and update the code to test the property isThemeFill
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property isThemeLine (base name: "isThemeLine")', function() {
      // uncomment below and update the code to test the property isThemeLine
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property line (base name: "line")', function() {
      // uncomment below and update the code to test the property line
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property ooxmlId (base name: "ooxmlId")', function() {
      // uncomment below and update the code to test the property ooxmlId
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property packageUri (base name: "packageUri")', function() {
      // uncomment below and update the code to test the property packageUri
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property presetTypeId (base name: "presetTypeId")', function() {
      // uncomment below and update the code to test the property presetTypeId
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property rotation (base name: "rotation")', function() {
      // uncomment below and update the code to test the property rotation
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property startConnectionIdx (base name: "startConnectionIdx")', function() {
      // uncomment below and update the code to test the property startConnectionIdx
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property startConnectionShape (base name: "startConnectionShape")', function() {
      // uncomment below and update the code to test the property startConnectionShape
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property startConnectionShapeId (base name: "startConnectionShapeId")', function() {
      // uncomment below and update the code to test the property startConnectionShapeId
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property svgBlobUrl (base name: "svgBlobUrl")', function() {
      // uncomment below and update the code to test the property svgBlobUrl
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property userCreated (base name: "userCreated")', function() {
      // uncomment below and update the code to test the property userCreated
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

    it('should have the property userModified (base name: "userModified")', function() {
      // uncomment below and update the code to test the property userModified
      //var instance = new OoxmlAutomation.SlideConnectorDetails();
      //expect(instance).to.be();
    });

  });

}));
