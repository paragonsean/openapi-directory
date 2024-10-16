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
    instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
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

  describe('PodcastSimple', function() {
    it('should create an instance of PodcastSimple', function() {
      // uncomment below and update the code to test PodcastSimple
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be.a(ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple);
    });

    it('should have the property audioLengthSec (base name: "audio_length_sec")', function() {
      // uncomment below and update the code to test the property audioLengthSec
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property country (base name: "country")', function() {
      // uncomment below and update the code to test the property country
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property earliestPubDateMs (base name: "earliest_pub_date_ms")', function() {
      // uncomment below and update the code to test the property earliestPubDateMs
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property explicitContent (base name: "explicit_content")', function() {
      // uncomment below and update the code to test the property explicitContent
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property extra (base name: "extra")', function() {
      // uncomment below and update the code to test the property extra
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property genreIds (base name: "genre_ids")', function() {
      // uncomment below and update the code to test the property genreIds
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property image (base name: "image")', function() {
      // uncomment below and update the code to test the property image
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property isClaimed (base name: "is_claimed")', function() {
      // uncomment below and update the code to test the property isClaimed
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property itunesId (base name: "itunes_id")', function() {
      // uncomment below and update the code to test the property itunesId
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property language (base name: "language")', function() {
      // uncomment below and update the code to test the property language
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property latestEpisodeId (base name: "latest_episode_id")', function() {
      // uncomment below and update the code to test the property latestEpisodeId
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property latestPubDateMs (base name: "latest_pub_date_ms")', function() {
      // uncomment below and update the code to test the property latestPubDateMs
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property listenScore (base name: "listen_score")', function() {
      // uncomment below and update the code to test the property listenScore
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property listenScoreGlobalRank (base name: "listen_score_global_rank")', function() {
      // uncomment below and update the code to test the property listenScoreGlobalRank
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property listennotesUrl (base name: "listennotes_url")', function() {
      // uncomment below and update the code to test the property listennotesUrl
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property lookingFor (base name: "looking_for")', function() {
      // uncomment below and update the code to test the property lookingFor
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property publisher (base name: "publisher")', function() {
      // uncomment below and update the code to test the property publisher
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property rss (base name: "rss")', function() {
      // uncomment below and update the code to test the property rss
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property thumbnail (base name: "thumbnail")', function() {
      // uncomment below and update the code to test the property thumbnail
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property totalEpisodes (base name: "total_episodes")', function() {
      // uncomment below and update the code to test the property totalEpisodes
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property updateFrequencyHours (base name: "update_frequency_hours")', function() {
      // uncomment below and update the code to test the property updateFrequencyHours
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

    it('should have the property website (base name: "website")', function() {
      // uncomment below and update the code to test the property website
      //var instance = new ListenApiPodcastSearchDirectoryAndInsightsApi.PodcastSimple();
      //expect(instance).to.be();
    });

  });

}));
