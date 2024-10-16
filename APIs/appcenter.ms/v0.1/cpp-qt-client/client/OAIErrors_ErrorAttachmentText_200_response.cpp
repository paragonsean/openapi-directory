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

#include "OAIErrors_ErrorAttachmentText_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIErrors_ErrorAttachmentText_200_response::OAIErrors_ErrorAttachmentText_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIErrors_ErrorAttachmentText_200_response::OAIErrors_ErrorAttachmentText_200_response() {
    this->initializeModel();
}

OAIErrors_ErrorAttachmentText_200_response::~OAIErrors_ErrorAttachmentText_200_response() {}

void OAIErrors_ErrorAttachmentText_200_response::initializeModel() {

    m_content_isSet = false;
    m_content_isValid = false;
}

void OAIErrors_ErrorAttachmentText_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIErrors_ErrorAttachmentText_200_response::fromJsonObject(QJsonObject json) {

    m_content_isValid = ::OpenAPI::fromJsonValue(m_content, json[QString("content")]);
    m_content_isSet = !json[QString("content")].isNull() && m_content_isValid;
}

QString OAIErrors_ErrorAttachmentText_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIErrors_ErrorAttachmentText_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_content_isSet) {
        obj.insert(QString("content"), ::OpenAPI::toJsonValue(m_content));
    }
    return obj;
}

QString OAIErrors_ErrorAttachmentText_200_response::getContent() const {
    return m_content;
}
void OAIErrors_ErrorAttachmentText_200_response::setContent(const QString &content) {
    m_content = content;
    m_content_isSet = true;
}

bool OAIErrors_ErrorAttachmentText_200_response::is_content_Set() const{
    return m_content_isSet;
}

bool OAIErrors_ErrorAttachmentText_200_response::is_content_Valid() const{
    return m_content_isValid;
}

bool OAIErrors_ErrorAttachmentText_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_content_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIErrors_ErrorAttachmentText_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
