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
    instance = new FigshareApi.PrivateFile();
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

  describe('PrivateFile', function() {
    it('should create an instance of PrivateFile', function() {
      // uncomment below and update the code to test PrivateFile
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be.a(FigshareApi.PrivateFile);
    });

    it('should have the property isAttachedToPublicVersion (base name: "is_attached_to_public_version")', function() {
      // uncomment below and update the code to test the property isAttachedToPublicVersion
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property previewState (base name: "preview_state")', function() {
      // uncomment below and update the code to test the property previewState
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property uploadToken (base name: "upload_token")', function() {
      // uncomment below and update the code to test the property uploadToken
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property uploadUrl (base name: "upload_url")', function() {
      // uncomment below and update the code to test the property uploadUrl
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property viewerType (base name: "viewer_type")', function() {
      // uncomment below and update the code to test the property viewerType
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property computedMd5 (base name: "computed_md5")', function() {
      // uncomment below and update the code to test the property computedMd5
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property downloadUrl (base name: "download_url")', function() {
      // uncomment below and update the code to test the property downloadUrl
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property isLinkOnly (base name: "is_link_only")', function() {
      // uncomment below and update the code to test the property isLinkOnly
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property size (base name: "size")', function() {
      // uncomment below and update the code to test the property size
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

    it('should have the property suppliedMd5 (base name: "supplied_md5")', function() {
      // uncomment below and update the code to test the property suppliedMd5
      //var instance = new FigshareApi.PrivateFile();
      //expect(instance).to.be();
    });

  });

}));
