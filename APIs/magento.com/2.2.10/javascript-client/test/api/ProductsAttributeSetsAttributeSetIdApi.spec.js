/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
    factory(root.expect, root.MagentoB2B);
  }
}(this, function(expect, MagentoB2B) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MagentoB2B.ProductsAttributeSetsAttributeSetIdApi();
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

  describe('ProductsAttributeSetsAttributeSetIdApi', function() {
    describe('catalogAttributeSetRepositoryV1DeleteByIdDelete', function() {
      it('should call catalogAttributeSetRepositoryV1DeleteByIdDelete successfully', function(done) {
        //uncomment below and update the code to test catalogAttributeSetRepositoryV1DeleteByIdDelete
        //instance.catalogAttributeSetRepositoryV1DeleteByIdDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('catalogAttributeSetRepositoryV1GetGet', function() {
      it('should call catalogAttributeSetRepositoryV1GetGet successfully', function(done) {
        //uncomment below and update the code to test catalogAttributeSetRepositoryV1GetGet
        //instance.catalogAttributeSetRepositoryV1GetGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('catalogAttributeSetRepositoryV1SavePut', function() {
      it('should call catalogAttributeSetRepositoryV1SavePut successfully', function(done) {
        //uncomment below and update the code to test catalogAttributeSetRepositoryV1SavePut
        //instance.catalogAttributeSetRepositoryV1SavePut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
