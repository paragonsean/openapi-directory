/**
 * eNanoMapper database
 * AMBIT REST web services [eNanoMapper profile] with free text & faceted search
 *
 * The version of the OpenAPI document: 4.0.0
 * Contact: support@ideaconsult.net
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
    factory(root.expect, root.ENanoMapperDatabase);
  }
}(this, function(expect, ENanoMapperDatabase) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ENanoMapperDatabase.SolrQuery();
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

  describe('SolrQuery', function() {
    it('should create an instance of SolrQuery', function() {
      // uncomment below and update the code to test SolrQuery
      //var instance = new ENanoMapperDatabase.SolrQuery();
      //expect(instance).to.be.a(ENanoMapperDatabase.SolrQuery);
    });

    it('should have the property facet (base name: "facet")', function() {
      // uncomment below and update the code to test the property facet
      //var instance = new ENanoMapperDatabase.SolrQuery();
      //expect(instance).to.be();
    });

    it('should have the property filter (base name: "filter")', function() {
      // uncomment below and update the code to test the property filter
      //var instance = new ENanoMapperDatabase.SolrQuery();
      //expect(instance).to.be();
    });

    it('should have the property query (base name: "query")', function() {
      // uncomment below and update the code to test the property query
      //var instance = new ENanoMapperDatabase.SolrQuery();
      //expect(instance).to.be();
    });

    it('should have the property rows (base name: "rows")', function() {
      // uncomment below and update the code to test the property rows
      //var instance = new ENanoMapperDatabase.SolrQuery();
      //expect(instance).to.be();
    });

    it('should have the property sort (base name: "sort")', function() {
      // uncomment below and update the code to test the property sort
      //var instance = new ENanoMapperDatabase.SolrQuery();
      //expect(instance).to.be();
    });

    it('should have the property start (base name: "start")', function() {
      // uncomment below and update the code to test the property start
      //var instance = new ENanoMapperDatabase.SolrQuery();
      //expect(instance).to.be();
    });

  });

}));
