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
    instance = new FlickrApiSchema.GetFavoritesContextByID200Response();
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

  describe('GetFavoritesContextByID200Response', function() {
    it('should create an instance of GetFavoritesContextByID200Response', function() {
      // uncomment below and update the code to test GetFavoritesContextByID200Response
      //var instance = new FlickrApiSchema.GetFavoritesContextByID200Response();
      //expect(instance).to.be.a(FlickrApiSchema.GetFavoritesContextByID200Response);
    });

    it('should have the property count (base name: "count")', function() {
      // uncomment below and update the code to test the property count
      //var instance = new FlickrApiSchema.GetFavoritesContextByID200Response();
      //expect(instance).to.be();
    });

    it('should have the property nextphoto (base name: "nextphoto")', function() {
      // uncomment below and update the code to test the property nextphoto
      //var instance = new FlickrApiSchema.GetFavoritesContextByID200Response();
      //expect(instance).to.be();
    });

    it('should have the property prevphoto (base name: "prevphoto")', function() {
      // uncomment below and update the code to test the property prevphoto
      //var instance = new FlickrApiSchema.GetFavoritesContextByID200Response();
      //expect(instance).to.be();
    });

    it('should have the property stat (base name: "stat")', function() {
      // uncomment below and update the code to test the property stat
      //var instance = new FlickrApiSchema.GetFavoritesContextByID200Response();
      //expect(instance).to.be();
    });

  });

}));
