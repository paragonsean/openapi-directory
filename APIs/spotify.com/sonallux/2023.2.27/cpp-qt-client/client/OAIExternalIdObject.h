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
 * OAIExternalIdObject.h
 *
 * 
 */

#ifndef OAIExternalIdObject_H
#define OAIExternalIdObject_H

#include <QJsonObject>

#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIExternalIdObject : public OAIObject {
public:
    OAIExternalIdObject();
    OAIExternalIdObject(QString json);
    ~OAIExternalIdObject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getEan() const;
    void setEan(const QString &ean);
    bool is_ean_Set() const;
    bool is_ean_Valid() const;

    QString getIsrc() const;
    void setIsrc(const QString &isrc);
    bool is_isrc_Set() const;
    bool is_isrc_Valid() const;

    QString getUpc() const;
    void setUpc(const QString &upc);
    bool is_upc_Set() const;
    bool is_upc_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_ean;
    bool m_ean_isSet;
    bool m_ean_isValid;

    QString m_isrc;
    bool m_isrc_isSet;
    bool m_isrc_isValid;

    QString m_upc;
    bool m_upc_isSet;
    bool m_upc_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIExternalIdObject)

#endif // OAIExternalIdObject_H
