/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
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
    factory(root.expect, root.ManagedLabsClient);
  }
}(this, function(expect, ManagedLabsClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ManagedLabsClient.GalleryImagesApi();
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

  describe('GalleryImagesApi', function() {
    describe('galleryImagesCreateOrUpdate', function() {
      it('should call galleryImagesCreateOrUpdate successfully', function(done) {
        //uncomment below and update the code to test galleryImagesCreateOrUpdate
        //instance.galleryImagesCreateOrUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('galleryImagesDelete', function() {
      it('should call galleryImagesDelete successfully', function(done) {
        //uncomment below and update the code to test galleryImagesDelete
        //instance.galleryImagesDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('galleryImagesGet', function() {
      it('should call galleryImagesGet successfully', function(done) {
        //uncomment below and update the code to test galleryImagesGet
        //instance.galleryImagesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('galleryImagesList', function() {
      it('should call galleryImagesList successfully', function(done) {
        //uncomment below and update the code to test galleryImagesList
        //instance.galleryImagesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('galleryImagesUpdate', function() {
      it('should call galleryImagesUpdate successfully', function(done) {
        //uncomment below and update the code to test galleryImagesUpdate
        //instance.galleryImagesUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
