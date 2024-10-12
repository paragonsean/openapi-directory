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
    instance = new FigshareApi.OtherApi();
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

  describe('OtherApi', function() {
    describe('categoriesList', function() {
      it('should call categoriesList successfully', function(done) {
        //uncomment below and update the code to test categoriesList
        //instance.categoriesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('fileDownload', function() {
      it('should call fileDownload successfully', function(done) {
        //uncomment below and update the code to test fileDownload
        //instance.fileDownload(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('itemTypesList', function() {
      it('should call itemTypesList successfully', function(done) {
        //uncomment below and update the code to test itemTypesList
        //instance.itemTypesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('licensesList', function() {
      it('should call licensesList successfully', function(done) {
        //uncomment below and update the code to test licensesList
        //instance.licensesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateAccount', function() {
      it('should call privateAccount successfully', function(done) {
        //uncomment below and update the code to test privateAccount
        //instance.privateAccount(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateFundingSearch', function() {
      it('should call privateFundingSearch successfully', function(done) {
        //uncomment below and update the code to test privateFundingSearch
        //instance.privateFundingSearch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateLicensesList', function() {
      it('should call privateLicensesList successfully', function(done) {
        //uncomment below and update the code to test privateLicensesList
        //instance.privateLicensesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
