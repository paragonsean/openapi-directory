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
 * OAILyrics.h
 *
 * a Lyrics in the Musixmatch database.
 */

#ifndef OAILyrics_H
#define OAILyrics_H

#include <QJsonObject>

#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAILyrics : public OAIObject {
public:
    OAILyrics();
    OAILyrics(QString json);
    ~OAILyrics() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getActionRequested() const;
    void setActionRequested(const QString &action_requested);
    bool is_action_requested_Set() const;
    bool is_action_requested_Valid() const;

    double getCanEdit() const;
    void setCanEdit(const double &can_edit);
    bool is_can_edit_Set() const;
    bool is_can_edit_Valid() const;

    double getRExplicit() const;
    void setRExplicit(const double &r_explicit);
    bool is_r_explicit_Set() const;
    bool is_r_explicit_Valid() const;

    QString getHtmlTrackingUrl() const;
    void setHtmlTrackingUrl(const QString &html_tracking_url);
    bool is_html_tracking_url_Set() const;
    bool is_html_tracking_url_Valid() const;

    double getInstrumental() const;
    void setInstrumental(const double &instrumental);
    bool is_instrumental_Set() const;
    bool is_instrumental_Valid() const;

    double getLocked() const;
    void setLocked(const double &locked);
    bool is_locked_Set() const;
    bool is_locked_Valid() const;

    QString getLyricsBody() const;
    void setLyricsBody(const QString &lyrics_body);
    bool is_lyrics_body_Set() const;
    bool is_lyrics_body_Valid() const;

    QString getLyricsCopyright() const;
    void setLyricsCopyright(const QString &lyrics_copyright);
    bool is_lyrics_copyright_Set() const;
    bool is_lyrics_copyright_Valid() const;

    double getLyricsId() const;
    void setLyricsId(const double &lyrics_id);
    bool is_lyrics_id_Set() const;
    bool is_lyrics_id_Valid() const;

    QString getLyricsLanguage() const;
    void setLyricsLanguage(const QString &lyrics_language);
    bool is_lyrics_language_Set() const;
    bool is_lyrics_language_Valid() const;

    QString getLyricsLanguageDescription() const;
    void setLyricsLanguageDescription(const QString &lyrics_language_description);
    bool is_lyrics_language_description_Set() const;
    bool is_lyrics_language_description_Valid() const;

    QString getPixelTrackingUrl() const;
    void setPixelTrackingUrl(const QString &pixel_tracking_url);
    bool is_pixel_tracking_url_Set() const;
    bool is_pixel_tracking_url_Valid() const;

    QList<QString> getPublisherList() const;
    void setPublisherList(const QList<QString> &publisher_list);
    bool is_publisher_list_Set() const;
    bool is_publisher_list_Valid() const;

    double getRestricted() const;
    void setRestricted(const double &restricted);
    bool is_restricted_Set() const;
    bool is_restricted_Valid() const;

    QString getScriptTrackingUrl() const;
    void setScriptTrackingUrl(const QString &script_tracking_url);
    bool is_script_tracking_url_Set() const;
    bool is_script_tracking_url_Valid() const;

    QString getUpdatedTime() const;
    void setUpdatedTime(const QString &updated_time);
    bool is_updated_time_Set() const;
    bool is_updated_time_Valid() const;

    double getVerified() const;
    void setVerified(const double &verified);
    bool is_verified_Set() const;
    bool is_verified_Valid() const;

    QList<QString> getWriterList() const;
    void setWriterList(const QList<QString> &writer_list);
    bool is_writer_list_Set() const;
    bool is_writer_list_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_action_requested;
    bool m_action_requested_isSet;
    bool m_action_requested_isValid;

    double m_can_edit;
    bool m_can_edit_isSet;
    bool m_can_edit_isValid;

    double m_r_explicit;
    bool m_r_explicit_isSet;
    bool m_r_explicit_isValid;

    QString m_html_tracking_url;
    bool m_html_tracking_url_isSet;
    bool m_html_tracking_url_isValid;

    double m_instrumental;
    bool m_instrumental_isSet;
    bool m_instrumental_isValid;

    double m_locked;
    bool m_locked_isSet;
    bool m_locked_isValid;

    QString m_lyrics_body;
    bool m_lyrics_body_isSet;
    bool m_lyrics_body_isValid;

    QString m_lyrics_copyright;
    bool m_lyrics_copyright_isSet;
    bool m_lyrics_copyright_isValid;

    double m_lyrics_id;
    bool m_lyrics_id_isSet;
    bool m_lyrics_id_isValid;

    QString m_lyrics_language;
    bool m_lyrics_language_isSet;
    bool m_lyrics_language_isValid;

    QString m_lyrics_language_description;
    bool m_lyrics_language_description_isSet;
    bool m_lyrics_language_description_isValid;

    QString m_pixel_tracking_url;
    bool m_pixel_tracking_url_isSet;
    bool m_pixel_tracking_url_isValid;

    QList<QString> m_publisher_list;
    bool m_publisher_list_isSet;
    bool m_publisher_list_isValid;

    double m_restricted;
    bool m_restricted_isSet;
    bool m_restricted_isValid;

    QString m_script_tracking_url;
    bool m_script_tracking_url_isSet;
    bool m_script_tracking_url_isValid;

    QString m_updated_time;
    bool m_updated_time_isSet;
    bool m_updated_time_isValid;

    double m_verified;
    bool m_verified_isSet;
    bool m_verified_isValid;

    QList<QString> m_writer_list;
    bool m_writer_list_isSet;
    bool m_writer_list_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILyrics)

#endif // OAILyrics_H
