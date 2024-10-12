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
    instance = new VocaDbWeb.ReleaseEventSeriesContract();
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

  describe('ReleaseEventSeriesContract', function() {
    it('should create an instance of ReleaseEventSeriesContract', function() {
      // uncomment below and update the code to test ReleaseEventSeriesContract
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be.a(VocaDbWeb.ReleaseEventSeriesContract);
    });

    it('should have the property additionalNames (base name: "additionalNames")', function() {
      // uncomment below and update the code to test the property additionalNames
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be();
    });

    it('should have the property category (base name: "category")', function() {
      // uncomment below and update the code to test the property category
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be();
    });

    it('should have the property deleted (base name: "deleted")', function() {
      // uncomment below and update the code to test the property deleted
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be();
    });

    it('should have the property pictureMime (base name: "pictureMime")', function() {
      // uncomment below and update the code to test the property pictureMime
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be();
    });

    it('should have the property urlSlug (base name: "urlSlug")', function() {
      // uncomment below and update the code to test the property urlSlug
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be();
    });

    it('should have the property version (base name: "version")', function() {
      // uncomment below and update the code to test the property version
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be();
    });

    it('should have the property webLinks (base name: "webLinks")', function() {
      // uncomment below and update the code to test the property webLinks
      //var instance = new VocaDbWeb.ReleaseEventSeriesContract();
      //expect(instance).to.be();
    });

  });

}));
