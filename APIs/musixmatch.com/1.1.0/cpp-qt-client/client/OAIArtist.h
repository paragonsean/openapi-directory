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

/*
 * OAIArtist.h
 *
 * a artist in the Musixmatch database.
 */

#ifndef OAIArtist_H
#define OAIArtist_H

#include <QJsonObject>

#include "OAIAlbum_primary_genres.h"
#include "OAIAlbum_secondary_genres.h"
#include "OAIArtist_artist_alias_list_inner.h"
#include "OAIArtist_artist_credits.h"
#include "OAIArtist_artist_name_translation_list_inner.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIArtist_artist_alias_list_inner;
class OAIArtist_artist_credits;
class OAIArtist_artist_name_translation_list_inner;
class OAIAlbum_primary_genres;
class OAIAlbum_secondary_genres;

class OAIArtist : public OAIObject {
public:
    OAIArtist();
    OAIArtist(QString json);
    ~OAIArtist() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIArtist_artist_alias_list_inner> getArtistAliasList() const;
    void setArtistAliasList(const QList<OAIArtist_artist_alias_list_inner> &artist_alias_list);
    bool is_artist_alias_list_Set() const;
    bool is_artist_alias_list_Valid() const;

    QString getArtistComment() const;
    void setArtistComment(const QString &artist_comment);
    bool is_artist_comment_Set() const;
    bool is_artist_comment_Valid() const;

    QString getArtistCountry() const;
    void setArtistCountry(const QString &artist_country);
    bool is_artist_country_Set() const;
    bool is_artist_country_Valid() const;

    OAIArtist_artist_credits getArtistCredits() const;
    void setArtistCredits(const OAIArtist_artist_credits &artist_credits);
    bool is_artist_credits_Set() const;
    bool is_artist_credits_Valid() const;

    QString getArtistEditUrl() const;
    void setArtistEditUrl(const QString &artist_edit_url);
    bool is_artist_edit_url_Set() const;
    bool is_artist_edit_url_Valid() const;

    double getArtistId() const;
    void setArtistId(const double &artist_id);
    bool is_artist_id_Set() const;
    bool is_artist_id_Valid() const;

    QString getArtistMbid() const;
    void setArtistMbid(const QString &artist_mbid);
    bool is_artist_mbid_Set() const;
    bool is_artist_mbid_Valid() const;

    QString getArtistName() const;
    void setArtistName(const QString &artist_name);
    bool is_artist_name_Set() const;
    bool is_artist_name_Valid() const;

    QList<OAIArtist_artist_name_translation_list_inner> getArtistNameTranslationList() const;
    void setArtistNameTranslationList(const QList<OAIArtist_artist_name_translation_list_inner> &artist_name_translation_list);
    bool is_artist_name_translation_list_Set() const;
    bool is_artist_name_translation_list_Valid() const;

    double getArtistRating() const;
    void setArtistRating(const double &artist_rating);
    bool is_artist_rating_Set() const;
    bool is_artist_rating_Valid() const;

    QString getArtistShareUrl() const;
    void setArtistShareUrl(const QString &artist_share_url);
    bool is_artist_share_url_Set() const;
    bool is_artist_share_url_Valid() const;

    QString getArtistTwitterUrl() const;
    void setArtistTwitterUrl(const QString &artist_twitter_url);
    bool is_artist_twitter_url_Set() const;
    bool is_artist_twitter_url_Valid() const;

    QString getArtistVanityId() const;
    void setArtistVanityId(const QString &artist_vanity_id);
    bool is_artist_vanity_id_Set() const;
    bool is_artist_vanity_id_Valid() const;

    double getManaged() const;
    void setManaged(const double &managed);
    bool is_managed_Set() const;
    bool is_managed_Valid() const;

    OAIAlbum_primary_genres getPrimaryGenres() const;
    void setPrimaryGenres(const OAIAlbum_primary_genres &primary_genres);
    bool is_primary_genres_Set() const;
    bool is_primary_genres_Valid() const;

    double getRestricted() const;
    void setRestricted(const double &restricted);
    bool is_restricted_Set() const;
    bool is_restricted_Valid() const;

    OAIAlbum_secondary_genres getSecondaryGenres() const;
    void setSecondaryGenres(const OAIAlbum_secondary_genres &secondary_genres);
    bool is_secondary_genres_Set() const;
    bool is_secondary_genres_Valid() const;

    QString getUpdatedTime() const;
    void setUpdatedTime(const QString &updated_time);
    bool is_updated_time_Set() const;
    bool is_updated_time_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIArtist_artist_alias_list_inner> m_artist_alias_list;
    bool m_artist_alias_list_isSet;
    bool m_artist_alias_list_isValid;

    QString m_artist_comment;
    bool m_artist_comment_isSet;
    bool m_artist_comment_isValid;

    QString m_artist_country;
    bool m_artist_country_isSet;
    bool m_artist_country_isValid;

    OAIArtist_artist_credits m_artist_credits;
    bool m_artist_credits_isSet;
    bool m_artist_credits_isValid;

    QString m_artist_edit_url;
    bool m_artist_edit_url_isSet;
    bool m_artist_edit_url_isValid;

    double m_artist_id;
    bool m_artist_id_isSet;
    bool m_artist_id_isValid;

    QString m_artist_mbid;
    bool m_artist_mbid_isSet;
    bool m_artist_mbid_isValid;

    QString m_artist_name;
    bool m_artist_name_isSet;
    bool m_artist_name_isValid;

    QList<OAIArtist_artist_name_translation_list_inner> m_artist_name_translation_list;
    bool m_artist_name_translation_list_isSet;
    bool m_artist_name_translation_list_isValid;

    double m_artist_rating;
    bool m_artist_rating_isSet;
    bool m_artist_rating_isValid;

    QString m_artist_share_url;
    bool m_artist_share_url_isSet;
    bool m_artist_share_url_isValid;

    QString m_artist_twitter_url;
    bool m_artist_twitter_url_isSet;
    bool m_artist_twitter_url_isValid;

    QString m_artist_vanity_id;
    bool m_artist_vanity_id_isSet;
    bool m_artist_vanity_id_isValid;

    double m_managed;
    bool m_managed_isSet;
    bool m_managed_isValid;

    OAIAlbum_primary_genres m_primary_genres;
    bool m_primary_genres_isSet;
    bool m_primary_genres_isValid;

    double m_restricted;
    bool m_restricted_isSet;
    bool m_restricted_isValid;

    OAIAlbum_secondary_genres m_secondary_genres;
    bool m_secondary_genres_isSet;
    bool m_secondary_genres_isValid;

    QString m_updated_time;
    bool m_updated_time_isSet;
    bool m_updated_time_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIArtist)

#endif // OAIArtist_H
