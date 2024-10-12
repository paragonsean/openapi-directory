/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
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
    factory(root.expect, root.MastodonApiSpecificationHttpsGithubComMastodonMastodon);
  }
}(this, function(expect, MastodonApiSpecificationHttpsGithubComMastodonMastodon) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1ListsPutRequest();
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

  describe('ApiV1ListsPutRequest', function() {
    it('should create an instance of ApiV1ListsPutRequest', function() {
      // uncomment below and update the code to test ApiV1ListsPutRequest
      //var instance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1ListsPutRequest();
      //expect(instance).to.be.a(MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1ListsPutRequest);
    });

    it('should have the property repliesPolicy (base name: "replies_policy")', function() {
      // uncomment below and update the code to test the property repliesPolicy
      //var instance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1ListsPutRequest();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new MastodonApiSpecificationHttpsGithubComMastodonMastodon.ApiV1ListsPutRequest();
      //expect(instance).to.be();
    });

  });

}));
