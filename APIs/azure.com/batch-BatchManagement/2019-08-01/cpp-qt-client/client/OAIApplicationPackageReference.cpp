/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApplicationPackageReference.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApplicationPackageReference::OAIApplicationPackageReference(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApplicationPackageReference::OAIApplicationPackageReference() {
    this->initializeModel();
}

OAIApplicationPackageReference::~OAIApplicationPackageReference() {}

void OAIApplicationPackageReference::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_version_isSet = false;
    m_version_isValid = false;
}

void OAIApplicationPackageReference::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApplicationPackageReference::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_version_isValid = ::OpenAPI::fromJsonValue(m_version, json[QString("version")]);
    m_version_isSet = !json[QString("version")].isNull() && m_version_isValid;
}

QString OAIApplicationPackageReference::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApplicationPackageReference::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_version_isSet) {
        obj.insert(QString("version"), ::OpenAPI::toJsonValue(m_version));
    }
    return obj;
}

QString OAIApplicationPackageReference::getId() const {
    return m_id;
}
void OAIApplicationPackageReference::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIApplicationPackageReference::is_id_Set() const{
    return m_id_isSet;
}

bool OAIApplicationPackageReference::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIApplicationPackageReference::getVersion() const {
    return m_version;
}
void OAIApplicationPackageReference::setVersion(const QString &version) {
    m_version = version;
    m_version_isSet = true;
}

bool OAIApplicationPackageReference::is_version_Set() const{
    return m_version_isSet;
}

bool OAIApplicationPackageReference::is_version_Valid() const{
    return m_version_isValid;
}

bool OAIApplicationPackageReference::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApplicationPackageReference::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && true;
}

} // namespace OpenAPI
