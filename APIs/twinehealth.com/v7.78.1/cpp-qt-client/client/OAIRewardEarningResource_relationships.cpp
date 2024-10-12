/**
 * Fitbit Plus API
 * # Overview The Fitbit Plus API is a RESTful API. The requests and responses are formated according to the [JSON API](http://jsonapi.org/format/1.0/) specification.  In addition to this documentation, we also provide an [OpenAPI](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) \"yaml\" file describing the API: [Fitbit Plus API Specification](swagger.yaml).  # Authentication Authentication for the Fitbit Plus API is based on the [OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749). Fitbit Plus currently supports grant types of **client_credentials** and **refresh_token**.  See [POST /oauth/token](#operation/createToken) for details on the request and response formats. <!-- ReDoc-Inject: <security-definitions> -->  ## Building Integrations We will provide customers with unique client credentials for each application/integration they build, allowing us to enforce appropriate access controls and monitor API usage. The client credentials will be scoped to the organization, and allow full access to all patients and related data within that organization.  These credentials are appropriate for creating an integration that does one of the following:  - background reporting/analysis  - synchronizing data with another system (such as an EMR)  The API credentials and oauth flows we currently support are **not** well suited for creating a user-facing application that allows a user (patient, coach, or admin) to login and have access to data which is appropriate to that specific user. It is possible to build such an application, but it is not possible to use Fitbit Plus as a federated identity provider. You would need to have a separate means of verifying a user's identity. We do not currently support the required password-based oauth flow to make this possible.  # Paging The Fitbit Plus API supports two different pagination strategies for GET collection endpoints.  #### Skip-based paging  Skip-based paging uses the query parameters `page[size]` and `page[number]` to specify the max number of resources returned and the page number. We default to skip-based paging if there are no page parameters. The response will include a `links` object containing links to the first, last, prev, and next pages of data.  If the contents of the collection change while you are iterating through the collection, you will see duplicate or missing documents. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=1`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[size]=50&page[number]=2`, the first entry in the second response will be a duplicate of the last entry in the first response.  #### Cursor-based paging Cursor-based paging uses the query parameters `page[limit]` and `page[after]` to specify the max number of entries returned and identify where to begin the next page. Add `page[limit]` to the parameters to use cursor-based paging. The response will include a `links` object containing a link to the next page of data, if the next page exists.  Cursor-based paging is not subject to duplication if new resources are added to the collection. For example, if you are iterating through the `calender_event` resource via `GET /pub/calendar_event?sort=start_at&page[limit]=50`, and a new `calendar_event` is created that has a `start_at` value before the first `calendar_event`, you will not see a duplicate entry when you fetch the next page at `GET /pub/calendar_event?sort=start_at&page[limit]=50&page[after]=<cursor>`.  We encourage the use of cursor-based paging for performance reasons.  In either form of paging, you can determine whether any resources were missed by comparing the number of fetched resources against `meta.count`. Set `page[size]` or `page[limit]` to 0 to get only the count.  It is not valid to mix the two strategies. 
 *
 * The version of the OpenAPI document: v7.78.1
 * Contact: apiteam@twinehealth.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIRewardEarningResource_relationships.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRewardEarningResource_relationships::OAIRewardEarningResource_relationships(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRewardEarningResource_relationships::OAIRewardEarningResource_relationships() {
    this->initializeModel();
}

OAIRewardEarningResource_relationships::~OAIRewardEarningResource_relationships() {}

void OAIRewardEarningResource_relationships::initializeModel() {

    m_group_isSet = false;
    m_group_isValid = false;

    m_patient_isSet = false;
    m_patient_isValid = false;

    m_reward_isSet = false;
    m_reward_isValid = false;

    m_reward_program_activation_isSet = false;
    m_reward_program_activation_isValid = false;
}

void OAIRewardEarningResource_relationships::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRewardEarningResource_relationships::fromJsonObject(QJsonObject json) {

    m_group_isValid = ::OpenAPI::fromJsonValue(m_group, json[QString("group")]);
    m_group_isSet = !json[QString("group")].isNull() && m_group_isValid;

    m_patient_isValid = ::OpenAPI::fromJsonValue(m_patient, json[QString("patient")]);
    m_patient_isSet = !json[QString("patient")].isNull() && m_patient_isValid;

    m_reward_isValid = ::OpenAPI::fromJsonValue(m_reward, json[QString("reward")]);
    m_reward_isSet = !json[QString("reward")].isNull() && m_reward_isValid;

    m_reward_program_activation_isValid = ::OpenAPI::fromJsonValue(m_reward_program_activation, json[QString("reward_program_activation")]);
    m_reward_program_activation_isSet = !json[QString("reward_program_activation")].isNull() && m_reward_program_activation_isValid;
}

QString OAIRewardEarningResource_relationships::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRewardEarningResource_relationships::asJsonObject() const {
    QJsonObject obj;
    if (m_group.isSet()) {
        obj.insert(QString("group"), ::OpenAPI::toJsonValue(m_group));
    }
    if (m_patient.isSet()) {
        obj.insert(QString("patient"), ::OpenAPI::toJsonValue(m_patient));
    }
    if (m_reward.isSet()) {
        obj.insert(QString("reward"), ::OpenAPI::toJsonValue(m_reward));
    }
    if (m_reward_program_activation.isSet()) {
        obj.insert(QString("reward_program_activation"), ::OpenAPI::toJsonValue(m_reward_program_activation));
    }
    return obj;
}

OAIRewardEarningFulfillmentResource_relationships_patient OAIRewardEarningResource_relationships::getGroup() const {
    return m_group;
}
void OAIRewardEarningResource_relationships::setGroup(const OAIRewardEarningFulfillmentResource_relationships_patient &group) {
    m_group = group;
    m_group_isSet = true;
}

bool OAIRewardEarningResource_relationships::is_group_Set() const{
    return m_group_isSet;
}

bool OAIRewardEarningResource_relationships::is_group_Valid() const{
    return m_group_isValid;
}

OAIRewardEarningFulfillmentResource_relationships_patient OAIRewardEarningResource_relationships::getPatient() const {
    return m_patient;
}
void OAIRewardEarningResource_relationships::setPatient(const OAIRewardEarningFulfillmentResource_relationships_patient &patient) {
    m_patient = patient;
    m_patient_isSet = true;
}

bool OAIRewardEarningResource_relationships::is_patient_Set() const{
    return m_patient_isSet;
}

bool OAIRewardEarningResource_relationships::is_patient_Valid() const{
    return m_patient_isValid;
}

OAIEmailHistoryResource_relationships_receiver OAIRewardEarningResource_relationships::getReward() const {
    return m_reward;
}
void OAIRewardEarningResource_relationships::setReward(const OAIEmailHistoryResource_relationships_receiver &reward) {
    m_reward = reward;
    m_reward_isSet = true;
}

bool OAIRewardEarningResource_relationships::is_reward_Set() const{
    return m_reward_isSet;
}

bool OAIRewardEarningResource_relationships::is_reward_Valid() const{
    return m_reward_isValid;
}

OAIRewardEarningFulfillmentResource_relationships_patient OAIRewardEarningResource_relationships::getRewardProgramActivation() const {
    return m_reward_program_activation;
}
void OAIRewardEarningResource_relationships::setRewardProgramActivation(const OAIRewardEarningFulfillmentResource_relationships_patient &reward_program_activation) {
    m_reward_program_activation = reward_program_activation;
    m_reward_program_activation_isSet = true;
}

bool OAIRewardEarningResource_relationships::is_reward_program_activation_Set() const{
    return m_reward_program_activation_isSet;
}

bool OAIRewardEarningResource_relationships::is_reward_program_activation_Valid() const{
    return m_reward_program_activation_isValid;
}

bool OAIRewardEarningResource_relationships::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_group.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_patient.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_reward.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_reward_program_activation.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRewardEarningResource_relationships::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_reward_isValid && true;
}

} // namespace OpenAPI
