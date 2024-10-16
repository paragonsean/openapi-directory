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
    instance = new AppCenterClient.ReleaseUpdateError();
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

  describe('ReleaseUpdateError', function() {
    it('should create an instance of ReleaseUpdateError', function() {
      // uncomment below and update the code to test ReleaseUpdateError
      //var instance = new AppCenterClient.ReleaseUpdateError();
      //expect(instance).to.be.a(AppCenterClient.ReleaseUpdateError);
    });

    it('should have the property code (base name: "code")', function() {
      // uncomment below and update the code to test the property code
      //var instance = new AppCenterClient.ReleaseUpdateError();
      //expect(instance).to.be();
    });

    it('should have the property message (base name: "message")', function() {
      // uncomment below and update the code to test the property message
      //var instance = new AppCenterClient.ReleaseUpdateError();
      //expect(instance).to.be();
    });

    it('should have the property destinations (base name: "destinations")', function() {
      // uncomment below and update the code to test the property destinations
      //var instance = new AppCenterClient.ReleaseUpdateError();
      //expect(instance).to.be();
    });

    it('should have the property mandatoryUpdate (base name: "mandatory_update")', function() {
      // uncomment below and update the code to test the property mandatoryUpdate
      //var instance = new AppCenterClient.ReleaseUpdateError();
      //expect(instance).to.be();
    });

    it('should have the property releaseNotes (base name: "release_notes")', function() {
      // uncomment below and update the code to test the property releaseNotes
      //var instance = new AppCenterClient.ReleaseUpdateError();
      //expect(instance).to.be();
    });

  });

}));
