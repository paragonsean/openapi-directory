/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
    factory(root.expect, root.AppCenterClient);
  }
}(this, function(expect, AppCenterClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AppCenterClient.Language();
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

  describe('Language', function() {
    it('should create an instance of Language', function() {
      // uncomment below and update the code to test Language
      //var instance = new AppCenterClient.Language();
      //expect(instance).to.be.a(AppCenterClient.Language);
    });

    it('should have the property count (base name: "count")', function() {
      // uncomment below and update the code to test the property count
      //var instance = new AppCenterClient.Language();
      //expect(instance).to.be();
    });

    it('should have the property languageName (base name: "language_name")', function() {
      // uncomment below and update the code to test the property languageName
      //var instance = new AppCenterClient.Language();
      //expect(instance).to.be();
    });

    it('should have the property previousCount (base name: "previous_count")', function() {
      // uncomment below and update the code to test the property previousCount
      //var instance = new AppCenterClient.Language();
      //expect(instance).to.be();
    });

  });

}));
