/**
 * shinobiapi
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
    factory(root.expect, root.Shinobiapi);
  }
}(this, function(expect, Shinobiapi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Shinobiapi.AlbumArt();
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

  describe('AlbumArt', function() {
    it('should create an instance of AlbumArt', function() {
      // uncomment below and update the code to test AlbumArt
      //var instance = new Shinobiapi.AlbumArt();
      //expect(instance).to.be.a(Shinobiapi.AlbumArt);
    });

    it('should have the property albumID (base name: "AlbumID")', function() {
      // uncomment below and update the code to test the property albumID
      //var instance = new Shinobiapi.AlbumArt();
      //expect(instance).to.be();
    });

    it('should have the property albumname (base name: "Albumname")', function() {
      // uncomment below and update the code to test the property albumname
      //var instance = new Shinobiapi.AlbumArt();
      //expect(instance).to.be();
    });

    it('should have the property art (base name: "Art")', function() {
      // uncomment below and update the code to test the property art
      //var instance = new Shinobiapi.AlbumArt();
      //expect(instance).to.be();
    });

  });

}));
