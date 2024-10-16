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
 * OAICurrentlyPlayingObject.h
 *
 * 
 */

#ifndef OAICurrentlyPlayingObject_H
#define OAICurrentlyPlayingObject_H

#include <QJsonObject>

#include "OAIContextObject.h"
#include "OAICurrentlyPlayingContextObject_item.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIContextObject;
class OAICurrentlyPlayingContextObject_item;

class OAICurrentlyPlayingObject : public OAIObject {
public:
    OAICurrentlyPlayingObject();
    OAICurrentlyPlayingObject(QString json);
    ~OAICurrentlyPlayingObject() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIContextObject getContext() const;
    void setContext(const OAIContextObject &context);
    bool is_context_Set() const;
    bool is_context_Valid() const;

    QString getCurrentlyPlayingType() const;
    void setCurrentlyPlayingType(const QString &currently_playing_type);
    bool is_currently_playing_type_Set() const;
    bool is_currently_playing_type_Valid() const;

    bool isIsPlaying() const;
    void setIsPlaying(const bool &is_playing);
    bool is_is_playing_Set() const;
    bool is_is_playing_Valid() const;

    OAICurrentlyPlayingContextObject_item getItem() const;
    void setItem(const OAICurrentlyPlayingContextObject_item &item);
    bool is_item_Set() const;
    bool is_item_Valid() const;

    qint32 getProgressMs() const;
    void setProgressMs(const qint32 &progress_ms);
    bool is_progress_ms_Set() const;
    bool is_progress_ms_Valid() const;

    qint32 getTimestamp() const;
    void setTimestamp(const qint32 &timestamp);
    bool is_timestamp_Set() const;
    bool is_timestamp_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIContextObject m_context;
    bool m_context_isSet;
    bool m_context_isValid;

    QString m_currently_playing_type;
    bool m_currently_playing_type_isSet;
    bool m_currently_playing_type_isValid;

    bool m_is_playing;
    bool m_is_playing_isSet;
    bool m_is_playing_isValid;

    OAICurrentlyPlayingContextObject_item m_item;
    bool m_item_isSet;
    bool m_item_isValid;

    qint32 m_progress_ms;
    bool m_progress_ms_isSet;
    bool m_progress_ms_isValid;

    qint32 m_timestamp;
    bool m_timestamp_isSet;
    bool m_timestamp_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAICurrentlyPlayingObject)

#endif // OAICurrentlyPlayingObject_H
