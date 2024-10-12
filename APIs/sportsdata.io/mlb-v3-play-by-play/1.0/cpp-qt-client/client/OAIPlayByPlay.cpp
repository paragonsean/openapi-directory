/**
 * MLB v3 Play-by-Play
 * MLB play-by-play API.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPlayByPlay.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPlayByPlay::OAIPlayByPlay(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPlayByPlay::OAIPlayByPlay() {
    this->initializeModel();
}

OAIPlayByPlay::~OAIPlayByPlay() {}

void OAIPlayByPlay::initializeModel() {

    m_game_isSet = false;
    m_game_isValid = false;

    m_plays_isSet = false;
    m_plays_isValid = false;
}

void OAIPlayByPlay::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPlayByPlay::fromJsonObject(QJsonObject json) {

    m_game_isValid = ::OpenAPI::fromJsonValue(m_game, json[QString("Game")]);
    m_game_isSet = !json[QString("Game")].isNull() && m_game_isValid;

    m_plays_isValid = ::OpenAPI::fromJsonValue(m_plays, json[QString("Plays")]);
    m_plays_isSet = !json[QString("Plays")].isNull() && m_plays_isValid;
}

QString OAIPlayByPlay::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPlayByPlay::asJsonObject() const {
    QJsonObject obj;
    if (m_game.isSet()) {
        obj.insert(QString("Game"), ::OpenAPI::toJsonValue(m_game));
    }
    if (m_plays.size() > 0) {
        obj.insert(QString("Plays"), ::OpenAPI::toJsonValue(m_plays));
    }
    return obj;
}

OAIGame OAIPlayByPlay::getGame() const {
    return m_game;
}
void OAIPlayByPlay::setGame(const OAIGame &game) {
    m_game = game;
    m_game_isSet = true;
}

bool OAIPlayByPlay::is_game_Set() const{
    return m_game_isSet;
}

bool OAIPlayByPlay::is_game_Valid() const{
    return m_game_isValid;
}

QList<OAIPlay> OAIPlayByPlay::getPlays() const {
    return m_plays;
}
void OAIPlayByPlay::setPlays(const QList<OAIPlay> &plays) {
    m_plays = plays;
    m_plays_isSet = true;
}

bool OAIPlayByPlay::is_plays_Set() const{
    return m_plays_isSet;
}

bool OAIPlayByPlay::is_plays_Valid() const{
    return m_plays_isValid;
}

bool OAIPlayByPlay::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_game.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_plays.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPlayByPlay::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
