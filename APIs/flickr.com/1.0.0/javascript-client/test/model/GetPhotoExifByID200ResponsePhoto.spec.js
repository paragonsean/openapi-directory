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
    instance = new FlickrApiSchema.GetPhotoExifByID200ResponsePhoto();
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

  describe('GetPhotoExifByID200ResponsePhoto', function() {
    it('should create an instance of GetPhotoExifByID200ResponsePhoto', function() {
      // uncomment below and update the code to test GetPhotoExifByID200ResponsePhoto
      //var instance = new FlickrApiSchema.GetPhotoExifByID200ResponsePhoto();
      //expect(instance).to.be.a(FlickrApiSchema.GetPhotoExifByID200ResponsePhoto);
    });

    it('should have the property camera (base name: "camera")', function() {
      // uncomment below and update the code to test the property camera
      //var instance = new FlickrApiSchema.GetPhotoExifByID200ResponsePhoto();
      //expect(instance).to.be();
    });

    it('should have the property exif (base name: "exif")', function() {
      // uncomment below and update the code to test the property exif
      //var instance = new FlickrApiSchema.GetPhotoExifByID200ResponsePhoto();
      //expect(instance).to.be();
    });

    it('should have the property farm (base name: "farm")', function() {
      // uncomment below and update the code to test the property farm
      //var instance = new FlickrApiSchema.GetPhotoExifByID200ResponsePhoto();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new FlickrApiSchema.GetPhotoExifByID200ResponsePhoto();
      //expect(instance).to.be();
    });

    it('should have the property secret (base name: "secret")', function() {
      // uncomment below and update the code to test the property secret
      //var instance = new FlickrApiSchema.GetPhotoExifByID200ResponsePhoto();
      //expect(instance).to.be();
    });

    it('should have the property server (base name: "server")', function() {
      // uncomment below and update the code to test the property server
      //var instance = new FlickrApiSchema.GetPhotoExifByID200ResponsePhoto();
      //expect(instance).to.be();
    });

  });

}));
