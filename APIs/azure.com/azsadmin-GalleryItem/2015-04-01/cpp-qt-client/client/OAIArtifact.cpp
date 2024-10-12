/**
 * GalleryManagementClient
 * The Admin Gallery Management Client.
 *
 * The version of the OpenAPI document: 2015-04-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIArtifact.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIArtifact::OAIArtifact(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIArtifact::OAIArtifact() {
    this->initializeModel();
}

OAIArtifact::~OAIArtifact() {}

void OAIArtifact::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_uri_isSet = false;
    m_uri_isValid = false;
}

void OAIArtifact::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIArtifact::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_uri_isValid = ::OpenAPI::fromJsonValue(m_uri, json[QString("uri")]);
    m_uri_isSet = !json[QString("uri")].isNull() && m_uri_isValid;
}

QString OAIArtifact::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIArtifact::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_uri_isSet) {
        obj.insert(QString("uri"), ::OpenAPI::toJsonValue(m_uri));
    }
    return obj;
}

QString OAIArtifact::getName() const {
    return m_name;
}
void OAIArtifact::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIArtifact::is_name_Set() const{
    return m_name_isSet;
}

bool OAIArtifact::is_name_Valid() const{
    return m_name_isValid;
}

QString OAIArtifact::getType() const {
    return m_type;
}
void OAIArtifact::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIArtifact::is_type_Set() const{
    return m_type_isSet;
}

bool OAIArtifact::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIArtifact::getUri() const {
    return m_uri;
}
void OAIArtifact::setUri(const QString &uri) {
    m_uri = uri;
    m_uri_isSet = true;
}

bool OAIArtifact::is_uri_Set() const{
    return m_uri_isSet;
}

bool OAIArtifact::is_uri_Valid() const{
    return m_uri_isValid;
}

bool OAIArtifact::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_uri_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIArtifact::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
