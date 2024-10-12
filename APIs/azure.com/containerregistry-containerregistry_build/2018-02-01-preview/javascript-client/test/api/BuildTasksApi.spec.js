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
    instance = new ContainerRegistryManagementClient.BuildTasksApi();
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

  describe('BuildTasksApi', function() {
    describe('buildTasksCreate', function() {
      it('should call buildTasksCreate successfully', function(done) {
        //uncomment below and update the code to test buildTasksCreate
        //instance.buildTasksCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('buildTasksDelete', function() {
      it('should call buildTasksDelete successfully', function(done) {
        //uncomment below and update the code to test buildTasksDelete
        //instance.buildTasksDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('buildTasksGet', function() {
      it('should call buildTasksGet successfully', function(done) {
        //uncomment below and update the code to test buildTasksGet
        //instance.buildTasksGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('buildTasksList', function() {
      it('should call buildTasksList successfully', function(done) {
        //uncomment below and update the code to test buildTasksList
        //instance.buildTasksList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('buildTasksListSourceRepositoryProperties', function() {
      it('should call buildTasksListSourceRepositoryProperties successfully', function(done) {
        //uncomment below and update the code to test buildTasksListSourceRepositoryProperties
        //instance.buildTasksListSourceRepositoryProperties(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('buildTasksUpdate', function() {
      it('should call buildTasksUpdate successfully', function(done) {
        //uncomment below and update the code to test buildTasksUpdate
        //instance.buildTasksUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
