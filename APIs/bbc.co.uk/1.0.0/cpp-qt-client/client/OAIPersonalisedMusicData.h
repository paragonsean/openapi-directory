/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPersonalisedMusicData.h
 *
 * 
 */

#ifndef OAIPersonalisedMusicData_H
#define OAIPersonalisedMusicData_H

#include <QJsonObject>

#include "OAIPersonalisedMusicArtist.h"
#include "OAIPersonalisedMusicClip.h"
#include "OAIPersonalisedMusicGenre.h"
#include "OAIPersonalisedMusicPlaylist.h"
#include "OAIPersonalisedMusicService.h"
#include "OAIPersonalisedMusicTrack.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIPersonalisedMusicArtist;
class OAIPersonalisedMusicClip;
class OAIPersonalisedMusicGenre;
class OAIPersonalisedMusicPlaylist;
class OAIPersonalisedMusicService;
class OAIPersonalisedMusicTrack;

class OAIPersonalisedMusicData : public OAIObject {
public:
    OAIPersonalisedMusicData();
    OAIPersonalisedMusicData(QString json);
    ~OAIPersonalisedMusicData() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIPersonalisedMusicArtist getArtist() const;
    void setArtist(const OAIPersonalisedMusicArtist &artist);
    bool is_artist_Set() const;
    bool is_artist_Valid() const;

    OAIPersonalisedMusicClip getClip() const;
    void setClip(const OAIPersonalisedMusicClip &clip);
    bool is_clip_Set() const;
    bool is_clip_Valid() const;

    OAIPersonalisedMusicGenre getGenre() const;
    void setGenre(const OAIPersonalisedMusicGenre &genre);
    bool is_genre_Set() const;
    bool is_genre_Valid() const;

    OAIPersonalisedMusicPlaylist getPlaylist() const;
    void setPlaylist(const OAIPersonalisedMusicPlaylist &playlist);
    bool is_playlist_Set() const;
    bool is_playlist_Valid() const;

    OAIPersonalisedMusicService getService() const;
    void setService(const OAIPersonalisedMusicService &service);
    bool is_service_Set() const;
    bool is_service_Valid() const;

    OAIPersonalisedMusicTrack getTrack() const;
    void setTrack(const OAIPersonalisedMusicTrack &track);
    bool is_track_Set() const;
    bool is_track_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIPersonalisedMusicArtist m_artist;
    bool m_artist_isSet;
    bool m_artist_isValid;

    OAIPersonalisedMusicClip m_clip;
    bool m_clip_isSet;
    bool m_clip_isValid;

    OAIPersonalisedMusicGenre m_genre;
    bool m_genre_isSet;
    bool m_genre_isValid;

    OAIPersonalisedMusicPlaylist m_playlist;
    bool m_playlist_isSet;
    bool m_playlist_isValid;

    OAIPersonalisedMusicService m_service;
    bool m_service_isSet;
    bool m_service_isValid;

    OAIPersonalisedMusicTrack m_track;
    bool m_track_isSet;
    bool m_track_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPersonalisedMusicData)

#endif // OAIPersonalisedMusicData_H
