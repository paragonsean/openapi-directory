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
 * OAIFollow_playlist_request.h
 *
 * 
 */

#ifndef OAIFollow_playlist_request_H
#define OAIFollow_playlist_request_H

#include <QJsonObject>

#include <QJsonValue>
#include <QMap>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIFollow_playlist_request : public OAIObject {
public:
    OAIFollow_playlist_request();
    OAIFollow_playlist_request(QString json);
    ~OAIFollow_playlist_request() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    bool isRPublic() const;
    void setRPublic(const bool &r_public);
    bool is_r_public_Set() const;
    bool is_r_public_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    bool m_r_public;
    bool m_r_public_isSet;
    bool m_r_public_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIFollow_playlist_request)

#endif // OAIFollow_playlist_request_H
