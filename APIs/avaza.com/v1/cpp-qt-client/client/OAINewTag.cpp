/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAINewTag.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAINewTag::OAINewTag(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAINewTag::OAINewTag() {
    this->initializeModel();
}

OAINewTag::~OAINewTag() {}

void OAINewTag::initializeModel() {

    m_color_isSet = false;
    m_color_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAINewTag::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAINewTag::fromJsonObject(QJsonObject json) {

    m_color_isValid = ::OpenAPI::fromJsonValue(m_color, json[QString("Color")]);
    m_color_isSet = !json[QString("Color")].isNull() && m_color_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("Name")]);
    m_name_isSet = !json[QString("Name")].isNull() && m_name_isValid;
}

QString OAINewTag::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAINewTag::asJsonObject() const {
    QJsonObject obj;
    if (m_color_isSet) {
        obj.insert(QString("Color"), ::OpenAPI::toJsonValue(m_color));
    }
    if (m_name_isSet) {
        obj.insert(QString("Name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAINewTag::getColor() const {
    return m_color;
}
void OAINewTag::setColor(const QString &color) {
    m_color = color;
    m_color_isSet = true;
}

bool OAINewTag::is_color_Set() const{
    return m_color_isSet;
}

bool OAINewTag::is_color_Valid() const{
    return m_color_isValid;
}

QString OAINewTag::getName() const {
    return m_name;
}
void OAINewTag::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAINewTag::is_name_Set() const{
    return m_name_isSet;
}

bool OAINewTag::is_name_Valid() const{
    return m_name_isValid;
}

bool OAINewTag::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_color_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAINewTag::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
