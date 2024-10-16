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
    instance = new AppCenterClient.StoresReleaseDetails();
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

  describe('StoresReleaseDetails', function() {
    it('should create an instance of StoresReleaseDetails', function() {
      // uncomment below and update the code to test StoresReleaseDetails
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be.a(AppCenterClient.StoresReleaseDetails);
    });

    it('should have the property androidMinApiLevel (base name: "android_min_api_level")', function() {
      // uncomment below and update the code to test the property androidMinApiLevel
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property appDisplayName (base name: "app_display_name")', function() {
      // uncomment below and update the code to test the property appDisplayName
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property appName (base name: "app_name")', function() {
      // uncomment below and update the code to test the property appName
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property bundleIdentifier (base name: "bundle_identifier")', function() {
      // uncomment below and update the code to test the property bundleIdentifier
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property distributionStores (base name: "distribution_stores")', function() {
      // uncomment below and update the code to test the property distributionStores
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property downloadUrl (base name: "download_url")', function() {
      // uncomment below and update the code to test the property downloadUrl
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property fingerprint (base name: "fingerprint")', function() {
      // uncomment below and update the code to test the property fingerprint
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property installUrl (base name: "install_url")', function() {
      // uncomment below and update the code to test the property installUrl
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property minOs (base name: "min_os")', function() {
      // uncomment below and update the code to test the property minOs
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property releaseNotes (base name: "release_notes")', function() {
      // uncomment below and update the code to test the property releaseNotes
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property shortVersion (base name: "short_version")', function() {
      // uncomment below and update the code to test the property shortVersion
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property size (base name: "size")', function() {
      // uncomment below and update the code to test the property size
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property uploadedAt (base name: "uploaded_at")', function() {
      // uncomment below and update the code to test the property uploadedAt
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

    it('should have the property version (base name: "version")', function() {
      // uncomment below and update the code to test the property version
      //var instance = new AppCenterClient.StoresReleaseDetails();
      //expect(instance).to.be();
    });

  });

}));
