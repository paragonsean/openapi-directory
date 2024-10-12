/**
 * NHL v3 Stats
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIDfsSlateGame.h
 *
 * 
 */

#ifndef OAIDfsSlateGame_H
#define OAIDfsSlateGame_H

#include <QJsonObject>

#include "OAIGame.h"

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGame;

class OAIDfsSlateGame : public OAIObject {
public:
    OAIDfsSlateGame();
    OAIDfsSlateGame(QString json);
    ~OAIDfsSlateGame() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    OAIGame getGame() const;
    void setGame(const OAIGame &game);
    bool is_game_Set() const;
    bool is_game_Valid() const;

    qint32 getGameId() const;
    void setGameId(const qint32 &game_id);
    bool is_game_id_Set() const;
    bool is_game_id_Valid() const;

    qint32 getOperatorGameId() const;
    void setOperatorGameId(const qint32 &operator_game_id);
    bool is_operator_game_id_Set() const;
    bool is_operator_game_id_Valid() const;

    bool isRemovedByOperator() const;
    void setRemovedByOperator(const bool &removed_by_operator);
    bool is_removed_by_operator_Set() const;
    bool is_removed_by_operator_Valid() const;

    qint32 getSlateGameId() const;
    void setSlateGameId(const qint32 &slate_game_id);
    bool is_slate_game_id_Set() const;
    bool is_slate_game_id_Valid() const;

    qint32 getSlateId() const;
    void setSlateId(const qint32 &slate_id);
    bool is_slate_id_Set() const;
    bool is_slate_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    OAIGame m_game;
    bool m_game_isSet;
    bool m_game_isValid;

    qint32 m_game_id;
    bool m_game_id_isSet;
    bool m_game_id_isValid;

    qint32 m_operator_game_id;
    bool m_operator_game_id_isSet;
    bool m_operator_game_id_isValid;

    bool m_removed_by_operator;
    bool m_removed_by_operator_isSet;
    bool m_removed_by_operator_isValid;

    qint32 m_slate_game_id;
    bool m_slate_game_id_isSet;
    bool m_slate_game_id_isValid;

    qint32 m_slate_id;
    bool m_slate_id_isSet;
    bool m_slate_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIDfsSlateGame)

#endif // OAIDfsSlateGame_H
