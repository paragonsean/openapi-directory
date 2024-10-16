/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIResendInvitationsRequestBody.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIResendInvitationsRequestBody::OAIResendInvitationsRequestBody(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIResendInvitationsRequestBody::OAIResendInvitationsRequestBody() {
    this->initializeModel();
}

OAIResendInvitationsRequestBody::~OAIResendInvitationsRequestBody() {}

void OAIResendInvitationsRequestBody::initializeModel() {

    m_recipient_id_isSet = false;
    m_recipient_id_isValid = false;
}

void OAIResendInvitationsRequestBody::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIResendInvitationsRequestBody::fromJsonObject(QJsonObject json) {

    m_recipient_id_isValid = ::OpenAPI::fromJsonValue(m_recipient_id, json[QString("recipientId")]);
    m_recipient_id_isSet = !json[QString("recipientId")].isNull() && m_recipient_id_isValid;
}

QString OAIResendInvitationsRequestBody::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIResendInvitationsRequestBody::asJsonObject() const {
    QJsonObject obj;
    if (m_recipient_id_isSet) {
        obj.insert(QString("recipientId"), ::OpenAPI::toJsonValue(m_recipient_id));
    }
    return obj;
}

qint32 OAIResendInvitationsRequestBody::getRecipientId() const {
    return m_recipient_id;
}
void OAIResendInvitationsRequestBody::setRecipientId(const qint32 &recipient_id) {
    m_recipient_id = recipient_id;
    m_recipient_id_isSet = true;
}

bool OAIResendInvitationsRequestBody::is_recipient_id_Set() const{
    return m_recipient_id_isSet;
}

bool OAIResendInvitationsRequestBody::is_recipient_id_Valid() const{
    return m_recipient_id_isValid;
}

bool OAIResendInvitationsRequestBody::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_recipient_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIResendInvitationsRequestBody::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
