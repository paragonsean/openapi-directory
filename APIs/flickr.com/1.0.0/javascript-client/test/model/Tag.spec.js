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
    instance = new FlickrApiSchema.Tag();
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

  describe('Tag', function() {
    it('should create an instance of Tag', function() {
      // uncomment below and update the code to test Tag
      //var instance = new FlickrApiSchema.Tag();
      //expect(instance).to.be.a(FlickrApiSchema.Tag);
    });

    it('should have the property content (base name: "_content")', function() {
      // uncomment below and update the code to test the property content
      //var instance = new FlickrApiSchema.Tag();
      //expect(instance).to.be();
    });

    it('should have the property author (base name: "author")', function() {
      // uncomment below and update the code to test the property author
      //var instance = new FlickrApiSchema.Tag();
      //expect(instance).to.be();
    });

    it('should have the property authorname (base name: "authorname")', function() {
      // uncomment below and update the code to test the property authorname
      //var instance = new FlickrApiSchema.Tag();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new FlickrApiSchema.Tag();
      //expect(instance).to.be();
    });

    it('should have the property machineTag (base name: "machine_tag")', function() {
      // uncomment below and update the code to test the property machineTag
      //var instance = new FlickrApiSchema.Tag();
      //expect(instance).to.be();
    });

    it('should have the property raw (base name: "raw")', function() {
      // uncomment below and update the code to test the property raw
      //var instance = new FlickrApiSchema.Tag();
      //expect(instance).to.be();
    });

  });

}));
