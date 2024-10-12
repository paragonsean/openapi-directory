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

#include "OAIPatientResource_attributes.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPatientResource_attributes::OAIPatientResource_attributes(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPatientResource_attributes::OAIPatientResource_attributes() {
    this->initializeModel();
}

OAIPatientResource_attributes::~OAIPatientResource_attributes() {}

void OAIPatientResource_attributes::initializeModel() {

    m_addresses_isSet = false;
    m_addresses_isValid = false;

    m_archive_history_isSet = false;
    m_archive_history_isValid = false;

    m_archived_isSet = false;
    m_archived_isValid = false;

    m_birth_date_isSet = false;
    m_birth_date_isValid = false;

    m_email_address_isSet = false;
    m_email_address_isValid = false;

    m_enrolled_at_isSet = false;
    m_enrolled_at_isValid = false;

    m_first_access_at_isSet = false;
    m_first_access_at_isValid = false;

    m_first_name_isSet = false;
    m_first_name_isValid = false;

    m_gender_isSet = false;
    m_gender_isValid = false;

    m_identifiers_isSet = false;
    m_identifiers_isValid = false;

    m_invited_at_isSet = false;
    m_invited_at_isValid = false;

    m_last_access_at_isSet = false;
    m_last_access_at_isValid = false;

    m_last_name_isSet = false;
    m_last_name_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_phone_numbers_isSet = false;
    m_phone_numbers_isValid = false;

    m_statement_isSet = false;
    m_statement_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAIPatientResource_attributes::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPatientResource_attributes::fromJsonObject(QJsonObject json) {

    m_addresses_isValid = ::OpenAPI::fromJsonValue(m_addresses, json[QString("addresses")]);
    m_addresses_isSet = !json[QString("addresses")].isNull() && m_addresses_isValid;

    m_archive_history_isValid = ::OpenAPI::fromJsonValue(m_archive_history, json[QString("archive_history")]);
    m_archive_history_isSet = !json[QString("archive_history")].isNull() && m_archive_history_isValid;

    m_archived_isValid = ::OpenAPI::fromJsonValue(m_archived, json[QString("archived")]);
    m_archived_isSet = !json[QString("archived")].isNull() && m_archived_isValid;

    m_birth_date_isValid = ::OpenAPI::fromJsonValue(m_birth_date, json[QString("birth_date")]);
    m_birth_date_isSet = !json[QString("birth_date")].isNull() && m_birth_date_isValid;

    m_email_address_isValid = ::OpenAPI::fromJsonValue(m_email_address, json[QString("email_address")]);
    m_email_address_isSet = !json[QString("email_address")].isNull() && m_email_address_isValid;

    m_enrolled_at_isValid = ::OpenAPI::fromJsonValue(m_enrolled_at, json[QString("enrolled_at")]);
    m_enrolled_at_isSet = !json[QString("enrolled_at")].isNull() && m_enrolled_at_isValid;

    m_first_access_at_isValid = ::OpenAPI::fromJsonValue(m_first_access_at, json[QString("first_access_at")]);
    m_first_access_at_isSet = !json[QString("first_access_at")].isNull() && m_first_access_at_isValid;

    m_first_name_isValid = ::OpenAPI::fromJsonValue(m_first_name, json[QString("first_name")]);
    m_first_name_isSet = !json[QString("first_name")].isNull() && m_first_name_isValid;

    m_gender_isValid = ::OpenAPI::fromJsonValue(m_gender, json[QString("gender")]);
    m_gender_isSet = !json[QString("gender")].isNull() && m_gender_isValid;

    m_identifiers_isValid = ::OpenAPI::fromJsonValue(m_identifiers, json[QString("identifiers")]);
    m_identifiers_isSet = !json[QString("identifiers")].isNull() && m_identifiers_isValid;

    m_invited_at_isValid = ::OpenAPI::fromJsonValue(m_invited_at, json[QString("invited_at")]);
    m_invited_at_isSet = !json[QString("invited_at")].isNull() && m_invited_at_isValid;

    m_last_access_at_isValid = ::OpenAPI::fromJsonValue(m_last_access_at, json[QString("last_access_at")]);
    m_last_access_at_isSet = !json[QString("last_access_at")].isNull() && m_last_access_at_isValid;

    m_last_name_isValid = ::OpenAPI::fromJsonValue(m_last_name, json[QString("last_name")]);
    m_last_name_isSet = !json[QString("last_name")].isNull() && m_last_name_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_phone_numbers_isValid = ::OpenAPI::fromJsonValue(m_phone_numbers, json[QString("phone_numbers")]);
    m_phone_numbers_isSet = !json[QString("phone_numbers")].isNull() && m_phone_numbers_isValid;

    m_statement_isValid = ::OpenAPI::fromJsonValue(m_statement, json[QString("statement")]);
    m_statement_isSet = !json[QString("statement")].isNull() && m_statement_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;
}

QString OAIPatientResource_attributes::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPatientResource_attributes::asJsonObject() const {
    QJsonObject obj;
    if (m_addresses.size() > 0) {
        obj.insert(QString("addresses"), ::OpenAPI::toJsonValue(m_addresses));
    }
    if (m_archive_history.size() > 0) {
        obj.insert(QString("archive_history"), ::OpenAPI::toJsonValue(m_archive_history));
    }
    if (m_archived_isSet) {
        obj.insert(QString("archived"), ::OpenAPI::toJsonValue(m_archived));
    }
    if (m_birth_date_isSet) {
        obj.insert(QString("birth_date"), ::OpenAPI::toJsonValue(m_birth_date));
    }
    if (m_email_address_isSet) {
        obj.insert(QString("email_address"), ::OpenAPI::toJsonValue(m_email_address));
    }
    if (m_enrolled_at_isSet) {
        obj.insert(QString("enrolled_at"), ::OpenAPI::toJsonValue(m_enrolled_at));
    }
    if (m_first_access_at_isSet) {
        obj.insert(QString("first_access_at"), ::OpenAPI::toJsonValue(m_first_access_at));
    }
    if (m_first_name_isSet) {
        obj.insert(QString("first_name"), ::OpenAPI::toJsonValue(m_first_name));
    }
    if (m_gender_isSet) {
        obj.insert(QString("gender"), ::OpenAPI::toJsonValue(m_gender));
    }
    if (m_identifiers.size() > 0) {
        obj.insert(QString("identifiers"), ::OpenAPI::toJsonValue(m_identifiers));
    }
    if (m_invited_at_isSet) {
        obj.insert(QString("invited_at"), ::OpenAPI::toJsonValue(m_invited_at));
    }
    if (m_last_access_at_isSet) {
        obj.insert(QString("last_access_at"), ::OpenAPI::toJsonValue(m_last_access_at));
    }
    if (m_last_name_isSet) {
        obj.insert(QString("last_name"), ::OpenAPI::toJsonValue(m_last_name));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_phone_numbers.size() > 0) {
        obj.insert(QString("phone_numbers"), ::OpenAPI::toJsonValue(m_phone_numbers));
    }
    if (m_statement.isSet()) {
        obj.insert(QString("statement"), ::OpenAPI::toJsonValue(m_statement));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

QList<OAIAddress> OAIPatientResource_attributes::getAddresses() const {
    return m_addresses;
}
void OAIPatientResource_attributes::setAddresses(const QList<OAIAddress> &addresses) {
    m_addresses = addresses;
    m_addresses_isSet = true;
}

bool OAIPatientResource_attributes::is_addresses_Set() const{
    return m_addresses_isSet;
}

bool OAIPatientResource_attributes::is_addresses_Valid() const{
    return m_addresses_isValid;
}

QList<OAIArchiveHistory> OAIPatientResource_attributes::getArchiveHistory() const {
    return m_archive_history;
}
void OAIPatientResource_attributes::setArchiveHistory(const QList<OAIArchiveHistory> &archive_history) {
    m_archive_history = archive_history;
    m_archive_history_isSet = true;
}

bool OAIPatientResource_attributes::is_archive_history_Set() const{
    return m_archive_history_isSet;
}

bool OAIPatientResource_attributes::is_archive_history_Valid() const{
    return m_archive_history_isValid;
}

bool OAIPatientResource_attributes::isArchived() const {
    return m_archived;
}
void OAIPatientResource_attributes::setArchived(const bool &archived) {
    m_archived = archived;
    m_archived_isSet = true;
}

bool OAIPatientResource_attributes::is_archived_Set() const{
    return m_archived_isSet;
}

bool OAIPatientResource_attributes::is_archived_Valid() const{
    return m_archived_isValid;
}

QDate OAIPatientResource_attributes::getBirthDate() const {
    return m_birth_date;
}
void OAIPatientResource_attributes::setBirthDate(const QDate &birth_date) {
    m_birth_date = birth_date;
    m_birth_date_isSet = true;
}

bool OAIPatientResource_attributes::is_birth_date_Set() const{
    return m_birth_date_isSet;
}

bool OAIPatientResource_attributes::is_birth_date_Valid() const{
    return m_birth_date_isValid;
}

QString OAIPatientResource_attributes::getEmailAddress() const {
    return m_email_address;
}
void OAIPatientResource_attributes::setEmailAddress(const QString &email_address) {
    m_email_address = email_address;
    m_email_address_isSet = true;
}

bool OAIPatientResource_attributes::is_email_address_Set() const{
    return m_email_address_isSet;
}

bool OAIPatientResource_attributes::is_email_address_Valid() const{
    return m_email_address_isValid;
}

QString OAIPatientResource_attributes::getEnrolledAt() const {
    return m_enrolled_at;
}
void OAIPatientResource_attributes::setEnrolledAt(const QString &enrolled_at) {
    m_enrolled_at = enrolled_at;
    m_enrolled_at_isSet = true;
}

bool OAIPatientResource_attributes::is_enrolled_at_Set() const{
    return m_enrolled_at_isSet;
}

bool OAIPatientResource_attributes::is_enrolled_at_Valid() const{
    return m_enrolled_at_isValid;
}

QString OAIPatientResource_attributes::getFirstAccessAt() const {
    return m_first_access_at;
}
void OAIPatientResource_attributes::setFirstAccessAt(const QString &first_access_at) {
    m_first_access_at = first_access_at;
    m_first_access_at_isSet = true;
}

bool OAIPatientResource_attributes::is_first_access_at_Set() const{
    return m_first_access_at_isSet;
}

bool OAIPatientResource_attributes::is_first_access_at_Valid() const{
    return m_first_access_at_isValid;
}

QString OAIPatientResource_attributes::getFirstName() const {
    return m_first_name;
}
void OAIPatientResource_attributes::setFirstName(const QString &first_name) {
    m_first_name = first_name;
    m_first_name_isSet = true;
}

bool OAIPatientResource_attributes::is_first_name_Set() const{
    return m_first_name_isSet;
}

bool OAIPatientResource_attributes::is_first_name_Valid() const{
    return m_first_name_isValid;
}

QString OAIPatientResource_attributes::getGender() const {
    return m_gender;
}
void OAIPatientResource_attributes::setGender(const QString &gender) {
    m_gender = gender;
    m_gender_isSet = true;
}

bool OAIPatientResource_attributes::is_gender_Set() const{
    return m_gender_isSet;
}

bool OAIPatientResource_attributes::is_gender_Valid() const{
    return m_gender_isValid;
}

QList<OAIPatientIdentifier> OAIPatientResource_attributes::getIdentifiers() const {
    return m_identifiers;
}
void OAIPatientResource_attributes::setIdentifiers(const QList<OAIPatientIdentifier> &identifiers) {
    m_identifiers = identifiers;
    m_identifiers_isSet = true;
}

bool OAIPatientResource_attributes::is_identifiers_Set() const{
    return m_identifiers_isSet;
}

bool OAIPatientResource_attributes::is_identifiers_Valid() const{
    return m_identifiers_isValid;
}

QString OAIPatientResource_attributes::getInvitedAt() const {
    return m_invited_at;
}
void OAIPatientResource_attributes::setInvitedAt(const QString &invited_at) {
    m_invited_at = invited_at;
    m_invited_at_isSet = true;
}

bool OAIPatientResource_attributes::is_invited_at_Set() const{
    return m_invited_at_isSet;
}

bool OAIPatientResource_attributes::is_invited_at_Valid() const{
    return m_invited_at_isValid;
}

QString OAIPatientResource_attributes::getLastAccessAt() const {
    return m_last_access_at;
}
void OAIPatientResource_attributes::setLastAccessAt(const QString &last_access_at) {
    m_last_access_at = last_access_at;
    m_last_access_at_isSet = true;
}

bool OAIPatientResource_attributes::is_last_access_at_Set() const{
    return m_last_access_at_isSet;
}

bool OAIPatientResource_attributes::is_last_access_at_Valid() const{
    return m_last_access_at_isValid;
}

QString OAIPatientResource_attributes::getLastName() const {
    return m_last_name;
}
void OAIPatientResource_attributes::setLastName(const QString &last_name) {
    m_last_name = last_name;
    m_last_name_isSet = true;
}

bool OAIPatientResource_attributes::is_last_name_Set() const{
    return m_last_name_isSet;
}

bool OAIPatientResource_attributes::is_last_name_Valid() const{
    return m_last_name_isValid;
}

QString OAIPatientResource_attributes::getNote() const {
    return m_note;
}
void OAIPatientResource_attributes::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAIPatientResource_attributes::is_note_Set() const{
    return m_note_isSet;
}

bool OAIPatientResource_attributes::is_note_Valid() const{
    return m_note_isValid;
}

QList<OAIPhoneNumber> OAIPatientResource_attributes::getPhoneNumbers() const {
    return m_phone_numbers;
}
void OAIPatientResource_attributes::setPhoneNumbers(const QList<OAIPhoneNumber> &phone_numbers) {
    m_phone_numbers = phone_numbers;
    m_phone_numbers_isSet = true;
}

bool OAIPatientResource_attributes::is_phone_numbers_Set() const{
    return m_phone_numbers_isSet;
}

bool OAIPatientResource_attributes::is_phone_numbers_Valid() const{
    return m_phone_numbers_isValid;
}

OAIPatientResource_attributes_statement OAIPatientResource_attributes::getStatement() const {
    return m_statement;
}
void OAIPatientResource_attributes::setStatement(const OAIPatientResource_attributes_statement &statement) {
    m_statement = statement;
    m_statement_isSet = true;
}

bool OAIPatientResource_attributes::is_statement_Set() const{
    return m_statement_isSet;
}

bool OAIPatientResource_attributes::is_statement_Valid() const{
    return m_statement_isValid;
}

QString OAIPatientResource_attributes::getUpdatedAt() const {
    return m_updated_at;
}
void OAIPatientResource_attributes::setUpdatedAt(const QString &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIPatientResource_attributes::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIPatientResource_attributes::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIPatientResource_attributes::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_addresses.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_archive_history.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_archived_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_birth_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_email_address_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_enrolled_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_access_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gender_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_identifiers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_invited_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_access_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_phone_numbers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_statement.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPatientResource_attributes::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
