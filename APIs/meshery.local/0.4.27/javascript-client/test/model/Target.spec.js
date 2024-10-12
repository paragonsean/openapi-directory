/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
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
    factory(root.expect, root.MesheryApi);
  }
}(this, function(expect, MesheryApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MesheryApi.Target();
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

  describe('Target', function() {
    it('should create an instance of Target', function() {
      // uncomment below and update the code to test Target
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be.a(MesheryApi.Target);
    });

    it('should have the property alias (base name: "alias")', function() {
      // uncomment below and update the code to test the property alias
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property aliasBy (base name: "aliasBy")', function() {
      // uncomment below and update the code to test the property aliasBy
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property alignOptions (base name: "alignOptions")', function() {
      // uncomment below and update the code to test the property alignOptions
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property alignmentPeriod (base name: "alignmentPeriod")', function() {
      // uncomment below and update the code to test the property alignmentPeriod
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property bucketAggs (base name: "bucketAggs")', function() {
      // uncomment below and update the code to test the property bucketAggs
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property crossSeriesReducer (base name: "crossSeriesReducer")', function() {
      // uncomment below and update the code to test the property crossSeriesReducer
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property datasource (base name: "datasource")', function() {
      // uncomment below and update the code to test the property datasource
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property dimensions (base name: "dimensions")', function() {
      // uncomment below and update the code to test the property dimensions
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property dsType (base name: "dsType")', function() {
      // uncomment below and update the code to test the property dsType
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property expr (base name: "expr")', function() {
      // uncomment below and update the code to test the property expr
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property filters (base name: "filters")', function() {
      // uncomment below and update the code to test the property filters
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property format (base name: "format")', function() {
      // uncomment below and update the code to test the property format
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property group (base name: "group")', function() {
      // uncomment below and update the code to test the property group
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property groupBys (base name: "groupBys")', function() {
      // uncomment below and update the code to test the property groupBys
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property hide (base name: "hide")', function() {
      // uncomment below and update the code to test the property hide
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property instant (base name: "instant")', function() {
      // uncomment below and update the code to test the property instant
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property interval (base name: "interval")', function() {
      // uncomment below and update the code to test the property interval
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property intervalFactor (base name: "intervalFactor")', function() {
      // uncomment below and update the code to test the property intervalFactor
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property legendFormat (base name: "legendFormat")', function() {
      // uncomment below and update the code to test the property legendFormat
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property measurement (base name: "measurement")', function() {
      // uncomment below and update the code to test the property measurement
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property metricColumn (base name: "metricColumn")', function() {
      // uncomment below and update the code to test the property metricColumn
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property metricKind (base name: "metricKind")', function() {
      // uncomment below and update the code to test the property metricKind
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property metricName (base name: "metricName")', function() {
      // uncomment below and update the code to test the property metricName
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property metricType (base name: "metricType")', function() {
      // uncomment below and update the code to test the property metricType
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property metrics (base name: "metrics")', function() {
      // uncomment below and update the code to test the property metrics
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property namespace (base name: "namespace")', function() {
      // uncomment below and update the code to test the property namespace
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property perSeriesAligner (base name: "perSeriesAligner")', function() {
      // uncomment below and update the code to test the property perSeriesAligner
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property period (base name: "period")', function() {
      // uncomment below and update the code to test the property period
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property projectName (base name: "projectName")', function() {
      // uncomment below and update the code to test the property projectName
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property query (base name: "query")', function() {
      // uncomment below and update the code to test the property query
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property rawQuery (base name: "rawQuery")', function() {
      // uncomment below and update the code to test the property rawQuery
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property rawSql (base name: "rawSql")', function() {
      // uncomment below and update the code to test the property rawSql
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property refId (base name: "refId")', function() {
      // uncomment below and update the code to test the property refId
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property region (base name: "region")', function() {
      // uncomment below and update the code to test the property region
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property select (base name: "select")', function() {
      // uncomment below and update the code to test the property select
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property statistics (base name: "statistics")', function() {
      // uncomment below and update the code to test the property statistics
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property step (base name: "step")', function() {
      // uncomment below and update the code to test the property step
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property table (base name: "table")', function() {
      // uncomment below and update the code to test the property table
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property target (base name: "target")', function() {
      // uncomment below and update the code to test the property target
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property timeColumn (base name: "timeColumn")', function() {
      // uncomment below and update the code to test the property timeColumn
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property timeField (base name: "timeField")', function() {
      // uncomment below and update the code to test the property timeField
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property valueType (base name: "valueType")', function() {
      // uncomment below and update the code to test the property valueType
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

    it('should have the property where (base name: "where")', function() {
      // uncomment below and update the code to test the property where
      //var instance = new MesheryApi.Target();
      //expect(instance).to.be();
    });

  });

}));
