/**
 * Musixmatch API
 * Musixmatch lyrics API is a robust service that permits you to search and retrieve lyrics in the simplest possible way. It just works.  Include millions of licensed lyrics on your website or in your application legally.  The fastest, most powerful and legal way to display lyrics on your website or in your application.  #### Read musixmatch API Terms & Conditions and the Privacy Policy: Before getting started, you must take a look at the [API Terms & Conditions](http://musixmatch.com/apiterms/) and the [Privacy Policy](https://developer.musixmatch.com/privacy). We’ve worked hard to make this service completely legal so that we are all protected from any foreseeable liability. Take the time to read this stuff.  #### Register for an API key: All you need to do is [register](https://developer.musixmatch.com/signup) in order to get your API key, a mandatory parameter for most of our API calls. It’s your personal identifier and should be kept secret:  ```   https://api.musixmatch.com/ws/v1.1/track.get?apikey=YOUR_API_KEY ``` #### Integrate the musixmatch service with your web site or application In the most common scenario you only need to implement two API calls:  The first call is to match your catalog to ours using the [track.search](#!/Track/get_track_search) function and the second is to get the lyrics using the [track.lyrics.get](#!/Lyrics/get_track_lyrics_get) api. That’s it!  ## API Methods What does the musiXmatch API do?  The musiXmatch API allows you to read objects from our huge 100% licensed lyrics database.  To make your life easier we are providing you with one or more examples to show you how it could work in the wild. You’ll find both the API request and API response in all the available output formats for each API call. Follow the links below for the details.  The current API version is 1.1, the root URL is located at https://api.musixmatch.com/ws/1.1/  Supported input parameters can be found on the page [Input Parameters](https://developer.musixmatch.com/documentation/input-parameters). Use UTF-8 to encode arguments when calling API methods.  Every response includes a status_code. A list of all status codes can be consulted at [Status Codes](https://developer.musixmatch.com/documentation/status-codes).  ## Music meta data The musiXmatch api is built around lyrics, but there are many other data we provide through the api that can be used to improve every existent music service.  ## Track Inside the track object you can get the following extra information:  ### TRACK RATING  The track rating is a score 0-100 identifying how popular is a song in musixmatch.  You can use this information to sort search results, like the most popular songs of an artist, of a music genre, of a lyrics language.  ### INSTRUMENTAL AND EXPLICIT FLAGS  The instrumental flag identifies songs with music only, no lyrics.  The explicit flag identifies songs with explicit lyrics or explicit title. We're able to identify explicit words and set the flag for the most common languages.  ### FAVOURITES  How many users have this song in their list of favourites.  Can be used to sort tracks by num favourite to identify more popular tracks within a set.  ### MUSIC GENRE  The music genere of the song.  Can be used to group songs by genre, as input for similarity alghorithms, artist genre identification, navigate songs by genere, etc.  ### SONG TITLES TRANSLATIONS  The track title, as translated in different lanauages, can be used to display the right writing for a given user, example:  LIES (Bigbang) becomes 在光化門 in chinese HALLELUJAH (Bigbang) becomes ハレルヤ in japanese   ## Artist Inside the artist object you can get the following nice extra information:  ### COMMENTS AND COUNTRY  An artist comment is a short snippet of text which can be mainly used for disambiguation.  The artist country is the born country of the artist/group  There are two perfect search result if you search by artist with the keyword \"U2\". Indeed there are two distinct music groups with this same name, one is the most known irish group of Bono Vox, the other is a less popular (world wide speaking) group from Japan.  Here's how you can made use of the artist comment in your search result page:  U2 (Irish rock band) U2 (あきやまうに) You can also show the artist country for even better disambiguation:  U2 (Irish rock band) from Ireland U2 (あきやまうに) from Japan ARTIST TRANSLATIONS  When you create a world wide music related service you have to take into consideration to display the artist name in the user's local language. These translation are also used as aliases to improve the search results.  Let's use PSY for this example.  Western people know him as PSY but korean want to see the original name 싸이.  Using the name translations provided by our api you can show to every user the writing they expect to see.  Furthermore, when you search for \"psy gangnam style\" or \"싸이 gangnam style\" with our search/match api you will still be able to find the song.  ### ARTIST RATING  The artist rating is a score 0-100 identifying how popular is an artist in musixmatch.  You can use this information to build charts, for suggestions, to sort search results. In the example above about U2, we use the artist rating to show the irish band before the japanese one in our serp.  ### ARTIST MUSIC GENRE  We provide one or more main artist genre, this information can be used to calculate similar artist, suggestions, or the filter a search by artist genre.    ## Album Inside the album object you can get the following nice extra information:  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM RATING  The album rating is a score 0-100 identifying how popular is an album in musixmatch.  You can use this information to sort search results, like the most popular albums of an artist.  ### ALBUM COPYRIGHT AND LABEL  For most of our albums we can provide extra information like for example:  Label: Universal-Island Records Ltd. Copyright: (P) 2013 Rubyworks, under license to Columbia Records, a Division of Sony Music Entertainment. ALBUM TYPE AND RELEASE DATE  The album official release date can be used to sort an artist's albums view starting by the most recent one.  Album can also be filtered or grouped by type: Single, Album, Compilation, Remix, Live. This can help to build an artist page with a more organized structure.  ### ALBUM MUSIC GENRE  For most of the albums we provide two groups of music genres. Primary and secondary. This information can be used to help user navigate albums by genre.  An example could be:  Primary genere: POP Secondary genre: K-POP or Mandopop 
 *
 * The version of the OpenAPI document: 1.1.0
 * Contact: info@musixmatch.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAITrackApi_H
#define OAI_OAITrackApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAI_album_tracks_get_get_200_response.h"
#include "OAI_chart_tracks_get_get_200_response.h"
#include "OAI_matcher_track_get_get_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITrackApi : public QObject {
    Q_OBJECT

public:
    OAITrackApi(const int timeOut = 0);
    ~OAITrackApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  album_id QString [required]
    * @param[in]  format QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  f_has_lyrics QString [optional]
    * @param[in]  page double [optional]
    * @param[in]  page_size double [optional]
    */
    virtual void albumTracksGetGet(const QString &album_id, const ::OpenAPI::OptionalParam<QString> &format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &f_has_lyrics = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &page = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &page_size = ::OpenAPI::OptionalParam<double>());

    /**
    * @param[in]  format QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  page double [optional]
    * @param[in]  page_size double [optional]
    * @param[in]  country QString [optional]
    * @param[in]  f_has_lyrics QString [optional]
    */
    virtual void chartTracksGetGet(const ::OpenAPI::OptionalParam<QString> &format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &page = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &page_size = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<QString> &country = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &f_has_lyrics = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  format QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  q_artist QString [optional]
    * @param[in]  q_track QString [optional]
    * @param[in]  f_has_lyrics double [optional]
    * @param[in]  f_has_subtitle double [optional]
    */
    virtual void matcherTrackGetGet(const ::OpenAPI::OptionalParam<QString> &format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_artist = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_track = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &f_has_lyrics = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &f_has_subtitle = ::OpenAPI::OptionalParam<double>());

    /**
    * @param[in]  track_id QString [required]
    * @param[in]  format QString [optional]
    * @param[in]  callback QString [optional]
    */
    virtual void trackGetGet(const QString &track_id, const ::OpenAPI::OptionalParam<QString> &format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  format QString [optional]
    * @param[in]  callback QString [optional]
    * @param[in]  q_track QString [optional]
    * @param[in]  q_artist QString [optional]
    * @param[in]  q_lyrics QString [optional]
    * @param[in]  f_artist_id double [optional]
    * @param[in]  f_music_genre_id double [optional]
    * @param[in]  f_lyrics_language double [optional]
    * @param[in]  f_has_lyrics double [optional]
    * @param[in]  s_artist_rating QString [optional]
    * @param[in]  s_track_rating QString [optional]
    * @param[in]  quorum_factor double [optional]
    * @param[in]  page_size double [optional]
    * @param[in]  page double [optional]
    */
    virtual void trackSearchGet(const ::OpenAPI::OptionalParam<QString> &format = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &callback = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_track = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_artist = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &q_lyrics = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &f_artist_id = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &f_music_genre_id = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &f_lyrics_language = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &f_has_lyrics = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<QString> &s_artist_rating = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &s_track_rating = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &quorum_factor = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &page_size = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &page = ::OpenAPI::OptionalParam<double>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void albumTracksGetGetCallback(OAIHttpRequestWorker *worker);
    void chartTracksGetGetCallback(OAIHttpRequestWorker *worker);
    void matcherTrackGetGetCallback(OAIHttpRequestWorker *worker);
    void trackGetGetCallback(OAIHttpRequestWorker *worker);
    void trackSearchGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void albumTracksGetGetSignal(OAI_album_tracks_get_get_200_response summary);
    void chartTracksGetGetSignal(OAI_chart_tracks_get_get_200_response summary);
    void matcherTrackGetGetSignal(OAI_matcher_track_get_get_200_response summary);
    void trackGetGetSignal(OAI_matcher_track_get_get_200_response summary);
    void trackSearchGetSignal(OAI_chart_tracks_get_get_200_response summary);


    void albumTracksGetGetSignalFull(OAIHttpRequestWorker *worker, OAI_album_tracks_get_get_200_response summary);
    void chartTracksGetGetSignalFull(OAIHttpRequestWorker *worker, OAI_chart_tracks_get_get_200_response summary);
    void matcherTrackGetGetSignalFull(OAIHttpRequestWorker *worker, OAI_matcher_track_get_get_200_response summary);
    void trackGetGetSignalFull(OAIHttpRequestWorker *worker, OAI_matcher_track_get_get_200_response summary);
    void trackSearchGetSignalFull(OAIHttpRequestWorker *worker, OAI_chart_tracks_get_get_200_response summary);

    Q_DECL_DEPRECATED_X("Use albumTracksGetGetSignalError() instead")
    void albumTracksGetGetSignalE(OAI_album_tracks_get_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void albumTracksGetGetSignalError(OAI_album_tracks_get_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use chartTracksGetGetSignalError() instead")
    void chartTracksGetGetSignalE(OAI_chart_tracks_get_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void chartTracksGetGetSignalError(OAI_chart_tracks_get_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use matcherTrackGetGetSignalError() instead")
    void matcherTrackGetGetSignalE(OAI_matcher_track_get_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void matcherTrackGetGetSignalError(OAI_matcher_track_get_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use trackGetGetSignalError() instead")
    void trackGetGetSignalE(OAI_matcher_track_get_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void trackGetGetSignalError(OAI_matcher_track_get_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use trackSearchGetSignalError() instead")
    void trackSearchGetSignalE(OAI_chart_tracks_get_get_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void trackSearchGetSignalError(OAI_chart_tracks_get_get_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use albumTracksGetGetSignalErrorFull() instead")
    void albumTracksGetGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void albumTracksGetGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use chartTracksGetGetSignalErrorFull() instead")
    void chartTracksGetGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void chartTracksGetGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use matcherTrackGetGetSignalErrorFull() instead")
    void matcherTrackGetGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void matcherTrackGetGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use trackGetGetSignalErrorFull() instead")
    void trackGetGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void trackGetGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use trackSearchGetSignalErrorFull() instead")
    void trackSearchGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void trackSearchGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
