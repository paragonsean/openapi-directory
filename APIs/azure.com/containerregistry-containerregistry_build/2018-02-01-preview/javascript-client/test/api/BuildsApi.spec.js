/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
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
    factory(root.expect, root.ContainerRegistryManagementClient);
  }
}(this, function(expect, ContainerRegistryManagementClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ContainerRegistryManagementClient.BuildsApi();
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

  describe('BuildsApi', function() {
    describe('buildsCancel', function() {
      it('should call buildsCancel successfully', function(done) {
        //uncomment below and update the code to test buildsCancel
        //instance.buildsCancel(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('buildsGet', function() {
      it('should call buildsGet successfully', function(done) {
        //uncomment below and update the code to test buildsGet
        //instance.buildsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('buildsGetLogLink', function() {
      it('should call buildsGetLogLink successfully', function(done) {
        //uncomment below and update the code to test buildsGetLogLink
        //instance.buildsGetLogLink(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('buildsList', function() {
      it('should call buildsList successfully', function(done) {
        //uncomment below and update the code to test buildsList
        //instance.buildsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('buildsUpdate', function() {
      it('should call buildsUpdate successfully', function(done) {
        //uncomment below and update the code to test buildsUpdate
        //instance.buildsUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
