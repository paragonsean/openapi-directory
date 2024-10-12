/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.2
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
    factory(root.expect, root.TrainingApi);
  }
}(this, function(expect, TrainingApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TrainingApi.ImageApiApi();
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

  describe('ImageApiApi', function() {
    describe('createImagesFromData', function() {
      it('should call createImagesFromData successfully', function(done) {
        //uncomment below and update the code to test createImagesFromData
        //instance.createImagesFromData(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createImagesFromFiles', function() {
      it('should call createImagesFromFiles successfully', function(done) {
        //uncomment below and update the code to test createImagesFromFiles
        //instance.createImagesFromFiles(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createImagesFromPredictions', function() {
      it('should call createImagesFromPredictions successfully', function(done) {
        //uncomment below and update the code to test createImagesFromPredictions
        //instance.createImagesFromPredictions(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createImagesFromUrls', function() {
      it('should call createImagesFromUrls successfully', function(done) {
        //uncomment below and update the code to test createImagesFromUrls
        //instance.createImagesFromUrls(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteImageTags', function() {
      it('should call deleteImageTags successfully', function(done) {
        //uncomment below and update the code to test deleteImageTags
        //instance.deleteImageTags(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('deleteImages', function() {
      it('should call deleteImages successfully', function(done) {
        //uncomment below and update the code to test deleteImages
        //instance.deleteImages(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getTaggedImages', function() {
      it('should call getTaggedImages successfully', function(done) {
        //uncomment below and update the code to test getTaggedImages
        //instance.getTaggedImages(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getUntaggedImages', function() {
      it('should call getUntaggedImages successfully', function(done) {
        //uncomment below and update the code to test getUntaggedImages
        //instance.getUntaggedImages(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('postImageTags', function() {
      it('should call postImageTags successfully', function(done) {
        //uncomment below and update the code to test postImageTags
        //instance.postImageTags(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
