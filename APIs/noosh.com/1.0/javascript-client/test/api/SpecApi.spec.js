/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.NooshApiApplication);
  }
}(this, function(expect, NooshApiApplication) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NooshApiApplication.SpecApi();
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

  describe('SpecApi', function() {
    describe('getProductTypeListOfWorkgroup', function() {
      it('should call getProductTypeListOfWorkgroup successfully', function(done) {
        //uncomment below and update the code to test getProductTypeListOfWorkgroup
        //instance.getProductTypeListOfWorkgroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getSpec', function() {
      it('should call getSpec successfully', function(done) {
        //uncomment below and update the code to test getSpec
        //instance.getSpec(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getSpecList', function() {
      it('should call getSpecList successfully', function(done) {
        //uncomment below and update the code to test getSpecList
        //instance.getSpecList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getSpecProductTypeListOfWorkgroup', function() {
      it('should call getSpecProductTypeListOfWorkgroup successfully', function(done) {
        //uncomment below and update the code to test getSpecProductTypeListOfWorkgroup
        //instance.getSpecProductTypeListOfWorkgroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getSpecTypeFields', function() {
      it('should call getSpecTypeFields successfully', function(done) {
        //uncomment below and update the code to test getSpecTypeFields
        //instance.getSpecTypeFields(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('postSpec', function() {
      it('should call postSpec successfully', function(done) {
        //uncomment below and update the code to test postSpec
        //instance.postSpec(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('postSpecProductTypeListOfWorkgroup', function() {
      it('should call postSpecProductTypeListOfWorkgroup successfully', function(done) {
        //uncomment below and update the code to test postSpecProductTypeListOfWorkgroup
        //instance.postSpecProductTypeListOfWorkgroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('putSpec', function() {
      it('should call putSpec successfully', function(done) {
        //uncomment below and update the code to test putSpec
        //instance.putSpec(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet', function() {
      it('should call v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet successfully', function(done) {
        //uncomment below and update the code to test v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet
        //instance.v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut', function() {
      it('should call v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut successfully', function(done) {
        //uncomment below and update the code to test v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut
        //instance.v1WorkgroupsWorkgroupIdProjectsProjectIdSpecsSpecIdPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet', function() {
      it('should call v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet successfully', function(done) {
        //uncomment below and update the code to test v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet
        //instance.v1WorkgroupsWorkgroupIdSpecTypesSpecTypeIdSpecTypeFieldsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
