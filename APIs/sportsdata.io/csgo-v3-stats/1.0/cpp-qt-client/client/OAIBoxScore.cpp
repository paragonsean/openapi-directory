/**
 * CS:GO v3 Stats
 * CS:GO v3 Stats
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBoxScore.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBoxScore::OAIBoxScore(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBoxScore::OAIBoxScore() {
    this->initializeModel();
}

OAIBoxScore::~OAIBoxScore() {}

void OAIBoxScore::initializeModel() {

    m_game_isSet = false;
    m_game_isValid = false;

    m_maps_isSet = false;
    m_maps_isValid = false;
}

void OAIBoxScore::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBoxScore::fromJsonObject(QJsonObject json) {

    m_game_isValid = ::OpenAPI::fromJsonValue(m_game, json[QString("Game")]);
    m_game_isSet = !json[QString("Game")].isNull() && m_game_isValid;

    m_maps_isValid = ::OpenAPI::fromJsonValue(m_maps, json[QString("Maps")]);
    m_maps_isSet = !json[QString("Maps")].isNull() && m_maps_isValid;
}

QString OAIBoxScore::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBoxScore::asJsonObject() const {
    QJsonObject obj;
    if (m_game.isSet()) {
        obj.insert(QString("Game"), ::OpenAPI::toJsonValue(m_game));
    }
    if (m_maps.size() > 0) {
        obj.insert(QString("Maps"), ::OpenAPI::toJsonValue(m_maps));
    }
    return obj;
}

OAIGame OAIBoxScore::getGame() const {
    return m_game;
}
void OAIBoxScore::setGame(const OAIGame &game) {
    m_game = game;
    m_game_isSet = true;
}

bool OAIBoxScore::is_game_Set() const{
    return m_game_isSet;
}

bool OAIBoxScore::is_game_Valid() const{
    return m_game_isValid;
}

QList<OAIMap> OAIBoxScore::getMaps() const {
    return m_maps;
}
void OAIBoxScore::setMaps(const QList<OAIMap> &maps) {
    m_maps = maps;
    m_maps_isSet = true;
}

bool OAIBoxScore::is_maps_Set() const{
    return m_maps_isSet;
}

bool OAIBoxScore::is_maps_Valid() const{
    return m_maps_isValid;
}

bool OAIBoxScore::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_game.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_maps.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBoxScore::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
