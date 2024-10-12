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

#include "OAI_album_tracks_get_get_200_response_message_header.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_album_tracks_get_get_200_response_message_header::OAI_album_tracks_get_get_200_response_message_header(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_album_tracks_get_get_200_response_message_header::OAI_album_tracks_get_get_200_response_message_header() {
    this->initializeModel();
}

OAI_album_tracks_get_get_200_response_message_header::~OAI_album_tracks_get_get_200_response_message_header() {}

void OAI_album_tracks_get_get_200_response_message_header::initializeModel() {

    m_available_isSet = false;
    m_available_isValid = false;

    m_execute_time_isSet = false;
    m_execute_time_isValid = false;

    m_status_code_isSet = false;
    m_status_code_isValid = false;
}

void OAI_album_tracks_get_get_200_response_message_header::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_album_tracks_get_get_200_response_message_header::fromJsonObject(QJsonObject json) {

    m_available_isValid = ::OpenAPI::fromJsonValue(m_available, json[QString("available")]);
    m_available_isSet = !json[QString("available")].isNull() && m_available_isValid;

    m_execute_time_isValid = ::OpenAPI::fromJsonValue(m_execute_time, json[QString("execute_time")]);
    m_execute_time_isSet = !json[QString("execute_time")].isNull() && m_execute_time_isValid;

    m_status_code_isValid = ::OpenAPI::fromJsonValue(m_status_code, json[QString("status_code")]);
    m_status_code_isSet = !json[QString("status_code")].isNull() && m_status_code_isValid;
}

QString OAI_album_tracks_get_get_200_response_message_header::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_album_tracks_get_get_200_response_message_header::asJsonObject() const {
    QJsonObject obj;
    if (m_available_isSet) {
        obj.insert(QString("available"), ::OpenAPI::toJsonValue(m_available));
    }
    if (m_execute_time_isSet) {
        obj.insert(QString("execute_time"), ::OpenAPI::toJsonValue(m_execute_time));
    }
    if (m_status_code_isSet) {
        obj.insert(QString("status_code"), ::OpenAPI::toJsonValue(m_status_code));
    }
    return obj;
}

double OAI_album_tracks_get_get_200_response_message_header::getAvailable() const {
    return m_available;
}
void OAI_album_tracks_get_get_200_response_message_header::setAvailable(const double &available) {
    m_available = available;
    m_available_isSet = true;
}

bool OAI_album_tracks_get_get_200_response_message_header::is_available_Set() const{
    return m_available_isSet;
}

bool OAI_album_tracks_get_get_200_response_message_header::is_available_Valid() const{
    return m_available_isValid;
}

double OAI_album_tracks_get_get_200_response_message_header::getExecuteTime() const {
    return m_execute_time;
}
void OAI_album_tracks_get_get_200_response_message_header::setExecuteTime(const double &execute_time) {
    m_execute_time = execute_time;
    m_execute_time_isSet = true;
}

bool OAI_album_tracks_get_get_200_response_message_header::is_execute_time_Set() const{
    return m_execute_time_isSet;
}

bool OAI_album_tracks_get_get_200_response_message_header::is_execute_time_Valid() const{
    return m_execute_time_isValid;
}

double OAI_album_tracks_get_get_200_response_message_header::getStatusCode() const {
    return m_status_code;
}
void OAI_album_tracks_get_get_200_response_message_header::setStatusCode(const double &status_code) {
    m_status_code = status_code;
    m_status_code_isSet = true;
}

bool OAI_album_tracks_get_get_200_response_message_header::is_status_code_Set() const{
    return m_status_code_isSet;
}

bool OAI_album_tracks_get_get_200_response_message_header::is_status_code_Valid() const{
    return m_status_code_isValid;
}

bool OAI_album_tracks_get_get_200_response_message_header::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_available_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_execute_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_code_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_album_tracks_get_get_200_response_message_header::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
