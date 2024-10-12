/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICompanyTeamRepositoryV1CreatePost_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICompanyTeamRepositoryV1CreatePost_request::OAICompanyTeamRepositoryV1CreatePost_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICompanyTeamRepositoryV1CreatePost_request::OAICompanyTeamRepositoryV1CreatePost_request() {
    this->initializeModel();
}

OAICompanyTeamRepositoryV1CreatePost_request::~OAICompanyTeamRepositoryV1CreatePost_request() {}

void OAICompanyTeamRepositoryV1CreatePost_request::initializeModel() {

    m_team_isSet = false;
    m_team_isValid = false;
}

void OAICompanyTeamRepositoryV1CreatePost_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICompanyTeamRepositoryV1CreatePost_request::fromJsonObject(QJsonObject json) {

    m_team_isValid = ::OpenAPI::fromJsonValue(m_team, json[QString("team")]);
    m_team_isSet = !json[QString("team")].isNull() && m_team_isValid;
}

QString OAICompanyTeamRepositoryV1CreatePost_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICompanyTeamRepositoryV1CreatePost_request::asJsonObject() const {
    QJsonObject obj;
    if (m_team.isSet()) {
        obj.insert(QString("team"), ::OpenAPI::toJsonValue(m_team));
    }
    return obj;
}

OAICompany_data_team_interface OAICompanyTeamRepositoryV1CreatePost_request::getTeam() const {
    return m_team;
}
void OAICompanyTeamRepositoryV1CreatePost_request::setTeam(const OAICompany_data_team_interface &team) {
    m_team = team;
    m_team_isSet = true;
}

bool OAICompanyTeamRepositoryV1CreatePost_request::is_team_Set() const{
    return m_team_isSet;
}

bool OAICompanyTeamRepositoryV1CreatePost_request::is_team_Valid() const{
    return m_team_isValid;
}

bool OAICompanyTeamRepositoryV1CreatePost_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_team.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICompanyTeamRepositoryV1CreatePost_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_team_isValid && true;
}

} // namespace OpenAPI
