/**
 * Listen API: Podcast Search, Directory, and Insights API
 * Simple & no-nonsense podcast search & directory API. Search all podcasts and episodes by people, places, or topics. 
 *
 * The version of the OpenAPI document: 2.0
 * Contact: hello@listennotes.com
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
    factory(root.expect, root.ListenApiPodcastSearchDirectoryAndInsightsApi);
  }
}(this, function(expect, ListenApiPodcastSearchDirectoryAndInsightsApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastTypeaheadResult();
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

  describe('PodcastTypeaheadResult', function() {
    it('should create an instance of PodcastTypeaheadResult', function() {
      // uncomment below and update the code to test PodcastTypeaheadResult
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastTypeaheadResult();
      //expect(instance).to.be.a(ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastTypeaheadResult);
    });

    it('should have the property explicitContent (base name: "explicit_content")', function() {
      // uncomment below and update the code to test the property explicitContent
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastTypeaheadResult();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastTypeaheadResult();
      //expect(instance).to.be();
    });

    it('should have the property image (base name: "image")', function() {
      // uncomment below and update the code to test the property image
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastTypeaheadResult();
      //expect(instance).to.be();
    });

    it('should have the property publisherHighlighted (base name: "publisher_highlighted")', function() {
      // uncomment below and update the code to test the property publisherHighlighted
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastTypeaheadResult();
      //expect(instance).to.be();
    });

    it('should have the property publisherOriginal (base name: "publisher_original")', function() {
      // uncomment below and update the code to test the property publisherOriginal
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastTypeaheadResult();
      //expect(instance).to.be();
    });

    it('should have the property thumbnail (base name: "thumbnail")', function() {
      // uncomment below and update the code to test the property thumbnail
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastTypeaheadResult();
      //expect(instance).to.be();
    });

    it('should have the property titleHighlighted (base name: "title_highlighted")', function() {
      // uncomment below and update the code to test the property titleHighlighted
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastTypeaheadResult();
      //expect(instance).to.be();
    });

    it('should have the property titleOriginal (base name: "title_original")', function() {
      // uncomment below and update the code to test the property titleOriginal
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastTypeaheadResult();
      //expect(instance).to.be();
    });

  });

}));
