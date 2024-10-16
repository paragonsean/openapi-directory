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
    instance = new RadioMusicServices.MusicExportError();
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

  describe('MusicExportError', function() {
    it('should create an instance of MusicExportError', function() {
      // uncomment below and update the code to test MusicExportError
      //var instance = new RadioMusicServices.MusicExportError();
      //expect(instance).to.be.a(RadioMusicServices.MusicExportError);
    });

    it('should have the property message (base name: "message")', function() {
      // uncomment below and update the code to test the property message
      //var instance = new RadioMusicServices.MusicExportError();
      //expect(instance).to.be();
    });

    it('should have the property repliedAt (base name: "replied_at")', function() {
      // uncomment below and update the code to test the property repliedAt
      //var instance = new RadioMusicServices.MusicExportError();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new RadioMusicServices.MusicExportError();
      //expect(instance).to.be();
    });

  });

}));
