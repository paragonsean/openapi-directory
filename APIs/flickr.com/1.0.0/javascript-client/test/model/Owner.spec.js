/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
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
    factory(root.expect, root.FlickrApiSchema);
  }
}(this, function(expect, FlickrApiSchema) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FlickrApiSchema.Owner();
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

  describe('Owner', function() {
    it('should create an instance of Owner', function() {
      // uncomment below and update the code to test Owner
      //var instance = new FlickrApiSchema.Owner();
      //expect(instance).to.be.a(FlickrApiSchema.Owner);
    });

    it('should have the property iconfarm (base name: "iconfarm")', function() {
      // uncomment below and update the code to test the property iconfarm
      //var instance = new FlickrApiSchema.Owner();
      //expect(instance).to.be();
    });

    it('should have the property iconserver (base name: "iconserver")', function() {
      // uncomment below and update the code to test the property iconserver
      //var instance = new FlickrApiSchema.Owner();
      //expect(instance).to.be();
    });

    it('should have the property isAdFree (base name: "is_ad_free")', function() {
      // uncomment below and update the code to test the property isAdFree
      //var instance = new FlickrApiSchema.Owner();
      //expect(instance).to.be();
    });

    it('should have the property ispro (base name: "ispro")', function() {
      // uncomment below and update the code to test the property ispro
      //var instance = new FlickrApiSchema.Owner();
      //expect(instance).to.be();
    });

    it('should have the property location (base name: "location")', function() {
      // uncomment below and update the code to test the property location
      //var instance = new FlickrApiSchema.Owner();
      //expect(instance).to.be();
    });

    it('should have the property noindexfollow (base name: "noindexfollow")', function() {
      // uncomment below and update the code to test the property noindexfollow
      //var instance = new FlickrApiSchema.Owner();
      //expect(instance).to.be();
    });

    it('should have the property nsid (base name: "nsid")', function() {
      // uncomment below and update the code to test the property nsid
      //var instance = new FlickrApiSchema.Owner();
      //expect(instance).to.be();
    });

    it('should have the property pathAlias (base name: "path_alias")', function() {
      // uncomment below and update the code to test the property pathAlias
      //var instance = new FlickrApiSchema.Owner();
      //expect(instance).to.be();
    });

    it('should have the property realname (base name: "realname")', function() {
      // uncomment below and update the code to test the property realname
      //var instance = new FlickrApiSchema.Owner();
      //expect(instance).to.be();
    });

    it('should have the property username (base name: "username")', function() {
      // uncomment below and update the code to test the property username
      //var instance = new FlickrApiSchema.Owner();
      //expect(instance).to.be();
    });

  });

}));
