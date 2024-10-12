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
    instance = new MagentoB2B.FrameworkSearchAggregationInterface();
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

  describe('FrameworkSearchAggregationInterface', function() {
    it('should create an instance of FrameworkSearchAggregationInterface', function() {
      // uncomment below and update the code to test FrameworkSearchAggregationInterface
      //var instance = new MagentoB2B.FrameworkSearchAggregationInterface();
      //expect(instance).to.be.a(MagentoB2B.FrameworkSearchAggregationInterface);
    });

    it('should have the property bucketNames (base name: "bucket_names")', function() {
      // uncomment below and update the code to test the property bucketNames
      //var instance = new MagentoB2B.FrameworkSearchAggregationInterface();
      //expect(instance).to.be();
    });

    it('should have the property buckets (base name: "buckets")', function() {
      // uncomment below and update the code to test the property buckets
      //var instance = new MagentoB2B.FrameworkSearchAggregationInterface();
      //expect(instance).to.be();
    });

  });

}));
