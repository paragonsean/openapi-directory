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

#include "OAIPersonalisedMusicVersion.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPersonalisedMusicVersion::OAIPersonalisedMusicVersion(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPersonalisedMusicVersion::OAIPersonalisedMusicVersion() {
    this->initializeModel();
}

OAIPersonalisedMusicVersion::~OAIPersonalisedMusicVersion() {}

void OAIPersonalisedMusicVersion::initializeModel() {

    m_classical_isSet = false;
    m_classical_isValid = false;

    m_duration_isSet = false;
    m_duration_isValid = false;

    m_radio_isSet = false;
    m_radio_isValid = false;

    m_vpid_isSet = false;
    m_vpid_isValid = false;
}

void OAIPersonalisedMusicVersion::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPersonalisedMusicVersion::fromJsonObject(QJsonObject json) {

    m_classical_isValid = ::OpenAPI::fromJsonValue(m_classical, json[QString("classical")]);
    m_classical_isSet = !json[QString("classical")].isNull() && m_classical_isValid;

    m_duration_isValid = ::OpenAPI::fromJsonValue(m_duration, json[QString("duration")]);
    m_duration_isSet = !json[QString("duration")].isNull() && m_duration_isValid;

    m_radio_isValid = ::OpenAPI::fromJsonValue(m_radio, json[QString("radio")]);
    m_radio_isSet = !json[QString("radio")].isNull() && m_radio_isValid;

    m_vpid_isValid = ::OpenAPI::fromJsonValue(m_vpid, json[QString("vpid")]);
    m_vpid_isSet = !json[QString("vpid")].isNull() && m_vpid_isValid;
}

QString OAIPersonalisedMusicVersion::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPersonalisedMusicVersion::asJsonObject() const {
    QJsonObject obj;
    if (m_classical_isSet) {
        obj.insert(QString("classical"), ::OpenAPI::toJsonValue(m_classical));
    }
    if (m_duration_isSet) {
        obj.insert(QString("duration"), ::OpenAPI::toJsonValue(m_duration));
    }
    if (m_radio_isSet) {
        obj.insert(QString("radio"), ::OpenAPI::toJsonValue(m_radio));
    }
    if (m_vpid_isSet) {
        obj.insert(QString("vpid"), ::OpenAPI::toJsonValue(m_vpid));
    }
    return obj;
}

bool OAIPersonalisedMusicVersion::isClassical() const {
    return m_classical;
}
void OAIPersonalisedMusicVersion::setClassical(const bool &classical) {
    m_classical = classical;
    m_classical_isSet = true;
}

bool OAIPersonalisedMusicVersion::is_classical_Set() const{
    return m_classical_isSet;
}

bool OAIPersonalisedMusicVersion::is_classical_Valid() const{
    return m_classical_isValid;
}

QString OAIPersonalisedMusicVersion::getDuration() const {
    return m_duration;
}
void OAIPersonalisedMusicVersion::setDuration(const QString &duration) {
    m_duration = duration;
    m_duration_isSet = true;
}

bool OAIPersonalisedMusicVersion::is_duration_Set() const{
    return m_duration_isSet;
}

bool OAIPersonalisedMusicVersion::is_duration_Valid() const{
    return m_duration_isValid;
}

bool OAIPersonalisedMusicVersion::isRadio() const {
    return m_radio;
}
void OAIPersonalisedMusicVersion::setRadio(const bool &radio) {
    m_radio = radio;
    m_radio_isSet = true;
}

bool OAIPersonalisedMusicVersion::is_radio_Set() const{
    return m_radio_isSet;
}

bool OAIPersonalisedMusicVersion::is_radio_Valid() const{
    return m_radio_isValid;
}

QString OAIPersonalisedMusicVersion::getVpid() const {
    return m_vpid;
}
void OAIPersonalisedMusicVersion::setVpid(const QString &vpid) {
    m_vpid = vpid;
    m_vpid_isSet = true;
}

bool OAIPersonalisedMusicVersion::is_vpid_Set() const{
    return m_vpid_isSet;
}

bool OAIPersonalisedMusicVersion::is_vpid_Valid() const{
    return m_vpid_isValid;
}

bool OAIPersonalisedMusicVersion::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_classical_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_duration_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_radio_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vpid_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPersonalisedMusicVersion::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
