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
    instance = new FlickrApiSchema.GetFavoritesByPersonID200Response();
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

  describe('GetFavoritesByPersonID200Response', function() {
    it('should create an instance of GetFavoritesByPersonID200Response', function() {
      // uncomment below and update the code to test GetFavoritesByPersonID200Response
      //var instance = new FlickrApiSchema.GetFavoritesByPersonID200Response();
      //expect(instance).to.be.a(FlickrApiSchema.GetFavoritesByPersonID200Response);
    });

    it('should have the property page (base name: "page")', function() {
      // uncomment below and update the code to test the property page
      //var instance = new FlickrApiSchema.GetFavoritesByPersonID200Response();
      //expect(instance).to.be();
    });

    it('should have the property pages (base name: "pages")', function() {
      // uncomment below and update the code to test the property pages
      //var instance = new FlickrApiSchema.GetFavoritesByPersonID200Response();
      //expect(instance).to.be();
    });

    it('should have the property perpage (base name: "perpage")', function() {
      // uncomment below and update the code to test the property perpage
      //var instance = new FlickrApiSchema.GetFavoritesByPersonID200Response();
      //expect(instance).to.be();
    });

    it('should have the property photos (base name: "photos")', function() {
      // uncomment below and update the code to test the property photos
      //var instance = new FlickrApiSchema.GetFavoritesByPersonID200Response();
      //expect(instance).to.be();
    });

    it('should have the property total (base name: "total")', function() {
      // uncomment below and update the code to test the property total
      //var instance = new FlickrApiSchema.GetFavoritesByPersonID200Response();
      //expect(instance).to.be();
    });

  });

}));
