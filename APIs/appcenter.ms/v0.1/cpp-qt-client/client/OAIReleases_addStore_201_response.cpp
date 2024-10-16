/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIReleases_addStore_201_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIReleases_addStore_201_response::OAIReleases_addStore_201_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIReleases_addStore_201_response::OAIReleases_addStore_201_response() {
    this->initializeModel();
}

OAIReleases_addStore_201_response::~OAIReleases_addStore_201_response() {}

void OAIReleases_addStore_201_response::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;
}

void OAIReleases_addStore_201_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIReleases_addStore_201_response::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;
}

QString OAIReleases_addStore_201_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIReleases_addStore_201_response::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    return obj;
}

QString OAIReleases_addStore_201_response::getId() const {
    return m_id;
}
void OAIReleases_addStore_201_response::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIReleases_addStore_201_response::is_id_Set() const{
    return m_id_isSet;
}

bool OAIReleases_addStore_201_response::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIReleases_addStore_201_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIReleases_addStore_201_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && true;
}

} // namespace OpenAPI
