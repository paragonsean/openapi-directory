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

#include "OAIAlbum.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAlbum::OAIAlbum(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAlbum::OAIAlbum() {
    this->initializeModel();
}

OAIAlbum::~OAIAlbum() {}

void OAIAlbum::initializeModel() {

    m_album_copyright_isSet = false;
    m_album_copyright_isValid = false;

    m_album_coverart_100x100_isSet = false;
    m_album_coverart_100x100_isValid = false;

    m_album_coverart_350x350_isSet = false;
    m_album_coverart_350x350_isValid = false;

    m_album_coverart_500x500_isSet = false;
    m_album_coverart_500x500_isValid = false;

    m_album_coverart_800x800_isSet = false;
    m_album_coverart_800x800_isValid = false;

    m_album_edit_url_isSet = false;
    m_album_edit_url_isValid = false;

    m_album_id_isSet = false;
    m_album_id_isValid = false;

    m_album_label_isSet = false;
    m_album_label_isValid = false;

    m_album_mbid_isSet = false;
    m_album_mbid_isValid = false;

    m_album_name_isSet = false;
    m_album_name_isValid = false;

    m_album_pline_isSet = false;
    m_album_pline_isValid = false;

    m_album_rating_isSet = false;
    m_album_rating_isValid = false;

    m_album_release_date_isSet = false;
    m_album_release_date_isValid = false;

    m_album_release_type_isSet = false;
    m_album_release_type_isValid = false;

    m_album_track_count_isSet = false;
    m_album_track_count_isValid = false;

    m_album_vanity_id_isSet = false;
    m_album_vanity_id_isValid = false;

    m_artist_id_isSet = false;
    m_artist_id_isValid = false;

    m_artist_name_isSet = false;
    m_artist_name_isValid = false;

    m_primary_genres_isSet = false;
    m_primary_genres_isValid = false;

    m_restricted_isSet = false;
    m_restricted_isValid = false;

    m_secondary_genres_isSet = false;
    m_secondary_genres_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;
}

void OAIAlbum::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAlbum::fromJsonObject(QJsonObject json) {

    m_album_copyright_isValid = ::OpenAPI::fromJsonValue(m_album_copyright, json[QString("album_copyright")]);
    m_album_copyright_isSet = !json[QString("album_copyright")].isNull() && m_album_copyright_isValid;

    m_album_coverart_100x100_isValid = ::OpenAPI::fromJsonValue(m_album_coverart_100x100, json[QString("album_coverart_100x100")]);
    m_album_coverart_100x100_isSet = !json[QString("album_coverart_100x100")].isNull() && m_album_coverart_100x100_isValid;

    m_album_coverart_350x350_isValid = ::OpenAPI::fromJsonValue(m_album_coverart_350x350, json[QString("album_coverart_350x350")]);
    m_album_coverart_350x350_isSet = !json[QString("album_coverart_350x350")].isNull() && m_album_coverart_350x350_isValid;

    m_album_coverart_500x500_isValid = ::OpenAPI::fromJsonValue(m_album_coverart_500x500, json[QString("album_coverart_500x500")]);
    m_album_coverart_500x500_isSet = !json[QString("album_coverart_500x500")].isNull() && m_album_coverart_500x500_isValid;

    m_album_coverart_800x800_isValid = ::OpenAPI::fromJsonValue(m_album_coverart_800x800, json[QString("album_coverart_800x800")]);
    m_album_coverart_800x800_isSet = !json[QString("album_coverart_800x800")].isNull() && m_album_coverart_800x800_isValid;

    m_album_edit_url_isValid = ::OpenAPI::fromJsonValue(m_album_edit_url, json[QString("album_edit_url")]);
    m_album_edit_url_isSet = !json[QString("album_edit_url")].isNull() && m_album_edit_url_isValid;

    m_album_id_isValid = ::OpenAPI::fromJsonValue(m_album_id, json[QString("album_id")]);
    m_album_id_isSet = !json[QString("album_id")].isNull() && m_album_id_isValid;

    m_album_label_isValid = ::OpenAPI::fromJsonValue(m_album_label, json[QString("album_label")]);
    m_album_label_isSet = !json[QString("album_label")].isNull() && m_album_label_isValid;

    m_album_mbid_isValid = ::OpenAPI::fromJsonValue(m_album_mbid, json[QString("album_mbid")]);
    m_album_mbid_isSet = !json[QString("album_mbid")].isNull() && m_album_mbid_isValid;

    m_album_name_isValid = ::OpenAPI::fromJsonValue(m_album_name, json[QString("album_name")]);
    m_album_name_isSet = !json[QString("album_name")].isNull() && m_album_name_isValid;

    m_album_pline_isValid = ::OpenAPI::fromJsonValue(m_album_pline, json[QString("album_pline")]);
    m_album_pline_isSet = !json[QString("album_pline")].isNull() && m_album_pline_isValid;

    m_album_rating_isValid = ::OpenAPI::fromJsonValue(m_album_rating, json[QString("album_rating")]);
    m_album_rating_isSet = !json[QString("album_rating")].isNull() && m_album_rating_isValid;

    m_album_release_date_isValid = ::OpenAPI::fromJsonValue(m_album_release_date, json[QString("album_release_date")]);
    m_album_release_date_isSet = !json[QString("album_release_date")].isNull() && m_album_release_date_isValid;

    m_album_release_type_isValid = ::OpenAPI::fromJsonValue(m_album_release_type, json[QString("album_release_type")]);
    m_album_release_type_isSet = !json[QString("album_release_type")].isNull() && m_album_release_type_isValid;

    m_album_track_count_isValid = ::OpenAPI::fromJsonValue(m_album_track_count, json[QString("album_track_count")]);
    m_album_track_count_isSet = !json[QString("album_track_count")].isNull() && m_album_track_count_isValid;

    m_album_vanity_id_isValid = ::OpenAPI::fromJsonValue(m_album_vanity_id, json[QString("album_vanity_id")]);
    m_album_vanity_id_isSet = !json[QString("album_vanity_id")].isNull() && m_album_vanity_id_isValid;

    m_artist_id_isValid = ::OpenAPI::fromJsonValue(m_artist_id, json[QString("artist_id")]);
    m_artist_id_isSet = !json[QString("artist_id")].isNull() && m_artist_id_isValid;

    m_artist_name_isValid = ::OpenAPI::fromJsonValue(m_artist_name, json[QString("artist_name")]);
    m_artist_name_isSet = !json[QString("artist_name")].isNull() && m_artist_name_isValid;

    m_primary_genres_isValid = ::OpenAPI::fromJsonValue(m_primary_genres, json[QString("primary_genres")]);
    m_primary_genres_isSet = !json[QString("primary_genres")].isNull() && m_primary_genres_isValid;

    m_restricted_isValid = ::OpenAPI::fromJsonValue(m_restricted, json[QString("restricted")]);
    m_restricted_isSet = !json[QString("restricted")].isNull() && m_restricted_isValid;

    m_secondary_genres_isValid = ::OpenAPI::fromJsonValue(m_secondary_genres, json[QString("secondary_genres")]);
    m_secondary_genres_isSet = !json[QString("secondary_genres")].isNull() && m_secondary_genres_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updated_time")]);
    m_updated_time_isSet = !json[QString("updated_time")].isNull() && m_updated_time_isValid;
}

QString OAIAlbum::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAlbum::asJsonObject() const {
    QJsonObject obj;
    if (m_album_copyright_isSet) {
        obj.insert(QString("album_copyright"), ::OpenAPI::toJsonValue(m_album_copyright));
    }
    if (m_album_coverart_100x100_isSet) {
        obj.insert(QString("album_coverart_100x100"), ::OpenAPI::toJsonValue(m_album_coverart_100x100));
    }
    if (m_album_coverart_350x350_isSet) {
        obj.insert(QString("album_coverart_350x350"), ::OpenAPI::toJsonValue(m_album_coverart_350x350));
    }
    if (m_album_coverart_500x500_isSet) {
        obj.insert(QString("album_coverart_500x500"), ::OpenAPI::toJsonValue(m_album_coverart_500x500));
    }
    if (m_album_coverart_800x800_isSet) {
        obj.insert(QString("album_coverart_800x800"), ::OpenAPI::toJsonValue(m_album_coverart_800x800));
    }
    if (m_album_edit_url_isSet) {
        obj.insert(QString("album_edit_url"), ::OpenAPI::toJsonValue(m_album_edit_url));
    }
    if (m_album_id_isSet) {
        obj.insert(QString("album_id"), ::OpenAPI::toJsonValue(m_album_id));
    }
    if (m_album_label_isSet) {
        obj.insert(QString("album_label"), ::OpenAPI::toJsonValue(m_album_label));
    }
    if (m_album_mbid_isSet) {
        obj.insert(QString("album_mbid"), ::OpenAPI::toJsonValue(m_album_mbid));
    }
    if (m_album_name_isSet) {
        obj.insert(QString("album_name"), ::OpenAPI::toJsonValue(m_album_name));
    }
    if (m_album_pline_isSet) {
        obj.insert(QString("album_pline"), ::OpenAPI::toJsonValue(m_album_pline));
    }
    if (m_album_rating_isSet) {
        obj.insert(QString("album_rating"), ::OpenAPI::toJsonValue(m_album_rating));
    }
    if (m_album_release_date_isSet) {
        obj.insert(QString("album_release_date"), ::OpenAPI::toJsonValue(m_album_release_date));
    }
    if (m_album_release_type_isSet) {
        obj.insert(QString("album_release_type"), ::OpenAPI::toJsonValue(m_album_release_type));
    }
    if (m_album_track_count_isSet) {
        obj.insert(QString("album_track_count"), ::OpenAPI::toJsonValue(m_album_track_count));
    }
    if (m_album_vanity_id_isSet) {
        obj.insert(QString("album_vanity_id"), ::OpenAPI::toJsonValue(m_album_vanity_id));
    }
    if (m_artist_id_isSet) {
        obj.insert(QString("artist_id"), ::OpenAPI::toJsonValue(m_artist_id));
    }
    if (m_artist_name_isSet) {
        obj.insert(QString("artist_name"), ::OpenAPI::toJsonValue(m_artist_name));
    }
    if (m_primary_genres.isSet()) {
        obj.insert(QString("primary_genres"), ::OpenAPI::toJsonValue(m_primary_genres));
    }
    if (m_restricted_isSet) {
        obj.insert(QString("restricted"), ::OpenAPI::toJsonValue(m_restricted));
    }
    if (m_secondary_genres.isSet()) {
        obj.insert(QString("secondary_genres"), ::OpenAPI::toJsonValue(m_secondary_genres));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updated_time"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    return obj;
}

QString OAIAlbum::getAlbumCopyright() const {
    return m_album_copyright;
}
void OAIAlbum::setAlbumCopyright(const QString &album_copyright) {
    m_album_copyright = album_copyright;
    m_album_copyright_isSet = true;
}

bool OAIAlbum::is_album_copyright_Set() const{
    return m_album_copyright_isSet;
}

bool OAIAlbum::is_album_copyright_Valid() const{
    return m_album_copyright_isValid;
}

QString OAIAlbum::getAlbumCoverart100x100() const {
    return m_album_coverart_100x100;
}
void OAIAlbum::setAlbumCoverart100x100(const QString &album_coverart_100x100) {
    m_album_coverart_100x100 = album_coverart_100x100;
    m_album_coverart_100x100_isSet = true;
}

bool OAIAlbum::is_album_coverart_100x100_Set() const{
    return m_album_coverart_100x100_isSet;
}

bool OAIAlbum::is_album_coverart_100x100_Valid() const{
    return m_album_coverart_100x100_isValid;
}

QString OAIAlbum::getAlbumCoverart350x350() const {
    return m_album_coverart_350x350;
}
void OAIAlbum::setAlbumCoverart350x350(const QString &album_coverart_350x350) {
    m_album_coverart_350x350 = album_coverart_350x350;
    m_album_coverart_350x350_isSet = true;
}

bool OAIAlbum::is_album_coverart_350x350_Set() const{
    return m_album_coverart_350x350_isSet;
}

bool OAIAlbum::is_album_coverart_350x350_Valid() const{
    return m_album_coverart_350x350_isValid;
}

QString OAIAlbum::getAlbumCoverart500x500() const {
    return m_album_coverart_500x500;
}
void OAIAlbum::setAlbumCoverart500x500(const QString &album_coverart_500x500) {
    m_album_coverart_500x500 = album_coverart_500x500;
    m_album_coverart_500x500_isSet = true;
}

bool OAIAlbum::is_album_coverart_500x500_Set() const{
    return m_album_coverart_500x500_isSet;
}

bool OAIAlbum::is_album_coverart_500x500_Valid() const{
    return m_album_coverart_500x500_isValid;
}

QString OAIAlbum::getAlbumCoverart800x800() const {
    return m_album_coverart_800x800;
}
void OAIAlbum::setAlbumCoverart800x800(const QString &album_coverart_800x800) {
    m_album_coverart_800x800 = album_coverart_800x800;
    m_album_coverart_800x800_isSet = true;
}

bool OAIAlbum::is_album_coverart_800x800_Set() const{
    return m_album_coverart_800x800_isSet;
}

bool OAIAlbum::is_album_coverart_800x800_Valid() const{
    return m_album_coverart_800x800_isValid;
}

QString OAIAlbum::getAlbumEditUrl() const {
    return m_album_edit_url;
}
void OAIAlbum::setAlbumEditUrl(const QString &album_edit_url) {
    m_album_edit_url = album_edit_url;
    m_album_edit_url_isSet = true;
}

bool OAIAlbum::is_album_edit_url_Set() const{
    return m_album_edit_url_isSet;
}

bool OAIAlbum::is_album_edit_url_Valid() const{
    return m_album_edit_url_isValid;
}

double OAIAlbum::getAlbumId() const {
    return m_album_id;
}
void OAIAlbum::setAlbumId(const double &album_id) {
    m_album_id = album_id;
    m_album_id_isSet = true;
}

bool OAIAlbum::is_album_id_Set() const{
    return m_album_id_isSet;
}

bool OAIAlbum::is_album_id_Valid() const{
    return m_album_id_isValid;
}

QString OAIAlbum::getAlbumLabel() const {
    return m_album_label;
}
void OAIAlbum::setAlbumLabel(const QString &album_label) {
    m_album_label = album_label;
    m_album_label_isSet = true;
}

bool OAIAlbum::is_album_label_Set() const{
    return m_album_label_isSet;
}

bool OAIAlbum::is_album_label_Valid() const{
    return m_album_label_isValid;
}

QString OAIAlbum::getAlbumMbid() const {
    return m_album_mbid;
}
void OAIAlbum::setAlbumMbid(const QString &album_mbid) {
    m_album_mbid = album_mbid;
    m_album_mbid_isSet = true;
}

bool OAIAlbum::is_album_mbid_Set() const{
    return m_album_mbid_isSet;
}

bool OAIAlbum::is_album_mbid_Valid() const{
    return m_album_mbid_isValid;
}

QString OAIAlbum::getAlbumName() const {
    return m_album_name;
}
void OAIAlbum::setAlbumName(const QString &album_name) {
    m_album_name = album_name;
    m_album_name_isSet = true;
}

bool OAIAlbum::is_album_name_Set() const{
    return m_album_name_isSet;
}

bool OAIAlbum::is_album_name_Valid() const{
    return m_album_name_isValid;
}

QString OAIAlbum::getAlbumPline() const {
    return m_album_pline;
}
void OAIAlbum::setAlbumPline(const QString &album_pline) {
    m_album_pline = album_pline;
    m_album_pline_isSet = true;
}

bool OAIAlbum::is_album_pline_Set() const{
    return m_album_pline_isSet;
}

bool OAIAlbum::is_album_pline_Valid() const{
    return m_album_pline_isValid;
}

double OAIAlbum::getAlbumRating() const {
    return m_album_rating;
}
void OAIAlbum::setAlbumRating(const double &album_rating) {
    m_album_rating = album_rating;
    m_album_rating_isSet = true;
}

bool OAIAlbum::is_album_rating_Set() const{
    return m_album_rating_isSet;
}

bool OAIAlbum::is_album_rating_Valid() const{
    return m_album_rating_isValid;
}

QString OAIAlbum::getAlbumReleaseDate() const {
    return m_album_release_date;
}
void OAIAlbum::setAlbumReleaseDate(const QString &album_release_date) {
    m_album_release_date = album_release_date;
    m_album_release_date_isSet = true;
}

bool OAIAlbum::is_album_release_date_Set() const{
    return m_album_release_date_isSet;
}

bool OAIAlbum::is_album_release_date_Valid() const{
    return m_album_release_date_isValid;
}

QString OAIAlbum::getAlbumReleaseType() const {
    return m_album_release_type;
}
void OAIAlbum::setAlbumReleaseType(const QString &album_release_type) {
    m_album_release_type = album_release_type;
    m_album_release_type_isSet = true;
}

bool OAIAlbum::is_album_release_type_Set() const{
    return m_album_release_type_isSet;
}

bool OAIAlbum::is_album_release_type_Valid() const{
    return m_album_release_type_isValid;
}

double OAIAlbum::getAlbumTrackCount() const {
    return m_album_track_count;
}
void OAIAlbum::setAlbumTrackCount(const double &album_track_count) {
    m_album_track_count = album_track_count;
    m_album_track_count_isSet = true;
}

bool OAIAlbum::is_album_track_count_Set() const{
    return m_album_track_count_isSet;
}

bool OAIAlbum::is_album_track_count_Valid() const{
    return m_album_track_count_isValid;
}

QString OAIAlbum::getAlbumVanityId() const {
    return m_album_vanity_id;
}
void OAIAlbum::setAlbumVanityId(const QString &album_vanity_id) {
    m_album_vanity_id = album_vanity_id;
    m_album_vanity_id_isSet = true;
}

bool OAIAlbum::is_album_vanity_id_Set() const{
    return m_album_vanity_id_isSet;
}

bool OAIAlbum::is_album_vanity_id_Valid() const{
    return m_album_vanity_id_isValid;
}

double OAIAlbum::getArtistId() const {
    return m_artist_id;
}
void OAIAlbum::setArtistId(const double &artist_id) {
    m_artist_id = artist_id;
    m_artist_id_isSet = true;
}

bool OAIAlbum::is_artist_id_Set() const{
    return m_artist_id_isSet;
}

bool OAIAlbum::is_artist_id_Valid() const{
    return m_artist_id_isValid;
}

QString OAIAlbum::getArtistName() const {
    return m_artist_name;
}
void OAIAlbum::setArtistName(const QString &artist_name) {
    m_artist_name = artist_name;
    m_artist_name_isSet = true;
}

bool OAIAlbum::is_artist_name_Set() const{
    return m_artist_name_isSet;
}

bool OAIAlbum::is_artist_name_Valid() const{
    return m_artist_name_isValid;
}

OAIAlbum_primary_genres OAIAlbum::getPrimaryGenres() const {
    return m_primary_genres;
}
void OAIAlbum::setPrimaryGenres(const OAIAlbum_primary_genres &primary_genres) {
    m_primary_genres = primary_genres;
    m_primary_genres_isSet = true;
}

bool OAIAlbum::is_primary_genres_Set() const{
    return m_primary_genres_isSet;
}

bool OAIAlbum::is_primary_genres_Valid() const{
    return m_primary_genres_isValid;
}

double OAIAlbum::getRestricted() const {
    return m_restricted;
}
void OAIAlbum::setRestricted(const double &restricted) {
    m_restricted = restricted;
    m_restricted_isSet = true;
}

bool OAIAlbum::is_restricted_Set() const{
    return m_restricted_isSet;
}

bool OAIAlbum::is_restricted_Valid() const{
    return m_restricted_isValid;
}

OAIAlbum_secondary_genres OAIAlbum::getSecondaryGenres() const {
    return m_secondary_genres;
}
void OAIAlbum::setSecondaryGenres(const OAIAlbum_secondary_genres &secondary_genres) {
    m_secondary_genres = secondary_genres;
    m_secondary_genres_isSet = true;
}

bool OAIAlbum::is_secondary_genres_Set() const{
    return m_secondary_genres_isSet;
}

bool OAIAlbum::is_secondary_genres_Valid() const{
    return m_secondary_genres_isValid;
}

QString OAIAlbum::getUpdatedTime() const {
    return m_updated_time;
}
void OAIAlbum::setUpdatedTime(const QString &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAIAlbum::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAIAlbum::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

bool OAIAlbum::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_album_copyright_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_coverart_100x100_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_coverart_350x350_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_coverart_500x500_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_coverart_800x800_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_edit_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_mbid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_pline_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_rating_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_release_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_release_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_track_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_vanity_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_artist_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_artist_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_genres.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_restricted_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_secondary_genres.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAlbum::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
