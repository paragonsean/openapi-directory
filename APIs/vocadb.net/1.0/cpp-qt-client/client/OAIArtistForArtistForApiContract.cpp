/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArtistForArtistForApiContract.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArtistForArtistForApiContract::OAIArtistForArtistForApiContract(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArtistForArtistForApiContract::OAIArtistForArtistForApiContract() {
    this->initializeModel();
}

OAIArtistForArtistForApiContract::~OAIArtistForArtistForApiContract() {}

void OAIArtistForArtistForApiContract::initializeModel() {

    m_artist_isSet = false;
    m_artist_isValid = false;

    m_link_type_isSet = false;
    m_link_type_isValid = false;
}

void OAIArtistForArtistForApiContract::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArtistForArtistForApiContract::fromJsonObject(QJsonObject json) {

    m_artist_isValid = ::OpenAPI::fromJsonValue(m_artist, json[QString("artist")]);
    m_artist_isSet = !json[QString("artist")].isNull() && m_artist_isValid;

    m_link_type_isValid = ::OpenAPI::fromJsonValue(m_link_type, json[QString("linkType")]);
    m_link_type_isSet = !json[QString("linkType")].isNull() && m_link_type_isValid;
}

QString OAIArtistForArtistForApiContract::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArtistForArtistForApiContract::asJsonObject() const {
    QJsonObject obj;
    if (m_artist.isSet()) {
        obj.insert(QString("artist"), ::OpenAPI::toJsonValue(m_artist));
    }
    if (m_link_type.isSet()) {
        obj.insert(QString("linkType"), ::OpenAPI::toJsonValue(m_link_type));
    }
    return obj;
}

OAIArtistContract OAIArtistForArtistForApiContract::getArtist() const {
    return m_artist;
}
void OAIArtistForArtistForApiContract::setArtist(const OAIArtistContract &artist) {
    m_artist = artist;
    m_artist_isSet = true;
}

bool OAIArtistForArtistForApiContract::is_artist_Set() const{
    return m_artist_isSet;
}

bool OAIArtistForArtistForApiContract::is_artist_Valid() const{
    return m_artist_isValid;
}

OAIArtistLinkType OAIArtistForArtistForApiContract::getLinkType() const {
    return m_link_type;
}
void OAIArtistForArtistForApiContract::setLinkType(const OAIArtistLinkType &link_type) {
    m_link_type = link_type;
    m_link_type_isSet = true;
}

bool OAIArtistForArtistForApiContract::is_link_type_Set() const{
    return m_link_type_isSet;
}

bool OAIArtistForArtistForApiContract::is_link_type_Valid() const{
    return m_link_type_isValid;
}

bool OAIArtistForArtistForApiContract::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_artist.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_link_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArtistForArtistForApiContract::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
