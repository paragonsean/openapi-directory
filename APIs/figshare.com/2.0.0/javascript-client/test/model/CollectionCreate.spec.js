/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
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
    factory(root.expect, root.FigshareApi);
  }
}(this, function(expect, FigshareApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FigshareApi.CollectionCreate();
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

  describe('CollectionCreate', function() {
    it('should create an instance of CollectionCreate', function() {
      // uncomment below and update the code to test CollectionCreate
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be.a(FigshareApi.CollectionCreate);
    });

    it('should have the property articles (base name: "articles")', function() {
      // uncomment below and update the code to test the property articles
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property authors (base name: "authors")', function() {
      // uncomment below and update the code to test the property authors
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property categories (base name: "categories")', function() {
      // uncomment below and update the code to test the property categories
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property categoriesBySourceId (base name: "categories_by_source_id")', function() {
      // uncomment below and update the code to test the property categoriesBySourceId
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property customFields (base name: "custom_fields")', function() {
      // uncomment below and update the code to test the property customFields
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property customFieldsList (base name: "custom_fields_list")', function() {
      // uncomment below and update the code to test the property customFieldsList
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property doi (base name: "doi")', function() {
      // uncomment below and update the code to test the property doi
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property funding (base name: "funding")', function() {
      // uncomment below and update the code to test the property funding
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property fundingList (base name: "funding_list")', function() {
      // uncomment below and update the code to test the property fundingList
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property groupId (base name: "group_id")', function() {
      // uncomment below and update the code to test the property groupId
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property handle (base name: "handle")', function() {
      // uncomment below and update the code to test the property handle
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property keywords (base name: "keywords")', function() {
      // uncomment below and update the code to test the property keywords
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property references (base name: "references")', function() {
      // uncomment below and update the code to test the property references
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property resourceDoi (base name: "resource_doi")', function() {
      // uncomment below and update the code to test the property resourceDoi
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property resourceId (base name: "resource_id")', function() {
      // uncomment below and update the code to test the property resourceId
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property resourceLink (base name: "resource_link")', function() {
      // uncomment below and update the code to test the property resourceLink
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property resourceTitle (base name: "resource_title")', function() {
      // uncomment below and update the code to test the property resourceTitle
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property resourceVersion (base name: "resource_version")', function() {
      // uncomment below and update the code to test the property resourceVersion
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property tags (base name: "tags")', function() {
      // uncomment below and update the code to test the property tags
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property timeline (base name: "timeline")', function() {
      // uncomment below and update the code to test the property timeline
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new FigshareApi.CollectionCreate();
      //expect(instance).to.be();
    });

  });

}));
