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
    instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
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

  describe('PlaylistResponse', function() {
    it('should create an instance of PlaylistResponse', function() {
      // uncomment below and update the code to test PlaylistResponse
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be.a(ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse);
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

    it('should have the property image (base name: "image")', function() {
      // uncomment below and update the code to test the property image
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

    it('should have the property items (base name: "items")', function() {
      // uncomment below and update the code to test the property items
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

    it('should have the property lastTimestampMs (base name: "last_timestamp_ms")', function() {
      // uncomment below and update the code to test the property lastTimestampMs
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

    it('should have the property listennotesUrl (base name: "listennotes_url")', function() {
      // uncomment below and update the code to test the property listennotesUrl
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

    it('should have the property thumbnail (base name: "thumbnail")', function() {
      // uncomment below and update the code to test the property thumbnail
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

    it('should have the property total (base name: "total")', function() {
      // uncomment below and update the code to test the property total
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

    it('should have the property totalAudioLengthSec (base name: "total_audio_length_sec")', function() {
      // uncomment below and update the code to test the property totalAudioLengthSec
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

    it('should have the property visibility (base name: "visibility")', function() {
      // uncomment below and update the code to test the property visibility
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PlaylistResponse();
      //expect(instance).to.be();
    });

  });

}));
