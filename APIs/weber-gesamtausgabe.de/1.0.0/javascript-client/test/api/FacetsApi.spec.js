/**
 * WeGA API
 * ⚠️<b>DEPRECATION WARNING</b>⚠️<br/>This version of the WeGA API specification is outdated and superseded by [version 1.1.0](https://weber-gesamtausgabe.de/api/v1/openapi.json).  <br/> <br/> For feedback or requests about this API please contact stadler@weber-gesamtausgabe.de or start the discussion at https://github.com/Edirom/WeGA-WebApp
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
    factory(root.expect, root.WeGaApi);
  }
}(this, function(expect, WeGaApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new WeGaApi.FacetsApi();
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

  describe('FacetsApi', function() {
    describe('facetsFacetGet', function() {
      it('should call facetsFacetGet successfully', function(done) {
        //uncomment below and update the code to test facetsFacetGet
        //instance.facetsFacetGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
