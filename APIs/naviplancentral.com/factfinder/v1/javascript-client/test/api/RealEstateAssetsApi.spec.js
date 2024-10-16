/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.AdvicentFactFinderService);
  }
}(this, function(expect, AdvicentFactFinderService) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AdvicentFactFinderService.RealEstateAssetsApi();
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

  describe('RealEstateAssetsApi', function() {
    describe('realEstateAssetsDeleteById', function() {
      it('should call realEstateAssetsDeleteById successfully', function(done) {
        //uncomment below and update the code to test realEstateAssetsDeleteById
        //instance.realEstateAssetsDeleteById(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realEstateAssetsGetById', function() {
      it('should call realEstateAssetsGetById successfully', function(done) {
        //uncomment below and update the code to test realEstateAssetsGetById
        //instance.realEstateAssetsGetById(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid', function() {
      it('should call realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid successfully', function(done) {
        //uncomment below and update the code to test realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid
        //instance.realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realEstateAssetsPostByModel', function() {
      it('should call realEstateAssetsPostByModel successfully', function(done) {
        //uncomment below and update the code to test realEstateAssetsPostByModel
        //instance.realEstateAssetsPostByModel(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('realEstateAssetsPutByIdModel', function() {
      it('should call realEstateAssetsPutByIdModel successfully', function(done) {
        //uncomment below and update the code to test realEstateAssetsPutByIdModel
        //instance.realEstateAssetsPutByIdModel(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
