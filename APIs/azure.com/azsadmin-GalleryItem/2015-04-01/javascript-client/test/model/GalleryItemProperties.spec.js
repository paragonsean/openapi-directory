/**
 * GalleryManagementClient
 * The Admin Gallery Management Client.
 *
 * The version of the OpenAPI document: 2015-04-01
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
    factory(root.expect, root.GalleryManagementClient);
  }
}(this, function(expect, GalleryManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new GalleryManagementClient.GalleryItemProperties();
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

  describe('GalleryItemProperties', function() {
    it('should create an instance of GalleryItemProperties', function() {
      // uncomment below and update the code to test GalleryItemProperties
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be.a(GalleryManagementClient.GalleryItemProperties);
    });

    it('should have the property additionalProperties (base name: "additionalProperties")', function() {
      // uncomment below and update the code to test the property additionalProperties
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property artifacts (base name: "artifacts")', function() {
      // uncomment below and update the code to test the property artifacts
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property categoryIds (base name: "categoryIds")', function() {
      // uncomment below and update the code to test the property categoryIds
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property changedTime (base name: "changedTime")', function() {
      // uncomment below and update the code to test the property changedTime
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property createdTime (base name: "createdTime")', function() {
      // uncomment below and update the code to test the property createdTime
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property definitionTemplates (base name: "definitionTemplates")', function() {
      // uncomment below and update the code to test the property definitionTemplates
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property filters (base name: "filters")', function() {
      // uncomment below and update the code to test the property filters
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property iconFileUris (base name: "iconFileUris")', function() {
      // uncomment below and update the code to test the property iconFileUris
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property identity (base name: "identity")', function() {
      // uncomment below and update the code to test the property identity
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property images (base name: "images")', function() {
      // uncomment below and update the code to test the property images
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property itemDisplayName (base name: "itemDisplayName")', function() {
      // uncomment below and update the code to test the property itemDisplayName
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property itemName (base name: "itemName")', function() {
      // uncomment below and update the code to test the property itemName
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property itemType (base name: "itemType")', function() {
      // uncomment below and update the code to test the property itemType
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property links (base name: "links")', function() {
      // uncomment below and update the code to test the property links
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property longSummary (base name: "longSummary")', function() {
      // uncomment below and update the code to test the property longSummary
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property marketingMaterial (base name: "marketingMaterial")', function() {
      // uncomment below and update the code to test the property marketingMaterial
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property metadata (base name: "metadata")', function() {
      // uncomment below and update the code to test the property metadata
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property products (base name: "products")', function() {
      // uncomment below and update the code to test the property products
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property properties (base name: "properties")', function() {
      // uncomment below and update the code to test the property properties
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property publisher (base name: "publisher")', function() {
      // uncomment below and update the code to test the property publisher
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property publisherDisplayName (base name: "publisherDisplayName")', function() {
      // uncomment below and update the code to test the property publisherDisplayName
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property resourceGroupName (base name: "resourceGroupName")', function() {
      // uncomment below and update the code to test the property resourceGroupName
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property screenshotUris (base name: "screenshotUris")', function() {
      // uncomment below and update the code to test the property screenshotUris
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property summary (base name: "summary")', function() {
      // uncomment below and update the code to test the property summary
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property uiDefinitionUri (base name: "uiDefinitionUri")', function() {
      // uncomment below and update the code to test the property uiDefinitionUri
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

    it('should have the property version (base name: "version")', function() {
      // uncomment below and update the code to test the property version
      //var instance = new GalleryManagementClient.GalleryItemProperties();
      //expect(instance).to.be();
    });

  });

}));
