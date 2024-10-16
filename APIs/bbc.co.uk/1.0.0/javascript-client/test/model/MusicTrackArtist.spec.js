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
    instance = new RadioMusicServices.MusicTrackArtist();
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

  describe('MusicTrackArtist', function() {
    it('should create an instance of MusicTrackArtist', function() {
      // uncomment below and update the code to test MusicTrackArtist
      //var instance = new RadioMusicServices.MusicTrackArtist();
      //expect(instance).to.be.a(RadioMusicServices.MusicTrackArtist);
    });

    it('should have the property gid (base name: "gid")', function() {
      // uncomment below and update the code to test the property gid
      //var instance = new RadioMusicServices.MusicTrackArtist();
      //expect(instance).to.be();
    });

    it('should have the property imagePid (base name: "imagePid")', function() {
      // uncomment below and update the code to test the property imagePid
      //var instance = new RadioMusicServices.MusicTrackArtist();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new RadioMusicServices.MusicTrackArtist();
      //expect(instance).to.be();
    });

    it('should have the property role (base name: "role")', function() {
      // uncomment below and update the code to test the property role
      //var instance = new RadioMusicServices.MusicTrackArtist();
      //expect(instance).to.be();
    });

    it('should have the property sortName (base name: "sortName")', function() {
      // uncomment below and update the code to test the property sortName
      //var instance = new RadioMusicServices.MusicTrackArtist();
      //expect(instance).to.be();
    });

  });

}));
