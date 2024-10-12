/**
 * Spotify Web API with fixes and improvements from sonallux
 * You can use Spotify's Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through <a href=\"https://developer.spotify.com/documentation/general/guides/authorization-guide/\">OAuth 2.0</a>.  The base URI for all Web API requests is `https://api.spotify.com/v1`.  Need help? See our <a href=\"https://developer.spotify.com/documentation/web-api/guides/\">Web API guides</a> for more information, or visit the <a href=\"https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\">Spotify for Developers community forum</a> to ask questions and connect with other developers. 
 *
 * The version of the OpenAPI document: 2023.2.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAlbumBase.h
 *
 * 
 */

#ifndef OAIAlbumBase_H
#define OAIAlbumBase_H

#include <QJsonObject>

#include "OAIAlbumRestrictionObject.h"
#include "OAIExternalUrlObject.h"
#include "OAIImageObject.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIExternalUrlObject;
class OAIImageObject;
class OAIAlbumRestrictionObject;

class OAIAlbumBase : public OAIObject {
public:
    OAIAlbumBase();
    OAIAlbumBase(QString json);
    ~OAIAlbumBase() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getAlbumType() const;
    void setAlbumType(const QString &album_type);
    bool is_album_type_Set() const;
    bool is_album_type_Valid() const;

    QList<QString> getAvailableMarkets() const;
    void setAvailableMarkets(const QList<QString> &available_markets);
    bool is_available_markets_Set() const;
    bool is_available_markets_Valid() const;

    OAIExternalUrlObject getExternalUrls() const;
    void setExternalUrls(const OAIExternalUrlObject &external_urls);
    bool is_external_urls_Set() const;
    bool is_external_urls_Valid() const;

    QString getHref() const;
    void setHref(const QString &href);
    bool is_href_Set() const;
    bool is_href_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<OAIImageObject> getImages() const;
    void setImages(const QList<OAIImageObject> &images);
    bool is_images_Set() const;
    bool is_images_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getReleaseDate() const;
    void setReleaseDate(const QString &release_date);
    bool is_release_date_Set() const;
    bool is_release_date_Valid() const;

    QString getReleaseDatePrecision() const;
    void setReleaseDatePrecision(const QString &release_date_precision);
    bool is_release_date_precision_Set() const;
    bool is_release_date_precision_Valid() const;

    OAIAlbumRestrictionObject getRestrictions() const;
    void setRestrictions(const OAIAlbumRestrictionObject &restrictions);
    bool is_restrictions_Set() const;
    bool is_restrictions_Valid() const;

    qint32 getTotalTracks() const;
    void setTotalTracks(const qint32 &total_tracks);
    bool is_total_tracks_Set() const;
    bool is_total_tracks_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    QString getUri() const;
    void setUri(const QString &uri);
    bool is_uri_Set() const;
    bool is_uri_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_album_type;
    bool m_album_type_isSet;
    bool m_album_type_isValid;

    QList<QString> m_available_markets;
    bool m_available_markets_isSet;
    bool m_available_markets_isValid;

    OAIExternalUrlObject m_external_urls;
    bool m_external_urls_isSet;
    bool m_external_urls_isValid;

    QString m_href;
    bool m_href_isSet;
    bool m_href_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<OAIImageObject> m_images;
    bool m_images_isSet;
    bool m_images_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_release_date;
    bool m_release_date_isSet;
    bool m_release_date_isValid;

    QString m_release_date_precision;
    bool m_release_date_precision_isSet;
    bool m_release_date_precision_isValid;

    OAIAlbumRestrictionObject m_restrictions;
    bool m_restrictions_isSet;
    bool m_restrictions_isValid;

    qint32 m_total_tracks;
    bool m_total_tracks_isSet;
    bool m_total_tracks_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;

    QString m_uri;
    bool m_uri_isSet;
    bool m_uri_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAlbumBase)

#endif // OAIAlbumBase_H
