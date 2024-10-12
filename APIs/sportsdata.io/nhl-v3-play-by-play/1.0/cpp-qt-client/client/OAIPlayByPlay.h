/**
 * NHL v3 Play-by-Play
 * NHL play-by-play API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIPlayByPlay.h
 *
 * 
 */

#ifndef OAIPlayByPlay_H
#define OAIPlayByPlay_H

#include <QJsonObject>

#include "OAIGame.h"
#include "OAIPlay.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGame;
class OAIPlay;

class OAIPlayByPlay : public OAIObject {
public:
    OAIPlayByPlay();
    OAIPlayByPlay(QString json);
    ~OAIPlayByPlay() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGame getGame() const;
    void setGame(const OAIGame &game);
    bool is_game_Set() const;
    bool is_game_Valid() const;

    QList<OAIPlay> getPlays() const;
    void setPlays(const QList<OAIPlay> &plays);
    bool is_plays_Set() const;
    bool is_plays_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGame m_game;
    bool m_game_isSet;
    bool m_game_isValid;

    QList<OAIPlay> m_plays;
    bool m_plays_isSet;
    bool m_plays_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPlayByPlay)

#endif // OAIPlayByPlay_H
