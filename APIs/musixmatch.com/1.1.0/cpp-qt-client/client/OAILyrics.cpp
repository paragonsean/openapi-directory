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

#include "OAILyrics.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILyrics::OAILyrics(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILyrics::OAILyrics() {
    this->initializeModel();
}

OAILyrics::~OAILyrics() {}

void OAILyrics::initializeModel() {

    m_action_requested_isSet = false;
    m_action_requested_isValid = false;

    m_can_edit_isSet = false;
    m_can_edit_isValid = false;

    m_r_explicit_isSet = false;
    m_r_explicit_isValid = false;

    m_html_tracking_url_isSet = false;
    m_html_tracking_url_isValid = false;

    m_instrumental_isSet = false;
    m_instrumental_isValid = false;

    m_locked_isSet = false;
    m_locked_isValid = false;

    m_lyrics_body_isSet = false;
    m_lyrics_body_isValid = false;

    m_lyrics_copyright_isSet = false;
    m_lyrics_copyright_isValid = false;

    m_lyrics_id_isSet = false;
    m_lyrics_id_isValid = false;

    m_lyrics_language_isSet = false;
    m_lyrics_language_isValid = false;

    m_lyrics_language_description_isSet = false;
    m_lyrics_language_description_isValid = false;

    m_pixel_tracking_url_isSet = false;
    m_pixel_tracking_url_isValid = false;

    m_publisher_list_isSet = false;
    m_publisher_list_isValid = false;

    m_restricted_isSet = false;
    m_restricted_isValid = false;

    m_script_tracking_url_isSet = false;
    m_script_tracking_url_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;

    m_verified_isSet = false;
    m_verified_isValid = false;

    m_writer_list_isSet = false;
    m_writer_list_isValid = false;
}

void OAILyrics::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILyrics::fromJsonObject(QJsonObject json) {

    m_action_requested_isValid = ::OpenAPI::fromJsonValue(m_action_requested, json[QString("action_requested")]);
    m_action_requested_isSet = !json[QString("action_requested")].isNull() && m_action_requested_isValid;

    m_can_edit_isValid = ::OpenAPI::fromJsonValue(m_can_edit, json[QString("can_edit")]);
    m_can_edit_isSet = !json[QString("can_edit")].isNull() && m_can_edit_isValid;

    m_r_explicit_isValid = ::OpenAPI::fromJsonValue(m_r_explicit, json[QString("explicit")]);
    m_r_explicit_isSet = !json[QString("explicit")].isNull() && m_r_explicit_isValid;

    m_html_tracking_url_isValid = ::OpenAPI::fromJsonValue(m_html_tracking_url, json[QString("html_tracking_url")]);
    m_html_tracking_url_isSet = !json[QString("html_tracking_url")].isNull() && m_html_tracking_url_isValid;

    m_instrumental_isValid = ::OpenAPI::fromJsonValue(m_instrumental, json[QString("instrumental")]);
    m_instrumental_isSet = !json[QString("instrumental")].isNull() && m_instrumental_isValid;

    m_locked_isValid = ::OpenAPI::fromJsonValue(m_locked, json[QString("locked")]);
    m_locked_isSet = !json[QString("locked")].isNull() && m_locked_isValid;

    m_lyrics_body_isValid = ::OpenAPI::fromJsonValue(m_lyrics_body, json[QString("lyrics_body")]);
    m_lyrics_body_isSet = !json[QString("lyrics_body")].isNull() && m_lyrics_body_isValid;

    m_lyrics_copyright_isValid = ::OpenAPI::fromJsonValue(m_lyrics_copyright, json[QString("lyrics_copyright")]);
    m_lyrics_copyright_isSet = !json[QString("lyrics_copyright")].isNull() && m_lyrics_copyright_isValid;

    m_lyrics_id_isValid = ::OpenAPI::fromJsonValue(m_lyrics_id, json[QString("lyrics_id")]);
    m_lyrics_id_isSet = !json[QString("lyrics_id")].isNull() && m_lyrics_id_isValid;

    m_lyrics_language_isValid = ::OpenAPI::fromJsonValue(m_lyrics_language, json[QString("lyrics_language")]);
    m_lyrics_language_isSet = !json[QString("lyrics_language")].isNull() && m_lyrics_language_isValid;

    m_lyrics_language_description_isValid = ::OpenAPI::fromJsonValue(m_lyrics_language_description, json[QString("lyrics_language_description")]);
    m_lyrics_language_description_isSet = !json[QString("lyrics_language_description")].isNull() && m_lyrics_language_description_isValid;

    m_pixel_tracking_url_isValid = ::OpenAPI::fromJsonValue(m_pixel_tracking_url, json[QString("pixel_tracking_url")]);
    m_pixel_tracking_url_isSet = !json[QString("pixel_tracking_url")].isNull() && m_pixel_tracking_url_isValid;

    m_publisher_list_isValid = ::OpenAPI::fromJsonValue(m_publisher_list, json[QString("publisher_list")]);
    m_publisher_list_isSet = !json[QString("publisher_list")].isNull() && m_publisher_list_isValid;

    m_restricted_isValid = ::OpenAPI::fromJsonValue(m_restricted, json[QString("restricted")]);
    m_restricted_isSet = !json[QString("restricted")].isNull() && m_restricted_isValid;

    m_script_tracking_url_isValid = ::OpenAPI::fromJsonValue(m_script_tracking_url, json[QString("script_tracking_url")]);
    m_script_tracking_url_isSet = !json[QString("script_tracking_url")].isNull() && m_script_tracking_url_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updated_time")]);
    m_updated_time_isSet = !json[QString("updated_time")].isNull() && m_updated_time_isValid;

    m_verified_isValid = ::OpenAPI::fromJsonValue(m_verified, json[QString("verified")]);
    m_verified_isSet = !json[QString("verified")].isNull() && m_verified_isValid;

    m_writer_list_isValid = ::OpenAPI::fromJsonValue(m_writer_list, json[QString("writer_list")]);
    m_writer_list_isSet = !json[QString("writer_list")].isNull() && m_writer_list_isValid;
}

QString OAILyrics::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILyrics::asJsonObject() const {
    QJsonObject obj;
    if (m_action_requested_isSet) {
        obj.insert(QString("action_requested"), ::OpenAPI::toJsonValue(m_action_requested));
    }
    if (m_can_edit_isSet) {
        obj.insert(QString("can_edit"), ::OpenAPI::toJsonValue(m_can_edit));
    }
    if (m_r_explicit_isSet) {
        obj.insert(QString("explicit"), ::OpenAPI::toJsonValue(m_r_explicit));
    }
    if (m_html_tracking_url_isSet) {
        obj.insert(QString("html_tracking_url"), ::OpenAPI::toJsonValue(m_html_tracking_url));
    }
    if (m_instrumental_isSet) {
        obj.insert(QString("instrumental"), ::OpenAPI::toJsonValue(m_instrumental));
    }
    if (m_locked_isSet) {
        obj.insert(QString("locked"), ::OpenAPI::toJsonValue(m_locked));
    }
    if (m_lyrics_body_isSet) {
        obj.insert(QString("lyrics_body"), ::OpenAPI::toJsonValue(m_lyrics_body));
    }
    if (m_lyrics_copyright_isSet) {
        obj.insert(QString("lyrics_copyright"), ::OpenAPI::toJsonValue(m_lyrics_copyright));
    }
    if (m_lyrics_id_isSet) {
        obj.insert(QString("lyrics_id"), ::OpenAPI::toJsonValue(m_lyrics_id));
    }
    if (m_lyrics_language_isSet) {
        obj.insert(QString("lyrics_language"), ::OpenAPI::toJsonValue(m_lyrics_language));
    }
    if (m_lyrics_language_description_isSet) {
        obj.insert(QString("lyrics_language_description"), ::OpenAPI::toJsonValue(m_lyrics_language_description));
    }
    if (m_pixel_tracking_url_isSet) {
        obj.insert(QString("pixel_tracking_url"), ::OpenAPI::toJsonValue(m_pixel_tracking_url));
    }
    if (m_publisher_list.size() > 0) {
        obj.insert(QString("publisher_list"), ::OpenAPI::toJsonValue(m_publisher_list));
    }
    if (m_restricted_isSet) {
        obj.insert(QString("restricted"), ::OpenAPI::toJsonValue(m_restricted));
    }
    if (m_script_tracking_url_isSet) {
        obj.insert(QString("script_tracking_url"), ::OpenAPI::toJsonValue(m_script_tracking_url));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updated_time"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    if (m_verified_isSet) {
        obj.insert(QString("verified"), ::OpenAPI::toJsonValue(m_verified));
    }
    if (m_writer_list.size() > 0) {
        obj.insert(QString("writer_list"), ::OpenAPI::toJsonValue(m_writer_list));
    }
    return obj;
}

QString OAILyrics::getActionRequested() const {
    return m_action_requested;
}
void OAILyrics::setActionRequested(const QString &action_requested) {
    m_action_requested = action_requested;
    m_action_requested_isSet = true;
}

bool OAILyrics::is_action_requested_Set() const{
    return m_action_requested_isSet;
}

bool OAILyrics::is_action_requested_Valid() const{
    return m_action_requested_isValid;
}

double OAILyrics::getCanEdit() const {
    return m_can_edit;
}
void OAILyrics::setCanEdit(const double &can_edit) {
    m_can_edit = can_edit;
    m_can_edit_isSet = true;
}

bool OAILyrics::is_can_edit_Set() const{
    return m_can_edit_isSet;
}

bool OAILyrics::is_can_edit_Valid() const{
    return m_can_edit_isValid;
}

double OAILyrics::getRExplicit() const {
    return m_r_explicit;
}
void OAILyrics::setRExplicit(const double &r_explicit) {
    m_r_explicit = r_explicit;
    m_r_explicit_isSet = true;
}

bool OAILyrics::is_r_explicit_Set() const{
    return m_r_explicit_isSet;
}

bool OAILyrics::is_r_explicit_Valid() const{
    return m_r_explicit_isValid;
}

QString OAILyrics::getHtmlTrackingUrl() const {
    return m_html_tracking_url;
}
void OAILyrics::setHtmlTrackingUrl(const QString &html_tracking_url) {
    m_html_tracking_url = html_tracking_url;
    m_html_tracking_url_isSet = true;
}

bool OAILyrics::is_html_tracking_url_Set() const{
    return m_html_tracking_url_isSet;
}

bool OAILyrics::is_html_tracking_url_Valid() const{
    return m_html_tracking_url_isValid;
}

double OAILyrics::getInstrumental() const {
    return m_instrumental;
}
void OAILyrics::setInstrumental(const double &instrumental) {
    m_instrumental = instrumental;
    m_instrumental_isSet = true;
}

bool OAILyrics::is_instrumental_Set() const{
    return m_instrumental_isSet;
}

bool OAILyrics::is_instrumental_Valid() const{
    return m_instrumental_isValid;
}

double OAILyrics::getLocked() const {
    return m_locked;
}
void OAILyrics::setLocked(const double &locked) {
    m_locked = locked;
    m_locked_isSet = true;
}

bool OAILyrics::is_locked_Set() const{
    return m_locked_isSet;
}

bool OAILyrics::is_locked_Valid() const{
    return m_locked_isValid;
}

QString OAILyrics::getLyricsBody() const {
    return m_lyrics_body;
}
void OAILyrics::setLyricsBody(const QString &lyrics_body) {
    m_lyrics_body = lyrics_body;
    m_lyrics_body_isSet = true;
}

bool OAILyrics::is_lyrics_body_Set() const{
    return m_lyrics_body_isSet;
}

bool OAILyrics::is_lyrics_body_Valid() const{
    return m_lyrics_body_isValid;
}

QString OAILyrics::getLyricsCopyright() const {
    return m_lyrics_copyright;
}
void OAILyrics::setLyricsCopyright(const QString &lyrics_copyright) {
    m_lyrics_copyright = lyrics_copyright;
    m_lyrics_copyright_isSet = true;
}

bool OAILyrics::is_lyrics_copyright_Set() const{
    return m_lyrics_copyright_isSet;
}

bool OAILyrics::is_lyrics_copyright_Valid() const{
    return m_lyrics_copyright_isValid;
}

double OAILyrics::getLyricsId() const {
    return m_lyrics_id;
}
void OAILyrics::setLyricsId(const double &lyrics_id) {
    m_lyrics_id = lyrics_id;
    m_lyrics_id_isSet = true;
}

bool OAILyrics::is_lyrics_id_Set() const{
    return m_lyrics_id_isSet;
}

bool OAILyrics::is_lyrics_id_Valid() const{
    return m_lyrics_id_isValid;
}

QString OAILyrics::getLyricsLanguage() const {
    return m_lyrics_language;
}
void OAILyrics::setLyricsLanguage(const QString &lyrics_language) {
    m_lyrics_language = lyrics_language;
    m_lyrics_language_isSet = true;
}

bool OAILyrics::is_lyrics_language_Set() const{
    return m_lyrics_language_isSet;
}

bool OAILyrics::is_lyrics_language_Valid() const{
    return m_lyrics_language_isValid;
}

QString OAILyrics::getLyricsLanguageDescription() const {
    return m_lyrics_language_description;
}
void OAILyrics::setLyricsLanguageDescription(const QString &lyrics_language_description) {
    m_lyrics_language_description = lyrics_language_description;
    m_lyrics_language_description_isSet = true;
}

bool OAILyrics::is_lyrics_language_description_Set() const{
    return m_lyrics_language_description_isSet;
}

bool OAILyrics::is_lyrics_language_description_Valid() const{
    return m_lyrics_language_description_isValid;
}

QString OAILyrics::getPixelTrackingUrl() const {
    return m_pixel_tracking_url;
}
void OAILyrics::setPixelTrackingUrl(const QString &pixel_tracking_url) {
    m_pixel_tracking_url = pixel_tracking_url;
    m_pixel_tracking_url_isSet = true;
}

bool OAILyrics::is_pixel_tracking_url_Set() const{
    return m_pixel_tracking_url_isSet;
}

bool OAILyrics::is_pixel_tracking_url_Valid() const{
    return m_pixel_tracking_url_isValid;
}

QList<QString> OAILyrics::getPublisherList() const {
    return m_publisher_list;
}
void OAILyrics::setPublisherList(const QList<QString> &publisher_list) {
    m_publisher_list = publisher_list;
    m_publisher_list_isSet = true;
}

bool OAILyrics::is_publisher_list_Set() const{
    return m_publisher_list_isSet;
}

bool OAILyrics::is_publisher_list_Valid() const{
    return m_publisher_list_isValid;
}

double OAILyrics::getRestricted() const {
    return m_restricted;
}
void OAILyrics::setRestricted(const double &restricted) {
    m_restricted = restricted;
    m_restricted_isSet = true;
}

bool OAILyrics::is_restricted_Set() const{
    return m_restricted_isSet;
}

bool OAILyrics::is_restricted_Valid() const{
    return m_restricted_isValid;
}

QString OAILyrics::getScriptTrackingUrl() const {
    return m_script_tracking_url;
}
void OAILyrics::setScriptTrackingUrl(const QString &script_tracking_url) {
    m_script_tracking_url = script_tracking_url;
    m_script_tracking_url_isSet = true;
}

bool OAILyrics::is_script_tracking_url_Set() const{
    return m_script_tracking_url_isSet;
}

bool OAILyrics::is_script_tracking_url_Valid() const{
    return m_script_tracking_url_isValid;
}

QString OAILyrics::getUpdatedTime() const {
    return m_updated_time;
}
void OAILyrics::setUpdatedTime(const QString &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAILyrics::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAILyrics::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

double OAILyrics::getVerified() const {
    return m_verified;
}
void OAILyrics::setVerified(const double &verified) {
    m_verified = verified;
    m_verified_isSet = true;
}

bool OAILyrics::is_verified_Set() const{
    return m_verified_isSet;
}

bool OAILyrics::is_verified_Valid() const{
    return m_verified_isValid;
}

QList<QString> OAILyrics::getWriterList() const {
    return m_writer_list;
}
void OAILyrics::setWriterList(const QList<QString> &writer_list) {
    m_writer_list = writer_list;
    m_writer_list_isSet = true;
}

bool OAILyrics::is_writer_list_Set() const{
    return m_writer_list_isSet;
}

bool OAILyrics::is_writer_list_Valid() const{
    return m_writer_list_isValid;
}

bool OAILyrics::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_requested_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_can_edit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_explicit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_html_tracking_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_instrumental_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_locked_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lyrics_body_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lyrics_copyright_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lyrics_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lyrics_language_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lyrics_language_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pixel_tracking_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_publisher_list.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_restricted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_script_tracking_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_verified_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_writer_list.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILyrics::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
