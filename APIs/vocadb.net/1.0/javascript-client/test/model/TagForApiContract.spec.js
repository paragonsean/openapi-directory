/**
 * VocaDbWeb
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
    factory(root.expect, root.VocaDbWeb);
  }
}(this, function(expect, VocaDbWeb) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new VocaDbWeb.TagForApiContract();
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

  describe('TagForApiContract', function() {
    it('should create an instance of TagForApiContract', function() {
      // uncomment below and update the code to test TagForApiContract
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be.a(VocaDbWeb.TagForApiContract);
    });

    it('should have the property additionalNames (base name: "additionalNames")', function() {
      // uncomment below and update the code to test the property additionalNames
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property aliasedTo (base name: "aliasedTo")', function() {
      // uncomment below and update the code to test the property aliasedTo
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property categoryName (base name: "categoryName")', function() {
      // uncomment below and update the code to test the property categoryName
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property createDate (base name: "createDate")', function() {
      // uncomment below and update the code to test the property createDate
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property defaultNameLanguage (base name: "defaultNameLanguage")', function() {
      // uncomment below and update the code to test the property defaultNameLanguage
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property mainPicture (base name: "mainPicture")', function() {
      // uncomment below and update the code to test the property mainPicture
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property names (base name: "names")', function() {
      // uncomment below and update the code to test the property names
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property parent (base name: "parent")', function() {
      // uncomment below and update the code to test the property parent
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property relatedTags (base name: "relatedTags")', function() {
      // uncomment below and update the code to test the property relatedTags
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property targets (base name: "targets")', function() {
      // uncomment below and update the code to test the property targets
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property translatedDescription (base name: "translatedDescription")', function() {
      // uncomment below and update the code to test the property translatedDescription
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property urlSlug (base name: "urlSlug")', function() {
      // uncomment below and update the code to test the property urlSlug
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property usageCount (base name: "usageCount")', function() {
      // uncomment below and update the code to test the property usageCount
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property version (base name: "version")', function() {
      // uncomment below and update the code to test the property version
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

    it('should have the property webLinks (base name: "webLinks")', function() {
      // uncomment below and update the code to test the property webLinks
      //var instance = new VocaDbWeb.TagForApiContract();
      //expect(instance).to.be();
    });

  });

}));
