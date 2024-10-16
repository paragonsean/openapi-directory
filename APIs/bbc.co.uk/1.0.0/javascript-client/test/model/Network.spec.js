/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.RadioMusicServices);
  }
}(this, function(expect, RadioMusicServices) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new RadioMusicServices.Network();
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

  describe('Network', function() {
    it('should create an instance of Network', function() {
      // uncomment below and update the code to test Network
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be.a(RadioMusicServices.Network);
    });

    it('should have the property active (base name: "active")', function() {
      // uncomment below and update the code to test the property active
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property contacts (base name: "contacts")', function() {
      // uncomment below and update the code to test the property contacts
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property dateRanges (base name: "date_ranges")', function() {
      // uncomment below and update the code to test the property dateRanges
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property group (base name: "group")', function() {
      // uncomment below and update the code to test the property group
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property international (base name: "international")', function() {
      // uncomment below and update the code to test the property international
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property key (base name: "key")', function() {
      // uncomment below and update the code to test the property key
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property preset (base name: "preset")', function() {
      // uncomment below and update the code to test the property preset
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property promotedCategorySummaries (base name: "promoted_category_summaries")', function() {
      // uncomment below and update the code to test the property promotedCategorySummaries
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property services (base name: "services")', function() {
      // uncomment below and update the code to test the property services
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property shortTitle (base name: "short_title")', function() {
      // uncomment below and update the code to test the property shortTitle
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property sort (base name: "sort")', function() {
      // uncomment below and update the code to test the property sort
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new RadioMusicServices.Network();
      //expect(instance).to.be();
    });

  });

}));
