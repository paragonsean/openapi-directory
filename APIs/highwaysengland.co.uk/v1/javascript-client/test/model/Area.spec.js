/**
 * Highways England API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.HighwaysEnglandApi);
  }
}(this, function(expect, HighwaysEnglandApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new HighwaysEnglandApi.Area();
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

  describe('Area', function() {
    it('should create an instance of Area', function() {
      // uncomment below and update the code to test Area
      //var instance = new HighwaysEnglandApi.Area();
      //expect(instance).to.be.a(HighwaysEnglandApi.Area);
    });

    it('should have the property description (base name: "Description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new HighwaysEnglandApi.Area();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "Id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new HighwaysEnglandApi.Area();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "Name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new HighwaysEnglandApi.Area();
      //expect(instance).to.be();
    });

    it('should have the property xLatitude (base name: "XLatitude")', function() {
      // uncomment below and update the code to test the property xLatitude
      //var instance = new HighwaysEnglandApi.Area();
      //expect(instance).to.be();
    });

    it('should have the property xLongitude (base name: "XLongitude")', function() {
      // uncomment below and update the code to test the property xLongitude
      //var instance = new HighwaysEnglandApi.Area();
      //expect(instance).to.be();
    });

    it('should have the property yLatitude (base name: "YLatitude")', function() {
      // uncomment below and update the code to test the property yLatitude
      //var instance = new HighwaysEnglandApi.Area();
      //expect(instance).to.be();
    });

    it('should have the property yLongitude (base name: "YLongitude")', function() {
      // uncomment below and update the code to test the property yLongitude
      //var instance = new HighwaysEnglandApi.Area();
      //expect(instance).to.be();
    });

  });

}));
