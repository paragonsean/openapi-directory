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

#include "OAITrack.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITrack::OAITrack(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITrack::OAITrack() {
    this->initializeModel();
}

OAITrack::~OAITrack() {}

void OAITrack::initializeModel() {

    m_album_coverart_100x100_isSet = false;
    m_album_coverart_100x100_isValid = false;

    m_album_coverart_350x350_isSet = false;
    m_album_coverart_350x350_isValid = false;

    m_album_coverart_500x500_isSet = false;
    m_album_coverart_500x500_isValid = false;

    m_album_coverart_800x800_isSet = false;
    m_album_coverart_800x800_isValid = false;

    m_album_id_isSet = false;
    m_album_id_isValid = false;

    m_album_name_isSet = false;
    m_album_name_isValid = false;

    m_artist_id_isSet = false;
    m_artist_id_isValid = false;

    m_artist_mbid_isSet = false;
    m_artist_mbid_isValid = false;

    m_artist_name_isSet = false;
    m_artist_name_isValid = false;

    m_commontrack_id_isSet = false;
    m_commontrack_id_isValid = false;

    m_commontrack_vanity_id_isSet = false;
    m_commontrack_vanity_id_isValid = false;

    m_r_explicit_isSet = false;
    m_r_explicit_isValid = false;

    m_first_release_date_isSet = false;
    m_first_release_date_isValid = false;

    m_has_lyrics_isSet = false;
    m_has_lyrics_isValid = false;

    m_has_subtitles_isSet = false;
    m_has_subtitles_isValid = false;

    m_instrumental_isSet = false;
    m_instrumental_isValid = false;

    m_lyrics_id_isSet = false;
    m_lyrics_id_isValid = false;

    m_num_favourite_isSet = false;
    m_num_favourite_isValid = false;

    m_primary_genres_isSet = false;
    m_primary_genres_isValid = false;

    m_restricted_isSet = false;
    m_restricted_isValid = false;

    m_secondary_genres_isSet = false;
    m_secondary_genres_isValid = false;

    m_subtitle_id_isSet = false;
    m_subtitle_id_isValid = false;

    m_track_edit_url_isSet = false;
    m_track_edit_url_isValid = false;

    m_track_id_isSet = false;
    m_track_id_isValid = false;

    m_track_isrc_isSet = false;
    m_track_isrc_isValid = false;

    m_track_length_isSet = false;
    m_track_length_isValid = false;

    m_track_mbid_isSet = false;
    m_track_mbid_isValid = false;

    m_track_name_isSet = false;
    m_track_name_isValid = false;

    m_track_name_translation_list_isSet = false;
    m_track_name_translation_list_isValid = false;

    m_track_rating_isSet = false;
    m_track_rating_isValid = false;

    m_track_share_url_isSet = false;
    m_track_share_url_isValid = false;

    m_track_soundcloud_id_isSet = false;
    m_track_soundcloud_id_isValid = false;

    m_track_spotify_id_isSet = false;
    m_track_spotify_id_isValid = false;

    m_track_xboxmusic_id_isSet = false;
    m_track_xboxmusic_id_isValid = false;

    m_updated_time_isSet = false;
    m_updated_time_isValid = false;
}

void OAITrack::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITrack::fromJsonObject(QJsonObject json) {

    m_album_coverart_100x100_isValid = ::OpenAPI::fromJsonValue(m_album_coverart_100x100, json[QString("album_coverart_100x100")]);
    m_album_coverart_100x100_isSet = !json[QString("album_coverart_100x100")].isNull() && m_album_coverart_100x100_isValid;

    m_album_coverart_350x350_isValid = ::OpenAPI::fromJsonValue(m_album_coverart_350x350, json[QString("album_coverart_350x350")]);
    m_album_coverart_350x350_isSet = !json[QString("album_coverart_350x350")].isNull() && m_album_coverart_350x350_isValid;

    m_album_coverart_500x500_isValid = ::OpenAPI::fromJsonValue(m_album_coverart_500x500, json[QString("album_coverart_500x500")]);
    m_album_coverart_500x500_isSet = !json[QString("album_coverart_500x500")].isNull() && m_album_coverart_500x500_isValid;

    m_album_coverart_800x800_isValid = ::OpenAPI::fromJsonValue(m_album_coverart_800x800, json[QString("album_coverart_800x800")]);
    m_album_coverart_800x800_isSet = !json[QString("album_coverart_800x800")].isNull() && m_album_coverart_800x800_isValid;

    m_album_id_isValid = ::OpenAPI::fromJsonValue(m_album_id, json[QString("album_id")]);
    m_album_id_isSet = !json[QString("album_id")].isNull() && m_album_id_isValid;

    m_album_name_isValid = ::OpenAPI::fromJsonValue(m_album_name, json[QString("album_name")]);
    m_album_name_isSet = !json[QString("album_name")].isNull() && m_album_name_isValid;

    m_artist_id_isValid = ::OpenAPI::fromJsonValue(m_artist_id, json[QString("artist_id")]);
    m_artist_id_isSet = !json[QString("artist_id")].isNull() && m_artist_id_isValid;

    m_artist_mbid_isValid = ::OpenAPI::fromJsonValue(m_artist_mbid, json[QString("artist_mbid")]);
    m_artist_mbid_isSet = !json[QString("artist_mbid")].isNull() && m_artist_mbid_isValid;

    m_artist_name_isValid = ::OpenAPI::fromJsonValue(m_artist_name, json[QString("artist_name")]);
    m_artist_name_isSet = !json[QString("artist_name")].isNull() && m_artist_name_isValid;

    m_commontrack_id_isValid = ::OpenAPI::fromJsonValue(m_commontrack_id, json[QString("commontrack_id")]);
    m_commontrack_id_isSet = !json[QString("commontrack_id")].isNull() && m_commontrack_id_isValid;

    m_commontrack_vanity_id_isValid = ::OpenAPI::fromJsonValue(m_commontrack_vanity_id, json[QString("commontrack_vanity_id")]);
    m_commontrack_vanity_id_isSet = !json[QString("commontrack_vanity_id")].isNull() && m_commontrack_vanity_id_isValid;

    m_r_explicit_isValid = ::OpenAPI::fromJsonValue(m_r_explicit, json[QString("explicit")]);
    m_r_explicit_isSet = !json[QString("explicit")].isNull() && m_r_explicit_isValid;

    m_first_release_date_isValid = ::OpenAPI::fromJsonValue(m_first_release_date, json[QString("first_release_date")]);
    m_first_release_date_isSet = !json[QString("first_release_date")].isNull() && m_first_release_date_isValid;

    m_has_lyrics_isValid = ::OpenAPI::fromJsonValue(m_has_lyrics, json[QString("has_lyrics")]);
    m_has_lyrics_isSet = !json[QString("has_lyrics")].isNull() && m_has_lyrics_isValid;

    m_has_subtitles_isValid = ::OpenAPI::fromJsonValue(m_has_subtitles, json[QString("has_subtitles")]);
    m_has_subtitles_isSet = !json[QString("has_subtitles")].isNull() && m_has_subtitles_isValid;

    m_instrumental_isValid = ::OpenAPI::fromJsonValue(m_instrumental, json[QString("instrumental")]);
    m_instrumental_isSet = !json[QString("instrumental")].isNull() && m_instrumental_isValid;

    m_lyrics_id_isValid = ::OpenAPI::fromJsonValue(m_lyrics_id, json[QString("lyrics_id")]);
    m_lyrics_id_isSet = !json[QString("lyrics_id")].isNull() && m_lyrics_id_isValid;

    m_num_favourite_isValid = ::OpenAPI::fromJsonValue(m_num_favourite, json[QString("num_favourite")]);
    m_num_favourite_isSet = !json[QString("num_favourite")].isNull() && m_num_favourite_isValid;

    m_primary_genres_isValid = ::OpenAPI::fromJsonValue(m_primary_genres, json[QString("primary_genres")]);
    m_primary_genres_isSet = !json[QString("primary_genres")].isNull() && m_primary_genres_isValid;

    m_restricted_isValid = ::OpenAPI::fromJsonValue(m_restricted, json[QString("restricted")]);
    m_restricted_isSet = !json[QString("restricted")].isNull() && m_restricted_isValid;

    m_secondary_genres_isValid = ::OpenAPI::fromJsonValue(m_secondary_genres, json[QString("secondary_genres")]);
    m_secondary_genres_isSet = !json[QString("secondary_genres")].isNull() && m_secondary_genres_isValid;

    m_subtitle_id_isValid = ::OpenAPI::fromJsonValue(m_subtitle_id, json[QString("subtitle_id")]);
    m_subtitle_id_isSet = !json[QString("subtitle_id")].isNull() && m_subtitle_id_isValid;

    m_track_edit_url_isValid = ::OpenAPI::fromJsonValue(m_track_edit_url, json[QString("track_edit_url")]);
    m_track_edit_url_isSet = !json[QString("track_edit_url")].isNull() && m_track_edit_url_isValid;

    m_track_id_isValid = ::OpenAPI::fromJsonValue(m_track_id, json[QString("track_id")]);
    m_track_id_isSet = !json[QString("track_id")].isNull() && m_track_id_isValid;

    m_track_isrc_isValid = ::OpenAPI::fromJsonValue(m_track_isrc, json[QString("track_isrc")]);
    m_track_isrc_isSet = !json[QString("track_isrc")].isNull() && m_track_isrc_isValid;

    m_track_length_isValid = ::OpenAPI::fromJsonValue(m_track_length, json[QString("track_length")]);
    m_track_length_isSet = !json[QString("track_length")].isNull() && m_track_length_isValid;

    m_track_mbid_isValid = ::OpenAPI::fromJsonValue(m_track_mbid, json[QString("track_mbid")]);
    m_track_mbid_isSet = !json[QString("track_mbid")].isNull() && m_track_mbid_isValid;

    m_track_name_isValid = ::OpenAPI::fromJsonValue(m_track_name, json[QString("track_name")]);
    m_track_name_isSet = !json[QString("track_name")].isNull() && m_track_name_isValid;

    m_track_name_translation_list_isValid = ::OpenAPI::fromJsonValue(m_track_name_translation_list, json[QString("track_name_translation_list")]);
    m_track_name_translation_list_isSet = !json[QString("track_name_translation_list")].isNull() && m_track_name_translation_list_isValid;

    m_track_rating_isValid = ::OpenAPI::fromJsonValue(m_track_rating, json[QString("track_rating")]);
    m_track_rating_isSet = !json[QString("track_rating")].isNull() && m_track_rating_isValid;

    m_track_share_url_isValid = ::OpenAPI::fromJsonValue(m_track_share_url, json[QString("track_share_url")]);
    m_track_share_url_isSet = !json[QString("track_share_url")].isNull() && m_track_share_url_isValid;

    m_track_soundcloud_id_isValid = ::OpenAPI::fromJsonValue(m_track_soundcloud_id, json[QString("track_soundcloud_id")]);
    m_track_soundcloud_id_isSet = !json[QString("track_soundcloud_id")].isNull() && m_track_soundcloud_id_isValid;

    m_track_spotify_id_isValid = ::OpenAPI::fromJsonValue(m_track_spotify_id, json[QString("track_spotify_id")]);
    m_track_spotify_id_isSet = !json[QString("track_spotify_id")].isNull() && m_track_spotify_id_isValid;

    m_track_xboxmusic_id_isValid = ::OpenAPI::fromJsonValue(m_track_xboxmusic_id, json[QString("track_xboxmusic_id")]);
    m_track_xboxmusic_id_isSet = !json[QString("track_xboxmusic_id")].isNull() && m_track_xboxmusic_id_isValid;

    m_updated_time_isValid = ::OpenAPI::fromJsonValue(m_updated_time, json[QString("updated_time")]);
    m_updated_time_isSet = !json[QString("updated_time")].isNull() && m_updated_time_isValid;
}

QString OAITrack::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITrack::asJsonObject() const {
    QJsonObject obj;
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
    if (m_album_id_isSet) {
        obj.insert(QString("album_id"), ::OpenAPI::toJsonValue(m_album_id));
    }
    if (m_album_name_isSet) {
        obj.insert(QString("album_name"), ::OpenAPI::toJsonValue(m_album_name));
    }
    if (m_artist_id_isSet) {
        obj.insert(QString("artist_id"), ::OpenAPI::toJsonValue(m_artist_id));
    }
    if (m_artist_mbid_isSet) {
        obj.insert(QString("artist_mbid"), ::OpenAPI::toJsonValue(m_artist_mbid));
    }
    if (m_artist_name_isSet) {
        obj.insert(QString("artist_name"), ::OpenAPI::toJsonValue(m_artist_name));
    }
    if (m_commontrack_id_isSet) {
        obj.insert(QString("commontrack_id"), ::OpenAPI::toJsonValue(m_commontrack_id));
    }
    if (m_commontrack_vanity_id_isSet) {
        obj.insert(QString("commontrack_vanity_id"), ::OpenAPI::toJsonValue(m_commontrack_vanity_id));
    }
    if (m_r_explicit_isSet) {
        obj.insert(QString("explicit"), ::OpenAPI::toJsonValue(m_r_explicit));
    }
    if (m_first_release_date_isSet) {
        obj.insert(QString("first_release_date"), ::OpenAPI::toJsonValue(m_first_release_date));
    }
    if (m_has_lyrics_isSet) {
        obj.insert(QString("has_lyrics"), ::OpenAPI::toJsonValue(m_has_lyrics));
    }
    if (m_has_subtitles_isSet) {
        obj.insert(QString("has_subtitles"), ::OpenAPI::toJsonValue(m_has_subtitles));
    }
    if (m_instrumental_isSet) {
        obj.insert(QString("instrumental"), ::OpenAPI::toJsonValue(m_instrumental));
    }
    if (m_lyrics_id_isSet) {
        obj.insert(QString("lyrics_id"), ::OpenAPI::toJsonValue(m_lyrics_id));
    }
    if (m_num_favourite_isSet) {
        obj.insert(QString("num_favourite"), ::OpenAPI::toJsonValue(m_num_favourite));
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
    if (m_subtitle_id_isSet) {
        obj.insert(QString("subtitle_id"), ::OpenAPI::toJsonValue(m_subtitle_id));
    }
    if (m_track_edit_url_isSet) {
        obj.insert(QString("track_edit_url"), ::OpenAPI::toJsonValue(m_track_edit_url));
    }
    if (m_track_id_isSet) {
        obj.insert(QString("track_id"), ::OpenAPI::toJsonValue(m_track_id));
    }
    if (m_track_isrc_isSet) {
        obj.insert(QString("track_isrc"), ::OpenAPI::toJsonValue(m_track_isrc));
    }
    if (m_track_length_isSet) {
        obj.insert(QString("track_length"), ::OpenAPI::toJsonValue(m_track_length));
    }
    if (m_track_mbid_isSet) {
        obj.insert(QString("track_mbid"), ::OpenAPI::toJsonValue(m_track_mbid));
    }
    if (m_track_name_isSet) {
        obj.insert(QString("track_name"), ::OpenAPI::toJsonValue(m_track_name));
    }
    if (m_track_name_translation_list.size() > 0) {
        obj.insert(QString("track_name_translation_list"), ::OpenAPI::toJsonValue(m_track_name_translation_list));
    }
    if (m_track_rating_isSet) {
        obj.insert(QString("track_rating"), ::OpenAPI::toJsonValue(m_track_rating));
    }
    if (m_track_share_url_isSet) {
        obj.insert(QString("track_share_url"), ::OpenAPI::toJsonValue(m_track_share_url));
    }
    if (m_track_soundcloud_id_isSet) {
        obj.insert(QString("track_soundcloud_id"), ::OpenAPI::toJsonValue(m_track_soundcloud_id));
    }
    if (m_track_spotify_id_isSet) {
        obj.insert(QString("track_spotify_id"), ::OpenAPI::toJsonValue(m_track_spotify_id));
    }
    if (m_track_xboxmusic_id_isSet) {
        obj.insert(QString("track_xboxmusic_id"), ::OpenAPI::toJsonValue(m_track_xboxmusic_id));
    }
    if (m_updated_time_isSet) {
        obj.insert(QString("updated_time"), ::OpenAPI::toJsonValue(m_updated_time));
    }
    return obj;
}

QString OAITrack::getAlbumCoverart100x100() const {
    return m_album_coverart_100x100;
}
void OAITrack::setAlbumCoverart100x100(const QString &album_coverart_100x100) {
    m_album_coverart_100x100 = album_coverart_100x100;
    m_album_coverart_100x100_isSet = true;
}

bool OAITrack::is_album_coverart_100x100_Set() const{
    return m_album_coverart_100x100_isSet;
}

bool OAITrack::is_album_coverart_100x100_Valid() const{
    return m_album_coverart_100x100_isValid;
}

QString OAITrack::getAlbumCoverart350x350() const {
    return m_album_coverart_350x350;
}
void OAITrack::setAlbumCoverart350x350(const QString &album_coverart_350x350) {
    m_album_coverart_350x350 = album_coverart_350x350;
    m_album_coverart_350x350_isSet = true;
}

bool OAITrack::is_album_coverart_350x350_Set() const{
    return m_album_coverart_350x350_isSet;
}

bool OAITrack::is_album_coverart_350x350_Valid() const{
    return m_album_coverart_350x350_isValid;
}

QString OAITrack::getAlbumCoverart500x500() const {
    return m_album_coverart_500x500;
}
void OAITrack::setAlbumCoverart500x500(const QString &album_coverart_500x500) {
    m_album_coverart_500x500 = album_coverart_500x500;
    m_album_coverart_500x500_isSet = true;
}

bool OAITrack::is_album_coverart_500x500_Set() const{
    return m_album_coverart_500x500_isSet;
}

bool OAITrack::is_album_coverart_500x500_Valid() const{
    return m_album_coverart_500x500_isValid;
}

QString OAITrack::getAlbumCoverart800x800() const {
    return m_album_coverart_800x800;
}
void OAITrack::setAlbumCoverart800x800(const QString &album_coverart_800x800) {
    m_album_coverart_800x800 = album_coverart_800x800;
    m_album_coverart_800x800_isSet = true;
}

bool OAITrack::is_album_coverart_800x800_Set() const{
    return m_album_coverart_800x800_isSet;
}

bool OAITrack::is_album_coverart_800x800_Valid() const{
    return m_album_coverart_800x800_isValid;
}

double OAITrack::getAlbumId() const {
    return m_album_id;
}
void OAITrack::setAlbumId(const double &album_id) {
    m_album_id = album_id;
    m_album_id_isSet = true;
}

bool OAITrack::is_album_id_Set() const{
    return m_album_id_isSet;
}

bool OAITrack::is_album_id_Valid() const{
    return m_album_id_isValid;
}

QString OAITrack::getAlbumName() const {
    return m_album_name;
}
void OAITrack::setAlbumName(const QString &album_name) {
    m_album_name = album_name;
    m_album_name_isSet = true;
}

bool OAITrack::is_album_name_Set() const{
    return m_album_name_isSet;
}

bool OAITrack::is_album_name_Valid() const{
    return m_album_name_isValid;
}

double OAITrack::getArtistId() const {
    return m_artist_id;
}
void OAITrack::setArtistId(const double &artist_id) {
    m_artist_id = artist_id;
    m_artist_id_isSet = true;
}

bool OAITrack::is_artist_id_Set() const{
    return m_artist_id_isSet;
}

bool OAITrack::is_artist_id_Valid() const{
    return m_artist_id_isValid;
}

QString OAITrack::getArtistMbid() const {
    return m_artist_mbid;
}
void OAITrack::setArtistMbid(const QString &artist_mbid) {
    m_artist_mbid = artist_mbid;
    m_artist_mbid_isSet = true;
}

bool OAITrack::is_artist_mbid_Set() const{
    return m_artist_mbid_isSet;
}

bool OAITrack::is_artist_mbid_Valid() const{
    return m_artist_mbid_isValid;
}

QString OAITrack::getArtistName() const {
    return m_artist_name;
}
void OAITrack::setArtistName(const QString &artist_name) {
    m_artist_name = artist_name;
    m_artist_name_isSet = true;
}

bool OAITrack::is_artist_name_Set() const{
    return m_artist_name_isSet;
}

bool OAITrack::is_artist_name_Valid() const{
    return m_artist_name_isValid;
}

double OAITrack::getCommontrackId() const {
    return m_commontrack_id;
}
void OAITrack::setCommontrackId(const double &commontrack_id) {
    m_commontrack_id = commontrack_id;
    m_commontrack_id_isSet = true;
}

bool OAITrack::is_commontrack_id_Set() const{
    return m_commontrack_id_isSet;
}

bool OAITrack::is_commontrack_id_Valid() const{
    return m_commontrack_id_isValid;
}

QString OAITrack::getCommontrackVanityId() const {
    return m_commontrack_vanity_id;
}
void OAITrack::setCommontrackVanityId(const QString &commontrack_vanity_id) {
    m_commontrack_vanity_id = commontrack_vanity_id;
    m_commontrack_vanity_id_isSet = true;
}

bool OAITrack::is_commontrack_vanity_id_Set() const{
    return m_commontrack_vanity_id_isSet;
}

bool OAITrack::is_commontrack_vanity_id_Valid() const{
    return m_commontrack_vanity_id_isValid;
}

double OAITrack::getRExplicit() const {
    return m_r_explicit;
}
void OAITrack::setRExplicit(const double &r_explicit) {
    m_r_explicit = r_explicit;
    m_r_explicit_isSet = true;
}

bool OAITrack::is_r_explicit_Set() const{
    return m_r_explicit_isSet;
}

bool OAITrack::is_r_explicit_Valid() const{
    return m_r_explicit_isValid;
}

QString OAITrack::getFirstReleaseDate() const {
    return m_first_release_date;
}
void OAITrack::setFirstReleaseDate(const QString &first_release_date) {
    m_first_release_date = first_release_date;
    m_first_release_date_isSet = true;
}

bool OAITrack::is_first_release_date_Set() const{
    return m_first_release_date_isSet;
}

bool OAITrack::is_first_release_date_Valid() const{
    return m_first_release_date_isValid;
}

double OAITrack::getHasLyrics() const {
    return m_has_lyrics;
}
void OAITrack::setHasLyrics(const double &has_lyrics) {
    m_has_lyrics = has_lyrics;
    m_has_lyrics_isSet = true;
}

bool OAITrack::is_has_lyrics_Set() const{
    return m_has_lyrics_isSet;
}

bool OAITrack::is_has_lyrics_Valid() const{
    return m_has_lyrics_isValid;
}

double OAITrack::getHasSubtitles() const {
    return m_has_subtitles;
}
void OAITrack::setHasSubtitles(const double &has_subtitles) {
    m_has_subtitles = has_subtitles;
    m_has_subtitles_isSet = true;
}

bool OAITrack::is_has_subtitles_Set() const{
    return m_has_subtitles_isSet;
}

bool OAITrack::is_has_subtitles_Valid() const{
    return m_has_subtitles_isValid;
}

double OAITrack::getInstrumental() const {
    return m_instrumental;
}
void OAITrack::setInstrumental(const double &instrumental) {
    m_instrumental = instrumental;
    m_instrumental_isSet = true;
}

bool OAITrack::is_instrumental_Set() const{
    return m_instrumental_isSet;
}

bool OAITrack::is_instrumental_Valid() const{
    return m_instrumental_isValid;
}

double OAITrack::getLyricsId() const {
    return m_lyrics_id;
}
void OAITrack::setLyricsId(const double &lyrics_id) {
    m_lyrics_id = lyrics_id;
    m_lyrics_id_isSet = true;
}

bool OAITrack::is_lyrics_id_Set() const{
    return m_lyrics_id_isSet;
}

bool OAITrack::is_lyrics_id_Valid() const{
    return m_lyrics_id_isValid;
}

double OAITrack::getNumFavourite() const {
    return m_num_favourite;
}
void OAITrack::setNumFavourite(const double &num_favourite) {
    m_num_favourite = num_favourite;
    m_num_favourite_isSet = true;
}

bool OAITrack::is_num_favourite_Set() const{
    return m_num_favourite_isSet;
}

bool OAITrack::is_num_favourite_Valid() const{
    return m_num_favourite_isValid;
}

OAIAlbum_primary_genres OAITrack::getPrimaryGenres() const {
    return m_primary_genres;
}
void OAITrack::setPrimaryGenres(const OAIAlbum_primary_genres &primary_genres) {
    m_primary_genres = primary_genres;
    m_primary_genres_isSet = true;
}

bool OAITrack::is_primary_genres_Set() const{
    return m_primary_genres_isSet;
}

bool OAITrack::is_primary_genres_Valid() const{
    return m_primary_genres_isValid;
}

double OAITrack::getRestricted() const {
    return m_restricted;
}
void OAITrack::setRestricted(const double &restricted) {
    m_restricted = restricted;
    m_restricted_isSet = true;
}

bool OAITrack::is_restricted_Set() const{
    return m_restricted_isSet;
}

bool OAITrack::is_restricted_Valid() const{
    return m_restricted_isValid;
}

OAIAlbum_primary_genres OAITrack::getSecondaryGenres() const {
    return m_secondary_genres;
}
void OAITrack::setSecondaryGenres(const OAIAlbum_primary_genres &secondary_genres) {
    m_secondary_genres = secondary_genres;
    m_secondary_genres_isSet = true;
}

bool OAITrack::is_secondary_genres_Set() const{
    return m_secondary_genres_isSet;
}

bool OAITrack::is_secondary_genres_Valid() const{
    return m_secondary_genres_isValid;
}

double OAITrack::getSubtitleId() const {
    return m_subtitle_id;
}
void OAITrack::setSubtitleId(const double &subtitle_id) {
    m_subtitle_id = subtitle_id;
    m_subtitle_id_isSet = true;
}

bool OAITrack::is_subtitle_id_Set() const{
    return m_subtitle_id_isSet;
}

bool OAITrack::is_subtitle_id_Valid() const{
    return m_subtitle_id_isValid;
}

QString OAITrack::getTrackEditUrl() const {
    return m_track_edit_url;
}
void OAITrack::setTrackEditUrl(const QString &track_edit_url) {
    m_track_edit_url = track_edit_url;
    m_track_edit_url_isSet = true;
}

bool OAITrack::is_track_edit_url_Set() const{
    return m_track_edit_url_isSet;
}

bool OAITrack::is_track_edit_url_Valid() const{
    return m_track_edit_url_isValid;
}

double OAITrack::getTrackId() const {
    return m_track_id;
}
void OAITrack::setTrackId(const double &track_id) {
    m_track_id = track_id;
    m_track_id_isSet = true;
}

bool OAITrack::is_track_id_Set() const{
    return m_track_id_isSet;
}

bool OAITrack::is_track_id_Valid() const{
    return m_track_id_isValid;
}

QString OAITrack::getTrackIsrc() const {
    return m_track_isrc;
}
void OAITrack::setTrackIsrc(const QString &track_isrc) {
    m_track_isrc = track_isrc;
    m_track_isrc_isSet = true;
}

bool OAITrack::is_track_isrc_Set() const{
    return m_track_isrc_isSet;
}

bool OAITrack::is_track_isrc_Valid() const{
    return m_track_isrc_isValid;
}

double OAITrack::getTrackLength() const {
    return m_track_length;
}
void OAITrack::setTrackLength(const double &track_length) {
    m_track_length = track_length;
    m_track_length_isSet = true;
}

bool OAITrack::is_track_length_Set() const{
    return m_track_length_isSet;
}

bool OAITrack::is_track_length_Valid() const{
    return m_track_length_isValid;
}

QString OAITrack::getTrackMbid() const {
    return m_track_mbid;
}
void OAITrack::setTrackMbid(const QString &track_mbid) {
    m_track_mbid = track_mbid;
    m_track_mbid_isSet = true;
}

bool OAITrack::is_track_mbid_Set() const{
    return m_track_mbid_isSet;
}

bool OAITrack::is_track_mbid_Valid() const{
    return m_track_mbid_isValid;
}

QString OAITrack::getTrackName() const {
    return m_track_name;
}
void OAITrack::setTrackName(const QString &track_name) {
    m_track_name = track_name;
    m_track_name_isSet = true;
}

bool OAITrack::is_track_name_Set() const{
    return m_track_name_isSet;
}

bool OAITrack::is_track_name_Valid() const{
    return m_track_name_isValid;
}

QList<QString> OAITrack::getTrackNameTranslationList() const {
    return m_track_name_translation_list;
}
void OAITrack::setTrackNameTranslationList(const QList<QString> &track_name_translation_list) {
    m_track_name_translation_list = track_name_translation_list;
    m_track_name_translation_list_isSet = true;
}

bool OAITrack::is_track_name_translation_list_Set() const{
    return m_track_name_translation_list_isSet;
}

bool OAITrack::is_track_name_translation_list_Valid() const{
    return m_track_name_translation_list_isValid;
}

double OAITrack::getTrackRating() const {
    return m_track_rating;
}
void OAITrack::setTrackRating(const double &track_rating) {
    m_track_rating = track_rating;
    m_track_rating_isSet = true;
}

bool OAITrack::is_track_rating_Set() const{
    return m_track_rating_isSet;
}

bool OAITrack::is_track_rating_Valid() const{
    return m_track_rating_isValid;
}

QString OAITrack::getTrackShareUrl() const {
    return m_track_share_url;
}
void OAITrack::setTrackShareUrl(const QString &track_share_url) {
    m_track_share_url = track_share_url;
    m_track_share_url_isSet = true;
}

bool OAITrack::is_track_share_url_Set() const{
    return m_track_share_url_isSet;
}

bool OAITrack::is_track_share_url_Valid() const{
    return m_track_share_url_isValid;
}

double OAITrack::getTrackSoundcloudId() const {
    return m_track_soundcloud_id;
}
void OAITrack::setTrackSoundcloudId(const double &track_soundcloud_id) {
    m_track_soundcloud_id = track_soundcloud_id;
    m_track_soundcloud_id_isSet = true;
}

bool OAITrack::is_track_soundcloud_id_Set() const{
    return m_track_soundcloud_id_isSet;
}

bool OAITrack::is_track_soundcloud_id_Valid() const{
    return m_track_soundcloud_id_isValid;
}

QString OAITrack::getTrackSpotifyId() const {
    return m_track_spotify_id;
}
void OAITrack::setTrackSpotifyId(const QString &track_spotify_id) {
    m_track_spotify_id = track_spotify_id;
    m_track_spotify_id_isSet = true;
}

bool OAITrack::is_track_spotify_id_Set() const{
    return m_track_spotify_id_isSet;
}

bool OAITrack::is_track_spotify_id_Valid() const{
    return m_track_spotify_id_isValid;
}

QString OAITrack::getTrackXboxmusicId() const {
    return m_track_xboxmusic_id;
}
void OAITrack::setTrackXboxmusicId(const QString &track_xboxmusic_id) {
    m_track_xboxmusic_id = track_xboxmusic_id;
    m_track_xboxmusic_id_isSet = true;
}

bool OAITrack::is_track_xboxmusic_id_Set() const{
    return m_track_xboxmusic_id_isSet;
}

bool OAITrack::is_track_xboxmusic_id_Valid() const{
    return m_track_xboxmusic_id_isValid;
}

QString OAITrack::getUpdatedTime() const {
    return m_updated_time;
}
void OAITrack::setUpdatedTime(const QString &updated_time) {
    m_updated_time = updated_time;
    m_updated_time_isSet = true;
}

bool OAITrack::is_updated_time_Set() const{
    return m_updated_time_isSet;
}

bool OAITrack::is_updated_time_Valid() const{
    return m_updated_time_isValid;
}

bool OAITrack::isSet() const {
    bool isObjectUpdated = false;
    do {
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

        if (m_album_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_album_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_artist_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_artist_mbid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_artist_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_commontrack_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_commontrack_vanity_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_explicit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_release_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_lyrics_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_has_subtitles_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_instrumental_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lyrics_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_num_favourite_isSet) {
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

        if (m_subtitle_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_edit_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_isrc_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_mbid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_name_translation_list.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_rating_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_share_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_soundcloud_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_spotify_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_track_xboxmusic_id_isSet) {
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

bool OAITrack::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
