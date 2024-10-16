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

#include "OAIPodcastSynopses.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPodcastSynopses::OAIPodcastSynopses(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPodcastSynopses::OAIPodcastSynopses() {
    this->initializeModel();
}

OAIPodcastSynopses::~OAIPodcastSynopses() {}

void OAIPodcastSynopses::initializeModel() {

    m_r_long_isSet = false;
    m_r_long_isValid = false;

    m_medium_isSet = false;
    m_medium_isValid = false;

    m_r_short_isSet = false;
    m_r_short_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIPodcastSynopses::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPodcastSynopses::fromJsonObject(QJsonObject json) {

    m_r_long_isValid = ::OpenAPI::fromJsonValue(m_r_long, json[QString("long")]);
    m_r_long_isSet = !json[QString("long")].isNull() && m_r_long_isValid;

    m_medium_isValid = ::OpenAPI::fromJsonValue(m_medium, json[QString("medium")]);
    m_medium_isSet = !json[QString("medium")].isNull() && m_medium_isValid;

    m_r_short_isValid = ::OpenAPI::fromJsonValue(m_r_short, json[QString("short")]);
    m_r_short_isSet = !json[QString("short")].isNull() && m_r_short_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIPodcastSynopses::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPodcastSynopses::asJsonObject() const {
    QJsonObject obj;
    if (m_r_long_isSet) {
        obj.insert(QString("long"), ::OpenAPI::toJsonValue(m_r_long));
    }
    if (m_medium_isSet) {
        obj.insert(QString("medium"), ::OpenAPI::toJsonValue(m_medium));
    }
    if (m_r_short_isSet) {
        obj.insert(QString("short"), ::OpenAPI::toJsonValue(m_r_short));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIPodcastSynopses::getRLong() const {
    return m_r_long;
}
void OAIPodcastSynopses::setRLong(const QString &r_long) {
    m_r_long = r_long;
    m_r_long_isSet = true;
}

bool OAIPodcastSynopses::is_r_long_Set() const{
    return m_r_long_isSet;
}

bool OAIPodcastSynopses::is_r_long_Valid() const{
    return m_r_long_isValid;
}

QString OAIPodcastSynopses::getMedium() const {
    return m_medium;
}
void OAIPodcastSynopses::setMedium(const QString &medium) {
    m_medium = medium;
    m_medium_isSet = true;
}

bool OAIPodcastSynopses::is_medium_Set() const{
    return m_medium_isSet;
}

bool OAIPodcastSynopses::is_medium_Valid() const{
    return m_medium_isValid;
}

QString OAIPodcastSynopses::getRShort() const {
    return m_r_short;
}
void OAIPodcastSynopses::setRShort(const QString &r_short) {
    m_r_short = r_short;
    m_r_short_isSet = true;
}

bool OAIPodcastSynopses::is_r_short_Set() const{
    return m_r_short_isSet;
}

bool OAIPodcastSynopses::is_r_short_Valid() const{
    return m_r_short_isValid;
}

QString OAIPodcastSynopses::getType() const {
    return m_type;
}
void OAIPodcastSynopses::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIPodcastSynopses::is_type_Set() const{
    return m_type_isSet;
}

bool OAIPodcastSynopses::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIPodcastSynopses::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_r_long_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_medium_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_r_short_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPodcastSynopses::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_r_long_isValid && m_medium_isValid && m_r_short_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
