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
    instance = new FlickrApiSchema.GroupThrottle();
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

  describe('GroupThrottle', function() {
    it('should create an instance of GroupThrottle', function() {
      // uncomment below and update the code to test GroupThrottle
      //var instance = new FlickrApiSchema.GroupThrottle();
      //expect(instance).to.be.a(FlickrApiSchema.GroupThrottle);
    });

    it('should have the property count (base name: "count")', function() {
      // uncomment below and update the code to test the property count
      //var instance = new FlickrApiSchema.GroupThrottle();
      //expect(instance).to.be();
    });

    it('should have the property mode (base name: "mode")', function() {
      // uncomment below and update the code to test the property mode
      //var instance = new FlickrApiSchema.GroupThrottle();
      //expect(instance).to.be();
    });

    it('should have the property remaining (base name: "remaining")', function() {
      // uncomment below and update the code to test the property remaining
      //var instance = new FlickrApiSchema.GroupThrottle();
      //expect(instance).to.be();
    });

  });

}));
