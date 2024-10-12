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

#include "OAIMarketingMaterial.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMarketingMaterial::OAIMarketingMaterial(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMarketingMaterial::OAIMarketingMaterial() {
    this->initializeModel();
}

OAIMarketingMaterial::~OAIMarketingMaterial() {}

void OAIMarketingMaterial::initializeModel() {

    m_learn_uri_isSet = false;
    m_learn_uri_isValid = false;

    m_path_isSet = false;
    m_path_isValid = false;
}

void OAIMarketingMaterial::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMarketingMaterial::fromJsonObject(QJsonObject json) {

    m_learn_uri_isValid = ::OpenAPI::fromJsonValue(m_learn_uri, json[QString("learnUri")]);
    m_learn_uri_isSet = !json[QString("learnUri")].isNull() && m_learn_uri_isValid;

    m_path_isValid = ::OpenAPI::fromJsonValue(m_path, json[QString("path")]);
    m_path_isSet = !json[QString("path")].isNull() && m_path_isValid;
}

QString OAIMarketingMaterial::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMarketingMaterial::asJsonObject() const {
    QJsonObject obj;
    if (m_learn_uri_isSet) {
        obj.insert(QString("learnUri"), ::OpenAPI::toJsonValue(m_learn_uri));
    }
    if (m_path_isSet) {
        obj.insert(QString("path"), ::OpenAPI::toJsonValue(m_path));
    }
    return obj;
}

QString OAIMarketingMaterial::getLearnUri() const {
    return m_learn_uri;
}
void OAIMarketingMaterial::setLearnUri(const QString &learn_uri) {
    m_learn_uri = learn_uri;
    m_learn_uri_isSet = true;
}

bool OAIMarketingMaterial::is_learn_uri_Set() const{
    return m_learn_uri_isSet;
}

bool OAIMarketingMaterial::is_learn_uri_Valid() const{
    return m_learn_uri_isValid;
}

QString OAIMarketingMaterial::getPath() const {
    return m_path;
}
void OAIMarketingMaterial::setPath(const QString &path) {
    m_path = path;
    m_path_isSet = true;
}

bool OAIMarketingMaterial::is_path_Set() const{
    return m_path_isSet;
}

bool OAIMarketingMaterial::is_path_Valid() const{
    return m_path_isValid;
}

bool OAIMarketingMaterial::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_learn_uri_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_path_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMarketingMaterial::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
